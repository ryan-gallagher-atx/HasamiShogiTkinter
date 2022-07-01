# Author: Ryan Gallagher
# Date: 6/30/2022
# Description: Hasami Shogi but with a usable GUI created via Tkinter

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hasami Shogi')

clicked = True
count = 0
winner = False
player = " "


# disable all buttons
def disable_all_buttons():
    """Disables all buttons after a win or a stalemate."""
    pass


# check to see if there is a win scenario
def checkifwon():
    """Checks to see if a player has won."""
    pass


# button clicked function
def b_click(b):
    """Allows a button to be clicked."""
    global clicked, count

    if b["text"] == " " and clicked is True:
        b["text"] = "R"
        count += 1
        checkifwon()
        clicked = False

    elif b["text"] == " " and clicked is False:
        b["text"] = "B"
        count += 1
        checkifwon()
        clicked = True

    else:
        messagebox.showerror("Hasami Shogi", "That box has already been selected\nPick another box...")


# start the game over
def reset():
    """Resets the game and generates new buttons."""
    global b1, b2, b3, b4, b5, b6, b7, b8, b9,\
        b10, b11, b12, b13, b14, b15, b16, b17, b18,\
        b19, b20, b21, b22, b23, b24, b25, b26, b27, \
        b28, b29, b30, b31, b32, b33, b34, b35, b36, \
        b37, b38, b39, b40, b41, b42, b43, b44, b45, \
        b46, b47, b48, b49, b50, b51, b52, b53, b54, \
        b55, b56, b57, b58, b59, b60, b61, b62, b63, \
        b64, b65, b66, b67, b68, b69, b70, b71, b72, \
        b73, b74, b75, b76, b77, b78, b79, b80, b81
    global clicked, count
    clicked = True
    count = 0

    # Build buttons
    b1 = Button(root, text="R", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b1))
    b2 = Button(root, text="R", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b2))
    b3 = Button(root, text="R", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b3))
    b4 = Button(root, text="R", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b4))
    b5 = Button(root, text="R", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b5))
    b6 = Button(root, text="R", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b6))
    b7 = Button(root, text="R", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b7))
    b8 = Button(root, text="R", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b8))
    b9 = Button(root, text="R", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b9))

    b10 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b10))
    b11 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b11))
    b12 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b12))
    b13 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b13))
    b14 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b14))
    b15 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b15))
    b16 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b16))
    b17 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b17))
    b18 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b18))

    b19 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b19))
    b20 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b20))
    b21 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b21))
    b22 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b22))
    b23 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b23))
    b24 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b24))
    b25 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b25))
    b26 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b26))
    b27 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b27))

    b28 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b28))
    b29 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b29))
    b30 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b30))
    b31 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b31))
    b32 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b32))
    b33 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b33))
    b34 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b34))
    b35 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b35))
    b36 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b36))

    b37 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b37))
    b38 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b38))
    b39 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b39))
    b40 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b40))
    b41 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b41))
    b42 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b42))
    b43 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b43))
    b44 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b44))
    b45 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b45))

    b46 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b46))
    b47 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b47))
    b48 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b48))
    b49 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b49))
    b50 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b50))
    b51 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b51))
    b52 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b52))
    b53 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b53))
    b54 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b54))

    b55 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b55))
    b56 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b56))
    b57 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b57))
    b58 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b58))
    b59 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b59))
    b60 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b60))
    b61 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b61))
    b62 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b62))
    b63 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b63))

    b64 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b64))
    b65 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b65))
    b66 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b66))
    b67 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b67))
    b68 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b68))
    b69 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b69))
    b70 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b70))
    b71 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b71))
    b72 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b72))

    b73 = Button(root, text="B", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b73))
    b74 = Button(root, text="B", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b74))
    b75 = Button(root, text="B", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b75))
    b76 = Button(root, text="B", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b76))
    b77 = Button(root, text="B", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b77))
    b78 = Button(root, text="B", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b78))
    b79 = Button(root, text="B", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b79))
    b80 = Button(root, text="B", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b80))
    b81 = Button(root, text="B", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                 command=lambda: b_click(b81))

    # Grid our buttons to screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=3)
    b5.grid(row=0, column=4)
    b6.grid(row=0, column=5)
    b7.grid(row=0, column=6)
    b8.grid(row=0, column=7)
    b9.grid(row=0, column=8)

    b10.grid(row=1, column=0)
    b11.grid(row=1, column=1)
    b12.grid(row=1, column=2)
    b13.grid(row=1, column=3)
    b14.grid(row=1, column=4)
    b15.grid(row=1, column=5)
    b16.grid(row=1, column=6)
    b17.grid(row=1, column=7)
    b18.grid(row=1, column=8)

    b19.grid(row=2, column=0)
    b20.grid(row=2, column=1)
    b21.grid(row=2, column=2)
    b22.grid(row=2, column=3)
    b23.grid(row=2, column=4)
    b24.grid(row=2, column=5)
    b25.grid(row=2, column=6)
    b26.grid(row=2, column=7)
    b27.grid(row=2, column=8)

    b28.grid(row=3, column=0)
    b29.grid(row=3, column=1)
    b30.grid(row=3, column=2)
    b31.grid(row=3, column=3)
    b32.grid(row=3, column=4)
    b33.grid(row=3, column=5)
    b34.grid(row=3, column=6)
    b35.grid(row=3, column=7)
    b36.grid(row=3, column=8)

    b37.grid(row=4, column=0)
    b38.grid(row=4, column=1)
    b39.grid(row=4, column=2)
    b40.grid(row=4, column=3)
    b41.grid(row=4, column=4)
    b42.grid(row=4, column=5)
    b43.grid(row=4, column=6)
    b44.grid(row=4, column=7)
    b45.grid(row=4, column=8)

    b46.grid(row=5, column=0)
    b47.grid(row=5, column=1)
    b48.grid(row=5, column=2)
    b49.grid(row=5, column=3)
    b50.grid(row=5, column=4)
    b51.grid(row=5, column=5)
    b52.grid(row=5, column=6)
    b53.grid(row=5, column=7)
    b54.grid(row=5, column=8)

    b55.grid(row=6, column=0)
    b56.grid(row=6, column=1)
    b57.grid(row=6, column=2)
    b58.grid(row=6, column=3)
    b59.grid(row=6, column=4)
    b60.grid(row=6, column=5)
    b61.grid(row=6, column=6)
    b62.grid(row=6, column=7)
    b63.grid(row=6, column=8)

    b64.grid(row=7, column=0)
    b65.grid(row=7, column=1)
    b66.grid(row=7, column=2)
    b67.grid(row=7, column=3)
    b68.grid(row=7, column=4)
    b69.grid(row=7, column=5)
    b70.grid(row=7, column=6)
    b71.grid(row=7, column=7)
    b72.grid(row=7, column=8)

    b73.grid(row=8, column=0)
    b74.grid(row=8, column=1)
    b75.grid(row=8, column=2)
    b76.grid(row=8, column=3)
    b77.grid(row=8, column=4)
    b78.grid(row=8, column=5)
    b79.grid(row=8, column=6)
    b80.grid(row=8, column=7)
    b81.grid(row=8, column=8)


# Create a menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()
root.mainloop()
