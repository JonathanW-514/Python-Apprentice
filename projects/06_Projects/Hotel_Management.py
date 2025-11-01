from guizero import App, Box, Text, TextBox, PushButton, ListBox, question, error
from tkinter import messagebox, simpledialog, Tk
avalible_rooms = (1, 100)
cost = 40
while True:
    uwanttocheckin = simpledialog.askstring(title = "do u want to checkin", prompt = "yes or no") 
    if uwanttocheckin == "yes":
        checkoutroom = simpledialog.askinteger(title="say now or ur getting kicked", prompt="how much rooms bwoi")
    if checkoutroom:
        total = checkoutroom * cost
        print("pls pay " + str(total) + "$ maam")
        wantanyservice = simpledialog.askstring(title = "u want any roomservice", prompt = "say yes pls")
    elif wantanyservice == "yes":
            extratotal = total + total + 67410
            print("now u have to pay " + str(extratotal) + " u manke")
    wanttoeatfish = simpledialog.askstring(title="yes or no want fish", prompt="yes or no")
    if wanttoeatfish == "yes":
         print(" heheheha u ate zeckys relitives")