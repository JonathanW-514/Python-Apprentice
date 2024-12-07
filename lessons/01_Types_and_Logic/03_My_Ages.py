
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")


Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")

"""

from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
 # Hide the window; we just want to see pop ups
age = simpledialog.askinteger("Your Age", "How old are you?") 

if age < 0:
   messagebox.showinfo('tha jay + gorivia web (no changing)', "You are not born(you are a gorivia).")
elif age < 3:
    messagebox.showinfo(None, "You are a baby.")
if age < 6:
   messagebox.showinfo('tha jay + gorivia web (no changing)', "You are a toddler.")
if age == 10:
   messagebox.showinfo('tha jay + gorivia web (no changing)', "You are jay + gorivia.")
if age < 13:
   messagebox.showinfo('Jay tha gorivia', "You are a child.")
if age < 20:
   messagebox.showinfo('Jay tha gorivia', "You are a teen.")
if age < 65:
   messagebox.showinfo('Jay tha gorivia', "You are a adult.")
if age < 169:
    messagebox.showinfo('Jay tha gorivia', "You are so old hahahahahahaha.")
if age < 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001:
   messagebox.showinfo('Jay tha gorivia', "You are dead say goodbye.")
# and create a message

# Show the message to the user



#window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.
