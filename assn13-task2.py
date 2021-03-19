from password import Password


def main():
    again = True
    while again:
        password = Password()
        password.setPassword(input("Enter a password (minimum of eight characters and needs two numbers): "))
        if password.isValid():
            print("Valid Password.")
        else:
            print(password.getErrorMessage())

        playAgain = input("Do you want to play again?(Y/N): ").upper()
        if playAgain == "Y":
            pass
        else:
            again = False
            print("Thanks for playing!")


main()
