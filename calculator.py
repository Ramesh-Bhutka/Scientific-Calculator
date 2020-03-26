from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x568")

calc = Frame(root)
calc.grid()


# ======================Menu and Functions=========================

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return


def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("950x568")


def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568")


def unit():
    root.resizable(width=False, height=False)
    root.geometry("1317x568")




menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Standard", command=Standard)
filemenu.add_separator()


menubar.add_command(label="Exit", command=iExit)


# ============================= Functions ==========================

class Calc():

    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

added_value = Calc()

# ========================== Entrybox ============================

txtDisplay = Entry(calc, font=('arial', 20, 'bold'), background="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

# ========================= NumberPad ============================

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1

# ======================== Standard ==============================

# ======================== Row[1] =================================

btnClear = Button(calc, text=chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                  command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="powder blue",
                     command=added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)

btnSq = Button(calc, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
               command=added_value.squared).grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                command=lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)

# ======================== Row[2,3,4] =================================

btnSub = Button(calc, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                command=lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)

btnMult = Button(calc, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                 command=lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)

btnDiv = Button(calc, text=chr(247), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                command=lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)

# ======================== Row[5] =================================

btnZero = Button(calc, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                 command=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)

btnDot = Button(calc, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                command=lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)

btnPM = Button(calc, text=chr(177), width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
               command=added_value.mathsPM).grid(row=5, column=2, pady=1)

btnEquals = Button(calc, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue",
                   command=added_value.sum_of_total).grid(row=5, column=3, pady=1)



root.config(menu=menubar)
root.mainloop()
