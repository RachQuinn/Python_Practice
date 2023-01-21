import random
import os
from tkinter import *

root = Tk()
result_label = Label(root, text="")
result_label.pack()


def roll_dice():
    result = random.randint(1, 20)
    script_dir = os.path.dirname(__file__)
    image_to_display = "./sample.png"
    print(image_to_display)
    img = PhotoImage(file=image_to_display)
    Label(root, image=img).pack()
    result_label.config(text="Result: " + str(result))


roll_button = Button(root, text="Roll the dice", command=roll_dice)
roll_button.pack()

root.mainloop()
