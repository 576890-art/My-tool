import os
import random
import string
import time

os.system("clear")

print("\033[1;32m")

print("""
 █████╗ ██████╗  █████╗ ███████╗ █████╗ ████████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
███████║██████╔╝███████║█████╗  ███████║   ██║
██╔══██║██╔══██╗██╔══██║██╔══╝  ██╔══██║   ██║
██║  ██║██║  ██║██║  ██║██║     ██║  ██║   ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝   ╚═╝
""")

print("=================================")
print(" Developer : Arafat")
print(" GitHub    : https://github.com/576890-art")
print(" Facebook  : https://www.facebook.com/arafat576890")
print(" WhatsApp  : 01989333156")
print("=================================")

print("\n========= MENU =========")
print("1. Password Generator")
print("2. 100 Password Generate")
print("3. 1000 Password Generate")
print("4. Password Strength Check")
print("5. Matrix Effect")
print("6. Exit")

while True:

    choice = input("\nSelect option: ")

    # Single password
    if choice == "1":
        length = int(input("Password length: "))
        chars = string.ascii_letters + string.digits + "!@#$%"
        password = "".join(random.choice(chars) for i in range(length))
        print("Generated Password:", password)

    # 100 password
    elif choice == "2":
        chars = string.ascii_letters + string.digits
        for i in range(100):
            password = "".join(random.choice(chars) for i in range(8))
            print(password)

    # 1000 password
    elif choice == "3":
        chars = string.ascii_letters + string.digits
        for i in range(1000):
            password = "".join(random.choice(chars) for i in range(8))
            print(password)

    # Password strength
    elif choice == "4":
        password = input("Enter password: ")
        strength = 0

        if len(password) >= 8:
            strength += 1
        if any(c.islower() for c in password):
            strength += 1
        if any(c.isupper() for c in password):
            strength += 1
        if any(c.isdigit() for c in password):
            strength += 1

        if strength <= 2:
            print("Weak Password")
        elif strength == 3:
            print("Medium Password")
        else:
            print("Strong Password")

    # Matrix effect
    elif choice == "5":
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        while True:
            print("\033[1;32m" + "".join(random.choice(chars) for i in range(60)))
            time.sleep(0.05)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
