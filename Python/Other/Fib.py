def fib():
    lst = [0, 1]
    userinput = int(input('How many numbers do you want:        '))
    if userinput <= 0:
        return 'Invalid Response Entered'
    else:
        userinput -= 2
    for _ in range(userinput):
        last1 = lst[-1]
        last2 = lst[-2]
        newnum = last1 + last2
        lst.append(newnum)
    print(lst)
    return 'Done'


print(fib())