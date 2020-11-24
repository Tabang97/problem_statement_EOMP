from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Lottery Numbers Challenge")
root.geometry("400x350")
root.configure(background="indigo")



def confirm():
    age = int(age_entry.get())
    try:
        if age > 18:
         messagebox.showinfo("INFO", "CORRECT LOGIN")
         root.withdraw()

         import draw_numbers
         draw_numbers.mainloop()

        else:
            messagebox.showinfo("INFO", "INCORRECT LOGIN")

            name_entry.delete(0, END)
            age_entry.delete(0, END)
    except ValueError:
        pass


#heading_label
heading = Label(root, text="Ithuba National Lottery of SA", font="bold", background="aquamarine")
heading.pack()

#Name label & Entry
name = Label(root, text="Name & Surname", background="aqua")
name.pack()
name_entry = Entry(root, borderwidth=2)
name_entry.pack()

#Age label & Entry
age = Label(root, text="Enter your Age", background="aqua")
age.pack()
age_entry = Entry(root, borderwidth=2)
age_entry.pack()

#button
conf_btn = Button(root, text="Confirm", background="violet", command=confirm)
conf_btn.pack()




root.mainloop()
