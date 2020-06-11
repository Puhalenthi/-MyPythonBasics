num = int(input('Enter the number of rows:     '))

for i in range(num, num * 2):
    lst = [' '] * i
    length = len(lst) - 1
    if i == num:
        x = length
    for counter in range(length, x - 1, -1):
        lst[counter] = '*'
    x -= 1
    finallst = ''
    for item in lst:
        finallst += item
        finallst += ' '
    print(finallst)

