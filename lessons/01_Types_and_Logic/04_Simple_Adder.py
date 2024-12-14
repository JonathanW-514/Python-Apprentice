"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

from tkinter import messagebox, simpledialog, Tk # import required modules
import time


window = Tk()

number = simpledialog.askinteger('None',"Magic Numbers") 
number2 = simpledialog.askinteger("None", "What's ur second magic number")
message = number + number2
messagebox.showerror("calculating", "ples wait we calculating sum haiyah")
time.sleep(1)
