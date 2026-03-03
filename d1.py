num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

op = input("Enter operation from (+, -, *, /): ")
result = ((op == "+") and (int(num1) + int(num2))) or \
        ((op == "-") and (int(num1) - int(num2))) or \
        ((op == "*") and (int(num1) * int(num2))) or \
        ((op == "/") and (float(num1) / float(num2)))
print("Result: ", result)