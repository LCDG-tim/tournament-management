# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:21:23 2021

@author: Elève
"""


import random as rdm
import tkinter.ttk as ttk
import tkinter as tk


import string




TITLE_FONT = ("Arial bold", 30)
BG = "#999999"


def get_rdm_pseudo():
    return "".join(rdm.choices(string.ascii_letters, k=rdm.randint(4, 16)))


def create_new_tab(frame: tk.Frame) -> None:
    tab = ttk.Treeview(frame,
                           columns=('Id', 'Pseudo', 'Plateform',
                                    'Mmr', 'Hour of game', 'Goals',
                                    "Assists", "Saves", "MVPs"),
                                height=10
                           )

    tab.heading('Id', text='Id')
    tab.column("Id", width=30)

    tab.heading('Pseudo', text='Pseudo')
    tab.column("Pseudo", width=100)

    tab.heading('Plateform', text='Plateform')
    tab.column("Plateform", width=100)

    tab.heading('Mmr', text="Mmr")
    tab.column("Mmr", width=70)

    tab.heading('Hour of game', text='Hour of game')
    tab.column("Hour of game", width=50)

    tab.heading('Goals', text='Assists')
    tab.column("Goals", width=70)

    tab.heading("Assists", text="Assists")
    tab.column("Assists", width=70)

    tab.heading('Saves', text='Saves')
    tab.column("Saves", width=70)

    tab.heading('MVPs', text='MVPs')
    tab.column("MVPs", width=70)

    tab['show'] = 'headings'
    return tab

