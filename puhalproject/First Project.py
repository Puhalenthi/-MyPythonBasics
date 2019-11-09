num1 = input("What is number 1")
num2 = input("What is number 2")
operator = input("What is the operator. The operators are +,-,*,/,**,%")
num1 = int(num1)
num2 = int(num2)
if (operator == '+'):
    print("The answer is ", num1 + num2)
elif (operator == '-'):
    print(" The answer is ", num1 -num2)
elif (operator == '*'):
    print(" The answer is ", num1*num2)
elif (operator == '/'):
    print(" The answer is ", num1/num2)
elif (operator == '**'):
    print(" The answer is ", num1**num2)
elif (operator == '%'):
    print(" The answer is ", num1%num2)
else:
    print(" Whoops! Something went wrong.")