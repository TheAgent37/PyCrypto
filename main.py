import color

# TODO: Add support for public, private keys
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


def main(wb):
    if wb:
        print("Welcome back!")
    choise = input(
        "Please select operation. encrypt(e), decrypt(d), key generator(kg), quit(q): "
    )
    # Encrypt
    if choise == "e":
        from encrypt import encrypt

        encrypt()
        main(True)

    # Decrypt
    elif choise == "d":
        from decrypt import decrypt

        decrypt()
        main(True)

    # Key Generator
    elif choise == "kg":
        from keygen import keygen

        keygen()
        main(True)

    # Exit
    elif choise == "q":
        exit()
    else:
        print(color.RED, "Invalid input", color.END)
        main(wb)


wb = False
main(wb)
