from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")


class MyWindow:
    def __init__(self, window):
        self.lbl1 = Label(window, text="Standard Calculator")
        self.lbl1.place(relx=0.5, y=50, anchor="center")

        self.lbl2 = Label(window, text="Input the 1st number:")
        self.lbl2.place(x=50, y=80)

        self.txt2 = Entry(window, bd=3)
        self.txt2.place(relx=0.5, y=80)

        self.lbl3 = Label(window, text="Input the 2nd number:")
        self.lbl3.place(x=50, y=120)

        self.txt3 = Entry(window, bd=3)
        self.txt3.place(relx=0.5, y=120)

        self.btn1 = Button(window, text="Addition", command=self.add)
        self.btn1.place(x=50, y=160)
        # self.btn1.bind("<Button-1>", self.add)

        self.btn2 = Button(window, text="Subtraction", command=self.sub)
        self.btn2.place(x=110, y=160)

        self.btn3 = Button(window, text="Multiplication", command=self.mul)
        self.btn3.place(x=185, y=160)

        self.btn4 = Button(window, text="Division", command=self.div)
        self.btn4.place(x=275, y=160)

        self.lbl4 = Label(window, text="Result:")
        self.lbl4.place(x=50, y=200)

        self.txt4 = Entry(window, bd=3)
        self.txt4.place(x=110, y=200)

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
