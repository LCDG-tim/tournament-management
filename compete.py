# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:12:55 2021

@author: Elève
"""


import random as rdm


class Player:

    def __init__(self, pseudo, plateform, hours, mmr, goals, assists,
                 saves, mvps) -> None:
        self.pseudo = pseudo
        self.plateform = plateform
        self.hours = hours
        self.mmr = mmr
        self.goals = goals
        self.assists = assists
        self.saves = saves
        self.mvps = mvps

    def __str__(self) -> str:
        return self.pseudo


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

print(compo_poules)


if __name__ == "__main__":
    pass
