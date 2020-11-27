#TABANG DUDA CLASS1

from tkinter import *
from tkinter import messagebox
import random
from datetime import *


lotto = Tk()
lotto.title("Lottery Numbers Challenge")
lotto.geometry("600x500")
lotto.configure(background="aqua")


#Date
date = datetime.now()
dtm = Label(lotto)
dtm.place(x=200, y=200)
dtm.config(text="date: " + date.strftime("(%d/ %m/ %y   %H: %M: %S)"))

#clear function
def clearing():
    entries_1.delete(0, END)
    entries_2.delete(0, END)
    entries_3.delete(0, END)
    entries_4.delete(0, END)
    entries_5.delete(0, END)
    entries_6.delete(0, END)
    result_lbl.delete("1.0", END)



#random winning numbers
def win():

    res = []
    res.append(int(entries_1.get()))
    res.append(int(entries_2.get()))
    res.append(int(entries_3.get()))
    res.append(int(entries_4.get()))
    res.append(int(entries_5.get()))
    res.append(int(entries_6.get()))



    win_nums = random.sample(range(1, 50), 6)
    win_nums.sort()

    res.sort()
    result_lbl.delete(1.0, END)
    result_lbl.insert(1.0, win_nums)


    #
    # if len(win_nums) != len(set(win_nums)):
    #     messagebox.config(text="Do not replicate numbers")
    # else:
    #     messagebox.config(text="Result")



    right = set(res).intersection(win_nums)

    ##########
    ok = Label(lotto)
    ok.place(x=300, y=200)

    if res == win_nums:
        messagebox.showinfo("message", "You won: R10 000 000.00")

    elif len(right) == 0:
        messagebox.showinfo("message", "you won: Nothing, better luck next time")

    elif len(right) == 1:
        messagebox.showinfo("message", "you won: Nothing, better luck next time")

    elif len(right) == 2:
        messagebox.showinfo("message", "you just won yourself: R20.00")

    elif len(right) == 3:
        messagebox.showinfo("message", "you won: 100.50 ")

    elif len(right) == 4:
        messagebox.showinfo("message", "you won: R2,384.00")

    elif len(right) == 5:
        messagebox.showinfo("message", "you won: 8,584.00")

    elif len(right) == 6:
        messagebox.showinfo("message", "you won:10, 000 000.00 ")







#text_box entries

entries_1 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entries_1.place(x=0, y=3)
entries_2 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entries_2.place(x=100, y=3)
entries_3 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entries_3.place(x=200, y=3)
entries_4 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entries_4.place(x=300, y=3)
entries_5 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entries_5.place(x=400, y=3)
entries_6 = Entry(lotto, borderwidth=2, font="bold", width=5, bd=5)
entries_6.place(x=500, y=3)




#play button
play_btn = Button(lotto, text="Play", background="blue", command=win)
play_btn.place(x=250, y=50)

#clear button
clear_btn = Button(lotto, text="clear", command=clearing)
clear_btn.place(x=0, y=400)

#exit button
exit_btn = Button(lotto, text="Exit", background="red", command=lotto.quit)
exit_btn.place(x=500, y=400)

#Result labels
results = Label(lotto, text="winning numbers:", background="lime", font="bold")
results.place(x=0, y=100)
result_lbl = Text(lotto, font="bold", width=30, height=1, bd=2)
result_lbl.place(x=150, y=100)





lotto.mainloop()
