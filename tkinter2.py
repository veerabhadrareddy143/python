from tkinter import *
v=Tk()
v.title("veeers calci")
e=Entry(v,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def click(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))



b1=Button(v,text="1",padx=30,pady=10,bg="blue",command=lambda :click(1))
b2=Button(v,text="2",padx=45,pady=10,bg="white",command=lambda :click(2))
b3=Button(v,text="3",padx=45,pady=10,bg="green",command=lambda :click(3))
b4=Button(v,text="4",padx=30,pady=10,bg="pink",command=lambda :click(4))
b5=Button(v,text="5",padx=45,pady=10,bg="yellow",command=lambda :click(5))
b6=Button(v,text="6",padx=45,pady=10,bg="orange",command=lambda :click(6))
b7=Button(v,text="7",padx=30,pady=10,bg="orange",command=lambda :click(7))
b8=Button(v,text="8",padx=45,pady=10,bg="orange",command=lambda :click(8))
b9=Button(v,text="9",padx=45,pady=10,bg="orange",command=lambda :click(9))
b0=Button(v,text="0",padx=30,pady=10,bg="red",command=lambda :click(0))
b=Button(v,text="+",padx=97,pady=10,bg="red",)
bs=Button(v,text="-",padx=30,pady=10,bg="red")
be=Button(v,text="=",padx=97,pady=10,bg="red")


b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)

b0.grid(row=4,column=0)
b.grid(row=4,column=1,columnspan=2)
bs.grid(row=5,column=0)
be.grid(row=5,column=1,columnspan=2)

v.mainloop()