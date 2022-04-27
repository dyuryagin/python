from tkinter import *


def calculate_click():
    km_counted = round(int(entr_mile_count.get()) * 1.6, 1)
    lbl_km_count.configure(text=km_counted)


window = Tk()
window.title("Mile to km converter")
window.config(padx=20, pady=20)

lbl_is_equal_to = Label(text="is equal to")
lbl_is_equal_to.grid(column=1, row=2)

lbl_mile = Label(text="miles")
lbl_mile.grid(column=3, row=1)

lbl_km = Label(window, text="km")
lbl_km.grid(column=3, row=2)

lbl_km_count = Label(text="0")
lbl_km_count.grid(column=2, row=2)

btn_calculate = Button(text="Calculate", command=calculate_click)
btn_calculate.grid(column=2, row=3)

entr_mile_count = Entry(width=10)
entr_mile_count.grid(column=2, row=1)


window.mainloop()