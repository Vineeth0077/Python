from tkinter import *
from tkcalendar import *

root = Tk()
root.title("Calender")

cal = Calendar(root,selectmode="day",background="blue",bordercolor="red",headersbackground="white",
               normalbackground="blue",foreground="white",normalforeground="white",headersforeground="indigo")

cal.pack()

root.mainloop()
