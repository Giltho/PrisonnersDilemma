# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 16:16:42 2014
PROJECT : TIPE_DILEMME
@author: Sacha
"""
from Strategy import strategy

class ai(strategy):
    
    def __init__(self, D):
        strategy.__init__(self)
        if len(D) != 1000:
            raise Exception("Error in Decisions table")
        self.name = "Artificial Intelligence"
        self.histoScores = []
        self.decisions = D
        self.betrayed = 0
        self.nbCoups = 0
 
    def __repr__(self):
        return strategy.__repr__(self) + \
        "Here are my last scores : {}".format(self.histoScores)
     
    def reinit(self):
        self.histoScores.append(self.points)
        self.points = 0
        self.moves=[]
        self.cooperated = 0
        self.betrayed = 0
        self.nbCoups = 0
        
    def getmove(self, opponent):
        if self.moves == []:
            self.nbCoups += 1
            self.moves.append(True)
            return True
        if opponent.moves[-1] == False:
            self.betrayed += 1
        KP = self.points/ (self.nbCoups * 5)
        KCS = self.cooperated / self.nbCoups
        KCO = (self.nbCoups - opponent.cooperated) / self.nbCoups
        K = (KP + KCS + KCO)/3

        #print("K : {} doit etre  a {}  pour coopérer".format(K, self.decisions[self.whereDecide][self.betrayed]))
        mv = self.decisions[int(opponent.moves[-1])][self.betrayed] <= K
        self.nbCoups +=1
        if mv:
            self.cooperated += 1
        self.moves.append(mv)
        return mv
    
    def __lt__(self, other):
        return sum(self.histoScores) < sum(other.histoScores)
    def __le__(self,other):
        return sum(self.histoScores) <= sum(other.histoScores)
    def __gt__(self,other):
        return sum(self.histoScores) > sum(other.histoScores)
    def __ge__(self,other):
        return sum(self.histoScores) >= sum(other.histoScores)
