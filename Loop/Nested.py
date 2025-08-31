for i in range(1, 3): #By default step is one
    """
    i = 1
        j = 3
        j = 4
        j = 5
        j = 6 Exclude
    i = 2
    i = 3 Exclude
    """
    for j in range(3, 6):
        print(f'{i}, {j}')