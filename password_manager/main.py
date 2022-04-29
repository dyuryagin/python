from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    if not entry_website.get() or not entry_password:
        messagebox.showwarning(message="Fill out all the fields")
    else:
        is_ok = messagebox.askokcancel(title=entry_website.get(), message=f"Email: {entry_email.get()}, "
                                                                          f"password: {entry_password.get()}. Is it ok?")
        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{entry_website.get()} | {entry_email.get()} | {entry_password.get()}\n")
            file.close()
            entry_website.delete(0, END)
            entry_email.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)
canvas = Canvas(window, width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(0, 0, image=img, anchor="nw")
canvas.grid(row=0, column=1)

lbl_website = Label(text="Website:")
lbl_website.grid(row=1, column=0)


lbl_email = Label(text="Email/Username:")
lbl_email.grid(row=2, column=0)

lbl_password = Label(text="Password:")
lbl_password.grid(row=3, column=0)

entry_website = Entry(width=38)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_email = Entry(width=38)
entry_email.grid(row=2, column=1, columnspan=2)

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

btn_generate = Button(text="Generate password", command=generate_password)
btn_generate.grid(row=3, column=2)

btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(row=4, column=1, columnspan=2)




window.mainloop()