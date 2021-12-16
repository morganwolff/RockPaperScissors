import tkinter
import random
from tkinter.font import BOLD

root = tkinter.Tk()
root.title("Rock, Paper, Scissors by MorganWolff")

screen_x = int(root.winfo_screenwidth())
screen_y = int(root.winfo_screenheight())
window_x = 500
window_y = 650

posX = (screen_x//2) - (window_x//2)
posY = (screen_y//2) - (window_y//2)

root.resizable(False, False)
geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
root.geometry(geo)

random_nb = random.randint(1, 3)
if random_nb == 1:
    computer_choice = "R"
elif random_nb == 2:
    computer_choice = "P"
elif random_nb == 3:
    computer_choice = "S"

#ASCII ART

rock_image = """
        ________
    ---|    _____)_
           (_______)
           (_______)
     ___   (_______)
        \___(____)
    
YOU CHOSE ROCK
"""

paper_image = """
    _________
---/     ____)______
         ___________)_
          ____________)
 __      ___________)
   \______________)

YOU CHOSE PAPER
"""

scissors_image = """
    __________
---/     _____)_____
            ________)
         ____________)
 __     (_____)   
   \____(___)

YOU CHOSE SCISSORS
"""

c_rock_image = """
        ________
    ---|    _____)_
           (_______)
           (_______)
     ___   (_______)
        \___(____)

COMPUTER CHOSE ROCK
"""

c_paper_image = """
    _________
---/     ____)______
         ___________)_
          ____________)
 __      ___________)
   \______________)

COMPUTER CHOSE PAPER
"""

c_scissors_image = """
    __________
---/     _____)_____
            ________)
         ____________)
 __     (_____)   
   \____(___)

COMPUTER CHOSE SCISSORS
"""

#Create Functions
def rock():
    reset()
    label_user_choice['text'] = rock_image
    if computer_choice == "R":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = c_rock_image
    elif computer_choice == "P":
        label_result['text'] = "Computer Wins"
        label_computer_choice['text'] = c_paper_image
    elif computer_choice == "S":
        label_result['text'] = "Player Wins"
        label_computer_choice['text'] = c_scissors_image

def paper():
    reset()
    label_user_choice['text'] = paper_image
    if computer_choice == "R":
        label_result['text'] = "Player Wins"
        label_computer_choice['text'] = c_rock_image
    elif computer_choice == "P":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = c_paper_image
    elif computer_choice == "S":
        label_result['text'] = "Computer Wins"
        label_computer_choice['text'] = c_scissors_image

def scissors():
    reset()
    label_user_choice['text'] = scissors_image
    if computer_choice == "R":
        label_result['text'] = "Computer Wins"
        label_computer_choice['text'] = c_rock_image
    elif computer_choice == "P":
        label_result['text'] = "Player Wins"
        label_computer_choice['text'] = c_paper_image
    elif computer_choice == "S":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = c_scissors_image

def reset():
    global computer_choice
    random_nb = random.randint(1, 3)
    if random_nb == 1:
        computer_choice = "R"
    elif random_nb == 2:
        computer_choice = "P"
    elif random_nb == 3:
        computer_choice = "S"
    label_computer_choice['text'] = ""
    label_user_choice['text'] = ""
    label_result['text'] = "Choose..."

#Create widgets

button_rock = tkinter.Button(root, text="Rock", command= rock, width=25, bg='#ACD2A4')
button_rock.pack()
button_paper = tkinter.Button(root, text="Paper", command= paper, width=25, bg='#ACD2A4')
button_paper.pack()
button_scissors = tkinter.Button(root, text="Scissors", command= scissors, width=25, bg='#ACD2A4')
button_scissors.pack()

label_computer = tkinter.Label(root, text="Computer Choice:", font=("Helvetica", 15), justify=tkinter.LEFT)
label_computer.pack()
label_computer_choice = tkinter.Label(root, text="", font="Courier", justify=tkinter.LEFT)
label_computer_choice.pack()

label_user = tkinter.Label(root, text="User Choice:", font=("Helvetica", 15), justify=tkinter.LEFT)
label_user.pack()
label_user_choice = tkinter.Label(root, text="", font="Courier", justify=tkinter.LEFT)
label_user_choice.pack()

label_result = tkinter.Label(root, text="Choose...")
label_result.pack()

button_reset = tkinter.Button(root, text="Reset", command= reset, width=25, bg='#D2A7A4')
button_reset.pack()

root.mainloop()