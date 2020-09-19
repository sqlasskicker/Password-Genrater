                    #PASSWORD GENRATER

import os
import random
import time
# PLAY WITH COLOURS
#red='\033[1;91m'
#green='\033[1;92m'                                            yellow='\033[1;93m'
#blue='\033[1;94m'
#purple='\033[1;95m'
#cyan='\033[1;96m'
#white='\033[1;97m
os.system('clear')
os.system("echo")
print("\033[34m  ╔═╗╔═╗╔═╗╔═╗  ╔═╗╔═╗╔╗╔╦═╗╔═╗╔╦╗╔═╗╦═╗ ")
print("\033[34m  ╠═╝╠═╣╚═╗╚═╗  ║ ╦║╣ ║║║╠╦╝╠═╣ ║ ║╣ ╠╦╝ ")
print("\033[34m  ╩  ╩ ╩╚═╝╚═╝  ╚═╝╚═╝╝╚╝╩╚═╩ ╩ ╩ ╚═╝╩╚═ ")
print("\033[34m =================×××××××××===============")
time.sleep(1)
os.system("echo")
os.system(" echo -e \"\\033[1;91m  • Author Information •\" ")
os.system(" echo -e  \"\\033[1;91m  ×××××××××××××××××××× \" ")
os.system(" echo -e \"\\033[1;91m > Name    : SQL ASSKICKER \" ")
os.system(" echo -e \"\\033[1;91m > Github  : https://github.com/sqlasskicker \" ")
os.system(" echo -e \"\\033[1;91m > YouTube : C4PT4IN R34P3R \" ")
os.system(" echo -e \"\\033[1;91m > STAY TUNED :)\" ")
os.system(" echo -e \"\\033[1;91m  ×××××××××××××××××××××\" ")
os.system(" echo")
chars = "abcdefghijklmnopqrstuvwxyz1234657890#_*@&!£ ZABCDEFGHIJKLMNOPQRSTUVWXY"
password = ""
os.system("echo")
length =  int(input( "\033[34m [•] ENTER PASSWORD LENGTH : "))
os.system("echo")
os.system ("echo -e \"\\033[1;96m Generating Password  Please Wait.... \"")
time.sleep(3)
os.system("echo")
while len(password) != length:
    password = password + random.choice(chars)
    if len(password) == length:
        print(" \033[32m [•] Your  Password: %s " % password)
os.system("echo")
print(" \033[32m STAY SAFE & SECURE")
os.system("echo")
