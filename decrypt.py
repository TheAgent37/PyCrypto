from cryptography.fernet import Fernet
from os import path, mkdir
import color


def decrypt():
    # * Get key
    key = bytes(input("Please enter your key: \n"), "UTF-8")
    try:
        fe = Fernet(key)
    except ValueError:
        print(color.RED, "Invalid input. Your key should be 32 bytes", color.END)
        decrypt()

    # * Get type
    ask_type = input("Select input type: text(t), file(f): ")
    fe = Fernet(key)

    # * Text
    if ask_type == "t":
        text = input("Enter encrypted test: \n")
        try:
            decrypted_text = fe.decrypt(bytes(text, "utf-8"))
        except:
            print(color.RED, "Err! Encrypted text and key doesn't match.", color.END)
            decrypt()
        decrypted_text = fe.decrypt(bytes(text, "utf-8"))
        if not path.exists("output"):
            mkdir("output")
        file_path = path.join("output", "decrypted.txt")
        with open(file_path, "wb") as f:
            f.write(decrypted_text)
        print(
            f"Decrypted text will be saved to{color.BOLD}{color.YELLOW} decrypted.txt{color.END}"
        )

    # * File
    elif ask_type == "f":
        file_path = input("Enter the file path: ")
        try:
            with open(f"{file_path}", "rb") as file_decrypt:
                pass
        except FileNotFoundError:
            print(color.RED, "Invalid input. File not found.", color.END)
        with open(f"{file_path}", "rb") as file_decrypt:
            try:
                decrypted_text = fe.decrypt(bytes(text, "utf-8"))
            except:
                print(
                    color.RED, "Err! Encrypted text and key doesn't match.", color.END
                )
                decrypt()
            decrypted_text = fe.decrypt(file_decrypt.read())
            if not path.exists("output"):
                mkdir("output")
            file_path = path.join("output", "decrypted.txt")
        with open(file_path, "wb") as f:
            f.write(decrypted_text)
        print(
            f"Decrypted text will besaved to{color.BOLD}{color.YELLOW} decrypted.txt\n{color.END}"
        )

    else:
        print(color.RED, "Invalid input", color.END)
        decrypt()
