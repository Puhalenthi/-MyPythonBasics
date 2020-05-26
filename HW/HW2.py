num = int(input('Give me the number of rows:        '))
for i in range(num, num * 2 - 1):
    currentline = [' '] * i
    length = len(currentline) - 1
    currentline[length] = 'A'
    if i > num:
        currentline[length - (2 * x)] = 'A'
    else:
        x = 0
    finalline = ''
    for letter in currentline:
        finalline += letter
    print(finalline)
    x += 1

print('A' * ((num * 2) - 1))