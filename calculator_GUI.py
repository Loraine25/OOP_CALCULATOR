import tkinter as tk
from tkinter import messagebox

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.create_widgets()

    def create_widgets(self):
        # Label for operation selection
        operation_label = tk.Label(self.root, text="Select an operation:")
        operation_label.pack()

        # Radio buttons for operation selection
        self.operation_var = tk.StringVar()
        operations = ["+", "-", "*", "/"]
        for operation in operations:
            operation_radio = tk.Radiobutton(
                self.root,
                text=operation,
                variable=self.operation_var,
                value=operation
            )
            operation_radio.pack()

        # Entry fields for numbers
        self.first_number_entry = tk.Entry(self.root)
        self.first_number_entry.pack()
        self.second_number_entry = tk.Entry(self.root)
        self.second_number_entry.pack()

        # Calculate button
        calculate_button = tk.Button(self.root, text="Calculate", command=self.perform_calculation)
        calculate_button.pack()

    def perform_calculation(self):
        try:
            operation = self.operation_var.get()
            first_number = float(self.first_number_entry.get())
            second_number = float(self.second_number_entry.get())

            if operation == "+":
                result = first_number + second_number
            elif operation == "-":
                result = first_number - second_number
            elif operation == "*":
                result = first_number * second_number
            elif operation == "/":
                if second_number != 0:
                    result = first_number / second_number
                else:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
            else:
                messagebox.showerror("Error", "Invalid operation")
                return

            messagebox.showinfo("Result", f"The result is: {result}")

        except ValueError:
            messagebox.showerror("Error", "Invalid input")
            return

    def start(self):
        self.root.mainloop()

# Create the root window
root = tk.Tk()

# Create an instance of the CalculatorGUI class
calculator_gui = CalculatorGUI(root)

# Start the calculator program
calculator_gui.start()
