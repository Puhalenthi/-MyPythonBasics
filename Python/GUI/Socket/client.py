import socket
import threading
from colorama import Fore, Back, Style
import random

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '192.168.1.198'
ADDR = (SERVER, PORT)

clientcolors = [
    Fore.BLUE,
    Fore.CYAN,
    Fore.GREEN,
    Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX,
    Fore.LIGHTCYAN_EX,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTRED_EX,
    Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX,
    Fore.MAGENTA,
    Fore.RED,
    Fore.WHITE,
    Fore.YELLOW
]



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

clientcolor = int(client.recv(1024))

name = input('Enter your name:      ').encode(FORMAT)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    client.send(name)


def recieve():
    msgtorecv = client.recv(1024).decode('utf-8')
    try:
        counter, msg = msgtorecv.split('!SPLIT!')
        counter = int(counter)
        
        try:
            var1 = int(var1)
        except:
            try:
                var2 = int(var2)
                var1, var2 = var2, var1
            except:
                pass
        


        try:
            print(clientcolors[var1] + var2)
        except:
            try: #Var1 has all info and has 2 integers
                int(var1[:2])
                var2 = var1[2:]
                var1 = int(var1[:2])
            except:
                try: #Var1 has all info and has 1 integer
                    var2 = var1[1:]
                    var1 = int(var1[:1])
                except:
                    try: #Var2 has all info and has 2 integers
                        var1 = var2[2:]
                        var2 = int(var2[:2])
                    except: #Var2 has all info and has 1 integer
                        var1 = var2[1:]
                        var2 = int(var2[:2])
            
            
        print(clientcolors[counter] + msg)

        print(Fore.RESET)
    except:
        pass

while True:
    thread = threading.Thread(target=recieve)
    thread.start()
    msg = input()
    send(msg)