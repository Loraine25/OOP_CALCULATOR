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

    def perform_calculation(self):

# Choosing Operation
        operation = input(
            '"+" for addition\n'
            '"-" for subtraction\n'
            '"*" for multiplication\n'
            '"/" for division\n'
            'Select an operation: '
        )

# Ask to enter first and second number
        first_number = float(input("\033[;33m" "Enter the 1st number: "))
        second_number = float(input("\033[;33m" "Enter the 2nd number: "))

# If the user wants addition
        if operation == "+":
            self.addition(first_number, second_number)

# If the user wants subtraction
        elif operation == "-":
            self.subtraction(first_number, second_number)

# If the user wants multiplication
        elif operation == "*":
            self.multiplication(first_number, second_number)

# If the user wants division
        elif operation == "/":
            self.division(first_number, second_number)

    @staticmethod
    def addition(first_number, second_number):
        print(first_number, "+", second_number)
        result = first_number + second_number
        print("The result is:", "\033[;3m" + str(result) + "\033[;m")

    @staticmethod
    def subtraction(first_number, second_number):
        print(first_number, "-", second_number)
        result = first_number - second_number
        print("The difference:", "\033[;3m" + str(result) + "\033[;m")

    @staticmethod
    def multiplication(first_number, second_number):
        print(first_number, "*", second_number)
        result = first_number * second_number
        print("The product:", "\033[;3m" + str(result) + "\033[;m")

    @staticmethod
    def division(first_number, second_number):
        try:
            print(first_number, "/", second_number)
            result = first_number / second_number
            print("The quotient:", "\033[;3m" + str(result) + "\033[;m")
        except ZeroDivisionError as error:
            print("\033[1;31m" "Invalid equation\n")
            print(error)
            print("\nTry again, please insert a non-zero number")

    def ask_for_retry(self):
        while True:
            try:
                retry = input("\nDo you want to perform another calculation? (yes/no): ")
                if retry.lower() == "yes":
                    print("")
                    break
                elif retry.lower() == "no":
                    print("\033[;33m" + "Thank you for your hard work." + "\033[;3m")
                    print("")
                    self.retry = False
                    break
                else:
                    raise ValueError("Invalid Input")
            except ValueError:
                print("Invalid Input. Please enter 'yes' or 'no'.")

# Create an instance of the Calculator class
calc = Calculator()

# Start the calculator program
calc.start()