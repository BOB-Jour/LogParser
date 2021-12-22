import time
import os
import sys
import math
import subprocess
import datetime
import socket
import random

from socket import *

#Initialize Basic Elements
Temp = ''
LogPath = ''
Division = 'DIVISION.txt'
Result = 'RESULT.txt'
CurrentSend = 'CurrentSend.txt'
ConnectStatus = ''
Sock = None
SendCount = 0
MyDirectory = './OUTPUT'
NickName = ''
WIN = 0
Mode = 0
ServerIP = ''
Port = 0
Date = ''
DateHour = 0
Fuzzer = "Domino"

delaytime = 0.0

#Start
def Start():
    global LogPath

    while True:
        if WIN == 1:
            os.system("cls")
            os.system("cls")

        else:
            os.system("clear")
            os.system("clear")

        print("[ LogParser ]")
        print()
        print("[*] Enter Log Directory Path")
        print("EX) ./[DIRECTORY NAME] OR ../[DIRECTORY NAME]")

        #Selecting Log Path
        try:
            LogPath = input(">>> ")
            
            if LogPath == '':
                print()
                print("[-] INPUT ERROR")
                try:
                    input("[ Enter ] To Continue")
                    continue

                except KeyboardInterrupt:
                    print()
                    print("[*] BYE~!!")
                    exit(0)

        except KeyboardInterrupt: 
            print()
            print("[*] BYE~!!")
            exit(0)
        break

#Dashboard
def Dashboard():
    global ServerIP, SendCount, Port, LogPath, NickName, ConnectStatus, Date

    if WIN == 1:
        os.system("cls")
        os.system("cls")
                
    else:
        os.system("clear")
        os.system("clear")

    print("=================[ LogParser ]===============")
    print(" [*] Path          : %s"%(LogPath))
    print(" [*] NickName      : %s"%(NickName))
    print(" [*] ServerIP      : %s"%(ServerIP))
    print(" [*] Port          : %d"%(Port))
    print(" [*] ConnectStatus : %s"%(ConnectStatus))
    print(" [*] Count         : %d [%s delay]"%(SendCount, str(delaytime)))
    print(" [*] Current Date  : %s"%(Date))
    print("=============================================")

def Setting():
    global Mode, WIN, ServerIP, Port, NickName, Fuzzer
    
    while True:
        if WIN == 1:
            os.system("cls")
            os.system("cls")
        else:
            os.system("clear")
            os.system("clear")

        #Select Execution Mode
        print("[ LogParser ]")
        print()
        print("[*] Choose An Execution Mode")
        print("[1] Run As Client")
        print("[2] Just Run")
    
        try:
            Mode = int(input(">>> "))

        except KeyboardInterrupt:
            print()
            print("[*] BYE~!!")
            exit(0)

        except:
            print()
            print("[-] INPUT ERROR")
            try:
                input("[ Enter ] To Continue")
                continue

            except KeyboardInterrupt:
                print()
                print("[*] BYE~!!")
                exit(0)

        if WIN == 1:
            os.system("cls")
            os.system("cls")

        else:
            os.system("clear")
            os.system("clear")

        #Client Mode
        if Mode == 1:
            while True:
                if WIN == 1:
                    os.system("cls")
                    os.system("cls")

                else:
                    os.system("clear")
                    os.system("clear")

                print("[ LogParser ]")
                print()
                print("[*] Enter The Server IP Address")
                
                ServerIP = input(">>> ")

                if ServerIP == '':
                    print()
                    print("[-] INPUT ERROR")
                    try:
                        input("[ Enter ] To Continue")
                        continue

                    except KeyboardInterrupt:
                        print()
                        print("[*] BYE~!!")
                        exit(0)
                
                try:
                    print("[*] Enter The Port Number")
                    Port = int(input(">>> "))

                except KeyboardInterrupt: 
                    print()
                    print("[*] BYE~!!")
                    exit(0)

                except:
                    print()
                    print("[-] INPUT ERROR")
                    try:
                        input("[ Enter ] To Continue")
                        continue

                    except KeyboardInterrupt:
                        print()
                        print("[*] BYE~!!")
                        exit(0)
                
                print("[*] Enter NickName")
                try:
                    NickName = input(">>> ")
                
                    if NickName == '':
                        print()
                        print("[-] INPUT ERROR")
                        try:
                            input("[ Enter ] To Continue")
                            continue

                        except KeyboardInterrupt:
                            print()
                            print("[*] BYE~!!")
                            exit(0)
                except KeyboardInterrupt: 
                    print()
                    print("[*] BYE~!!")
                    exit(0)

                except:
                    print()
                    print("[-] INPUT ERROR")
                    try:
                        input("[ Enter ] To Continue")
                        continue

                    except KeyboardInterrupt:
                        print()
                        print("[*] BYE~!!")
                        exit(0)

                break

        elif Mode == 2:
            pass

        else:
            print()
            print("[-] NOT FOUND OPTION [ %d ]"%(Mode))
            print("[*] Shutting down..")
            exit(0)
        break
    
    while True:
        if WIN == 1:
            os.system("cls")
            os.system("cls")
        else:
            os.system("clear")
            os.system("clear")

        #Select Fuzzer Type
        print("[ LogParser ]")
        print()
        print("[*] What Fuzzer?")
        print("[1] Domino")
        print("[2] watTF")
        print("[3] Glitch")
        print("[4] IDL")
        
        try:
            tmp = int(input(">>> "))

        except KeyboardInterrupt:
            print()
            print("[*] BYE~!!")
            exit(0)

        except:
            print()
            print("[-] INPUT ERROR")
            try:
                input("[ Enter ] To Continue")
                continue
            
            except KeyboardInterrupt:
                print()
                print("[*] BYE~!!")
                exit(0)

        if tmp == 1:
            Fuzzer = "Domino"
        
        elif tmp == 2:
            Fuzzer = "watTF"
        
        elif tmp == 3:
            Fuzzer = "Glitch"
        
        elif tmp == 4:
            Fuzzer = "IDL"

        break

#LogParser Class
class LogParser:
    #Initialize Basic Elements In LogParser
    def __init__(self):
        global Mode

        self.CrashDictionary = {'Check failed':[], 'use-after-poison':[], 'stack-buffer-overflow':[], 'heap-buffer-overflow':[], 'heap-use-after-free':[]}
        self.DCheckDictionary = {'FATAL:ng_length_utils.cc(220)] Check failed: intrinsic_size':[]}
        self.ASan_Check = 0
        self.DCheck_Check = 0

        if Mode == 2:
            self.EditCount = 1
            self.EditList = {}
            self.EditSelect = -1

    #Parsing
    def Parsing(self, path):
        global Division, Result, MyDirectory, ServerIP, Port, NickName, SendCount, CurrentSend, ConnectStatus, Sock, delaytime, Date, DateHour, Fuzzer
        FileList = []

        #Search Files
        try:
            Temp_FileList = os.listdir(path)

        except FileNotFoundError:
            print()
            print("[-] NOT FOUND DICTORY [ %s ]"%path)
            print("[*] Shutting down..")
            exit(0)
        
        #Sort Out Log Files
        for file in Temp_FileList:
            if '.log' in file:
                FileList.append(path+'/'+file)

        if FileList == []:
            print("[-] NOT FOUND LOG FILE")
            print("[*] Shutting down..")
            exit(0)

        #Total
        Total = len(FileList)

        #LogList
        if Mode == 2:
            print()
            print("====================[ LogList ]====================")
            for logfile in FileList:
                print("[+] %s"%(logfile))
            print("===================================================")

            #Printing Division
            print("[*] Loading...")
            print()
            time.sleep(0.2)

        
            print("====================[ Parsing ]====================")
        for LOG in FileList:
            self.ASan_Check = 0
            try:
                f = open(LOG, "r")
                line = f.readline()

                for ASanString in list(self.CrashDictionary.keys()):
                    self.DCheck_Check = 0

                    #Setting ASan List
                    if ASanString in line:
                        if Mode == 2:
                            print("[+] [ %s ] : %s"%(LOG, ASanString))
                        self.CrashDictionary[ASanString].append(LOG)
                        self.ASan_Check = 1
                    
                    #Setting DCheck List
                    if ASanString == 'Check failed':
                        for DCheckString in list(self.DCheckDictionary.keys()):
                            if DCheckString in line:
                                self.DCheckDictionary[DCheckString].append(LOG)
                                self.DCheck_Check = 1

                        #New Type Of DCheck
                        if self.DCheck_Check == 0:
                            try:
                                index = line.index("FATAL:")
                                ENDindex = line.index(": ")
                                Temp = line.split(' ')
                                for i in range(len(Temp)):
                                    if Temp[i] == "failed:":
                                        Keyword = "".join(line[index:ENDindex+2]+Temp[i+1])
                                        self.DCheckDictionary[Keyword] = []
                                        self.DCheckDictionary[Keyword].append(LOG)
                            except:
                                pass

                #Appending Unknown Type Of Crash & Setting Keyword
                if self.ASan_Check == 0:
                    #Unknown AddressSanitizer
                    if "AddressSanitizer" in line:
                        if "out of memory" in line:
                            pass
                        elif "requested allocation size" in line:
                            pass
                        else:
                            Temp = line.split(' ')
                            for j in range(len(Temp)):
                                if Temp[j] == "AddressSanitizer:":
                                    self.CrashDictionary[Temp[j+1]] = []
                                    self.CrashDictionary[Temp[j+1]].append(LOG)

                    #Unknown
                    else:
                        pass

                f.close()

            except KeyboardInterrupt:
                print()
                print("[*] Shutting down..")
                exit(0)

            except:
                if Mode == 2:
                    print()
                    print("[-] READING FILE ERROR")
                    print("[!] [ %s ]"%(logfile))

        if Mode == 2:
            print("===================================================")

        #Creating DIVISION.txt
        try:
            d = open(MyDirectory+"/"+"["+Fuzzer+"]-"+Division, "w")
            Count = 1
            DCount = 1
            for i in range(len(self.CrashDictionary.keys())):
                if list(self.CrashDictionary.keys())[i] == "Check failed":
                    d.write("[%d] [ %s ]\n"%(Count, list(self.CrashDictionary.keys())[i]))
                    Count = Count + 1

                    
                    for j in range(len(self.DCheckDictionary.keys())):
                        if self.DCheckDictionary[list(self.DCheckDictionary.keys())[j]] != []:
                            d.write("        [%d] [ %s \n"%(DCount, list(self.DCheckDictionary.keys())[j]))
                            DCount = DCount + 1

                            for DCheckfile in self.DCheckDictionary[list(self.DCheckDictionary.keys())[j]]:
                                d.write("        [ㆍ] %s\n"%(DCheckfile))
                            d.write("\n")
                else:
                    if self.CrashDictionary[list(self.CrashDictionary.keys())[i]] != []:
                        d.write("[%d] [ %s ]\n"%(Count, list(self.CrashDictionary.keys())[i]))

                        for file in self.CrashDictionary[list(self.CrashDictionary.keys())[i]]:
                            d.write("[ㆍ] %s\n"%(file))
                        d.write("\n")
                

            d.close()
            if Mode == 2:
                print("[+] CREATING DIVISION FILE COMPLETE!")
                time.sleep(0.2)
        except:
            print()
            print("[!] CREATING DIVISION FILE FAILED..")
            print("[!] PLEASE CHECK THE PERMISSIONS")
        
        #ASan Line Up
        MAX_SPACE = 0
        for i in range(len(self.CrashDictionary.keys())):
            if len(list(self.CrashDictionary.keys())[i]) > MAX_SPACE:
                MAX_SPACE = len(list(self.CrashDictionary.keys())[i])
        
        #DCheck Line Up
        DCHECK_MAX_SPACE = 0
        for i in range(len(self.DCheckDictionary.keys())):
            if len(list(self.DCheckDictionary.keys())[i]) > DCHECK_MAX_SPACE:
                DCHECK_MAX_SPACE = len(list(self.DCheckDictionary.keys())[i])

        #Creating RESULT.txt
        ResultForm = "="*math.floor(MAX_SPACE/2)+"[RESULT]"+"="*math.floor(MAX_SPACE/2)
        TotalSpace = "ㅤ"*(MAX_SPACE-5)
        try:
            Count = 1
            DCount = 1
            r = open(MyDirectory+"/"+"["+Fuzzer+"]-"+Result, "w", encoding='utf-8')
            r.write(ResultForm+"\n")
            for i in range(len(self.CrashDictionary.keys())):
                if len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]) != 0:
                    if list(self.CrashDictionary.keys())[i] == "Check failed":
                        r.write("[%d][ㆍ] [ %s ]\n"%(Count,list(self.CrashDictionary.keys())[i]))
                        r.write("        %d Count(%d%%)\n\n"%(len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]), ((len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]) / Total) * 100)))
                        Count = Count + 1

                        for j in range(len(list(self.DCheckDictionary.keys()))):
                            if self.DCheckDictionary[list(self.DCheckDictionary.keys())[j]] != []:
                                r.write("        [%d]- [%s \n"%(DCount, list(self.DCheckDictionary.keys())[j]))
                                r.write("                %d Count(%d%%)\n"%(len(self.DCheckDictionary[list(self.DCheckDictionary.keys())[j]]), ((len(self.DCheckDictionary[list(self.DCheckDictionary.keys())[j]]) / len(self.CrashDictionary['Check failed'])) * 100)))
                                DCount = DCount + 1
                    else:
                        if self.CrashDictionary[list(self.CrashDictionary.keys())[i]] != []:
                            r.write("[%d][ㆍ] [ %s ]\n"%(Count, list(self.CrashDictionary.keys())[i]))
                            r.write("        %d Count(%d%%)\n"%(len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]), ((len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]) / Total) * 100)))
                            Count = Count + 1
            r.write("="*len(ResultForm)+"\n")
            r.write("[ㆍ] [ Total ]\n")
            r.write("        %d Count\n"%(Total))
            r.write("="*len(ResultForm)+"\n")
            r.close()
        except:
            print()
            print("[!] CREATING RESULT FILE FAILED..")
            print("[!] PLEASE CHECK PERMISSIONS")

        if Mode == 2:
                print("[+] CREATING RESULT FILE COMPLETE!")
                print("[*] Loading..")
                print()
                time.sleep(0.2)
                
                if WIN == 1:
                    os.system("cls")
                    os.system("cls")
                
                else:
                    os.system("clear")
                    os.system("clear")
                

        #Printing Result
        try:
            if Mode == 2:
                print(ResultForm)
            for i in range(len(self.CrashDictionary.keys())):
                RegularSpace = " "*(MAX_SPACE-(len(list(self.CrashDictionary.keys())[i])))

                if len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]) != 0:
                    if list(self.CrashDictionary.keys())[i] == "Check failed":
                        if Mode == 2:
                            print("[ㆍ] %s"%(list(self.CrashDictionary.keys())[i])+RegularSpace+" : %d Count(%d%%)"%(len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]), ((len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]) / Total) * 100)))
                        
                        for j in range(len(list(self.DCheckDictionary.keys()))):
                            if self.DCheckDictionary[list(self.DCheckDictionary.keys())[j]] != []:
                                DCheck_Regularspace = " "*(DCHECK_MAX_SPACE-(len(list(self.DCheckDictionary.keys())[j])))
                                if Mode == 2:
                                    print("    - %s"%(list(self.DCheckDictionary.keys())[j])+DCheck_Regularspace+" : %d Count(%d%%)"%(len(self.DCheckDictionary[list(self.DCheckDictionary.keys())[j]]), ((len(self.DCheckDictionary[list(self.DCheckDictionary.keys())[j]]) / len(self.CrashDictionary['Check failed'])) * 100)))

                    else:
                        if Mode == 2:
                            if self.CrashDictionary[list(self.CrashDictionary.keys())[i]] != []:
                                print("[ㆍ] %s"%(list(self.CrashDictionary.keys())[i])+RegularSpace+" : %d Count(%d%%)"%(len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]), ((len(self.CrashDictionary[list(self.CrashDictionary.keys())[i]]) / Total) * 100)))

            if Mode == 2:
                print("="*len(ResultForm))
                print("[ㆍ] Total"+TotalSpace+" : %d Count"%(Total))
                print("="*len(ResultForm))

        except KeyboardInterrupt:
            print()
            print("[*] Shutting down..")
            exit(0)

        if Mode == 2:
            print()
            try:
                print("[ Enter ] To Editor")
                input("[ Ctrl+C ] To Exit")

            except KeyboardInterrupt:
                print()
                print("[*] BYE~!!")
                exit(0)

        #Socket(Send to LogCollector)
        elif Mode == 1:
            Sock = socket(AF_INET, SOCK_STREAM)
            delaytime = random.randrange(2, 10) / 10
            time.sleep(delaytime)
            try:
                if SendCount != 0:
                    
                    Date = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
                    if DateHour == datetime.datetime.now().hour:
                        ConnectStatus = '[ Pause ]'
                        return
                    else:
                        DateHour = DateHour = datetime.datetime.now().hour
                else:
                    Date = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
                    DateHour = datetime.datetime.now().hour

                Sock.connect((ServerIP, Port))
                ConnectStatus = '[ Allowed ]'

                try:
                    r = open(MyDirectory+"/"+"["+Fuzzer+"]-"+Result, "r", encoding='utf-8')
                except:
                    print("[-] NOT FOUND OUTPUT FILE")
                    exit(0)
                
                #NickName
                Sock.send(NickName.encode('utf-8')+"\n\nSIGNAMEEND".encode('utf-8'))
                
                #Fuzzer
                Sock.send(Fuzzer.encode('utf-8')+"\n\nSIGFUZZER".encode('utf-8'))
                
                LogContent = r.read()
                if len(LogContent) > 1024:
                    tmp = [LogContent[i:i+1023] for i in range(0, len(LogContent), 1023)]
                    try:
                        for SegData in tmp:
                            Sock.send(SegData.encode('utf-8'))
                        Sock.send("\n\nSIGEND".encode('utf-8'))
                    except:
                        print("[-] Encoding ERROR")
                        exit(0)
                else:
                    try:
                        Sock.send(LogContent.encode('utf-8')+"\n\nSIGEND".encode('utf-8'))
                    except:
                        print("[-] Encoding ERROR")
                        exit(0)
                Sock.close()

                time.sleep(delaytime)
                

                #SCP
                LOGFileList = ''
                #ASan List
                for ASan in list(self.CrashDictionary.keys()):
                    if ASan != 'Check failed':
                        if self.CrashDictionary[ASan] != []:
                            for i in range(len(self.CrashDictionary[ASan])):
                                ASanFile = self.CrashDictionary[ASan][i]
                                LOGFileList = LOGFileList + (ASanFile + " ")
                                LOGFileList = LOGFileList + (ASanFile.replace(".log", ".html") + " ")

                #DCheck List
                for DCheck in list(self.DCheckDictionary.keys()):
                    if self.DCheckDictionary[DCheck] != []:
                        for i in range(len(self.DCheckDictionary[DCheck])):
                            DCheckFile = self.DCheckDictionary[DCheck][i]
                            LOGFileList = LOGFileList + (DCheckFile + " ")
                            LOGFileList = LOGFileList + (DCheckFile.replace(".log", ".html") + " ")
                
                if WIN != 1:
                    time.sleep(delaytime)
                    zipfile = "["+Fuzzer+"]"+"["+NickName+"]-["+Date+"]-[POC].zip"
                    os.system("zip \"./"+zipfile+"\" "+LOGFileList)
                    os.system("sshpass -p \"logparser\" scp \"./"+zipfile+"\" ec2-user@"+ServerIP+":/home/ec2-user/Cache/POC")
                    os.remove(zipfile)
                    Divisionfile = "["+Fuzzer+"]"+"["+NickName+"]-["+Date+"]-[DIVISION].txt"
                    os.system("cp \""+MyDirectory+"/"+"["+Fuzzer+"]-"+"DIVISION.txt\" \"./"+Divisionfile+"\"")
                    os.system("sshpass -p \"logparser\" scp \"./"+Divisionfile+"\" ec2-user@"+ServerIP+":/home/ec2-user/Cache/POC")
                    os.remove(Divisionfile)
                SendCount = SendCount + 1

            except KeyboardInterrupt:
                Sock.close()
                exit(0)
            
            except Exception:
                ConnectStatus = '[ Denied ]'

    #Editor
    def Editor(self):
        global WIN

        while True:
            if WIN == 1:
                os.system("cls")
                os.system("cls")
                
            else:
                os.system("clear")
                os.system("clear")

            self.EditCount = 1
            self.EditList = {}
            self.EditSelect = -1

            print("====================[ Editor ]====================")
            #ASan List
            for types in self.CrashDictionary:
                if types != "Check failed":
                    if self.CrashDictionary[types] != []:
                        print("[ %s ]"%(types))
                        for i in range(len(self.CrashDictionary[types])):
                            print("[%s] "%(str(self.EditCount))+self.CrashDictionary[types][i])
                            self.EditList[str(self.EditCount)] = self.CrashDictionary[types][i]
                            self.EditCount = self.EditCount + 1

                        print()

            #DCheck List
            print("[ Check failed ]")
            for types in self.DCheckDictionary:
                if self.DCheckDictionary[types] != []:
                    print("    [ %s "%(types))
                    for i in range(len(self.DCheckDictionary[types])):
                        print("    [%s] "%(str(self.EditCount))+self.DCheckDictionary[types][i])
                        self.EditList[str(self.EditCount)] = self.DCheckDictionary[types][i]
                        self.EditCount = self.EditCount + 1
                    
                    print()

            print("[ Ctrl+C ] To Exit")
            try:
                self.EditSelect = input("[NUM]> ")

            except KeyboardInterrupt: 
                print()
                print("[*] BYE~!!")
                break
        
            if self.EditSelect == -1:
                print()
                print("[-] NOT FOUND KEY [ ]")
                try:
                    print("[ Enter ] To Continue")
                    input("[ Ctrl+C ] To Exit")
                    continue

                except KeyboardInterrupt:
                    print()
                    print("[*] BYE~!!")
                    break

            else:
                #Notepad
                if WIN == 1:
                    try:
                        CMD = ["notepad",self.EditList[self.EditSelect]]
                    
                    except KeyError:
                        print()
                        print("[-] NOT FOUND KEY [ %s ]"%(self.EditSelect))
                        try:
                            print("[ Enter ] To Continue")
                            input("[ Ctrl+C ] To Exit")
                            continue

                        except KeyboardInterrupt:
                            print()
                            print("[*] BYE~!!")
                            break

                    notepad = subprocess.Popen(CMD, shell=True)

                    while True:
                        try:
                            input("[ Ctrl+C ] To Close")
                    
                        except KeyboardInterrupt:
                            subprocess.call("taskkill /im notepad.exe /f", shell=True)
                            notepad.terminate()
                            break
                
                #Gedit
                else:
                    try:
                        CMD = "gedit "+self.EditList[self.EditSelect]
                        
                    except KeyError:
                        print()
                        print("[-] NOT FOUND KEY [ %s ]"%(self.EditSelect))
                        try:
                            print("[ Enter ] To Continue")
                            input("[ Ctrl+C ] To Exit")
                            continue

                        except KeyboardInterrupt:
                            print()
                            print("[*] BYE~!!")
                            break

                    gedit = subprocess.Popen(CMD, shell=True)

                    while True:
                        try:
                            input("[ Ctrl+C ] To Close")
                    
                        except KeyboardInterrupt:
                            subprocess.call("pkill -9 gedit", shell=True)
                            gedit.terminate()
                            break
        
if __name__ == '__main__':
    print("[ LogParser ]")
    print()

    #Argv 0
    if len(sys.argv) <= 1:
        Start()

    #Argv 1
    elif len(sys.argv) == 2:
        if sys.argv[1] == '-p':
            print("[!] Add Log Directory Path!!")
            print("EX) python LogParser.py -p ./[DIRECTORY NAME] OR ../[DIRECTORY NAME]")
            exit(0)

        elif sys.argv[1] == '--win':
            print("[*] Windows Version!")
            print()
            WIN = 1

            Start()

        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print("-p : Log Directory Path")
            print("EX) python LogParser.py -p ./[DIRECTORY NAME] OR ../[DIRECTORY NAME]")
            print()
            print("--win : Run On Windows")
            print("EX) python LogParser.py --win")
            exit(0)
        
        else:
            Start()

    #Argv 2
    elif len(sys.argv) == 3:
        if sys.argv[1] == '--win' or sys.argv[2] == '--win':
            print("[*] Windows Version!")
            print()
            WIN = 1

        if sys.argv[1] == '-p' and (sys.argv[2] != '--win' and (sys.argv[2] != '-h' or sys.argv[2] != '--help')):
            print("[*] Setting Log Directory Path Complete!")
            print()
            LogPath = sys.argv[2]

        elif sys.argv[2] == '-p':
            print("[!] Add Log Directory Path!!")
            print("EX) python LogParser.py -p ./[DIRECTORY NAME] OR ../[DIRECTORY NAME]")
            exit(0)

        else:
            print("[-] MATCHING OPTIONS FAILED..")
            exit(0)

    #Argv 3
    elif len(sys.argv) == 4:
        if sys.argv[3] == '--win' or sys.argv[2] == '--win' or sys.argv[1] == '--win':
            print("[*] Windows Version!")
            print()
            WIN = 1

        if sys.argv[1] == '-p' and (sys.argv[2] != '--win' and (sys.argv[2] != '-h' or sys.argv[2] != '--help')) or sys.argv[2] == '-p' and (sys.argv[3] != '--win' and (sys.argv[3] != '-h' or sys.argv[3] != '--help')):
            if sys.argv[1] == '-p':
                print("[*] Setting Log Directory Path Complete!")
                print()
                LogPath = sys.argv[2]
            elif sys.argv[2] == '-p':
                print("[*] Setting Log Directory Path Complete!")
                print()
                LogPath = sys.argv[3]
        
        elif sys.argv[3] == '-p':
            print("[!] Add Log Directory Path!!")
            print("EX) python LogParser.py -p ./[DIRECTORY NAME] OR ../[DIRECTORY NAME]")
            exit(0)
        
        else:
            print("[-] MATCHING OPTIONS FAILED..")
            exit(0)

    #Argv Overflow
    elif len(sys.argv) > 4:
        print("[!] 3 Argvs Are The MAXIUM!")
        exit(0)

    #Setting
    Setting()

    if WIN == 1:
        os.system("cls")
        os.system("cls")
                
    else:
        os.system("clear")
        os.system("clear")

    #Manage Path
    if LogPath[-1] == '/':
        LogPath = LogPath[:-1]

    if not os.path.exists(MyDirectory):
        os.makedirs(MyDirectory)

    if Mode == 2:
        LP = LogParser()
        print("====================[ INFO ]====================")
        print(" [*] Path         : %s"%(LogPath))
        print("================================================")

        LP.Parsing(LogPath)
        LP.Editor()

    if Mode == 1:
        while True:
            LP = LogParser()
            LP.Parsing(LogPath)
            Dashboard()
            #10 Minutes
            try:
                time.sleep(600)
            except KeyboardInterrupt:
                exit(0)