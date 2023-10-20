from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PURPLE = "#5D12D2"
PINK = "#B931FC"
RED = "#FF6AC2"
YELLOW = "#FFE5E5"
BLUE = "#5CD2E6"
FONT_NAME = "Phosphate"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work = WORK_MIN
    long_break = LONG_BREAK_MIN
    short_break = SHORT_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break * 60)
        title_label.config(text="Break", fg=YELLOW)
    else:
        count_down(work * 60)
        title_label.config(text="Work", fg=BLUE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(bg=PURPLE, pady=20)

# Tomato image
canvas = Canvas(width=500 , height=450, bg=PURPLE, highlightthickness=0)
synth_image = PhotoImage(file="synthwave.png")
canvas.create_image(250, 250, image=synth_image)
timer_text = canvas.create_text(240, 220, text="00:00", fill=YELLOW, font=(FONT_NAME, 50, "normal"))
canvas.grid(column=1, row=1)

# The word timer above the Tomato image
title_label = Label(text="Timer", fg=RED, bg=PURPLE, font=(FONT_NAME, 60, "normal"))
title_label.place(x=155, y=25)

# Check marks that appear below the tomato every time the timer completes
check_mark = Label(fg=PINK, bg=PURPLE, font=(FONT_NAME, 25, "normal"))
check_mark.place(x=225, y=410)

# Starts the Timer
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.place(x=50, y=410)

# Resets the timer to 0
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.place(x=350, y=410)


window.mainloop()
