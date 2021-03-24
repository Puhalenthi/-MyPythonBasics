import tkinter as t
import time

screen = t.Tk()

screen.geometry('700x800')

screen.title('Puhal\'s Notepad Editor')

def savefile():
    global text3
    filename = textfilename.get()
    textinput = text.get('1.0', 'end')
    filename += '.txt'
    with open(filename, 'w') as f:
        f.write(textinput)
    
    previouscontent = text3['text']
    previouscontent += 'Successfully Saved File!\n\n'
    text3.config(text=previouscontent)
    screen.after(3)

def loadfile():
    global text3
    filename = textfilename1.get()
    filename += '.txt'
    try:
        with open(filename, 'r') as f:
            context = f.read()
    except FileNotFoundError:
        previouscontent = text3['text']
        previouscontent += 'File Does Not Exist\n\n'
        text3.config(text=previouscontent)
        text3.pack()
    else:        
        previouscontent = text3['text']
        previouscontent += 'Finished Loading!\n\n'
        text3.config(text=previouscontent)
        text.delete('1.0', 'end')
        text.insert('1.0', context)



#Text Box Creation
text = t.Text(master=screen)
text.pack()

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
label1 = t.Label(master=frame1, text='Type the File Name You Would Like To Load Here:  ')
label1.pack(side='left')
textfilename1 = t.Entry(master=frame1)
textfilename1.pack(side='left')
button1 = t.Button(master=frame1, text='Submit', width='7', height='2', command=loadfile)
button1.pack(side='left')

#Audit Log
text3 = t.Label(master=screen, text='Audit Log:\n\n')
text3.pack()

screen.mainloop()