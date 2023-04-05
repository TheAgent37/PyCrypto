from cryptography.fernet import Fernet
from os import path, mkdir
import color


def keygen(asym=None):
    # * asymetric key generation
    if asym:
        from cryptography.hazmat.primitives.asymmetric import rsa
        from cryptography.hazmat.primitives import serialization

        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        public_key_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )

        private_key_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.SubjectPrivateKeyInfo,
        )

        while True:
            ask_save = input("Do you want to save your key as txt file yes(y), no(n): ")

            if ask_save == "y":
                if not path.exists("output"):
                    mkdir("output")
                file_path = path.join("output", "private.key")
                with open(file_path, "wb") as f:
                    f.write(private_key_bytes)
                file_path = path.join("output", "public.key")
                with open(file_path, "wb") as f:
                    f.write(public_key_bytes)
                print(
                    f"Your key will be saved to{color.BOLD}{color.YELLOW} output{color.END}"
                )
                break
            elif ask_save == "n":
                print(f"Here is your key: {color.LIGHT_BLUE} {str(key)}{color.END}")
                break
            else:
                print(color.RED, "Invalid input", color.END)
                continue

    # * symetric key generation
    else:
        key = Fernet.generate_key()
        print("Your random key is generated!\n")

        while True:
            ask_save = input("Do you want to save your key as txt file yes(y), no(n): ")

            if ask_save == "y":
                if not path.exists("output"):
                    mkdir("output")
                file_path = path.join("output", "key.key")
                with open(file_path, "wb") as f:
                    f.write(key)
                print(
                    f"Your key will be saved to{color.BOLD}{color.YELLOW} key.key{color.END}"
                )
                return key
            elif ask_save == "n":
                print(f"Here is your key: {color.LIGHT_BLUE} {str(key)}{color.END}")
                return key

            else:
                print(color.RED, "Invalid input", color.END)
                continue
