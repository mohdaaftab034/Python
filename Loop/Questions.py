# 1 - 10 Even number
"""
1 - 10
2, 4, 6, 8, 10

1, 3, 5, 7, 9

%2 = 0 - Even number

2 % 3 = 1 
"""

for num in range(1, 11):
    if num % 2 == 0:
        # print('Even: ', num)
    else:
        # print('Odd: ', num)


"""
start
stop
step
skip
"""

start = int(input("Enter the start = "))
stop = int(input("Enter the stop = "))

skip = int(input('Number you want to skip = '))


for i in range(start, stop):
    if i == skip:
        continue
    print(i)