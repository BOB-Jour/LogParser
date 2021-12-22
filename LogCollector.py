import socketserver
import os
import threading
import datetime
import socket

#Thread Lock
threadLock = threading.Lock()


IP = socket.gethostbyname(socket.getfqdn())
Port = 8080
DataFolder = './Cache'
DataFile = 'Data.txt'
Fuzzer = ''

class UserManager:
    def __init__(self):
        self.users = {}
    
    def addUser(self, username, conn, addr):
        threadLock.acquire()
        self.users[username] = []
        threadLock.release()
        return 1
    
    def removeUser(self, username, conn, addr):
        threadLock.acquire()
        del self.users[username]
        conn.close()
        threadLock.release()

class MySocketHandler(socketserver.BaseRequestHandler):
    usermanager = UserManager()
    def handle(self):
        global Fuzzer

        username = self.registerUsername()
        while True:
            try:
                self.usermanager.users[username].append(self.request.recv(1024).decode('utf-8'))
            except KeyboardInterrupt:
                os._exit(1)
            except:
                print("\n[-] Closed")
                self.usermanager.removeUser(username)
                return
        
            for i in range(len(self.usermanager.users[username])):
                if 'SIGEND' in self.usermanager.users[username][i]:
                    tmp = "".join(str(_) for _ in self.usermanager.users[username])
                    #Printing Packet
                    f = open(DataFolder+"/"+DataFile, "a+", encoding="UTF-8")

                    PacketForm = "[ %s ] - %s\n[ %s ]\n\n"%(username, datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'), Fuzzer)
                    print(PacketForm)
                    print(tmp)
                    f.write(PacketForm)
                    f.write(tmp)

                    print("[*] [ %s ] Closed\n"%(username))
                    
                    self.usermanager.removeUser(username, self.request, self.client_address)
                    f.close()
                    return
            continue
        
    def registerUsername(self):
        global Fuzzer
        
        username = self.request.recv(1024).decode('utf-8')
        if 'SIGNAMEEND' in username:
            username = username.replace("\n\nSIGNAMEEND", "")
        else:
            self.request.close()
        
        Fuzzer = self.request.recv(1024).decode('utf-8')
        if 'SIGFUZZER' in Fuzzer:
            Fuzzer = Fuzzer.replace("\n\nSIGFUZZER", "")
        else:
            self.request.close()
            
        if self.usermanager.addUser(username, self.request, self.client_address):
            print("[ %s ] Connected!"%(username))
            return username

class MyServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    if not os.path.exists(DataFolder):
        os.makedirs(DataFolder)

    os.system("clear")
    os.system("clear")
    print("[ LogCollector ]")
    print()
    print("===============================")
    print("[*] IP        : %s"%(IP))
    print("[*] Port      : %d"%(Port))
    print("===============================")
    print()

    print("[*] Socket Creating..")
    print("[*] Listening..")
    print("-------------------------------")
    print()

    #Auto
    try:
        ServerSock = MyServer((IP, Port), MySocketHandler)
        ServerSock.serve_forever()

    except KeyboardInterrupt:
        ServerSock.shutdown()
        ServerSock.server_close()