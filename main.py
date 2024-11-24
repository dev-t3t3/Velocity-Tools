#================================================================#
#   Copyright (c)  DedSec Developers.                            #
#   Licensed under the DedSec License, Version 1.0               #
#================================================================#


import os
import json
import time
import subprocess
import datetime
from requests import get
from pypresence import Presence 

from colorama import *
from fade import *

try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
try:
    import colorama
except ModuleNotFoundError:
    os.system('pip install colorama')
try:
    import fade
except ModuleNotFoundError:
    os.system('pip install fade')
try:
    import socket
except ModuleNotFoundError:
    os.system('pip install socket')
try:
    import threading
except ModuleNotFoundError:
    os.system('pip install threading')

with open("settings.json") as config:
    config = json.load(config)
    theme = config["Theme_Color"]

now = datetime.datetime.utcnow()
d2 = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

banner = f"""


         ██▒   █▓▓█████  ██▓     ▒█████   ▄████▄   ██▓▄▄▄█████▓▓██   ██▓
        ▓██░   █▒▓█   ▀ ▓██▒    ▒██▒  ██▒▒██▀ ▀█  ▓██▒▓  ██▒ ▓▒ ▒██  ██▒
         ▓██  █▒░▒███   ▒██░    ▒██░  ██▒▒▓█    ▄ ▒██▒▒ ▓██░ ▒░  ▒██ ██░
          ▒██ █░░▒▓█  ▄ ▒██░    ▒██   ██░▒▓▓▄ ▄██▒░██░░ ▓██▓ ░   ░ ▐██▓░
           ▒▀█░  ░▒████▒░██████▒░ ████▓▒░▒ ▓███▀ ░░██░  ▒██▒ ░   ░ ██▒▓░
           ░ ▐░  ░░ ▒░ ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░░▓    ▒ ░░      ██▒▒▒ 
           ░ ░░   ░ ░  ░░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒    ▒ ░    ░     ▓██ ░▒░ 
             ░░     ░     ░ ░   ░ ░ ░ ▒  ░         ▒ ░  ░       ▒ ▒ ░░  
              ░     ░  ░    ░  ░    ░ ░  ░ ░       ░            ░ ░     
             ░                           ░                      ░ ░     

"""

if theme == "yellow":
    faded_text = fade.fire(banner)
    shr6h = f"{Fore.RESET}[{Fore.YELLOW}>{Fore.RESET}]"
    number1 = f"{Fore.LIGHTYELLOW_EX}1"
    number2 = f"{Fore.LIGHTYELLOW_EX}2"
    number3 = f"{Fore.LIGHTYELLOW_EX}3"
    number4 = f"{Fore.LIGHTYELLOW_EX}4"
    number5 = f"{Fore.LIGHTYELLOW_EX}5"
    number6 = f"{Fore.LIGHTYELLOW_EX}6"
    number7 = f"{Fore.LIGHTYELLOW_EX}7"
    number8 = f"{Fore.LIGHTYELLOW_EX}8"
    number9 = f"{Fore.LIGHTYELLOW_EX}9"

if theme == "green":
    faded_text = fade.brazil(banner)
    shr6h = f"{Fore.RESET}[{Fore.GREEN}>{Fore.RESET}]"
    number1 = f"{Fore.LIGHTGREEN_EX}1"
    number2 = f"{Fore.LIGHTGREEN_EX}2"
    number3 = f"{Fore.LIGHTGREEN_EX}3"
    number4 = f"{Fore.LIGHTGREEN_EX}4"
    number5 = f"{Fore.LIGHTGREEN_EX}5"
    number6 = f"{Fore.LIGHTGREEN_EX}6"
    number7 = f"{Fore.LIGHTGREEN_EX}7"
    number8 = f"{Fore.LIGHTGREEN_EX}8"
    number9 = f"{Fore.LIGHTGREEN_EX}9"

if theme == "red":
    faded_text = fade.pinkred(banner)
    shr6h = f"{Fore.RESET}[{Fore.RED}>{Fore.RESET}]"
    number1 = f"{Fore.LIGHTRED_EX}1"
    number2 = f"{Fore.LIGHTRED_EX}2"
    number3 = f"{Fore.LIGHTRED_EX}3"
    number4 = f"{Fore.LIGHTRED_EX}4"
    number5 = f"{Fore.LIGHTRED_EX}5"
    number6 = f"{Fore.LIGHTRED_EX}6"
    number7 = f"{Fore.LIGHTRED_EX}7"
    number8 = f"{Fore.LIGHTRED_EX}8"
    number9 = f"{Fore.LIGHTRED_EX}9"

if theme == "default":
    faded_text = fade.purplepink(banner)
    shr6h = f"{Fore.RESET}[{Fore.MAGENTA}>{Fore.RESET}]"
    number1 = f"{Fore.LIGHTMAGENTA_EX}1"
    number2 = f"{Fore.LIGHTMAGENTA_EX}2"
    number3 = f"{Fore.LIGHTMAGENTA_EX}3"
    number4 = f"{Fore.LIGHTMAGENTA_EX}4"
    number5 = f"{Fore.LIGHTMAGENTA_EX}5"
    number6 = f"{Fore.LIGHTMAGENTA_EX}6"
    number7 = f"{Fore.LIGHTMAGENTA_EX}7"
    number8 = f"{Fore.LIGHTMAGENTA_EX}8"
    number9 = f"{Fore.LIGHTMAGENTA_EX}9"


def menu():
    os.system('cls')
    os.system(f'title Velocity Protection - Main ')
    print(faded_text)
    print()
    print(f'''
                 
{Fore.RESET}({number1}{Fore.RESET}) Windows Activation
{Fore.RESET}({number2}{Fore.RESET}) Deleted temporary files
{Fore.RESET}({number3}{Fore.RESET}) Fix & Reinstall System File
{Fore.RESET}({number4}{Fore.RESET}) Repair System damaged files
{Fore.RESET}({number5}{Fore.RESET}) Research and repair
{Fore.RESET}({number9}{Fore.RESET}) About

''')


    print()
    choice = input(f"{Fore.GREEN}Velocity @~ {Fore.RESET}")
    choice = int(choice)
    if choice == 1:
        os.system('cls')
        os.system(f'title Velocity Protection - Windows Activation ')
        print(faded_text)
        print('Please wait to activate')
        os.system('slmgr /upk')
        os.system('slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
        os.system('slmgr /skms kms8.msguides.com')
        print('Your Windows Has been Activated')
        time.sleep(4)
        input("Press Enter to Exit : ")
        menu()
    elif choice == 2:
        os.system('cls')
        os.system(f'title Velocity Protection - Deleted temporary files ')
        print(faded_text)
        print('Please wait to deleted your file')
        os.system('del *.log /a /s /q /f')
        os.system('takeown /f "%temp%" /r /d y')
        os.system('deltree /y c:\windows\tempor~1')
        print('The files have been completely deleted')
        time.sleep(2)
        input("Press Enter to Exit : ")
        menu()
    elif choice == 3:
        os.system('cls')
        os.system(f'title Velocity Protection - Fix & Reinstall System File ')
        print(faded_text)
        print('Please wait to Fix File')
        os.system(f'ipconfig /flushdns')
        print('The Files Fixed')
        time.sleep(2)
        input("Press Enter to Exit : ")
        menu()
    elif choice == 4:
        os.system('cls')
        os.system(f'title Velocity Protection - Repair System damaged files ')
        print(faded_text)
        print('Please wait to See For Your File')
        os.system(f'DISM /Online /Cleanup-Image /RestoreHealth')
        print('The Files Fixed')
        time.sleep(2)
        input("Press Enter to Exit : ")
        menu()
    elif choice == 5:
        os.system('cls')
        os.system(f'title Velocity Protection - Research and Repair ')
        print(faded_text)
        print('Please wait to See For Your File')
        os.system(f'sfc /scannow')
        print('Done Now Restart Your PC')
        time.sleep(2)
        input("Press Enter to Exit : ")
    elif choice == 6:
        soon()
    elif choice == 7:
        soon()
    elif choice == 8:
        soon()
    elif choice == 9:
        os.system('cls')
        os.system(f'title Velocity Protection - About Velocity ')
        print(faded_text)
        print("\nHello, thanks for using Velocity!\nif you run into any problems make sure to let me know asap!\nGithub: https://github.com/dev-t3t3")
        time.sleep(5)
        input("Press Enter to Exit : ")
        menu()



menu()