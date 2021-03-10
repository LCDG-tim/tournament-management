# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:38:32 2021

@author: Elève
"""


import tkinter as tk
import sqlite3


BDD = sqlite3.connect("players.db")
CURSOR = BDD.cursor()

CURSOR.execute("create table if not exists Players(id INTEGER primary key "
               "autoincrement, pseudo TEXT, rl_mrr FLOAT, hours int,"
               "goals int, assists int, saves int, mvps int)")


TITLE_FONT = ("Arial bold", 30)
YES = tk.YES
BG = "#999999"

class App(tk.Frame):

    def __init__(self) -> None:
        super().__init__()

        self["bg"] = BG

        tk.Label(self, text="Welcome in the tournament manager",
                 bg=BG,
                 font=TITLE_FONT).pack(expand=YES)

        tk.Button(self, text="add a player",
                  command=self.add_player_p).pack(expand=YES)

        self.pack(expand=YES)

        BDD.commit()

        CURSOR.close()
        BDD.close()

    def add_player_p(self):
        def add_player(*evt) -> None:
            elt = (self.pseudo)

        win = tk.Tk()
        win.geometry("400x400")
        win.config(bg=BG)

        master_add_p = tk.Frame(win, bg = BG)

        tk.Label(master_add_p, text="New Player", font=TITLE_FONT,
                 bg=BG).pack(expand=YES)

        form = tk.Frame(master_add_p, bg=BG)
        tk.Label(form, text="Pseudo : ", bg=BG).grid(row=0, column=0,
                sticky=tk.W)
        pseudo = tk.Entry(form, bg=BG)
        pseudo.grid(row=0, column=1)
        tk.Label(form, text="Mmr : ", bg=BG).grid(row=1, column=0, sticky=tk.W)
        self.mmr = tk.Entry(form, bg=BG)
        self.mmr.grid(row=1, column=1)
        tk.Label(form, text="hour of game : ", bg=BG).grid(row=2, sticky=tk.W, column=0)
        self.hdj = tk.Entry(form, bg=BG)
        self.hdj.grid(row=2, column=1)

        form.pack(expand=YES)

        tk.Button(master_add_p, text="Add this players",
                  command=self.add_player)

        master_add_p.pack(expand=YES)

        win.mainloop()


if __name__ == "__main__":
    App().mainloop()
