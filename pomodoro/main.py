from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(lbl_timer, text="00:00")
    lbl_main.config(text="Timer")
    lbl_progressbar.config(text="")
    btn_start.config(state="normal")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    btn_start.config(state="disabled")

    if reps % 8 == 0:
        count_down(long_break_sec)
        lbl_main.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        lbl_main.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        lbl_main.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    mins, secs = divmod(count, 60)
    canvas.itemconfig(lbl_timer, text='{:02d}:{:02d}'.format(mins, secs))
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
    global reps
    reps += 1


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
lbl_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

lbl_main = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
lbl_main.grid(column=2, row=1)

btn_start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
btn_start.grid(column=1, row=3)

btn_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
btn_reset.grid(column=3, row=3)

lbl_progressbar = Label(bg=YELLOW, fg=GREEN)
lbl_progressbar.grid(column=2, row=4)

window.mainloop()