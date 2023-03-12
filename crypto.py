from cryptography.fernet import Fernet
import color
import os

print(
    f"""
{color.CYAN}
|||||||| ||     || ||||||||     |||     ||||||   |||||||| ||    || ||||||||  |||||||  |||||||| 
   ||    ||     || ||          || ||   ||    ||  ||       |||   ||    ||    ||     || ||    || 
   ||    ||     || ||         ||   ||  ||        ||       ||||  ||    ||           ||     ||   
   ||    ||||||||| ||||||    ||     || ||   |||| ||||||   || || ||    ||     |||||||     ||    
   ||    ||     || ||        ||||||||| ||    ||  ||       ||  ||||    ||           ||   ||     
   ||    ||     || ||        ||     || ||    ||  ||       ||   |||    ||    ||     ||   ||     
   ||    ||     || ||||||||  ||     ||  ||||||   |||||||| ||    ||    ||     |||||||    ||   
{color.END}

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
        file_path = os.path.join("output", "encrypted.txt")
        with open(file_path, "wb") as f:
            f.write(encrypted_text)
        print(
            f"Encrypted text will be saved to{color.BOLD}{color.YELLOW} encrypted.txt\n{color.END}"
        )
        Main(True)

    elif ask_file == "f":
        path_file = input("Enter the file path: ")
        try:
            with open(f"{path_file}", "rb") as file_encrypt:
                encrypted_text = fe.encrypt(file_encrypt.read())
        except FileNotFoundError:
            print(color.RED, "Invalid input. File not found.", color.END)
            Encrypt(key)
        with open(f"{path_file}", "rb") as file_encrypt:
            encrypted_text = fe.encrypt(file_encrypt.read())
            file_path = os.path.join("output", "encrypted.txt")
        with open(file_path, "wb") as f:
            f.write(encrypted_text)
        print(
            f"Encrypted text will be saved to{color.BOLD}{color.YELLOW} encrypted.txt\n{color.END}"
        )
        Main(True)

    elif ask_file == "b":
        Main(True)

    else:
        print(color.RED, "Invalid input", color.END)
        Encrypt(key)


# ? This is the decryption code
def Decrypt(key):
    ask_file = input("Select input type: text(t), file(f), back(b): ")
    try:
        fe = Fernet(key)
    except ValueError:
        print(color.RED, "Invalid input. Your key should be 32 bytes", color.END)
        Decrypt()
    fe = Fernet(key)

    if ask_file == "t":
        text = input("Enter encrypted test: \n")
        try:
            decrypted_text = fe.decrypt(bytes(text, "utf-8"))
        except:
            print(color.RED, "Err! Encrypted text and key doesn't match.", color.END)
            Decrypt()
        decrypted_text = fe.decrypt(bytes(text, "utf-8"))
        file_path = os.path.join("output", "decrypted.txt")
        with open(file_path, "wb") as f:
            f.write(decrypted_text)
        print(
            f"Decrypted text will be saved to{color.BOLD}{color.YELLOW} decrypted.txt{color.END}"
        )
        Main(True)

    # ? This part of the code takes input from a file given by user
    elif ask_file == "f":
        path_file = input("Enter the file path: ")
        try:
            with open(f"{path_file}", "rb") as file_decrypt:
                pass
        except FileNotFoundError:
            print(color.RED, "Invalid input. File not found.", color.END)
        with open(f"{path_file}", "rb") as file_decrypt:
            try:
                decrypted_text = fe.decrypt(bytes(text, "utf-8"))
            except:
                print(
                    color.RED, "Err! Encrypted text and key doesn't match.", color.END
                )
                Decrypt(key)
            decrypted_text = fe.decrypt(file_decrypt.read())
            file_path = os.path.join("output", "decrypted.txt")
        with open(file_path, "wb") as f:
            f.write(decrypted_text)
        print(
            f"Decrypted text will besaved to{color.BOLD}{color.YELLOW} decrypted.txt\n{color.END}"
        )
        Main(True)

    elif ask_file == "b":
        Main(True)

    else:
        print(color.RED, "Invalid input", color.END)
        Decrypt(key)


# ? This is the key generator
def Keygen():
    key = Fernet.generate_key()
    print("Your random key is generated!\n")

    ask_save = input("Do you want to save your key as txt file yes(y), no(n): ")

    if ask_save == "y":
        file_path = os.path.join("output", "keygen.txt")
        with open(file_path, "wb") as f:
            f.write(key)
        print(
            f"Your key will be saved to{color.BOLD}{color.YELLOW} keygen.txt{color.END}"
        )
        Main(True)

    elif ask_save == "n":
        print(f"Here is your key: {color.LIGHT_BLUE} {key}{color.END}")
        Main(True)

    else:
        print(color.RED, "Invalid input", color.END)
        Main(True)


# ? This is the Main function for program
def Main(wb):
    if wb:
        print("Welcome back!")
    choise = input(
        "Please select operation. encrypt(e), decrypt(d), key generator(kg), quit(q): "
    )
    if choise == "e":
        has_key = input("Do you have a key yes(y), no(n) back(b): ")

        if has_key == "y":
            key = bytes(input("Please enter your key: "), "utf-8")
            try:
                fe = Fernet(key)
            except ValueError:
                print(
                    color.RED, "Invalid input. Your key should be 32 bytes", color.END
                )
                Main(True)
            Encrypt(key)

        elif has_key == "n":
            print("Program will generate random key for you.")
            key = Fernet.generate_key()
            file_path = os.path.join("output", "key.txt")
            with open(file_path, "wb") as f:
                f.write(key)

            print(
                f"Your key will be saved to{color.BOLD}{color.YELLOW} key.txt{color.END}"
            )
            Encrypt(key)

        elif has_key == "b":
            Main(wb)

        else:
            print(color.RED, "Invalid input", color.END)
            Main(wb)

    elif choise == "d":
        key = input("Please enter your key: \n")
        try:
            fe = Fernet(key)
        except ValueError:
            print(color.RED, "Invalid input. Your key should be 32 bytes", color.END)
            Main(wb)
        Decrypt(key)

    elif choise == "kg":
        Keygen()

    elif choise == "q":
        exit()
    else:
        print(color.RED, "Invalid input", color.END)
        Main(wb)


Main()
