# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:38:32 2021

@author: Elève
"""


import tkinter as tk
import tkinter.ttk as ttk


import sqlite3


import fonction_utiles as fu


import compete


BDD = sqlite3.connect("players.db")
CURSOR = BDD.cursor()

CURSOR.execute("create table if not exists Players(id INTEGER primary key "
               "autoincrement, pseudo TEXT, plateform text, rl_mmr int, hours int,"
               "goals int, assists int, saves int, mvps int);")



YES = tk.YES


class App(tk.Frame):

    def __init__(self) -> None:
        super().__init__()

        self["bg"] = fu.BG

        tk.Label(self, text="Welcome in the tournament manager",
                 bg=fu.BG,
                 font=fu.TITLE_FONT).pack(expand=YES, pady=7)

        tk.Button(self, text="Add a player",
                  command=self.add_player_p).pack(expand=YES, pady=7)

        tk.Button(self, text="Show All Players", command=self.show_players).pack(expand=YES, pady=7)

        tk.Button(self, text="Delete DB", command=self.execute_code).pack(expand=YES, pady=7)

        tk.Button(self, text="Competition", command=self.compete).pack(expand=YES, pady=7)

        tk.Button(self, text="Quit the App", command=self.quit_main).pack(expand=YES, pady=7)

        tk.Button(self, text="Manage teams", command=self.team_manager).pack(expand=YES, pady=7)

        self.players = []
        self.teams = []
        self.tab = ttk.Treeview()

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
        self.fill_db()

    def quit_main(self) -> None:
        self.quit()
        self.destroy()

    def compete(self):
        compete.App_compete(compete.compo_poules).mainloop()

    def add_player_p(self, *evt):
        def add_player(*evt) -> None:
            elt = (self.pseudo.get(), self.plateform.get(), self.mmr.get(), self.hdj.get(),
                   self.goals.get(), self.assists.get(), self.saves.get(), self.mvps.get())
            CURSOR\
                .execute("insert into Players(pseudo, plateform, "
                        "rl_mmr, hours, goals, assists, saves, mvps)"
                        " VALUES (?, ?, ?, ?, ?, ?, ?, ?)", elt)
            self.win1.destroy()

        self.win1 = tk.Toplevel(self)
        self.win1.geometry("400x400")
        self.win1.config(bg=fu.BG)

        master_add_p = tk.Frame(self.win1, bg = fu.BG)

        tk.Label(master_add_p, text="New Player", font=fu.TITLE_FONT,
                 bg=fu.BG).pack(expand=YES)

        form = tk.Frame(master_add_p, bg=fu.BG)

        tk.Label(form, text="Pseudo : ", bg=fu.BG).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.pseudo = tk.Entry(form, bg=fu.BG)
        self.pseudo.grid(row=0, column=1)

        tk.Label(form, text="Plateform : ", bg=fu.BG).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.plateform = tk.Entry(form, bg=fu.BG)
        self.plateform.grid(row=1, column=1)

        tk.Label(form, text="Mmr : ", bg=fu.BG).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.mmr = tk.Entry(form, bg=fu.BG)
        self.mmr.grid(row=2, column=1)

        tk.Label(form, text="hour of game : ", bg=fu.BG).grid(row=3, sticky=tk.W, pady=5, column=0)
        self.hdj = tk.Entry(form, bg=fu.BG)
        self.hdj.grid(row=3, column=1)

        tk.Label(form, text="Goals : ", bg=fu.BG).grid(row=4, sticky=tk.W, pady=5, column=0)
        self.goals = tk.Entry(form, bg=fu.BG)
        self.goals.grid(row=4, column=1)

        tk.Label(form, text="Saves : ", bg=fu.BG).grid(row=5, column=0, sticky=tk.W, pady=5)
        self.saves = tk.Entry(form, bg=fu.BG)
        self.saves.grid(row=5, column=1)

        tk.Label(form, text="Assists : ", bg=fu.BG).grid(row=6, column=0, sticky=tk.W, pady=5)
        self.assists = tk.Entry(form, bg=fu.BG)
        self.assists.grid(row=6, column=1)

        tk.Label(form, text="MVPs : ", bg=fu.BG).grid(row=7, column=0, sticky=tk.W, pady=5)
        self.mvps = tk.Entry(form, bg=fu.BG)
        self.mvps.grid(row=7, column=1)

        form.pack(expand=YES)

        tk.Button(master_add_p, text="Add this players",
                  command=add_player).pack(expand=YES)

        master_add_p.pack(expand=YES)

        self.win1.mainloop()

    def fill_db(self):
        for i in range(10):
            CURSOR.execute(f"""insert into players (pseudo, plateform,
                                                   hours, rl_mmr, goals,
                                                   saves, assists, mvps)
            values
            {str((fu.get_rdm_pseudo(), fu.get_rdm_pseudo(),
            fu.rdm.randint(20, 2000), fu.rdm.randint(20, 2000), fu.rdm.randint(20, 2000),
            fu.rdm.randint(20, 2000), fu.rdm.randint(20, 2000), fu.rdm.randint(20, 2000)))}""")

    def show_players(self, *evt) -> None:
        tab = None

        CURSOR.execute("select * from players")

        liste = CURSOR.fetchall()

        self.win2 = tk.Toplevel(self)
        self.win2.config(bg=fu.BG)

        tk.Label(self.win2, text="List of Player", font=fu.TITLE_FONT, bg=fu.BG) \
            .pack(expand=YES)

        master = tk.Frame(self.win2, bg=fu.BG)

        tabf = tk.Frame(master, bg=fu.BG)

        self.tab = fu.create_new_tab(tabf)

        tab = self.tab

        tab.pack(side=tk.LEFT, padx=5, pady=(0, 5))

        for i, elt in enumerate(liste, start=1):
            elt = tuple([i] + list(elt[1:]))

            tab.insert('', 'end', iid=i+1, values=elt)

        tabf.pack(expand=YES)

        tk.Button(master, text="Select", command=self.select) \
            .pack(expand=YES, ipadx=100, pady=10)
        scroll = tk.Scrollbar(tabf, orient='vertical', bg=fu.BG, command=tab.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Button(master, text="Filter", command=self.add_filter)

        master.pack(expand=YES)
        self.win2.mainloop()

    def team_manager(self)  -> None:
        def team_selector() -> None:
            win = tk.Toplevel(self.win3)
            master = tk.Frame(win, bg=fu.BG)
            master.pack(expand=YES)

            title = tk.Label(win, text="Choose a teams", bg=fu.BG)
            title.pack(expand=YES)

            playerl = tk.Label(win, text="Player : ", bg=fu.BG)
            playerl.pack(expand=YES)

            for nb, team in enumerate(self.teams, start=1):
                tk.Label(master, text=f"Team {nb} : {team}", bg=fu.BG)

            players = self.tab2.item(self.tab2.selection())["values"]

            for player in players:
                playerl["text"] = "Player : " + str(player[1])



            win.mainloop()

        self.win3 = tk.Toplevel(self)
        self.win3.config(bg=fu.BG)

        tk.Label(self.win3, text="List of Player", font=fu.TITLE_FONT, bg=fu.BG) \
            .pack(expand=YES)

        master = tk.Frame(self.win3, bg=fu.BG)

        tabf = tk.Frame(master, bg=fu.BG)

        self.tab2 = fu.create_new_tab(tabf)

        tab = self.tab2

        tab.pack(side=tk.LEFT, padx=5, pady=(0, 5))

        for i, elt in enumerate(self.players, start=1):
            elt = tuple([i] + list(elt[1:]))

            tab.insert('', 'end', iid=i+1, values=elt)

        tabf.pack(expand=YES)

        tk.Button(master, text="Select", command=team_selector) \
            .pack(expand=YES, ipadx=100, pady=10)
        scroll = tk.Scrollbar(tabf, orient='vertical', bg=fu.BG, command=tab.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        tk.Button(master, text="Filter", command=self.add_filter)

        master.pack(expand=YES)

        self.win3.mainloop()

    def add_filter(self) -> None:
        self.tab = ttk.Treeview

    def execute_code(self, *evt) -> None:
        CURSOR.execute("delete from players")

    def select(self):
        for id_ in self.tab.selection():
            player = self.tab.item(id_).get("values")
            if player not in self.players:
                self.players.append(player)


if __name__ == "__main__":
    a = App()
    a.mainloop()

BDD.commit()

CURSOR.close()
BDD.close()