def DigitOfLife():
    userinput = input('Please enter you date of birth in the format YYYYMMDD:       ')
    if len(userinput) == 8 and userinput.isdigit():
        while len(userinput) > 1:
            sums = 0
            for i in userinput:
                sums += int(i)
            userinput = str(sums)
        return sums
    else:
        return 'Invalid Response Entered'
print(DigitOfLife())