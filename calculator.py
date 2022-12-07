#calculator

from tkinter import *

#start-up
wn = Tk()
wn.title("Calculator")
wn.resizable(0, 0)

#stored nums
global stored_1
stored_1 = ""
global stored_2
stored_2 = ""
global stage
stage = 0

def clear():
    global stored_1, stored_2, stage, operation
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    stored_1 = ""
    stored_2 = ""
    stage = 0
    operation = ""
    num_lb.config(text=0)
    
def equal_func():
    global stored_1, stored_2, operation, stage
    val1 = False
    val2 = False
    
    try:
        if operation == "":
            operation = "p"
            
    except NameError:
        operation = "p"


    #print(True, stored_1, stored_2)

    if stored_1 == "":
        stored_1 = 0
        val1 = True

    if stored_2 == "":
        stored_2 = 0
        val2 = True

    if val1 == True and val2 == False:
        stored_1 = 1
        operation = "m"

    stored_1 = int(stored_1)
    stored_2 = int(stored_2)

    if operation == "d":
        answer = stored_1 / stored_2
        num_lb.config(text=answer)

    elif operation == "m":
        answer = stored_1 * stored_2
        num_lb.config(text=answer)

    elif operation == "a":
        answer = stored_1 + stored_2
        num_lb.config(text=answer)

    elif operation == "s":
        answer = stored_1 - stored_2
        num_lb.config(text=answer)

    else:
        num_lb.config(text=stored_1)


    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    stored_1 = ""
    stored_2 = ""
    stage = 0
    operation = ""
        





#functions
def func_1():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "1"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "1"
        num_lb.config(text=stored_2)

def func_2():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "2"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "2"
        num_lb.config(text=stored_2)

def func_3():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "3"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "3"
        num_lb.config(text=stored_2)

def func_4():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "4"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "4"
        num_lb.config(text=stored_2)

def func_5():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "5"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "5"
        num_lb.config(text=stored_2)

def func_6():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "6"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "6"
        num_lb.config(text=stored_2)

def func_7():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "7"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "7"
        num_lb.config(text=stored_2)
        
def func_8():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "8"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "8"
        num_lb.config(text=stored_2)

def func_9():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "9"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "9"
        num_lb.config(text=stored_2)

def func_0():
    global stored_1, stored_2
    stored_1 = str(stored_1)
    stored_2 = str(stored_2)
    if stage == 0:
        stored_1 += "0"
        num_lb.config(text=stored_1)

    else:
        stored_2 += "0"
        num_lb.config(text=stored_2)

#divide func
def divide_func():
    global stage
    stage = 1
    global operation
    operation = "d"
    num_lb.config(text="÷")

def multi_func():
    global stage
    stage = 1
    global operation
    operation = "m"
    num_lb.config(text="x")

def sub_func():
    global stage
    stage = 1
    global operation
    operation = "s"
    num_lb.config(text="-")

def add_func():
    global stage
    stage = 1
    global operation
    operation = "a"
    num_lb.config(text="+")


    
          
    
#format

num_lb = Label(wn, text=0)
num_lb.grid(row=0, column=2)

num_1 = Button(wn, text="    1    ", command=func_1)
num_1.grid(row=1, column=0)
num_2 = Button(wn, text="    2    ", command=func_2)
num_2.grid(row=1, column=1)
num_3 = Button(wn, text="    3    ", command=func_3)
num_3.grid(row=1, column=2)
num_4 = Button(wn, text="    4    ", command=func_4)
num_4.grid(row=2, column=0)
num_5 = Button(wn, text="    5    ", command=func_5)
num_5.grid(row=2, column=1)
num_6 = Button(wn, text="    6    ", command=func_6)
num_6.grid(row=2, column=2)
num_7 = Button(wn, text="    7    ", command=func_7)
num_7.grid(row=3, column=0)
num_8 = Button(wn, text="    8    ", command=func_8)
num_8.grid(row=3, column=1)
num_9 = Button(wn, text="    9    ", command=func_9)
num_9.grid(row=3, column=2)
num_0 = Button(wn, text="    0    ", command=func_0)
num_0.grid(row=4, column=1)



#commands
divide = Button(wn, text="    ÷    ", command=divide_func)
divide.grid(row=1, column=3)
multi = Button(wn, text="    x    ", command=multi_func)
multi.grid(row=2, column=3)
sub = Button(wn, text="    -    ", command=sub_func)
sub.grid(row=3, column=3)
add = Button(wn, text="    +    ", command=add_func)
add.grid(row=4, column=3)
backBN = Button(wn, text="    C    ", command=clear)
backBN.grid(row=4, column=2)
equalBN = Button(wn, text="    =    ", command=equal_func)
equalBN.grid(row=4, column=0)


wn.mainloop()