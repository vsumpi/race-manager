######################################################################
######################################################################
##    /$$$$$$$  /$$ /$$$$$$$$                              /$$      ##
##   | $$__  $$|__/| $$_____/                             | $$      ##
##   | $$  \ $$ /$$| $$     /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$    ##
##   | $$$$$$$ | $$| $$$$$ /$$__  $$ /$$__  $$ /$$_____/|_  $$_/    ##
##   | $$__  $$| $$| $$__/| $$  \__/| $$  \ $$|  $$$$$$   | $$      ##
##   | $$  \ $$| $$| $$   | $$      | $$  | $$ \____  $$  | $$ /$$  ##
##   | $$$$$$$/| $$| $$   | $$      |  $$$$$$/ /$$$$$$$/  |  $$$$/  ##
##   |_______/ |__/|__/   |__/       \______/ |_______/    \___/    ##
######################################################################
##########From JS: https://codepen.io/sumpiii8/pen/bGKwwGY############
########################By: Varga Zsombor#############################
######################################################################

#imports
import datetime
import time
import os

#variables
h=0
m=0
s=0
difference=0
startDifference=0
on = 0

#functions
#def mp10():
#    startDifference = 10;
#    on = 1;
#
#def mp30():
#    startDifference = 30;
#    on = 1;
#
#def mp60():
#    startDifference = 60;
#    on = 1;
#
#def onoff():
#    startDifference = 0;
#    on = 0;


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def startTime():
    clear()
    #set date + store data
    today = datetime.datetime.now()
    h = today.strftime("%H")
    m = today.strftime("%M")
    s = today.strftime("%S")

    print(f'Jelenlegi idő: {h}:{m}:{s}', end='\r')
    try:
        print(f'\nKövetkező induló: {abs((int(s) % int(startDifference))-startDifference)}mp')
    except ZeroDivisionError:
        print(f'\nOFF')
    #delay
    time.sleep(1)

#loop
while True:
    clear()
    startDifference = 32
    startTime()