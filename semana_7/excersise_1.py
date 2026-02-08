def add(current, number):
    return current + number

def subtract(current, number):
    return current - number

def multiply(current, number):
    return current * number

def divide(current, number):
    if number == 0:
        print("Error: Cannot divide by 0.")
        return current
    return current / number

def clear():
    return 0.0

def show_menu():
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")

def ask_number():
    while True:
        entry = input("Enter a number: ")
        try:
            return float(entry)
        except ValueError:
            print("Error: You must enter a valid number.")

def calculator():
    current_number = 0.0

    while True:
        print(f"\n📌 Current number: {current_number}")
        show_menu()
        option = input("Choose an option (1-6): ")

        if option == "1":
            current_number = add(current_number, ask_number())

        elif option == "2":
            current_number = subtract(current_number, ask_number())

        elif option == "3":
            current_number = multiply(current_number, ask_number())

        elif option == "4":
            current_number = divide(current_number, ask_number())

        elif option == "5":
            current_number = clear()
            print("Number reset to 0.")

        elif option == "6":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid option. Try")
