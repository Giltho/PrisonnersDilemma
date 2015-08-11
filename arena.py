# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:05:08 2015
PROJECT : TIPE_DILEMME
@author: Sacha
"""

import Genetics
import matplotlib.pyplot as plt
import pickle
from Strategy import *
from Dilemme import game
stratlist = [pavlov,badcopycat,badguy,badmajority,gradual,nicecopycat,niceguy,\
 nicemajority,periodicBBC,periodicCCB,randomstrat,spiteful]
dico = {}
for strat1 in stratlist:
    p1 = strat1()
    print(p1.name)
    a=0
    for strat2 in stratlist:
        p2 = strat2()
        g = game(p1, p2)
        g.play(1000)
        a+= p1.points
        p1.reinit()
        del p2
        del g
    dico[p1.name]=a
    del p1

s=""
for i in dico.keys():
    s+="{} : {} \n".format(i, dico[i])

f=open("arenaScores.txt","w")
f.write(s)
f.close()        