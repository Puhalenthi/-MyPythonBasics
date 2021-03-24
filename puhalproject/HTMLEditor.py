import tkinter as t
import webbrowser
import requests
import google
screen = t.Tk()
screen.title('Puhal\'s Python Code Editor')
screen.geometry('700x800')


def savefile():
    global text3, filenamelabel
    filename = textfilename.get()
    code = codebox.get('1.0', 'end')
    filename += '.htm'
    with open(filename, 'w') as f:
        f.write(code)
    filenamelabel['text'] = filename
    previouscontent = text3['text']
    previouscontent += 'Saved File!\n\n'
    text3.config(text=previouscontent)




def loadfile():
    global text3, filenamelabel
    filename = textfilename1.get()
    filename += '.htm'
    try:
        with open(filename, 'r') as f:
            context = f.read()
    except FileNotFoundError:
        previouscontent = text3['text']
        previouscontent += 'Please Enter A Valid File Name\n\n'
        text3.config(text=previouscontent)
        text3.pack()
    else:        
        previouscontent = text3['text']
        filenamelabel['text'] = filename
        previouscontent += 'Finished Loading!\n\n'
        text3.config(text=previouscontent)
        codebox.delete('1.0', 'end')
        codebox.insert('1.0', context)
        filenamelabel['text'] = filename

def loadwebpage():
    global text3
    weblink = textfilename3.get()
    newweblink = 'https://' + weblink
    code = requests.get(newweblink)
    code = code.text
    codebox.delete('1.0', 'end')
    codebox.insert('1.0', code)
    previouscontent = text3['text']
    previouscontent += 'Loaded Webpage HTML Source Code!\n\n'
    text3.config(text=previouscontent)
    text3.pack()


def runfile():
    global text3
    filename = textfilename2.get()
    filename += '.htm'
    filename = 'file:///Users/puhal/Desktop/Python/' + filename
    try:
        webbrowser.open_new_tab(filename)
    except:
        previouscontent = text3['text']
        previouscontent += 'Please Enter A Valid File Name\n\n'
        text3.config(text=previouscontent)

def openwebpage():
    global text3
    weblink = textfilename4.get()
    newweblink = 'https://' + weblink
    webbrowser.open_new_tab(newweblink)
    previouscontent = text3['text']
    previouscontent += 'Opened Webpage!\n\n'
    text3.config(text=previouscontent)
    text3.pack()

#File Name
filenamelabel = t.Label(master=screen, text='Untitled')
filenamelabel.pack()

#Text Box
codebox = t.Text(master=screen, tabs=26)
codebox.pack()

#Output Box
outputbox = t.Label(master=screen, text='Click Run To See Results')
outputbox.pack()

#Save File Code
frame = t.Frame(master=screen)
frame.pack()
label = t.Label(master=frame, text='Type The File Name You Would Like To Save As Here:  ')
label.pack(side='left')
textfilename = t.Entry(master=frame)
textfilename.pack(side='left')
button = t.Button(master=frame, text='Submit', width='7', height='2', command=savefile)
button.pack(side='left')

#Load File Code
frame1 = t.Frame(master=screen)
frame1.pack()
label1 = t.Label(master=frame1, text='Type The File Name You Would Like To Load Here:  ')
label1.pack(side='left')
textfilename1 = t.Entry(master=frame1)
textfilename1.pack(side='left')
button1 = t.Button(master=frame1, text='Submit', width='7', height='2', command=loadfile)
button1.pack(side='left')

#Run File Code
frame2 = t.Frame(master=screen)
frame2.pack()
label2 = t.Label(master=frame2, text='Type The File Name You Would Like To Run Here:  ')
label2.pack(side='left')
textfilename2 = t.Entry(master=frame2)
textfilename2.pack(side='left')
button2 = t.Button(master=frame2, text='Submit', width='7', height='2', command=runfile)
button2.pack(side='left')

#Load Webpage Code
frame3 = t.Frame(master=screen)
frame3.pack()
label3 = t.Label(master=frame3, text='Type The Webpage Link You Would Like To Load Here:    ')
label3.pack(side='left')
textfilename3 = t.Entry(master=frame3)
textfilename3.pack(side='left')
button3 = t.Button(master=frame3, text='Submit', width='7', height='2', command=loadwebpage)
button3.pack(side='left')

#Open Webpage Code
frame4 = t.Frame(master=screen)
frame4.pack()
label4 = t.Label(master=frame4, text='Type The Webpage Link You Would Like To Open Here:    ')
label4.pack(side='left')
textfilename4 = t.Entry(master=frame4)
textfilename4.pack(side='left')
button4 = t.Button(master=frame4, text='Submit', width='7', height='2', command=openwebpage)
button4.pack(side='left')

#Audit Log
text3 = t.Label(master=screen, text='Audit Log:\n\n')
text3.pack()

screen.mainloop()