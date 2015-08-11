# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 20:21:13 2014
Project : TIPE_DILEMME
@author: Sacha
"""


import Genetics
import matplotlib.pyplot as plt
import pickle
from Strategy import *

#stratlist = [pavlov,badcopycat,badguy,badmajority,gradual,nicecopycat,niceguy,
# nicemajority,periodicBBC,periodicCCB,randomstrat,spiteful]
stratlist = [niceguy,badguy]
pop = Genetics.populationOfAi()
pop.fillWithRandomIndividuals(105)
for i in range(200):
    print(i+1)
    pop.createNewGeneration(15,stratlist)
plt.plot(pop.histoPerf)
plt.ylabel("scores")
plt.xlabel("generation")
with open("bg2.pop", "wb") as f:
    p = pickle.Pickler(f)
    p.dump(pop)
plt.show()
