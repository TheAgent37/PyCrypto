from cryptography.fernet import Fernet
import color


print(
    """
 |||||||| ||     || ||||||||     |||     ||||||   |||||||| ||    || ||||||||  |||||||  |||||||| 
    ||    ||     || ||          || ||   ||    ||  ||       |||   ||    ||    ||     || ||    || 
    ||    ||     || ||         ||   ||  ||        ||       ||||  ||    ||           ||     ||   
    ||    ||||||||| ||||||    ||     || ||   |||| ||||||   || || ||    ||     |||||||     ||    
    ||    ||     || ||        ||||||||| ||    ||  ||       ||  ||||    ||           ||   ||     
    ||    ||     || ||        ||     || ||    ||  ||       ||   |||    ||    ||     ||   ||     
    ||    ||     || ||||||||  ||     ||  ||||||   |||||||| ||    ||    ||     |||||||    ||   


Welcome to my encryption program!
Please update me with bugs and your ideas.
"""
)

# ? This is the encryption code
def Encrypt(key):
    fe = Fernet(key)
    ask_file = input("Select input type: text(t), file(f), back(b): ")

    if ask_file == "t":
        text = input("Enter text for encrypting with random key: ")
        encrypted_text = fe.encrypt(bytes(text, "utf-8"))
        with open("output\encrypted.txt", "wb") as f:
            f.write(encrypted_text)
        print(
            f"Encrypted text will be saved to{color.BOLD}{color.YELLOW} encrypted.txt\n{color.END}"
        )
        Sec()
    elif ask_file == "f":
        path_file = input("Enter the file path: ")
        with open(f"{path_file}", "rb") as file_encrypt:
            encrypted_text = fe.encrypt(file_encrypt.read())
        with open("output\encrypted.txt", "wb") as f:
            f.write(encrypted_text)
        print(
            f"Encrypted text will be saved to{color.BOLD}{color.YELLOW} encrypted.txt\n{color.END}"
        )
        Sec()
    elif ask_file == "b":
        return Main()

    else:
        print(color.RED, "Invalid input", color.END)
        return Main()


# ? This is the decryption code
def Decrypt():
    key = input("Please enter your key: \n")
    ask_file = input("Select input type: text(t), file(f), back(b): ")
    fe = Fernet(key)

    if ask_file == "t":
        text = input("Enter encrypted test: \n")
        decrypted_text = fe.decrypt(bytes(text, "utf-8"))
        with open("output\decrypted.txt", "wb") as f:
            f.write(decrypted_text)
        print(
            f"Decrypted text will be saved to{color.BOLD}{color.YELLOW} decrypted.txt{color.END}"
        )
        Sec()
    # ? This part of the code takes input from a file given by user
    elif ask_file == "f":
        path_file = input("Enter the file path: ")
        with open(f"{path_file}", "rb") as file_decrypt:
            decrypted_text = fe.decrypt(file_decrypt.read())
        with open("output\decrypted.txt", "wb") as f:
            f.write(decrypted_text)
        print(
            f"Decrypted text will besaved to{color.BOLD}{color.YELLOW} decrypted.txt\n{color.END}"
        )
        Sec()
    elif ask_file == "b":
        Main()

    else:
        print(color.RED, "Invalid input", color.END)
        Main()


# ? This is the key generator
def Keygen():
    key = Fernet.generate_key()
    print("Your random key is generated!\n")

    ask_save = input("Do you want to save your key as txt file yes(y), no(n): ")

    if ask_save == "y":
        with open("output\keygen.txt", "wb") as f:
            f.write(key)
        print(
            f"Your key will be saved to{color.BOLD}{color.YELLOW} keygen.txt{color.END}"
        )
        Sec()

    elif ask_save == "n":
        print(f"Here is your key: {color.LIGHT_BLUE} {key}{color.END}")
        Sec()

    else:
        print(color.RED, "Invalid input", color.END)
        Main()


# ? This is the secondary function for program
def Sec():
    pass
    ask = input("Do you want to go back yes(y), no(n): ")
    if ask == "y":
        Main()

    elif ask == "n":
        print("Exiting...")

    else:
        print(color.RED, "Invalid input", color.END)
        Sec()


# ? This is the Main function for program
def Main():
    choise = input(
        "What you want to do? encrypt(e), decrypt(d), key generator(kg), quit(q): "
    )
    if choise == "e":
        has_key = input("Do you have a key yes(y), no(n) back(b): ")

        if has_key == "y":
            key = bytes(input("Please enter your key: "), "utf-8")
            Encrypt(key)

        elif has_key == "n":
            print("Program will generate random key for you.")
            key = Fernet.generate_key()
            with open("output\key.txt", "wb") as f:
                f.write(key)

            print(
                f"Your key will be saved to{color.BOLD}{color.YELLOW} key.txt{color.END}"
            )
            Encrypt(key)

        elif has_key == "b":
            Main()

        else:
            print(color.RED, "Invalid input", color.END)
            Main()

    elif choise == "d":
        Decrypt()

    elif choise == "kg":
        Keygen()

    elif choise == "q":
        exit()
    else:
        print(color.RED, "Invalid input", color.END)
        Main()


Main()
