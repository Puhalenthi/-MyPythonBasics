import tkinter as tk
import time
import math

def addelement(num):
    previouscontent = inputoutput['text']
    newcontent = previouscontent + str(num)
    inputoutput['text'] = newcontent

def op(operator):
    global currentop, firstnum
    currentop = operator
    try:
        firstnum = int(inputoutput['text'])
    except:
        firstnum = float(inputoutput['text'])
    inputoutput['text'] = ''
    if operator == '√':
        calc()

def clear():
    global currentop
    currentop = ''
    inputoutput['text'] = ''

def calc():
    global firstnum, currentop
    if currentop != '√':
        try:
            secondnum = int(inputoutput['text'])
        except:
            secondnum = float(inputoutput['text'])
    if currentop == '+':
        calcresult = firstnum + secondnum
        inputoutput['text'] = calcresult
    elif currentop == '-':
        calcresult = firstnum - secondnum
        inputoutput['text'] = calcresult
    elif currentop == 'x':
        calcresult = firstnum * secondnum
        inputoutput['text'] = calcresult
    elif currentop == '/':
        try:
            calcresult = firstnum / secondnum
            inputoutput['text'] = calcresult
        except:
            calcresult = 'ERROR: CAN\'T DIVIDE BY 0'
            inputoutput['text'] = calcresult
    elif currentop == '^':
        calcresult = firstnum ** secondnum
        inputoutput['text'] = calcresult
    elif currentop == '√':
        calcresult = math.sqrt(firstnum)
        inputoutput['text'] = calcresult
    else:
        currentop = ''
        inputoutput['text'] = ''


screen = tk.Tk()

screen.title('Puhal\'s Calculator')

inputoutput = tk.Label(master=screen, text='')
inputoutput.grid(row=0, column=0, columnspan=5, padx='10', pady='10')

button1 = tk.Button(master=screen, text='1', width='10', height='5', command=lambda: addelement(1))
button2 = tk.Button(master=screen, text='2', width='10', height='5', command=lambda: addelement(2))
button3 = tk.Button(master=screen, text='3', width='10', height='5', command=lambda: addelement(3))
button4 = tk.Button(master=screen, text='4', width='10', height='5', command=lambda: addelement(4))
button5 = tk.Button(master=screen, text='5', width='10', height='5', command=lambda: addelement(5))
button6 = tk.Button(master=screen, text='6', width='10', height='5', command=lambda: addelement(6))
button7 = tk.Button(master=screen, text='7', width='10', height='5', command=lambda: addelement(7))
button8 = tk.Button(master=screen, text='8', width='10', height='5', command=lambda: addelement(8))
button9 = tk.Button(master=screen, text='9', width='10', height='5', command=lambda: addelement(9))
button0 = tk.Button(master=screen, text='0', width='10', height='5', command=lambda: addelement(0))
buttonadd = tk.Button(master=screen, text='+', width='10', height='5', command=lambda: op('+'))
buttonsub = tk.Button(master=screen, text='-', width='10', height='5', command=lambda: op('-'))
buttonmul = tk.Button(master=screen, text='x', width='10', height='5', command=lambda: op('x'))
buttondiv = tk.Button(master=screen, text='/', width='10', height='5', command=lambda: op('/'))
buttondot = tk.Button(master=screen, text='.', width='10', height='5', command=lambda: addelement('.'))
buttonsqrt = tk.Button(master=screen, text='√', width='10', height='5', command=lambda: op('√'))
buttonpower = tk.Button(master=screen, text='^', width='10', height='5', command=lambda: op('^'))
buttoncalc = tk.Button(master=screen, text='=', width='21', height='5', command=calc)
buttonclear = tk.Button(master=screen, text='Clear', width='10', height='5', command=clear)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
buttonadd.grid(row=1, column=3)
buttonsub.grid(row=2, column=3)
buttonmul.grid(row=3, column=3)
buttondiv.grid(row=4, column=3)
buttondot.grid(row=4, column=1)
buttonclear.grid(row=4, column=2)
buttonsqrt.grid(row=5, column=0)
buttonpower.grid(row=5, column=1)
buttoncalc.grid(row=5, column=2, columnspan=5)




screen.mainloop()