from cryptography.fernet import Fernet
import os
import color


def keygen():
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

    elif ask_save == "n":
        print(f"Here is your key: {color.LIGHT_BLUE} {key}{color.END}")

    else:
        print(color.RED, "Invalid input", color.END)
