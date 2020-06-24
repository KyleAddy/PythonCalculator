#Creator Kyle Addy
from tkinter import *

root = Tk()
root.title("Calculator by Kyle Addy")
root.iconbitmap('./CalculatorIcon.ico')
root.resizable(height = 0, width = 0)

#define global variables
global currentOperation
currentOperation = "none"
global num1
num1 = 0.0
global num2
num2 = 0.0

#Define and Display output field
output = Entry(root, width=40)
output.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def numberClicked(number):
    global currentOperation 
    global num1
    global num2
    if currentOperation == "none":
        current = output.get()
        output.delete(0, END)
        output.insert(0, str(current) + str(number))
        num1 = float(output.get())

    else:
        current = output.get()
        output.delete(0, END)
        output.insert(0, str(current) + str(number))
        num2 = float(output.get())

def clearOutput():
    global currentOperation
    global num1
    global num2
    output.delete(0, END)
    currentOperation = "none"
    num1 = 0
    num2 = 0

def setOperator(operation):
    global currentOperation 
    currentOperation= operation
    output.delete(0, END)

def calculate():
    global currentOperation
    global num1
    global num2
    if currentOperation == "+":
        output.delete(0, END)
        output.insert(0, num1 + num2)

    elif currentOperation == "-":
        output.delete(0, END)
        output.insert(0, num1 - num2)
    
    elif currentOperation == "*":
        output.delete(0, END)
        output.insert(0, num1 * num2)

    elif currentOperation == "/":
        output.delete(0, END)
        output.insert(0, num1 / num2)


#define number buttons
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: numberClicked(0))
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: numberClicked(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: numberClicked(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: numberClicked(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: numberClicked(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: numberClicked(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: numberClicked(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: numberClicked(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: numberClicked(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: numberClicked(9))


#Display number buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)

#define operation buttons
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: setOperator("+"))
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: setOperator("-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: setOperator("*"))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: setOperator("/"))
button_equal = Button(root, text="=", padx=40, pady=20, command=calculate)
button_clear = Button(root, text="Clear", padx=29, pady=20, command=clearOutput)

#display operation buttons
button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

root.mainloop()