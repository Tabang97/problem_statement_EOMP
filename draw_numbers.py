from tkinter import *
from tkinter import messagebox
from random import *
lotto = Tk()
lotto.title("Lottery Numbers Challenge")
lotto.geometry("600x500")
lotto.configure(background="aqua")




#text_box entries
entry_1 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entry_1.place(x=0, y=3)
entry_2 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entry_2.place(x=100, y=3)
entry_3 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entry_3.place(x=200, y=3)
entry_4 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entry_4.place(x=300, y=3)
entry_5 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entry_5.place(x=400, y=3)
entry_6 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entry_6.place(x=500, y=3)

#play button
play_btn = Button(lotto, text="Play", background="blue")
play_btn.place(x=250, y=50)


#Result labels
results = Label(lotto, text="Results", background="lime", font="bold")
results.place(x=50, y=100)
result_lbl = Label(lotto, font="bold", width=30)
result_lbl.place(x=150, y=100)



lotto.mainloop()
