import os
import random
import string

# Clear terminal
os.system("clear")

# Logo + Developer Info + Menu একসাথে
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
print("1. Show Files")
print("2. Show IP")
print("3. System Info")
print("4. Password Generator")
print("5. Username Generator")
print("6. Network Info")
print("7. Exit")

# Menu loop
while True:
    choice = input("\nSelect option: ")

    if choice == "1":
        os.system("ls")

    elif choice == "2":
        os.system("ip a")

    elif choice == "3":
        os.system("uname -a")

    elif choice == "4":
        length = int(input("Password length: "))
        chars = string.ascii_letters + string.digits + "!@#$%"
        password = "".join(random.choice(chars) for i in range(length))
        print("Generated Password:", password)

    elif choice == "5":
        name = input("Enter name: ")
        num = random.randint(10,999)
        print("Generated Username:", name + str(num))

    elif choice == "6":
        os.system("ifconfig")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
