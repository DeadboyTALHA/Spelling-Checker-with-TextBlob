import tkinter
from tkinter import *
from textblob import TextBlob


fun = Tk()
fun.title("Talha's Spelling Checker")
fun.geometry("700x400")
fun.config(background = "#dae6f6")

def check_function():
    word = enter_text.get()
    x = TextBlob(word)
    right = str(x.correct())

    cs = Label(fun, text = "Correct text is:", font = ("Futura", 20), bg = "#dae6f6", fg = "#364971")
    cs.place(x = 100, y = 250)
    spell.config(text = right)

heading = Label(fun, text = "Spelling Checker", font = ("Aerial", 30, "bold"), bg = "#dae6f6", fg ="#135AC5")
heading.pack(pady = (50, 0))
enter_text = Entry(fun, justify = "center", width = 30, font = ("Times New Roman", 25), bg = "white", border = 2)
enter_text.pack(pady = 10)
enter_text.focus()

button = Button(fun, text = "Check", font = ("Comic Sans", 20, "bold"), fg = "white", bg = "red", command = check_function)
button.pack()

spell = Label(fun, font = ("Helvetica", 20), bg = "#dae6f6", fg = "#364971")
spell.place(x = 350, y = 250)

fun.mainloop()