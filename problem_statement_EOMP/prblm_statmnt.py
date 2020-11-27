#TABANG DUDA CLASS 1

from tkinter import *
from tkinter import messagebox
from datetime import *

from PIL import *
root = Tk()
root.title("Lottery Numbers Challenge")
root.geometry("600x500")
root.configure(background="Navy")



#Date
date = datetime.now()
dtm = Label(root)
dtm.place(x=0, y=0)
dtm.config(text="date" + date.strftime("%d/ %m/ %y   %H: %M: %S"))



def confirm():
    age = int(age_entry.get())
    try:
        if age > 18:
         messagebox.showinfo("INFO", "Welcome to Ithuba National Lottery of SA ")
         root.withdraw()

         import draw_numbers
         draw_numbers.mainloop()

        else:
            messagebox.showinfo("INFO", "You're under age to play, sorry")

            name_entry.delete(0, END)
            age_entry.delete(0, END)
    except ValueError:
        pass


#heading_label
heading = Label(root, text="Ithuba National Lottery of SA", font="bold", background="aquamarine")
heading.place(x=200, y=0)

#Name label & Entry
name = Label(root, text="Name & Surname", background="yellow")
name.place(x=0, y=90)
name_entry = Entry(root, borderwidth=2, background="yellow")
name_entry.place(x=130, y=90)

#Age label & Entry
age = Label(root, text="Enter your Age", background="yellow")
age.place(x=0, y=150)
age_entry = Entry(root, borderwidth=2, background="yellow")
age_entry.place(x=130, y=150)

#button
conf_btn = Button(root, text="Confirm", background="violet", command=confirm)
conf_btn.place(x=400, y=120)



root.mainloop()
