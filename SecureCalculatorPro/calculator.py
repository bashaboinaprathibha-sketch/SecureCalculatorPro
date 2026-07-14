from collections import Counter
from exceptions import DivisionByZeroError

class Calculator:

    def __init__(self):
        self.history_file = "history.txt"
        self.error_types = []

    def save_history(self, text):
        with open(self.history_file, "a") as file:
            file.write(text + "\n")

    def add(self, a, b):
        result = a + b
        self.save_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.save_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.save_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")

        result = a / b
        self.save_history(f"{a} / {b} = {result}")
        return result

    def history(self):
        try:
            with open(self.history_file, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No history found.")

    def errors(self):
        try:
            with open("error.log", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No error report found.")

    def analytics(self):
        calculations = 0

        try:
            with open(self.history_file, "r") as file:
                calculations = len(file.readlines())
        except:
            calculations = 0

        try:
            with open("error.log", "r") as file:
                lines = file.readlines()

            errors = len(lines)

            error_list = []

            for line in lines:
                if "DivisionByZeroError" in line:
                    error_list.append("DivisionByZeroError")
                elif "InvalidInputError" in line:
                    error_list.append("InvalidInputError")
                else:
                    error_list.append("Other")

            if error_list:
                common = Counter(error_list).most_common(1)[0][0]
            else:
                common = "None"

        except:
            errors = 0
            common = "None"

        print("\n===== Analytics =====")
        print("Total Calculations :", calculations)
        print("Total Errors :", errors)
        print("Most Common Error :", common)