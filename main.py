import tkinter as tk
from tkinter import *
master = tk.Tk()
master.geometry("312x312")
master.resizable(0,0)
master.title("Your Calculator")
expression = ""
#Entry function
def entry(num):
    global expression
    expression = expression + str(num)
    input_text.set(expression)
#Clear function
def clear():
    global expression
    expression = ""
    input_text.set("0")
#Evaluation function
def equals():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression=""


input_text = StringVar()

input_frame=Frame(master,width=312,height=50,bd=0,highlightbackground="pink",highlightcolor="black",highlightthickness=1)
input_frame.pack(side=TOP)

input_box=Entry(input_frame,font=("arial",18),textvariable=input_text,width=50,bg="#eee",bd=0, justify=RIGHT)
input_box.grid(row=0,column=0)
input_box.pack(ipady=10)

button_frame=Frame(master,width=312,height=272.5,bg="pink")
button_frame.pack()

c=Button(button_frame,text="Clear",fg="black",width=32,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:clear()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
one=Button(button_frame,text="1",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(1)).grid(row=1,column=0,padx=1,pady=1)
two=Button(button_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(2)).grid(row=1,column=1,padx=1,pady=1)
three=Button(button_frame,text="3",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(3)).grid(row=1,column=2,padx=1,pady=1)
four=Button(button_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(4)).grid(row=2,column=0,padx=1,pady=1)
five=Button(button_frame,text="5",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(5)).grid(row=2,column=1,padx=1,pady=1)
six=Button(button_frame,text="6",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(6)).grid(row=2,column=2,padx=1,pady=1)
seven=Button(button_frame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(7)).grid(row=3,column=0,padx=1,pady=1)
eight=Button(button_frame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(8)).grid(row=3,column=1,padx=1,pady=1)
nine=Button(button_frame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(9)).grid(row=3,column=2,padx=1,pady=1)
zero=Button(button_frame,text="0",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command=lambda:entry(0)).grid(row=4,column=0,padx=1,pady=1)
add=Button(button_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:entry("+")).grid(row=1,column=3,padx=1,pady=1)
subtract=Button(button_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:entry("-")).grid(row=2,column=3,padx=1,pady=1)
multiply=Button(button_frame,text="*",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:entry("*")).grid(row=3,column=3,padx=1,pady=1)
divide=Button(button_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:entry("/")).grid(row=4,column=1,padx=1,pady=1)
decimal=Button(button_frame,text=".",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:entry(".")).grid(row=4,column=2,padx=1,pady=1)
equal=Button(button_frame,text="=",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=lambda:equals()).grid(row=4,column=3,padx=1,pady=1)

master.bind("1",lambda e:entry(1))
master.bind("2",lambda e:entry(2))
master.bind("3",lambda e:entry(3))
master.bind("4",lambda e:entry(4))
master.bind("5",lambda e:entry(5))
master.bind("6",lambda e:entry(6))
master.bind("7",lambda e:entry(7))
master.bind("8",lambda e:entry(8))
master.bind("9",lambda e:entry(9))
master.bind("0",lambda e:entry(0))
master.bind("<+>",lambda e:entry("+"))
master.bind("-",lambda e:entry("-"))
master.bind("<*>",lambda e:entry("*"))
master.bind("/",lambda e:entry("/"))
master.bind(".",lambda e:entry("."))
master.bind("<Return>",lambda e:equals())

master.mainloop()









