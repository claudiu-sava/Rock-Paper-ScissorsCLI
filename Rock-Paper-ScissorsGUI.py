from distutils import command
import random
from tkinter import *

# The main window is called window
window = Tk()
# Set the title
window.title("Rock, Paper, Scissors!")
# Set the window size
window.geometry("400x300")
# Make the window unsizable
window.resizable(False, False)

# The main title
label = Label(window, text="Rock, Paper, Scissors!", font=(None, 15), height=2, fg="black")
# Align the text to the top of page
label.pack(side=TOP)
# frame for items (without title)
gridFrame = Frame(window)
# Setting the frame anchor to the top
gridFrame.pack(side=TOP)

rockImage50 = PhotoImage(file = "img/rock50.png")
paperImage50 = PhotoImage(file = "img/paper50.png")
scissorsImage50 = PhotoImage(file = "img/scissors50.png")

rockImage100 = PhotoImage(file = "img/rock100.png")
paperImage100 = PhotoImage(file = "img/paper100.png")
scissorsImage100 = PhotoImage(file = "img/scissors100.png")

def pcGenerate(userChoice, points):
  choices = ["rock", "paper", "scissors"]
  pcChoice = random.choice(choices)
  points = points
  
  global generateFrame
  generateFrame = Frame(gridFrame)
  generateFrame.grid(row=0, column=1)

  pointsLabel = Label(generateFrame, text="Points: %s" % points)
  pointsLabel.grid(column=0, row=0)


  if pcChoice == "rock":
    pcChoiceButton = Button(generateFrame, image = rockImage100)
    pcChoiceButton.grid(column = 0, row=1)
  elif pcChoice == "paper":
    pcChoiceButton = Button(generateFrame, image = paperImage100)
    pcChoiceButton.grid(column = 0, row=1)
  else:
    pcChoiceButton = Button(generateFrame, image = scissorsImage100)
    pcChoiceButton.grid(column = 0, row=1)


  if pcChoice == userChoice:
    points = points + 1
    nextRoundButton = Button(generateFrame, text="You won! Next round?", command=lambda: play(points))
    nextRoundButton.grid(column=0, row=2)
  else:
    newGameButton = Button(generateFrame, text="You lost! Try again?", command=lambda: play(0))
    newGameButton.grid(column=0, row=2)


def rock(points):
  userChoice = "rock"
  pcGenerate(userChoice, points)


def paper(points):
  userChoice = "paper"
  pcGenerate(userChoice, points)


def scissors(points):
  userChoice = "scissors"
  pcGenerate(userChoice, points)


def play(points):
  try:
    generateFrame.grid_forget()
    generateFrame.destroy()
  except:
    pass
  rockButton = Button(gridFrame, image= rockImage50, command=lambda: rock(points))
  rockButton.grid(column=0, row=1)

  paperButton = Button(gridFrame, image = paperImage50, command=lambda: paper(points))
  paperButton.grid(column=1, row=1)

  scissorsButton = Button(gridFrame, image = scissorsImage50, command=lambda: scissors(points))
  scissorsButton.grid(column=2, row=1)

  window.mainloop()


play(0)
