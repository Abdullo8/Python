num1 = float(input("Enter first number: "))
op = input("Enter(+,-,*,/) ")
num2 = float(input("Enter second number:  "))


if op == "+":
    result = num1 + num2

if op == "-":
    result = num1 - num2

if op == "*":
    result = num1 * num2

if op == "/":
    result = num1 / num2
print("Result: " + str(result))