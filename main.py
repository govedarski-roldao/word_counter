from tkinter import *

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
button_start = Button(text="START", anchor="center", width=10)
button_start.grid(column=0, row=4, pady=(5, 5), padx=(15, 5), sticky="w")
# Button Reset
button_reset = Button(text="RESET", anchor="center", width=8)
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
