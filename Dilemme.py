# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 20:01:41 2014
PROJECT : TIPE_DILEMME
@author: Sacha
"""
from Strategy import *

class game:
    def __init__(self, strat1, strat2):
        self.player1 = strat1
        self.player2 = strat2
        self.scorespart = []

    def play_round(self):
        p1 = self.player1.getmove(self.player2)
        p2 = self.player2.getmove(self.player1)
        if p1 and p2:
            self.player1.addpoints(3)
            self.player2.addpoints(3)
        elif p1 and not p2:
            self.player2.addpoints(5)
            self.player1.addpoints(0)
        elif p2 and not p1:
            self.player1.addpoints(5)
            self.player2.addpoints(0)
        else:
            self.player2.addpoints(1)
            self.player1.addpoints(1)
        self.scorespart.append((self.player1.points,self.player2.points))
    
    def play(self,nb_move):
        for i in range(nb_move):
            self.play_round()
        return (self.scorespart[-1])
        
    def __repr__(self):
        s = "Player 1 says :\n{}\nPlayer 2 says :\
        \n{}\n\n".format(self.player1,self.player2)
        if self.scorespart != []:
            s += "For now the scores are :\nPlayer 1 : {}\nPlayer 2 \
            : {}".format(self.scorespart[-1][0],self.scorespart[-1][1])
        else:
            s+= "It is the begining of the game"
        return s
    