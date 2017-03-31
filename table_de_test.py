import led
import time
import math
#programme principale
#code pour eteindre toute les leds
def eteint_all():

    row=[61,115,47,112,46,45,44,69]
    col=[26,49,48,66,27,65,68,67]

    for i in col:
        init_gpio(i,'out')
        init_gpio(i, "out")
        write_gpio(i,1)
        time.sleep(0.1)
    for i in row:
        init_gpio(i,"out")
        write_gpio(i,0)
        time.sleep(0.1)

def allume_all():
    row=[61,115,47,112,46,45,44,69]
    col=[26,49,48,66,27,65,68,67]

    for i in col:
        init_gpio(i,'out')
        init_gpio(i, "out")
        write_gpio(i,0)
        time.sleep(0.1)
    for i in row:
        init_gpio(i,"out")
        write_gpio(i,1)
        time.sleep(0.1)

def clignote_all():
    i=1
    while(i<10):
        eteint_all()
        time.sleep(0.5)
        allume_all()
        time.sleep(0.5)
        i=i+1
