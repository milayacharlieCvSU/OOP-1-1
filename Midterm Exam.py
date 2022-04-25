# Program 1: Modify the program below by adding two conversion methods - Fahrenheit to
#   Celsius and Kelvin to Celsius (50 points)
"""
def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")

main()
"""


# Modified Code
def main():
    class TemperatureConversion:
        def __init__(self, temp=1.0):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp*9)/5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5/9

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")
    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheitToCelsius(tempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")
    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")


main()

# --------------------------------------------------------------------------------------------- #
from tkinter import *

# Program 2: Create a program to produce the interface. After typing the name in the first text
#   field, click the button to display the name to another text field. (50 points)

win = Tk()
win.geometry('600x300')
win.title('Midterm in OOP')

# Label
fullname_lbl = Label(win, text='Enter your fullname:', fg='red')
fullname_lbl.place(relx=0.1, rely=0.35)

# Input Entry Box
fullname = StringVar()
fullname_ent = Entry(win, textvariable=fullname, font=('Arial', 14), bd=3)
fullname_ent.place(relx=0.5, rely=0.35)

# Output Entry Box
name = StringVar()
name_output = Entry(win, textvariable=name, font=('Arial', 14), bd=3)
name_output.place(relx=0.5, rely=0.5)


# Button Command
def copy():
    name.set(fullname.get())


# Button
display_btn = Button(win, text='Click to display your Fullname', fg='red', command=copy)
display_btn.place(relx=0.1, rely=0.5)

win.mainloop()
