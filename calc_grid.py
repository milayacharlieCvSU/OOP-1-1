from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")


class MyWindow:
    def __init__(self, window):
        # Placeholder Widgets
        self.ilbl1 = Label(window, text='               \n ')
        self.ilbl1.grid(row=0, column=0)

        self.ilbl2 = Label(window, text=' ')
        self.ilbl2.grid(row=2, column=0)

        self.ilbl3 = Label(window, text=' ')
        self.ilbl3.grid(row=5, column=0)

        self.ilbl4 = Label(window, text=' ')
        self.ilbl4.grid(row=7, column=0)

        # Visible Widgets

        # Labels
        self.lbl1 = Label(window, text="Standard Calculator")
        self.lbl1.grid(row=2, column=1, columnspan=4, sticky=N)

        self.lbl2 = Label(window, text="Input the 1st number:")
        self.lbl2.grid(row=3, column=1, columnspan=2, sticky=W)

        self.lbl3 = Label(window, text="Input the 2nd number:")
        self.lbl3.grid(row=4, column=1, columnspan=2, sticky=W)

        self.lbl4 = Label(window, text="Result:")
        self.lbl4.grid(row=8, column=1, columnspan=2, sticky=W)

        # Entries
        self.txt2 = Entry(window, bd=3)
        self.txt2.grid(row=3, column=3, columnspan=2, sticky=E, pady=5)

        self.txt3 = Entry(window, bd=3)
        self.txt3.grid(row=4, column=3, columnspan=2, sticky=E, pady=5)

        self.txt4 = Entry(window, bd=3, state="readonly")
        self.txt4.grid(row=8, column=2, columnspan=2, sticky=W, pady=5)

        # Buttons
        self.btn1 = Button(window, text="Addition", command=self.add)
        self.btn1.grid(row=6, column=1, padx=2)

        self.btn2 = Button(window, text="Subtraction", command=self.sub)
        self.btn2.grid(row=6, column=2, padx=2)

        self.btn3 = Button(window, text="Multiplication", command=self.mul)
        self.btn3.grid(row=6, column=3, padx=2)

        self.btn4 = Button(window, text="Division", command=self.div)
        self.btn4.grid(row=6, column=4, padx=2)

    # Button Functions
    def add(self):
        self.txt4['state'] = 'normal'

        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 + num2
        self.txt4.insert(END, str(answer))

        self.txt4['state'] = 'readonly'

    def sub(self):
        self.txt4['state'] = 'normal'

        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 - num2
        self.txt4.insert(END, str(answer))

        self.txt4['state'] = 'readonly'

    def mul(self):
        self.txt4['state'] = 'normal'

        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1*num2
        self.txt4.insert(END, str(answer))

        self.txt4['state'] = 'readonly'

    def div(self):
        self.txt4['state'] = 'normal'

        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1/num2
        self.txt4.insert(END, str(answer))

        self.txt4['state'] = 'readonly'


myWin = MyWindow(window)
window.mainloop()
