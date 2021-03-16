# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:38:32 2021

@author: Elève
"""


import tkinter as tk


import tkinter.ttk as ttk


import sqlite3


BDD = sqlite3.connect("players.db")
CURSOR = BDD.cursor()

CURSOR.execute("create table if not exists Players(id INTEGER primary key "
               "autoincrement, pseudo TEXT, plateform text, rl_mrr int, hours int,"
               "goals int, assists int, saves int, mvps int);")


TITLE_FONT = ("Arial bold", 30)
YES = tk.YES
BG = "#999999"

class App(tk.Frame):

    def __init__(self) -> None:
        super().__init__()

        self["bg"] = BG

        tk.Label(self, text="Welcome in the tournament manager",
                 bg=BG,
                 font=TITLE_FONT).pack(expand=YES, pady=7)

        tk.Button(self, text="Add a player",
                  command=self.add_player_p).pack(expand=YES, pady=7)

        tk.Button(self, text="Show All Players", command=self.show_players).pack(expand=YES, pady=7)

        tk.Button(self, text="Execute code", command=self.execute_code).pack(expand=YES, pady=7)

        tk.Button(self, text="Quit the App", command=self.destroy).pack(expand=YES, pady=7)

        self.win1 = None
        self.win2 = None

        self.pack(expand=YES)

        self.pseudo = None
        self.plateform = None
        self.mmr = None
        self.goals = None
        self.mvps = None
        self.assists = None
        self.hdj = None

    def add_player_p(self, *evt):
        def add_player(*evt) -> None:
            elt = (self.pseudo.get(), self.plateform.get(), self.mmr.get(), self.hdj.get(),
                   self.goals.get(), self.assists.get(), self.saves.get(), self.mvps.get())
            CURSOR\
                .execute("insert into Players(pseudo, plateform, "
                        "rl_mrr, hours, goals, assists, saves, mvps)"
                        " VALUES (?, ?, ?, ?, ?, ?, ?, ?)", elt)
            self.win1.destroy()

        self.win1 = tk.Toplevel()
        self.win1.geometry("400x400")
        self.win1.config(bg=BG)

        master_add_p = tk.Frame(self.win1, bg = BG)

        tk.Label(master_add_p, text="New Player", font=TITLE_FONT,
                 bg=BG).pack(expand=YES)

        form = tk.Frame(master_add_p, bg=BG)

        tk.Label(form, text="Pseudo : ", bg=BG).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.pseudo = tk.Entry(form, bg=BG)
        self.pseudo.grid(row=0, column=1)

        tk.Label(form, text="Plateform : ", bg=BG).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.plateform = tk.Entry(form, bg=BG)
        self.plateform.grid(row=1, column=1)

        tk.Label(form, text="Mmr : ", bg=BG).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.mmr = tk.Entry(form, bg=BG)
        self.mmr.grid(row=2, column=1)

        tk.Label(form, text="hour of game : ", bg=BG).grid(row=3, sticky=tk.W, pady=5, column=0)
        self.hdj = tk.Entry(form, bg=BG)
        self.hdj.grid(row=3, column=1)

        tk.Label(form, text="Goals : ", bg=BG).grid(row=4, sticky=tk.W, pady=5, column=0)
        self.goals = tk.Entry(form, bg=BG)
        self.goals.grid(row=4, column=1)

        tk.Label(form, text="Saves : ", bg=BG).grid(row=5, column=0, sticky=tk.W, pady=5)
        self.saves = tk.Entry(form, bg=BG)
        self.saves.grid(row=5, column=1)

        tk.Label(form, text="Assists : ", bg=BG).grid(row=6, column=0, sticky=tk.W, pady=5)
        self.assists = tk.Entry(form, bg=BG)
        self.assists.grid(row=6, column=1)

        tk.Label(form, text="MVPs : ", bg=BG).grid(row=7, column=0, sticky=tk.W, pady=5)
        self.mvps = tk.Entry(form, bg=BG)
        self.mvps.grid(row=7, column=1)

        form.pack(expand=YES)

        tk.Button(master_add_p, text="Add this players",
                  command=add_player).pack(expand=YES)

        master_add_p.pack(expand=YES)

        self.win1.mainloop()

    def show_players(self, *evt) -> None:
        CURSOR.execute("select * from players")

        liste = CURSOR.fetchall()

        self.win2 = tk.Toplevel()
        self.win2.geometry("200x200")
        self.win2.config(bg=BG)

        tk.Label(self.win2, text="List of Player", font=TITLE_FONT, bg=BG) \
            .pack(expand=YES)

        master = tk.Frame(self.win2, bg=BG)

        scroll = tk.Scrollbar(master, orient='vertical', bg=BG)
        scroll.pack()

        tab = ttk.Treeview(master,
                           columns=('Id', 'Pseudo', 'Plateform',
                                    'Mmr', 'Hour of game', 'Goals',
                                    "Assists", "Saves", "MVPs")
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
        tab.pack(padx = 5, pady = (0, 5))

        print("=============================================\nPlayers : ")
        for i, elt in enumerate(liste, start=1):
            elt = tuple([i] + list(elt[1:]))

            tab.insert('', 'end', iid=i+1, values=elt)

            print(elt)

        print("=============================================")


        tk.Button(master, text="Select").pack(expand=YES, ipadx=100, pady=10)


        master.pack(expand=YES)
        self.win2.mainloop()

    def execute_code(self, *evt) -> None:
        CURSOR.execute("delete from players")


if __name__ == "__main__":
    a = App()
    a.mainloop()

BDD.commit()

CURSOR.close()
BDD.close()