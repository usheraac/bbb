import time
import os.path

#définition des fonctions

# permet de configurer une pin GPIO  en lecture ou ecriture
def init_gpio(pin,direct):
    try:

        ping = str(pin) #convertion en string

        #on n'arrive pas à accèder au export de notre bbb, du coup on mis les instructions concernées en commentaire
        #if True: not os.path.exists('/sys/class/gpio/gpio'+ping):
        with open('/sys/class/gpio/export', 'w') as file:
            file.write(ping)
            file.close()
    except OSError:
        print ('le pin '+ping+' a déjà été exporté')


    try:
        with open('/sys/class/gpio/gpio'+ping+'/direction', 'r') as file:
            contenu = file.read()
            file.close()
            if contenu == direct:
                print('la direction de la ping'+ping+'est déjà à '+direct)

            else:
                with open('/sys/class/gpio/gpio'+ping+'/direction', 'w') as file:
                    file.write(direct)
                    file.close()
                    print('la direction de la ping '+ping+' a été mis à '+direct)

    except OSError:
        print("pas d'accès au fichier 'direction' du pin "+ping)
        print("Peut être qu'il n'est pas encore exporté en GPIO")


#permet la lecture d'un pin GPIO
def read_gpio(pin):

        ping = str(pin)
        with open('/sys/class/gpio/gpio'+ping+'/value', 'r') as file:
            contenu = file.read()
            file.close()
        return contenu


#permet l'ecriture sur un pin GPIO
def write_gpio(pin,val):
        ping = str(pin)
        value = str(val)
        with open('/sys/class/gpio/gpio'+ping+'/value', 'w') as file:
                file.write(value)
                file.close()
                print("le fichier 'value' du pin "+ ping+" contient maintenant "+value)
