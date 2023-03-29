from cryptography.fernet import Fernet
from os import path, mkdir, remove, listdir
import color


def encrypt():
    # ? Get key
    has_key = input("Do you have a key yes(y), no(n): ")
    if has_key == "y":
        key = bytes(input("Please enter your key: "), "utf-8")
        try:
            fe = Fernet(key)
        except ValueError:
            print(color.RED, "Invalid input. Your key must be 32 bytes", color.END)
            encrypt()

    elif has_key == "n":
        print("Program will generate random key for you.")
        key = Fernet.generate_key()
        file_path = path.join("output", "key.txt")
        with open(file_path, "wb") as f:
            f.write(key)
        print(f"Your key will be saved to{color.BOLD}{color.YELLOW} key.txt{color.END}")

    else:
        print(color.RED, "Invalid input", color.END)
        encrypt()

    # ? Get method
    fe = Fernet(key)
    ask_type = input("Select input type: text(t), file(f), folder(fo): ")

    # ? Text
    if ask_type == "t":
        text = input("Enter text for encrypting with random key: ")
        encrypted_text = fe.encrypt(bytes(text, "utf-8"))
        file_path = path.join("output", "encrypted.txt")
        with open(file_path, "wb") as f:
            f.write(encrypted_text)
        print(
            f"Encrypted text will be saved to{color.BOLD}{color.YELLOW} encrypted.txt\n{color.END}"
        )

    # ? File
    elif ask_type == "f":
        file_path = input("Enter the file path: ")

        if not path.isfile(file_path):
            print(color.RED, "Invalid input. File not found.", color.END)
            encrypt()
        with open(f"{file_path}", "rb") as file_encrypt:
            encrypted_text = fe.encrypt(file_encrypt.read())
            if not path.exists("output"):
                mkdir("output")
            file_path = path.join("output", file_path)
        with open(file_path + ".encrypted", "wb") as f:
            f.write(encrypted_text)
        print(
            f"Encrypted text will be saved to{color.BOLD}{color.YELLOW} {file_path + '.encrypted'}\n{color.END}"
        )
        remove(file_path)

    # ? Entire Folder
    elif ask_type == "fo":
        folder_path = input("Enter folder path: ")
        if path.isdir(folder_path) is False:
            print(color.RED, "Invalid input,", color.END)
            encrypt()

        for filename in listdir(folder_path):
            if path.isfile(path.join(folder_path, filename)):
                with open(f"{folder_path}/{filename}", "rb") as f:
                    original = f.read()
                encrypted = fe.encrypt(original)
                with open(
                    f"{folder_path}/{filename}" + ".encrypted", "wb"
                ) as encrypted_file:
                    encrypted_file.write(encrypted)
                remove(f"{folder_path}/{filename}")

    else:
        print(color.RED, "Invalid input", color.END)
        encrypt()
