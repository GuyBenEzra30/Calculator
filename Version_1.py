while True:

    print("Please choose an option")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        print("You have chosen to Add")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(num1 + num2)

    elif choice == "2":
        print("You have chosen to Subtract")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        print(num1 - num2)

    elif choice == "3":
        print("You have chosen to Multiply")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 * num2)

    elif choice == "4":
        print("You have chosen to Divide")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Error! Division by zero is not allowed")
    
    elif choice == "5":
        print("Exiting the program")
        break
    else:
        print("Invalid choice. Please choose a valid option")
