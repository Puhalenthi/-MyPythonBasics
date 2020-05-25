def triangle():
    num = int(input('Enter the number of rows:      '))
    for i in range(1, num + 1):
        if i == 1:
            x = 1
            print(' ' * num, 'A')
        elif i == num:
            print(' ', 'A' * num * 2)
        else:
            print(' ' * (num - i + 1), 'A', ' ' * ((x * 2) - 2), 'A')
            x += 1


triangle()