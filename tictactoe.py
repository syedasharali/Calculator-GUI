# This code is incomplete. To get complete code, email me on 'syedasharali092@gmail.com'

from PIL import ImageGrab
from random import randint
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
from tkinter import *
from webbrowser import open_new_tab

# setting up new screen

root = Tk()
root.title("Tic Tac Toe")
root.geometry("500x550")
root.iconbitmap("data/tic.ico")
back_image = PhotoImage(file="data/back.png")
menu_image = PhotoImage(file="data/menu.png")
exit_image = PhotoImage(file="data/exit.png")
sound_play = PhotoImage(file="data/speakeron.png")
sound_mute = PhotoImage(file="data/speakeroff.png")
root.resizable(0, 0)
main_image = PhotoImage(file="data/main.png")
bg = Label(root, image=main_image)
bg.place(x=0, y=0)
frame = Frame(root, bg="#FFFFFF")
frame.place(relx=0.5, rely=0.6, anchor=CENTER)

# playing music


PlaySound("data/sounds/ticsoundtrack.wav", SND_FILENAME | SND_LOOP | SND_ASYNC)


# initialization

x = 0
y = 0
count = 0
cross_counter = 0
zero_counter = 0
flag = False
cell_size = 500 / 3

## functions will go here




"""This code has been removed to prevent unauthorized duplication. If you need to reach me, please send an email to syedasharali092@gmail.com."""



mute_button = Button(root, image=sound_play, command=mute, bd=0, bg="white")
mute_button.pack(side=BOTTOM, anchor=SE, padx=20, pady=20)
button1 = Button(
    frame,
    text="New Game",
    command=choice,
    font=("Arial Rounded MT Bold", 25, "bold"),
    bd=1,
    bg="white",
    width=15,
)
button1.pack()
button2 = Button(
    frame,
    text="Exit",
    font=("Arial Rounded MT Bold", 25, "bold"),
    width=15,
    bd=1,
    bg="white",
    command=exit_program,
)
button2.pack(pady=30)
button3 = Button(
    frame,
    text="How To Play?",
    font=("Arial Rounded MT Bold", 25, "bold"),
    width=15,
    bd=1,
    bg="white",
    command=howtoplay,
)
button3.pack()


root.protocol("WM_DELETE_WINDOW", exit_program)
root.config(cursor="plus red")


root.mainloop()


"""This code has been removed to prevent unauthorized duplication. If you need to reach me, please send an email to syedasharali092@gmail.com."""
