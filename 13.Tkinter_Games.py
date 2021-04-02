import random
from tkinter import *
from tkinter import messagebox
import time

# Imports

global b, c, d, e, timeRemaining

window = Tk()
window.geometry("510x270")
window.title("Python Games")
logo = PhotoImage(file="cooltext377121354457095.png")
# Setting up the main window

label2 = Label(window, image=logo, bg='black')
label2.pack(side=BOTTOM)
label = Label(window, font=20, text="Welcome To Python Games!")
label.pack()
label1 = Label(window, font=20, text="Press Enter to continue")
label1.pack()
entry = Entry(window)
entry.insert(END, 'What is your name?')
entry.pack()
# Creating the first window

name = ""
timeRemaining = 0
# Creating variables


def GetName(event):
    global name
    name = entry.get()
    Begin(1)
    # Getting the user's name and calling the "Begin" function


def Begin(event):
    global Button1, Button2, name, Button3
    # Globals

    entry.destroy()
    label.config(text=(name + ", what do you want to play?"))
    label1.config(text="")
    Button1 = Button(window, font=20, text="Color Game", command=ColorGame)
    Button1.pack()
    Button2 = Button(window, font=20, text="Space Quiz", command=QuizGame)
    Button2.pack()
    Button3 = Button(window, font=20, text="Word Type", command=WordGame)
    Button3.pack()
    # Creating the second screen, the "Main Menu"


def ColorGame():
    global timeRemaining, score, b, c, colors, e, d
    # Globals

    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    # Destroying the previous screen

    label.config(text="Write the color of the words, not what the word says!")
    label1.config(text="Press Enter to continue")
    b = Label(window, font=20, text=("Time:", timeRemaining))
    b.pack()
    c = Label(window, font=('Times', 50))
    c.pack()
    e = Entry(window)
    e.pack()
    d = Label(window, font=20, text="")
    d.pack()
    # Creating the Color Game screen

    colors = ["Red", "Blue", "Black", "Green", "Purple", "Brown", "Yellow", "Pink", "Orange"]
    score = 0
    timeRemaining = 30
    # Creating/Configuring variables

    def Start(event):
        global timeRemaining, c, colors
        # Globals

        if timeRemaining == 30:
            Timer()
        # Calling the "Timer" function

        random.shuffle(colors)
        c.config(fg=str(colors[0]), text=str(colors[1]))
        # Configuring the label with a random color and word

        window.bind("<Return>", Score)

    def Timer():
        global timeRemaining, b, e
        # Globals

        timeRemaining -= 1
        if timeRemaining > 0:
            b.config(text=("Time:", timeRemaining))
            b.after(1000, Timer)
        # Counting down

        else:
            e.destroy()
            messagebox_txt = "You finished with " + str(score) + " points!"
            messagebox.showinfo("Game Over!", messagebox_txt)
            # A PopUp telling the user's score is created when the time runs out

            Replay(ColorGame)

    def Score(event):
        global score, e
        if e.get().lower() == str(colors[0].lower()):
            score += 1
            label1.config(text=("Score:", score))
            label1.update()
        e.delete(0, 'end')
        Start(1)

    window.bind("<Return>", Start)


def QuizGame():
    global score, b, c, d, e, stringVar, questions
    # Globals

    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    # Destroying the previous screen

    label.config(text="Welcome to Space Quiz!")
    label1.config(text="Press Enter to continue")
    # Creating the main Quiz Game screen

    score = 0
    questions = [["When did the first manned spaceflight take place?", "1. 1958", "2. 1961", "3. 1967", "4. 1975", "2"],
                 ["When was the first Moon Landing?", "1. 1961", "2. 1965", "3. 1969", "4. 1975", "3"],
                 ["Which was the first artificial satellite to orbit Earth?", "1. Sputnik", "2. Skylab", "3. Vostok", "4. Hubble", "1"],
                 ["Which was the first planet to be visited by a space probe?", "1. Venus", "2. Mars", "3. Jupiter", "4. Mercury", "2"]]
    # Creating/Configuring variables

    def Start(event):
        global b, c, d, e, stringVar
        stringVar = StringVar()

        random.shuffle(questions)
        label.config(text=str(questions[0][0]))
        label.update()
        b = Radiobutton(window, font=20, text=str(questions[0][1]), value="1", var=stringVar)
        b.pack()
        c = Radiobutton(window, font=20, text=str(questions[0][2]), value="2", var=stringVar)
        c.pack()
        d = Radiobutton(window, font=20, text=str(questions[0][3]), value="3", var=stringVar)
        d.pack()
        e = Radiobutton(window, font=20, text=str(questions[0][4]), value="4", var=stringVar)
        e.pack()
        # Creating the question screens

        window.bind("<Return>", Question)

    def Question(event):
        global score, b, c, d, e, stringVar, timeRemaining
        # Globals

        if stringVar.get() == str(questions[0][5]):
            label1.config(text="Correct!")
            score += 1
        else:
            label1.configure(text="Wrong!")
        label1.update()
        time.sleep(1)
        questions.remove(questions[0])
        if len(questions) == 0:
            End()
        else:
            b.destroy()
            c.destroy()
            d.destroy()
            e.destroy()
            label1.configure(text=("Score", score))
            label.config(text="Press Enter to continue.")
            window.bind("<Return>", Start)

    def End():
        if score == 4:
            messagebox.showinfo("Game Over!", "You are great at this! You finished with 4 points!")
            Replay(QuizGame)
        elif score == 3:
            messagebox.showinfo("Game Over!", "You are pretty good at this! You finished with 3 points!")
            Replay(QuizGame)
        elif score == 2:
            messagebox.showinfo("Game Over!", "You did ok. You finished with 2 points.")
            Replay(QuizGame)
        elif score == 1:
            messagebox.showinfo("Game Over!", "You are... let's face it.Bad! You finished with 1 point.")
            Replay(QuizGame)
        else:
            messagebox.showinfo("Game Over!", "Wow! You really suck at this! You finished with 0 points!")
            Replay(QuizGame)
        # Creating a PopUp based on the player's score and calling the "Replay" function

    window.bind("<Return>", Start)


def WordGame():
    global c, d, e, timeRemaining, b, score
    # Globals

    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    # Destroying the previous screen

    label.config(text="Copy the word that appears!\nEvery word you copy correctly gives you one point.")
    label1.config(text="Press Enter to continue")
    b = Label(window, font=20, text=("Time:", timeRemaining))
    b.pack()
    c = Label(window, font=('Times', 30))
    c.pack()
    e = Entry(window)
    e.pack()
    d = Label(window)
    d.pack()
    # Creating the Word Game screen

    score = 0
    timeRemaining = 60
    dd = ["Hello", "Programming", "Python", "Error", "Variable", "Print", "Label", "Delete", "Import", "Random",
          "Global", "While", "List", "Input", "Copy-Paste", "String", "Integer", "Float", "Tkinter", "PyGame",
          "PyTurtle", "Button", "Entry", "Messagebox", "For i in range"]
    # Creating/Configuring variables

    def Start(event):
        global timeRemaining
        # Globals

        if timeRemaining == 60:
            Timer()
        # Calling the "Timer" function

        random.shuffle(dd)
        c.config(text=str(dd[0]))
        window.bind("<Return>", Score)

    def Timer():
        global timeRemaining
        # Globals

        timeRemaining -= 1
        if timeRemaining > 0:
            b.config(text=("Time:", timeRemaining))
            b.after(1000, Timer)
        # Counting down

        else:
            b.config(text="Time is up!")
            e.destroy()
            messagebox_txt = "You finished with " + str(score) + " points!"
            messagebox.showinfo("Game Over!", messagebox_txt)
            # A PopUp telling the user's score is created when the time runs out

            Replay(WordGame)

    def Score(event):
        global score
        # Globals

        if e.get() == str(dd[0]):
            score += 1
            d.config(text=("Score:", score))
            dd.remove(dd[0])
        # Checking if the answer was correct and changing the score

        e.delete(0, END)
        # Clearing the answer

        Start(1)

    window.bind("<Return>", Start)


def Replay(game):
    global b, c, d, e, label, label1
    # Globals

    b.destroy()
    c.destroy()
    d.destroy()
    e.destroy()
    # Destroying the previous screen

    label.config(text="What do you want to do?")
    label1.config(text="")
    GoBackButton = Button(window, font=20, text="Go Back", command=lambda: (Begin(""), GoBackButton.destroy(), ReplayButton.destroy(), ExitButton.destroy()))
    GoBackButton.pack()
    if game == ColorGame:
        ReplayButton = Button(window, font=20, text="Play Again", command=lambda: (ColorGame(), GoBackButton.destroy(), ReplayButton.destroy(), ExitButton.destroy()))
        ReplayButton.pack()
    elif game == QuizGame:
        ReplayButton = Button(window, font=20, text="Play Again", command=lambda: (QuizGame(), GoBackButton.destroy(), ReplayButton.destroy(), ExitButton.destroy()))
        ReplayButton.pack()
    elif game == WordGame:
        ReplayButton = Button(window, font=20, text="Play Again", command=lambda: (WordGame(), GoBackButton.destroy(), ReplayButton.destroy(), ExitButton.destroy()))
        ReplayButton.pack()
    ExitButton = Button(window, font=20, text="Exit", command=lambda: (window.quit(), GoBackButton.destroy(), ReplayButton.destroy(), ExitButton.destroy()))
    ExitButton.pack()
    # Creating the screen that appears when the user finishes a game


window.bind("<Return>", GetName)
window.mainloop()
