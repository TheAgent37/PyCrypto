from cryptography.fernet import Fernet


print("Welcome to my encryption program!")
print("Please update me with bugs and your ideas.")

# ? This is the encryption code
def Encrypt(key):
    fe = Fernet(key)
    ask_file = input("Select input type: text(t), file(f), back(b): ")

    if ask_file == "t":
        text = input("Enter text for encrypting with random key: ")
        encrypted_text = fe.encrypt(bytes(text, "utf-8"))
        with open("encrypted.txt", "wb") as f:
            f.write(encrypted_text)
        print("Encrypted text will be saved to encrypted.txt\n")

    elif ask_file == "f":
        path_file = input("Enter the file path: ")
        with open(f"{path_file}", "rb") as file_encrypt:
            encrypted_text = fe.encrypt(file_encrypt.read())
        with open("encrypted.txt", "wb") as f:
            f.write(encrypted_text)
        print("Encrypted text will be saved to encrypted.txt\n")

    elif ask_file == "b":
        return Main()

    else:
        print("\033[31mInvalid input\033[39m")  # TODO integrate color.py file
        return Main()


# ? This is the decryption code
def Decrypt():
    key = input("Please enter your key: \n")
    ask_file = input("Select input type: text(t), file(f), back(b): ")
    fe = Fernet(key)

    if ask_file == "t":
        text = input("Enter encrypted test: \n")
        decrypted_text = fe.decrypt(bytes(text, "utf-8"))
        with open("decrypted.txt", "wb") as f:
            f.write(decrypted_text)
        print("Decrypted text will be saved to decrypted.txt")

    # ? This part of the code takes input from a file given by user
    elif ask_file == "f":
        path_file = input("Enter the file path: ")
        with open(f"{path_file}", "rb") as file_decrypt:
            decrypted_text = fe.decrypt(file_decrypt.read())
        with open("decrypted.txt", "wb") as f:
            f.write(decrypted_text)
        print("Decrypted text will besaved to decrypted.txt\n")

    elif ask_file == "b":
        Main()

    else:
        print("\033[31mInvalid input\033[39m")
        Main()


# ? This is the key generator
def Keygen():
    key = Fernet.generate_key()
    print("Your random key is generated!\n")

    ask_save = input("Do you want to save your key as txt file yes(y), no(n): ")

    if ask_save == "y":
        with open("keygen.txt", "wb") as f:
            f.write(key)
        print("Your key will be saved to keygen.txt")

    elif ask_save == "n":
        print(f"Here is your key{key}")

    else:
        print("\033[31mInvalid input\033[39m")
        Main()


# ? This is the secondary function for program
def sec():
    pass
    ask = input("Do you want to go back yes(y), no(n): ")
    if ask == "y":
        Main()

    elif ask == "n":
        print("Exiting...")
        exit()

    else:
        print("\033[31mInvalid input\033[39m")


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
            with open("key.txt", "wb") as f:
                f.write(key)

            print("Your key will be saved to key.txt")
            Encrypt(key)

        elif has_key == "b":
            Main()

        else:
            print("\033[31mInvalid input\033[39m")
            Main()

    elif choise == "d":
        Decrypt()

    elif choise == "kg":
        Keygen()

    elif choise == "q":
        exit()
    else:
        print("\033[31mInvalid input\033[39m")
        Main()


Main()
