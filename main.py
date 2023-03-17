import color

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
        import encrypt as e

        e.encrypt()
        main(True)

    # Decrypt
    elif choise == "d":
        import decrypt as d

        d.decrypt()
        main(True)

    # Key Generator
    elif choise == "kg":
        import keygen as kg

        kg.keygen()
        main(True)

    # Exit
    elif choise == "q":
        exit()
    else:
        print(color.RED, "Invalid input", color.END)
        main(wb)


wb = False
main(wb)
