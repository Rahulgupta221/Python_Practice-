# Calc==>

num1 = int(input("Enter first number: "))
Operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))

if Operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif Operator == "-":
    result = num1 - num2
    print (f"{num1}-{num2} = {result}")
elif Operator =="*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif Operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:  
    print("Invalid operator. Please use +, -, *, or /.")
