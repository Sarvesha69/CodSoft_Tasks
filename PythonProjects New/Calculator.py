def show_menu():
    print("\n--- Basic Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

def get_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numbers.")
        return None, None

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is undefined!"
    return num1 / num2

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
        
        num1, num2 = get_numbers()
        if num1 is None: 
            continue
        
        if choice == '1':
            print(f"The result of addition is: {addition(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction is: {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication is: {multiplication(num1, num2)}")
        elif choice == '4':
            print(f"The result of division is: {division(num1, num2)}")
        else:
            print("Invalid choice! Please pick a number between 1 and 5.")

if __name__ == "__main__":
    main()
