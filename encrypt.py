from cryptography.fernet import Fernet
from os import path, mkdir, remove, listdir, walk
from zipfile import ZipFile
import color


def encrypt():
    while True:
        # * Get key
        has_key = input("Do you have a key yes(y), no(n): ")
        if has_key == "y":
            key = bytes(input("Please enter your key: "), "utf-8")
            try:
                fe = Fernet(key)
            except ValueError:
                print(color.RED, "Invalid input. Your key must be 32 bytes", color.END)
                continue

        elif has_key == "n":
            print("Program will generate random key for you.")
            from keygen import keygen

            key = keygen()

        else:
            print(color.RED, "Invalid input", color.END)
            continue

        # * Get type
        fe = Fernet(key)
        ask_type = input("Select input type: text(t), file(f), folder(fo): ")

        # * Text
        if ask_type == "t":
            while True:
                text = input("Enter text for encrypting with random key: ")
                encrypted_text = fe.encrypt(bytes(text, "utf-8"))
                if not path.exists("output"):
                    mkdir("output")
                file_path = path.join("output", "encrypted.txt")
                with open(file_path, "wb") as f:
                    f.write(encrypted_text)
                print(
                    f"Encrypted text will be saved to{color.BOLD}{color.YELLOW} encrypted.txt\n{color.END}"
                )
                break

        # * File
        elif ask_type == "f":
            while True:
                file_path = input("Enter the file path: ")
                if not path.isfile(file_path):
                    print(color.RED, "Invalid input. File not found.", color.END)
                    continue
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
                break

        # * Folder
        elif ask_type == "fo":
            while True:
                folder_path = input("Enter folder path: ")
                if not path.isdir(folder_path):
                    print(color.RED, "Invalid input,", color.END)
                    continue

                # * Zip
                with ZipFile(f"{folder_path}.zip", "w") as zip:
                    for root, dirs, files in walk(folder_path):
                        for file in files:
                            zip.write(path.join(root, file))

                # * Encryption
                with open(f"{folder_path}.zip", "rb") as zip_encrypt:
                    encrypted_text = fe.encrypt(zip_encrypt.read())
                    if not path.exists("output"):
                        mkdir("output")
                    folder_path = path.join("output", folder_path)
                with open(folder_path + ".encrypted", "wb") as z:
                    z.write(encrypted_text)
                remove(f"{folder_path}.zip")
                print(
                    f"Encrypted text will be saved to{color.BOLD}{color.YELLOW} {folder_path + '.encrypted'}\n{color.END}"
                )
                break

        else:
            print(color.RED, "Invalid input", color.END)
            continue
