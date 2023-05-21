# Anonuevo, Loraine N.
# BSCpE 1-4
# OOP CALCULATOR

#Header
print("\033[;33;1;3m\033[10m" * 65)
print("\033[;33;1;3mHi! It's a pleasure to have you here!\033[0m".center(81))
print("\033[;33;1;3mಠ\033[10m" * 65)

#Request about the user's name.
print("")
print("\033[1;3mMy name is \033[;45;1;3mLoraine\033[0m")
your_name = input("\033[1;3mWhat is your name?\033[0m")
print("\033[;1;3mI'm glad that you're here!\033[;34;1;3m" + your_name + "\033[0m \033[;1;3m, sit back and learn with me!\033[0m")

class Calculator:
    def __init__(self):
        self.retry = True

    def start(self):
        print("\n")
        while self.retry:
            self.perform_calculation()
            self.ask_for_retry()