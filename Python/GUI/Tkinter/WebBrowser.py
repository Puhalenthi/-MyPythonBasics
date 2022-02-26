import tkinter
import webbrowser

screen = tkinter.Tk()

screen.title('Puhal\'s Search Engine')

screen.geometry('700x800')

def googlesearch():
    query = textbox.get()
    query = query.replace('+', '%2B')
    query = query.replace(' ', '+')
    link = 'https://www.google.com/search?q={}&ie=utf-8&oe=utf-8'.format(query)
    webbrowser.open_new_tab(link)
def bingsearch():
    query = textbox.get()
    query = query.replace('+', '%2B')
    query = query.replace(' ', '+')
    link = 'https://www.bing.com/search?q={}&ie=utf-8&oe=utf-8'.format(query)
    webbrowser.open_new_tab(link)
def duckduckgosearch():
    query = textbox.get()
    query = query.replace('+', '%2B')
    query = query.replace(' ', '+')
    link = 'https://duckduckgo.com/?q={}&va=b&t=hr&ia=web'.format(query)
    webbrowser.open_new_tab(link)
frame1 = tkinter.Frame(master=screen)
frame1.pack()
label1 = tkinter.Label(master=frame1, text='Type Something To Search Here:   ')
label1.pack(side='left')
textbox = tkinter.Entry(master=frame1)
textbox.pack(side='left')



frame2 = tkinter.Frame(master=screen)
frame2.pack()
button1 = tkinter.Button(master=frame2, text='Google', width='7', height='2', command=googlesearch)
button1.pack(side='left')
button2 = tkinter.Button(master=frame2, text='Bing', width='7', height='2', command=bingsearch)
button2.pack(side='left')
button3 = tkinter.Button(master=frame2, text='DuckDuckGo', width='11', height='2', command=duckduckgosearch)
button3.pack()

screen.mainloop()
