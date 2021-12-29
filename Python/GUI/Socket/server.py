import socket 
import threading
from colorama import Fore, Back, Style
import random
import time

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # 192.168.1.198
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

clientlst = set()



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
    Fore.YELLOW,
]

chgclientcolors = clientcolors[:]

clientcolordict = {

}



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            name = conn.recv(1024).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
                clientcoloradd = clientcolordict.get(conn)
                clientcolors.append(clientcoloradd)
                
                clientlst.remove((conn, addr))
            for key, value in clientcolordict.items():
                if key == addr:
                    index = value
                    break
            
            counter = str(index)

            clientcolor = clientcolordict.get(addr)
            msgtosend = '{}:        {}'.format(name, msg)
            finalmsgtosend = counter + '!SPLIT!' + msgtosend
            for clientconn, clientaddr in clientlst:
                if clientaddr != addr:
                    clientconn.send(finalmsgtosend.encode('utf-8'))
    
            counter = int(counter)
            clientcolors[index]
            print(clientcolors[index] + msgtosend)

def start():
    server.listen()
    Fore.RESET
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        index = str(random.randrange(0, len(chgclientcolors) - 1))
        conn.send(index.encode(FORMAT))
        index = int(index)
        clientcolordict.update({addr:index})
        clientlst.add((conn, addr))
        chgclientcolors.remove(chgclientcolors[index])
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()