from src.main import main
import os
from src.colors import bcolors
from pwinput import pwinput

from pyvirtualdisplay import Display

print(bcolors.WARNING + """
  /$$$$$$  /$$$$$$ /$$      /$$       /$$$$$$$            /$$    
 /$$__  $$/$$__  $| $$$    /$$$      | $$__  $$          | $$    
| $$  \ $| $$  \__| $$$$  /$$$$      | $$  \ $$ /$$$$$$ /$$$$$$  
| $$  | $|  $$$$$$| $$ $$/$$ $$      | $$$$$$$ /$$__  $|_  $$_/  
| $$  | $$\____  $| $$  $$$| $$      | $$__  $| $$  \ $$ | $$    
| $$  | $$/$$  \ $| $$\  $ | $$      | $$  \ $| $$  | $$ | $$ /$$
|  $$$$$$|  $$$$$$| $$ \/  | $$      | $$$$$$$|  $$$$$$/ |  $$$$/
 \______/ \______/|__/     |__/      |_______/ \______/   \___/  
      """ + bcolors.ENDC)
print("\n")
print("Created by: FOliveira")
print("Version: 1.0")
print(bcolors.OKCYAN + "No GUI version." + bcolors.ENDC)
print("\n")

print(bcolors.OKBLUE + "Please, enter your credentials to start the bot." + bcolors.ENDC)
username = input("Username: ")
password = pwinput("Password: ")

os.system('cls' if os.name == 'nt' else 'clear')

print(bcolors.OKBLUE + "Starting bot...\n\n" + bcolors.ENDC)

with Display(visible=0, size=(800, 600)):
  main(username, password)
