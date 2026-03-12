import os
import random
import string

# Clear terminal
os.system("clear")

# Colors
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

# Banner + Info
print(GREEN + """
 █████╗ ██████╗  █████╗ ███████╗ █████╗ ████████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
███████║██████╔╝███████║█████╗  ███████║   ██║
██╔══██║██╔══██╗██╔══██║██╔══╝  ██╔══██║   ██║
██║  ██║██║  ██║██║  ██║██║     ██║  ██║   ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝
""" + RESET)

print(GREEN + "=================================" + RESET)
print(" Developer : Arafat")
print(" GitHub    : https://github.com/576890-art")
print(" Facebook  : https://www.facebook.com/arafat576890")
print(" WhatsApp  : 01989333156")
print(GREEN + "=================================" + RESET)

# Menu
print("\n" + CYAN + "========= MENU =========" + RESET)
print("1. Show Files")
print("2. Show IP")
print("3. System Info")
print("4. Password Generator (Single)")
print("5. Password Generator (100)")
print("6. Password Generator (1000 with name+number)")
print("7. Password Generator (10000 with name+number, fast!)")
print("8. Username Generator")
print("9. Network Info")
print("10. Exit")

# Function to generate password
def generate_password(name="", length=8, unique_num=True):
    chars = string.ascii_letters + string.digits + "!@#$%"
    num = str(random.randint(100, 99999)) if unique_num else ""
    return name + num + "".join(random.choice(chars) for _ in range(length))

# Menu loop
while True:
    choice = input(CYAN + "\nSelect option: " + RESET)

    if choice == "1":
        os.system("ls")

    elif choice == "2":
        os.system("ip a")

    elif choice == "3":
        os.system("uname -a")

    elif choice == "4":
        length = int(input("Password length: "))
        password = generate_password(length=length, unique_num=False)
        print(GREEN + "Generated Password:" + RESET, password)

    elif choice == "5":
        name = input("Enter name: ")
        length = int(input("Extra password length: "))
        print(GREEN + "\nGenerated 100 Passwords:\n" + RESET)
        for i in range(1, 101):
            print(i, ":", generate_password(name, length))

    elif choice == "6":
        name = input("Enter name: ")
        length = int(input("Extra password length: "))
        print(GREEN + "\nGenerated 1000 Passwords:\n" + RESET)
        for i in range(1, 1001):
            print(i, ":", generate_password(name, length))

    elif choice == "7":
        name = input("Enter name: ")
        length = int(input("Extra password length: "))
        print(GREEN + "\nGenerating 10000 passwords. Please wait...\n" + RESET)
        passwords = []
        for i in range(1, 10001):
            passwords.append(generate_password(name, length))
            if i <= 50 or i % 500 == 0:
                print(RED + f"{i} passwords generated..." + RESET)
        print(GREEN + "\n10000 passwords generated! Scroll terminal to view." + RESET)
        print(CYAN + "\nFirst 20 passwords preview:\n" + RESET)
        for i in range(20):
            print(i+1, ":", passwords[i])

    elif choice == "8":
        name = input("Enter name: ")
        num = random.randint(10,999)
        username = name + str(num)
        print(GREEN + "Generated Username:" + RESET, username)

    elif choice == "9":
        os.system("ifconfig")

    elif choice == "10":
        print(RED + "Goodbye!" + RESET)
        break

    else:
        print(RED + "Invalid option" + RESET)
