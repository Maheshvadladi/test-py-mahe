#Simple Calculator
import math
from tokenize import Double


print("Select an operation to perform")
print("1 Add")
print("2 Subtraction")
print("3 Multiplication")
print("4 Divison")
print("5 Modulus")
print("6 Power")

operation = input()

if operation == "1":
    num1 = input("Enter the first number : ")
    num2 = input("Enter the second number : ")
    if (num1.isnumeric() and num2.isnumeric()):
        sum  = int(num1) + int(num2)
        print("Sum of 2 numbers : " +str(sum))
    else:
        print("Enter integer values")
elif operation == "2":
    num1 = input("Enter the first number : ")
    num2 = input("Enter the second number : ")
    if (num1.isnumeric() and num2.isnumeric()):
        sub = int(num1) - int(num2)
        print("Subtraction of 2 numbers : " +str(sub))
    else:
        print("Enter integer values")
elif operation == "3":
    num1 = input("Enter the first number : ")
    num2 = input("Enter the second number : ")
    if (num1.isnumeric() and num2.isnumeric()):
        mult = int(num1) * int(num2)
        print("Multiplying 2 numbers : " +str(mult))
    else:
        print("Enter integer values")
elif operation == "4":
    num1 = input("Enter the first number : ")
    num2 = input("Enter the second number : ")
    if (num1.isnumeric() and num2.isnumeric()):
        div = int(num1) / int(num2)
        print("Divison of 2 numbers : " +str(div))
    else:
        print("Enter integer values")
elif operation == "5":
    num1 = input("Enter the first number : ")
    num2 = input("Enter the second number : ")
    if (num1.isnumeric() and num2.isnumeric()):
        mod = int(num1) % int(num2)
        print("Modulus of 2 numbers : " +str(mod))
    else:
        print("Enter integer values")
elif operation == "6":
    num = input("Enter the number : ")
    n = input("Enter the power : ")
    if (num.isnumeric() and n.isnumeric()):
        pow = int(num) ** int(n)
        print("Power of numbers : " +str(pow))
    else:
        print("Enter integer values")
else:
    print("Enter the given operations")