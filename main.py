import csv
from ctypes import alignment
from lib2to3.pgen2.token import EQUAL
from msilib.schema import Font
from multiprocessing.connection import answer_challenge
from tkinter import font
import turtle
import pandas as pd
from tkinter import *
import tkinter.messagebox
import os, sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
        
a = 0
b= []
screen =turtle.Screen()
screen.title("INDIAN STATE QUIZE")
image = resource_path("India.gif")
screen.addshape(image)

turtle.shape(image)

while a < 50:
    answer_state = screen.textinput(title= f"{a} Guess the State", prompt="What is the next state").title().lower()
    print(answer_state)
    data = pd.read_csv(resource_path("states.csv"))
    all_states = data.state.to_list()
    if answer_state in b:
        tkinter.messagebox.showinfo('','Already it has been entered')
    elif answer_state in all_states:
        b.append(answer_state)
        a=a+1
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        value = data[data.state == answer_state]
        t.goto(int(value.x), int(value.y))
        t.pendown()
        t.write(answer_state)
    else:
        tkinter.messagebox.showinfo('',f'Your Score is : {a}')
        missingstate= []
        missingstate = [new_state for new_state in all_states if new_state not in b]
        # for states in all_states:
            # if states not in b:
            #     missingstate.append(states)
            #     new_data = pd.DataFrame(missingstate)
            #     new_data.to_csv("Missed states.csv")
        new_data = pd.DataFrame(missingstate)
        new_data.to_csv("Missed states.csv")    
        print(missingstate)
        break    
        