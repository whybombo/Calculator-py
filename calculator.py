from functions import *

while True:
    print("Calculate! (only 2 numbers)")
    print("1 Addition")
    print("2 Subition")
    print("3 Multiplication")
    print("4 Division")
    print("Q Exit")

    choice = input("Enter your choice: ")
    if choice == 'q' or choice == 'Q':
        break

    num1 = float(input("Enter the 1st Number: "))
    num2 = float(input("Enter the 2nd Number: "))

    print("Calculating...")
    if choice == '1':
        addition(num1, num2)
    elif choice == '2':
        subtraction(num1, num2)
    elif choice == '3':
        multiplication(num1, num2)
    elif choice == '4':
        division(num1, num2)
    else:
        print("Not one of the choices, try again")

    print("\n")