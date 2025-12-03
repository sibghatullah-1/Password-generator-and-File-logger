import secrets
import string
from datetime import datetime
import json
import os


def clear_screen():
    # for Windows
    if os.name == "nt":
        os.system("cls")
    # for macOS / Linux
    else:
        os.system("clear")


# function to store the password in the json file
def write_to_file(filename, password_selector):
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = {}

    key = len(data) + 1

    dict = {"password": password_selector, "date and time": now}
    data[key] = dict

    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    except FileNotFoundError and FileExistsError:
        print("Couldn't open the file")


def search(filename, id):
    # FIX: Handle first run when file doesn't exist or is empty
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        print("No data exsits")
        return

    with open(filename, "r") as f:
        data = json.load(f)

    if id in data:
        print(data[id])
    else:
        print("\nNo data of this id exsists")


def password_generator(password_selector):
    rng = int(input("Enter the size of password that you want : "))
    for i in range(rng):
        password_selector += secrets.choice(str)
    print(f"The random passwrod generated is this : {password_selector}")

    write_to_file(filename, password_selector)


# var for the collection of random elements
str = string.ascii_letters + string.digits + string.ascii_letters + string.punctuation
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
password_selector = ""

# Automatically save json file in the same script directory
script_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(script_directory, "password_logger.json")


while True:
    clear_screen()
    print(
        """    ____                  __                                 
   / __ \____ _____  ____/ /___  ____ ___                    
  / /_/ / __ `/ __ \/ __  / __ \/ __ `__ \                   
 / _, _/ /_/ / / / / /_/ / /_/ / / / / / /                   
/_/ |_|\__,_/_/ /_/\__,_/\____/_/ /_/ /_/             __    
   / __ \____ ____________      ______  ___________/ /    
  / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  /     
 / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /      
/_/____\__,_/____/____/ |__/|__/\____/_/   \__,_/       
  / ____/__  ____  ___  _________ _/ /_____  _____      
 / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/      
/ /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /          
\____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/           
                                                          """
    )

    ch = input(
        "\nEnter 1 to generate password \nEnter 2 Search previously generated passwords \nEnter 3 to exit : "
    )
    match ch:
        case "1":
            password_generator(password_selector)
            input("\nPress Enter to return to the menu...")
        case "2":
            id = input("Enter the id you want to search :")
            search(filename, id)
            input("\nPress Enter to return to the menu...")
        case "3":
            break
