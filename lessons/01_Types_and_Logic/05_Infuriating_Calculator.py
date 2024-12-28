"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

from tkinter import messagebox, simpledialog, Tk
window = Tk()


num1 = simpledialog.askinteger('jay is a gorivia', "give a number")
num2 = simpledialog.askinteger('jay is a gorivia', "give a second number")
operation = simpledialog.askstring("any", "give a operation")
if operation == 'multiplication':
    message = num1 * num2
    messagebox = simpledialog.askinteger(message = message)
messagebox = simpledialog.askstring('None', "is this correct")