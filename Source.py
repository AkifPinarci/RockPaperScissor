# Mehmet Akif Pinarci
# CS 3750
# 9/7/2020
import tkinter as tk
import random
import time

gameWindow = tk.Tk()
user = str()
rock = "Rock"
paper = "Paper"
scissor = "Scissor"


def computerPick():
    options = ["Rock", "Paper", "Scissor"]
    computer = random.choice(options)
    return computer


def winner(entry1):
    entry2 = computerPick()
    if entry1 == entry2:
        time.sleep(0.2)
        result.insert(tk.INSERT, "Draw\n(Computer's Pick is {pick})\n".format(pick=entry1))
    elif entry1 == "Rock" and entry2 == "Paper":
        time.sleep(0.2)
        result.insert(tk.INSERT, "Computer won!\n(Computer's Pick is {pick})\n".format(pick=entry2))
    elif entry2 == "Rock" and entry1 == "Paper":
        time.sleep(0.2)
        result.insert(tk.INSERT, "You won!\n(Computer's Pick is {pick})\n".format(pick=entry2))
    elif entry2 == "Paper" and entry1 == "Scissor":
        time.sleep(0.2)
        result.insert(tk.INSERT, "You won!\n(Computer's Pick is {pick})\n".format(pick=entry2))
    elif entry1 == "Paper" and entry2 == "Scissor":
        time.sleep(0.2)
        result.insert(tk.INSERT, "Computer won!\n(Computer's Pick is {pick})\n".format(pick=entry2))
    elif entry2 == "Rock" and entry1 == "Scissor":
        time.sleep(0.2)
        result.insert(tk.INSERT, "Computer won!\n(Computer's Pick is {pick})\n".format(pick=entry2))
    elif entry1 == "Rock" and entry2 == "Scissor":
        time.sleep(0.2)
        result.insert(tk.INSERT, "You won!\n(Computer's Pick is {pick})\n".format(pick=entry2))

    return True



def printt():
    print("Akif")


button1 = tk.Button(gameWindow, text="Rock", fg="red", command=lambda: winner(rock))
# button1.bind("<Button-1>",winner(rock,computerPick()))
button2 = tk.Button(gameWindow, text="Paper", fg="green", command=lambda: winner(paper))
# button2.bind("<Button-1>",winner(paper,computerPick()))
button3 = tk.Button(gameWindow, text="Scissor", fg="blue", command=lambda: winner(scissor))
# button3.bind("<Button-1>",winner(scissor,computerPick()))
results = tk.Label(text="Results")
result = tk.Text(gameWindow, height=40, width=30)
button1.pack()
button2.pack()
button3.pack()
results.pack()
result.pack()

gameWindow.mainloop()
