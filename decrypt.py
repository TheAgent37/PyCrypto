from cryptography.fernet import Fernet
from os import path, mkdir, rename
import color


def decrypt():
    while True:
        # * Get key
        key = bytes(input("Please enter your key: \n"), "UTF-8")
        try:
            fe = Fernet(key)
        except ValueError:
            print(color.RED, "Invalid input. Your key should be 32 bytes", color.END)
            continue

        # * Get type
        ask_type = input("Select input type: text(t), file(f): ")
        fe = Fernet(key)

        # * Text
        if ask_type == "t":
            while True:
                text = input("Enter encrypted test: \n")
                try:
                    decrypted_text = fe.decrypt(bytes(text, "utf-8"))
                except:
                    print(
                        color.RED,
                        "Err! Encrypted text and key doesn't match.",
                        color.END,
                    )
                    continue
                decrypted_text = fe.decrypt(bytes(text, "utf-8"))
                if not path.exists("output"):
                    mkdir("output")
                file_path = path.join("output", "decrypted.txt")
                with open(file_path, "wb") as f:
                    f.write(decrypted_text)
                print(
                    f"Decrypted text will be saved to{color.BOLD}{color.YELLOW} decrypted.txt{color.END}"
                )
                break

        # * File
        elif ask_type == "f":
            while True:
                file_path = input("Enter the file path: ")
                if not path.exists(file_path):
                    print(color.RED, "Invalid input. File not found.", color.END)
                    continue
                with open(file_path, "rb") as file_decrypt:
                    text = file_decrypt.read()
                    try:
                        decrypted_text = fe.decrypt(text)
                    except:
                        print(
                            color.RED,
                            "Err! Encrypted text and key doesn't match.",
                            color.END,
                        )
                        continue
                    decrypted_text = fe.decrypt(text)
                    # if not path.exists("output"):
                    #     mkdir("output")
                    # file_path = path.join("output", file_path)
                with open(file_path, "wb") as f:
                    f.write(decrypted_text)
                new_path = file_path[: file_path.rfind(".")]
                rename(file_path, new_path)
                print(
                    f"Decrypted text will besaved to{color.BOLD}{color.YELLOW} {new_path} \n{color.END}"
                )
                break

        else:
            print(color.RED, "Invalid input", color.END)
            continue
