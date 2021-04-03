# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:12:55 2021

@author: Elève
"""


import random as rdm
import tkinter as tk


class Poule(list):

    def __init__(self, teams: list) -> None:
        super().__init__()
        self.nb_teams = len(teams)
        self.teams = teams
        pattern = {3: [(0, 1), (0, 2), (1, 2)],
                   4: [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)],
                   5: [(3, 4), (0, 1), (2, 3), (0, 4), (2, 4), (1, 3), (0, 3),
                       (1, 2), (0, 2), (1, 4)]}

        self.list_match = [Match(self, teams[i], teams[j])
                        for i, j in pattern[self.nb_teams]]

    def __str__(self) -> str:
        strr = "["
        for i in self.teams:

            strr += str(i) + ",\n"
        strr += "]"
        return strr



class Player:

    def __init__(self, pseudo: str, plateform: str, hours: int, mmr: int,
                 goals: int, assists: int, saves: int, mvps: int) -> None:
        self.pseudo = pseudo
        self.plateform = plateform
        self.hours = hours
        self.mmr = mmr
        self.goals = goals
        self.assists = assists
        self.saves = saves
        self.mvps = mvps

    def __str__(self) -> str:
        return str(self.pseudo)

    def add_win(self, goals: int = 0, assists: int = 0, saves: int = 0,
                mvps: bool = False) -> None:
        self.add_goals(goals)
        self.add_assists(goals)
        self.add_saves(goals)
        self.add_mvps(mvps)
        self.commit()

    def add_goals(self, nb: int = 0) -> None:
        self.goals += nb

    def add_assists(self, nb: int = 0) -> None:
        self.assists += nb

    def add_saves(self, nb: int = 0) -> None:
        self.saves += nb

    def add_mvps(self, is_: bool = 0) -> None:
        self.add_mvps += int(is_)

    def commit(self, db) -> None:
        db.execute(f"update from player set goals ={self.goals},"
                   " assists={self.assists}, saves={self.saves},"
                   " mvps={self.mvps} where pseudo='{self.pseudo}'")

playersl = [["tim", "Steam", 1, 2, 3, 4, 5, 6],
            ["loa", "Steam", 1, 2, 3, 4, 5, 6],
            ["lou", "Steam", 1, 2, 3, 4, 5, 6],

            ["flo", "Steam", 1, 2, 3, 4, 5, 6],
            ["log", "Steam", 1, 2, 3, 4, 5, 6],
            ["luc", "Steam", 1, 2, 3, 4, 5, 6],

            ["ale", "Steam", 1, 2, 3, 4, 5, 6],
            ["cle", "Steam", 1, 2, 3, 4, 5, 6],
            ["max", "Steam", 1, 2, 3, 4, 5, 6],

            ["mal", "Steam", 1, 2, 3, 4, 5, 6],
            ["eri", "Steam", 1, 2, 3, 4, 5, 6],
            ["mar", "Steam", 1, 2, 3, 4, 5, 6],

            ["mat", "Steam", 1, 2, 3, 4, 5, 6],
            ["ant", "Steam", 1, 2, 3, 4, 5, 6],
            ["tho", "Steam", 1, 2, 3, 4, 5, 6],

            ["leo", "Steam", 1, 2, 3, 4, 5, 6],
            ["aga", "Steam", 1, 2, 3, 4, 5, 6],
            ["luc", "Steam", 1, 2, 3, 4, 5, 6]
            ]


players = [Player(pseudo, plateform, hours, mmr, goals, assists, saves, mvps)
for pseudo, plateform, hours, mmr, goals, assists, saves, mvps in playersl]


rdm.shuffle(players)


nb = len(players)


nb_poules = nb // 3



compo_poules = [[] for i in range(nb_poules)]

for i, j in enumerate(players):
    compo_poules[i % nb_poules].append(j)


class Match:

    def __init__(self, poule: Poule, team1: Player, team2: Player) -> None:
        assert isinstance(poule, Poule), str(type(poule))
        self.team1 = team1
        self.team2 = team2
        self.poule = poule

    def __str__(self) -> str:
        return f"poule : {self.poule} /\n {self.team1} VS {self.team2}"

class App_compete(tk.Toplevel):

    def __init__(self, poules) -> None:
        super().__init__()
        self.poules = poules
        self["bg"] = "#A23434"

        tk.Label(self, text="Tournament").pack(side=tk.TOP, pady=30)

        master = tk.Frame(self, width=1920, height=1080, bg="#000000")
        master.pack()

        self.list_match = self.get_match()

        self.mainloop()

    def get_match(self) -> list:

        pattern = {3: [(0, 1), (0, 2), (1, 2)],
                   4: [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)],
                   5: [(3, 4), (0, 1), (2, 3), (0, 4), (2, 4), (1, 3), (0, 3),
                       (1, 2), (0, 2), (1, 4)]}

        list_match = []
        for poule in self.poules:
            poule2 = Poule(poule)
            for i, j in pattern[len(poule)]:
                list_match.append(Match(poule, poule[i], poule[j]))
#                print(Match(poule, poule[i], poule[j]))
        return list_match

if __name__ == "__main__":
    a = App_compete(compo_poules)
    a.mainloop()
    pass
