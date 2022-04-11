from tkinter import *

window = Tk()

# Window properties
window.geometry('500x400+30+20')
window.title('Welcome to Python Programming')

# Add Button Widget
btn = Button(window, text='Click to Add Name', fg='blue')
btn.place(x=60, y=100)

# Add Label widget
lbl1 = Label(window, text='Student Personal Information', fg='blue', bg='orange')
lbl1.place(relx=0.5, y=50, anchor='center')
lbl2 = Label(window, text='Gender', fg='red')
lbl2.place(x=80, y=150)

# Add Text Field widget
txtfld = Entry(window, bd=3, font=('Verdana', 16))
txtfld.place(x=170, y=100)

# Add Radio Button
v1 = StringVar()
v1.set(1)
r1 = Radiobutton(window, text='Male', variable=v1, value=1)
r1.place(x=80, y=180)
r2 = Radiobutton(window, text='Female', variable=v1, value=2)
r2.place(relx=0.5, y=180)

# Add Checkbox
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
chkbox = Checkbutton(window, text='Basketball', variable=v3)
chkbox2 = Checkbutton(window, text='Tennis', variable=v4)
chkbox3 = Checkbutton(window, text='Swimming', variable=v5)
chkbox.place(x=80, y=240)
chkbox2.place(x=200, y=240)
chkbox3.place(x=320, y=240)

lbl3 = Label(window, text='Sports')
lbl3.place(x=80, y=210)

# Add List Box
data1, data2, data3 = 'arithmetic', 'reading', 'writing'
lstbox = Listbox(window, height=5, selectmode='multiple')
lstbox.insert(END, data1, data2, data3)
lstbox.place(x=80, y=300)

lbl3 = Label(window, text='Subjects')
lbl3.place(x=80, y=270)

window.mainloop()
