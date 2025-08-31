age = int(input('Enter your age = '))

if (age >= 18 and age < 101):
    print("You can Vote")

elif age >= 101:
    print("Your age is greater then 100")

elif age <= 18:
    print("Invalid age")
    
else:
    print('Error incoured')