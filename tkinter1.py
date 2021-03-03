from tkinter import *
window=Tk();                                    #creating new blank window
window.title("welcome");                        #title presentation
txt=Entry(window,width=40)
txt.grid(column=20,row=13)
window.geometry('1000x1000')                      #mentioning size of window
lbl=Label(window,text="hello")                  #name to a window
lbl.grid(row=100,column=100)                    #size of label

def clicked():                                          #when button was clicked this executes
    lbl.configure(text="button was clicked sir")
b=Button(window,text="veera",command=clicked)                   #crating button
b.grid(column=1,row=2)                          #size of button
window.mainloop()

