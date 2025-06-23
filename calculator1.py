

def perform_addition(a, b):
    """Function to add two numbers"""
    return a + b

def perform_subtraction(a, b):
    """Function to subtract two numbers"""
    return a - b

def perform_multiplication(a, b):
    """Function to multiply two numbers"""
    return a * b

def perform_division(a, b):
    """Function to divide two numbers"""
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero!"

def show_options():
    """Display calculator options"""
    print("\n--- Simple Calculator ---")
    print("Choose an operation:")
    print("[1] Addition")
    print("[2] Subtraction") 
    print("[3] Multiplication")
    print("[4] Division")
    print("[0] Quit")
    print("-" * 25)

def get_user_numbers():
    """Get two numbers from user"""
    while True:
        try:
            first_num = float(input("Enter first number: "))
            second_num = float(input("Enter second number: "))
            return first_num, second_num
        except:
            print("Please enter valid numbers!")

def run_calculator():
    """Main calculator function"""
    print("Welcome to Simple Calculator!")
    print("Calculator is starting...")
    
    while True:
        show_options()
        
        try:
            user_choice = int(input("Select option: "))
        except:
            print("Invalid input! Please enter a number.")
            continue
        
        if user_choice == 0:
            print("Thanks for using calculator!")
            break
        
        if user_choice in [1, 2, 3, 4]:
            num1, num2 = get_user_numbers()
            
            if user_choice == 1:
                answer = perform_addition(num1, num2)
                symbol = "+"
                
            elif user_choice == 2:
                answer = perform_subtraction(num1, num2)
                symbol = "-"
                
            elif user_choice == 3:
                answer = perform_multiplication(num1, num2)
                symbol = "*"
                
            elif user_choice == 4:
                answer = perform_division(num1, num2)
                symbol = "/"
            
            print(f"\nAnswer: {num1} {symbol} {num2} = {answer}")
            
        else:
            print("Invalid choice! Please select 1-4 or 0 to quit.")
        
        input("\nPress Enter to continue...")

# Start the calculator
if __name__ == "__main__":
    run_calculator()