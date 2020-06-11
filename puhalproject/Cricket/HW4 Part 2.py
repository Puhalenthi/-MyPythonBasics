num = int(input('Enter the number of rows:      '))

for i in range(num * 2, num, -1):
    lst = [' '] * (i - 1)
    length = len(lst) - 1
    if i == num * 2:
        x = 0
    for counter in range(x, length + 1):
        lst[counter] = '*'
    x += 1
    finallst = ''
    for item in lst:
        finallst += item + ' '
    print(finallst)