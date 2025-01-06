from tkinter import *

running = True


def start_counting():
    global running
    reset_counter()
    running = True
    update_timer()


def reset_counter():
    time_counter.config(text="Time: 60:00")
    text_field.delete("1.0", "end-1c")


def update_timer():
    global running
    global time_left
    if running:
        if time_left > 0:
            minutes, seconds = divmod(time_left, 60)
            time_counter.config(text=f"Time: {minutes:02}:{seconds:02}")  # Update the label
            time_left -= 1
            # Call the update_timer function again after 1000ms (1 second)
            root.after(1000, update_timer)
            count_words()
        else:
            time_counter.config(text="Time's up!")
            running = False


def count_words():
    text = text_field.get("1.0", "end-1c")
    words = text.split(" ")
    text_length = len(words)
    if len(words) > 0 and words[len(words)]-1 == " ":
        text_length -= 1

    print(text_length)
    print(words)


time_left = 60

# region UI
# -----------------------    Window
root = Tk()
root.title("Word counter")
root.minsize(500, 300)
root.config(padx=30, pady=30)
# -----------------------    Labels
# Title
window_title = Label(text="Word Counter", font=("Arial", 21))
window_title.grid(column=0, row=0, columnspan=3)
# Sub-text
sub_title = Label(text="Write the max words you can in 1 minute")
sub_title.grid(column=0, row=1, columnspan=3, padx=(10, 0), pady=(15, 15), sticky="w")
# timer
time_counter = Label(text="Time: 01:00", font=("Arial", 15))
time_counter.grid(column=0, row=5, pady=(15, 5))
# current number of words
current_points = Label(text="Words written: 0", font=("Arial", 12), pady=5)
current_points.grid(column=0, row=6)
# total
record = Label(text="Record: 0", font=("Arial", 12), pady=5)
record.grid(column=2, row=6)
# -----------------------    Buttons
# Button Start
button_start = Button(text="START", anchor="center", width=10, command=start_counting)
button_start.grid(column=0, row=4, pady=(5, 5), padx=(15, 5), sticky="w")
# Button Reset
button_reset = Button(text="RESET", anchor="center", width=8, command=reset_counter)
button_reset.grid(column=1, row=4, pady=(5, 5), padx=(0, 5), sticky="nsew")
# Button Stop
button_stop = Button(text="STOP", anchor="center", width=10)
button_stop.grid(column=2, row=4, pady=(5, 5), padx=(15, 5), sticky="e")
# -----------------------    Entries
# text field
text_field = Text(width=50, height=8)
text_field.grid(column=0, row=2, padx=(10, 5), pady=(5, 10), rowspan=2, columnspan=3)

root.mainloop()
## endregion
