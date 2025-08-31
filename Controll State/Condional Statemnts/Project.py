num_1 = float(input("Enter number 1 = "))
num_2 = float(input("Enter number 2 = "))


choice = input("Enter your choice + - * = ")

if choice == "+":
    print(f'Addition: {num_1 + num_2}')

elif choice == '-':
    print(f'Subtraction: {num_1 - num_2}')

elif choice == '*':
    print(f'Multiplication: {num_1 * num_2}')

elif choice == '/':
    print(f'Division: {num_1 / num_2}')

elif choice == '//':
    print(f'Double Modules: {num_1 // num_2}')

elif choice == '%':
    print(f'Modules: {num_1 % num_2}')

elif choice == '**':
    print(f'Square of the Number: {num_1 ** num_2}')

else: 
    print("In-Valid Choice");