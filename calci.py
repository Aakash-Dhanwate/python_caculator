print("Welcome to Python Calculator ")
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter choice (1/2/3/4): ").strip()

if choice == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 + num2)

elif choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 - num2)

elif choice == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 * num2)

elif choice == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("❌ Cannot divide by zero!")
    else:
        print("Result:", num1 / num2)

else:
    print("❌ Invalid input! Please enter 1, 2, 3, or 4.")

