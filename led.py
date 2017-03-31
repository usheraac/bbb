import time
import os.path


# permet de configurer une pin GPIO  en lecture ou ecriture
def init_gpio(pin,direct):
        ping = str(pin)
        print('tre')
        #if True: not os.path.exists('/sys/class/gpio/gpio'+ping):
                #with open('/sys/class/gpio/export', 'w') as file:
                #file = open('/sys/class/gpio/export')
                #print('loop1')
                #file.write(ping)

        with open('/sys/class/gpio/gpio'+ping+'/direction', 'w') as file:
                        print('modification de la direction en'+direct)
                        file.write(direct)


##permet la lecture de pin GPIO
##def read_gpio(pin):
##    {
##    cd /sys/class/GPIO
##    cd gpio+pin
##    val = cat
##
##    }


#permet l ecriture sur une pin GPIO
def write_gpio(pin,val):
        ping = str(pin)
        value=str(val)
        with open('/sys/class/gpio/gpio'+ping+'/value', 'w') as file:
                file.write(value)



init_gpio(30,'out')

write_gpio(30,1)
