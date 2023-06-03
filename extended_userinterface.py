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


class CalculatorUI(Calculator):
    def __init__(self):
        super().__init__()

    def start(self):
        self.display_welcome_message()
        super().start()
        self.display_goodbye_message()

    def display_welcome_message(self):
        print("Welcome to the Calculator!")

    def display_goodbye_message(self):
        print("Thank you for using the Calculator!")

    def perform_calculation(self):
        super().perform_calculation()
        # Additional calculations or modifications can be
