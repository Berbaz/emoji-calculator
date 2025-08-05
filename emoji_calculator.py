# 🧮 Welcome to the Emoji Calculator 🎉
print("Welcome to the 🧮 Emoji Calculator 🎉")
print("This calculator can do ➕ Addition, ➖ Subtraction, ✖️ Multiplication, and ➗ Division!")
print("--------------------------------------------------")

def perform_operation(num1, num2, operator):
    """Performs the selected mathematical operation"""
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "🚫 Error: Division by zero is not allowed!"
            return num1 / num2
        else:
            return "🚫 Invalid operator!"
    except Exception as e:
        return f"🚫 An unexpected error occurred: {e}"

def get_float_input(prompt):
    """Gets a valid float input from the user"""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("⚠️ Please enter a valid number!")

def calculator():
    choice = input("Would you like to enter the full expression (like 10 + 5)? Type 'yes' or 'no': ").lower()

    if choice == "yes":
        expression = input("Enter the expression (e.g., 10 + 5): ")
        try:
            # Split the expression by space
            parts = expression.strip().split()
            if len(parts) != 3:
                print("⚠️ Please enter the expression in the format: number operator number (e.g., 10 + 5)")
                return

            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])

            result = perform_operation(num1, num2, operator)
            print(f"✅ Result: {num1} {operator} {num2} = {result}")
        except ValueError:
            print("⚠️ Invalid number format.")
    else:
        num1 = get_float_input("Enter the first number: ")
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = get_float_input("Enter the second number: ")

        result = perform_operation(num1, num2, operator)
        print(f"✅ Result: {num1} {operator} {num2} = {result}")

# Run the calculator
calculator()

print("🎉 Thanks for using the Emoji Calculator! Goodbye! 👋")
