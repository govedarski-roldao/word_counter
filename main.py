from tkinter import *

from sqlalchemy import column

# region UI
# -----------------------    Window
root = Tk()
root.title("Word counter")
root.minsize(500, 300)
root.config(padx=30, pady=30)
# -----------------------    Labels
# Title
window_title = Label(text="Word Counter", font=("Arial", 21))
window_title.grid(column=0, row=0, columnspan=2)
# Sub-text
sub_title = Label(text="Write the max words you can in 1 minute")
sub_title.grid(column=0, row=1, columnspan=3, padx=(5, 0), pady=(15, 15))
# -----------------------    Buttons
# Button Start
button_start = Button(text="START", anchor="w")
button_start.grid(column=0, row=2, pady=(20, 5), padx=(15, 5), sticky="w")
# Button Reset
button_reset = Button(text="RESET", anchor="w")
button_reset.grid(column=0, row=3, pady=(20, 5), padx=(15, 5), sticky="w")


root.mainloop()
## endregion
