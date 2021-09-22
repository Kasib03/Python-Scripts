from tkinter import *

root = Tk()
root.title("Calculator")
e= Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#Defing Function

def button_Click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
   
def button_Clear():
    e.delete(0,END)


def button_addition():
    first_num = e.get()
    global f_Number # Defining a global variable
    global math
    math="addition"
    f_Number=int(first_num)
    e.delete(0,END)

def button_subtract():
    first_num = e.get()
    global f_Number # Defining a global variable
    global math
    math="subtraction"
    f_Number=int(first_num)
    e.delete(0,END)

def button_multiply():
    first_num = e.get()
    global f_Number # Defining a global variable
    global math
    math="multiplication"
    f_Number=int(first_num)
    e.delete(0,END)
def button_division():
    first_num = e.get()
    global f_Number # Defining a global variable
    global math
    math="division"
    f_Number=int(first_num)
    e.delete(0,END)


def button_equal():
    second_num=e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0,f_Number + int(second_num))
    if math == "subtraction":
        e.insert(0,f_Number - int(second_num))
    if math == "multiplication":
        e.insert(0,f_Number * int(second_num))
    if math == "division":
        e.insert(0,f_Number / int(second_num))
    
#Defing Function


#Creating buttons (0-9)
button_1=Button(root,text="1",padx=40,pady=20,command=lambda:button_Click(1)) #Using "lambda" to pass in the values
button_2=Button(root,text="2",padx=40,pady=20,command=lambda:button_Click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda:button_Click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda:button_Click(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda:button_Click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda:button_Click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda:button_Click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda:button_Click(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda:button_Click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda:button_Click(0))
button_add=Button(root,text="+",padx=39,pady=20,command=button_addition)
button_sub=Button(root,text="-",padx=40,pady=20,command=button_subtract)
button_multi=Button(root,text="X",padx=40,pady=20,command=button_multiply)
button_div=Button(root,text="/",padx=40,pady=20,command=button_division)
button_eq=Button(root,text="=",padx=40,pady=20,command=button_equal)
button_clear=Button(root,text="C",padx=40,pady=20,command=button_Clear)


#Creating buttons

#Placing butttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=1)

button_clear.grid(row=4,column=0)
button_eq.grid(row=4,column=2)
button_div.grid(row=1,column=3)
button_multi.grid(row=2,column=3)
button_add.grid(row=3,column=3)
button_sub.grid(row=4,column=3)





#Placing butttons on the screen

root.mainloop()