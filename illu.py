#!python
#!C:\Python37\python.exe

import requests
from colorama import Fore, Back, Style
from src.asu import kitab

print(Fore.BLUE)
print("""
  __     __  _ _ _           _             _            _____                _             
/  //\  /\ \(_) | |_   _ ___| |_ _ __ __ _| |_ ___  _ _/__   \_ __ __ _  ___| | _____ _ __ 
| |/ /_/ /| | | | | | | / __| __| '__/ _` | __/ _ \| '__|/ /\/ '__/ _` |/ __| |/ / _ \ '__|
| / __  / | | | | | |_| \__ \ |_| | | (_| | || (_) | |  / /  | | | (_| | (__|   <  __/ |   
| \/ /_/  | |_|_|_|\__,_|___/\__|_|  \__,_|\__\___/|_|  \/   |_|  \__,_|\___|_|\_\___|_|   
\_\     /_/                                                -Sin                                                        
""")
print(Style.RESET_ALL)

siapa = input("illustrator/doujin artist name: ")
print("Find /",Style.BRIGHT+Fore.YELLOW+siapa+Style.RESET_ALL+"'s nickname\n")
def main(siapa):
    
    
    for i in kitab:
        r = requests.get(i+"{}".format(siapa))
        if r.status_code == 200:
            print("[!] "+i+"{} >> ".format(siapa) + Fore.GREEN + "true"+ Style.RESET_ALL)
        else:
            print("[x] "+i+"{} >> ".format(siapa) + Fore.RED + "false, or different name?"+ Style.RESET_ALL)

main(siapa)
