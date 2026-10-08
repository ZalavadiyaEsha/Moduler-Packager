import datetime
import math
import random
import uuid
import file_operations
def datetime_operations():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            current = datetime.datetime.now()
            print("\nCurrent Date and Time:", current.strftime("%Y-%m-%d %H:%M:%S"))
            print("========================")
        elif choice == "2":
            date1 = input("Enter the first date (YYYY-MM-DD): ")
            date2 = input("Enter the second date (YYYY-MM-DD): ")
            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
            difference = abs((d2 - d1).days)
            print("Difference:", difference, "days")
            print("========================")
        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            d = datetime.datetime.strptime(date, "%Y-%m-%d")
            print("Formatted Date:", d.strftime("%d-%m-%Y"))
            print("========================")
        elif choice == "4":
            import time
            print("Stopwatch started...")
            input("Press Enter to stop stopwatch.")
            print("Stopwatch stopped.")
        elif choice == "5":
            import time
            seconds = int(input("Enter time in seconds: "))
            while seconds > 0:
                print("Time left:", seconds, "seconds")
                time.sleep(1)
                seconds = seconds - 1
            print("Time's up!")
        elif choice == "6":
            break
        else:
            print("Invalid choice!")
def mathematical_operations():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            number = int(input("\nEnter a number: "))
            factorial = math.factorial(number)
            print("Factorial:", factorial)
            print("========================")
        elif choice == "2":
            principal = float(input("\nEnter principal amount: "))
            rate = float(input("Enter rate of interest (in %): "))
            time = float(input("Enter time (in years): "))
            amount = principal * (1 + rate / 100) ** time
            compound_interest = amount - principal
            print("Compound Interest:", round(compound_interest, 2))
            print("========================")
        elif choice == "3":
            angle = float(input("\nEnter angle in degrees: "))
            radians = math.radians(angle)
            print("Sin:", round(math.sin(radians), 2))
            print("Cos:", round(math.cos(radians), 2))
            print("Tan:", round(math.tan(radians), 2))
            print("========================")
        elif choice == "4":
            print("\n1. Circle")
            print("2. Rectangle")
            print("3. Triangle")
            shape = input("Enter your choice: ")
            if shape == "1":
                radius = float(input("Enter radius: "))
                area = math.pi * radius * radius
                print("Area of Circle:", round(area, 2))
            elif shape == "2":
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = length * width
                print("Area of Rectangle:", area)
            elif shape == "3":
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = 0.5 * base * height
                print("Area of Triangle:", area)
            else:
                print("Invalid choice!")
            print("========================")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
def random_data_generation():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            number = random.randint(1, 100)
            print("Random Number:", number)
            print("========================")
        elif choice == "2":
            numbers = []
            for i in range(5):
                numbers.append(random.randint(1, 100))
            print("Random List:", numbers)
            print("========================")
        elif choice == "3":
            length = int(input("\nEnter password length: "))
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$!"
            password = ""
            for i in range(length):
                password = password + random.choice(characters)
            print("Generated Password:", password)
            print("========================")
        elif choice == "4":
            otp = random.randint(100000, 999999)
            print("Generated OTP:", otp)
            print("========================")
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
def generate_uuid():
    print("\nGenerate Unique Identifiers:")
    print()
    unique_id = uuid.uuid4()
    print("Generated UUID:", unique_id)
    print("========================")
def file_operations_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            file_operations.create_file()
        elif choice == "2":
            file_operations.write_file()
        elif choice == "3":
            file_operations.read_file()
        elif choice == "4":
            file_operations.append_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")
def explore_module():
    print("\nExplore Module Attributes:")
    module_name = input("Enter module name to explore: ")
    if module_name == "math":
        print("Available Attributes in math module:")
        attributes = dir(math)
        print(attributes)
    elif module_name == "random":
        print("Available Attributes in random module:")
        attributes = dir(random)
        print(attributes)
    elif module_name == "datetime":
        print("Available Attributes in datetime module:")
        attributes = dir(datetime)
        print(attributes)
    else:
        print("Module not supported!")
def main():
    while True:
        print("\n========================")
        print("Welcome to Multi-Utility Toolkit")
        print("========================")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("========================")
        choice = input("Enter your choice: ")
        if choice == "1":
            datetime_operations()
        elif choice == "2":
            mathematical_operations()
        elif choice == "3":
            random_data_generation()
        elif choice == "4":
            generate_uuid()
        elif choice == "5":
            file_operations_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("\n========================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("========================")
            break
        else:
            print("Invalid choice! Please try again.")
main()