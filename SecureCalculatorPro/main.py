from calculator import Calculator
from exceptions import InvalidInputError, DivisionByZeroError
from logger import log_error

calc = Calculator()

while True:

    print("\n====== Secure Calculator Pro ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. View Error Report")
    print("7. Analytics")
    print("8. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice in ["1", "2", "3", "4"]:

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except:
                raise InvalidInputError("Only numbers are allowed.")

            if choice == "1":
                result = calc.add(num1, num2)

            elif choice == "2":
                result = calc.subtract(num1, num2)

            elif choice == "3":
                result = calc.multiply(num1, num2)

            elif choice == "4":
                result = calc.divide(num1, num2)

            else:
                result = None

        elif choice == "5":
            calc.history()
            continue

        elif choice == "6":
            calc.errors()
            continue

        elif choice == "7":
            calc.analytics()
            continue

        elif choice == "8":
            print("Thank you!")
            break

        else:
            raise InvalidInputError("Invalid Menu Choice")

    except DivisionByZeroError as e:
        print(e)
        log_error("DivisionByZeroError : " + str(e))

    except InvalidInputError as e:
        print(e)
        log_error("InvalidInputError : " + str(e))

    except Exception as e:
        print("Unexpected Error:", e)
        log_error(str(e))

    else:
        print("Result =", result)

    finally:
        print("Operation Completed.")