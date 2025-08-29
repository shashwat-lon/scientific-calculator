# Scientific Calculator in Python (Console Based)

import math

def scientific_calculator():
    print("🔢 Scientific Calculator")
    print("Available operations: add, sub, mul, div, sqrt, pow, sin, cos, tan, log, exp, exit")

    while True:
        op = input("\nEnter operation: ").lower()

        if op == "exit":
            print("Exiting calculator... 👋")
            break

        try:
            if op in ["add", "sub", "mul", "div", "pow"]:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                if op == "add":
                    print("Result =", x + y)
                elif op == "sub":
                    print("Result =", x - y)
                elif op == "mul":
                    print("Result =", x * y)
                elif op == "div":
                    print("Result =", x / y if y != 0 else "Error (divide by zero)")
                elif op == "pow":
                    print("Result =", math.pow(x, y))

            elif op in ["sqrt", "sin", "cos", "tan", "log", "exp"]:
                x = float(input("Enter number: "))

                if op == "sqrt":
                    print("Result =", math.sqrt(x))
                elif op == "sin":
                    print("Result =", math.sin(math.radians(x)))
                elif op == "cos":
                    print("Result =", math.cos(math.radians(x)))
                elif op == "tan":
                    print("Result =", math.tan(math.radians(x)))
                elif op == "log":
                    print("Result =", math.log(x))
                elif op == "exp":
                    print("Result =", math.exp(x))

            else:
                print("❌ Invalid operation, try again!")

        except Exception as e:
            print("Error:", e)

# Run the calculator
scientific_calculator()
