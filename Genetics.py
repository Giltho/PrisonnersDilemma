# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 17:30:20 2014
PROJECT : TIPE_DILEMME
@author: Sacha
"""
from Ai import ai
import random
from Strategy import *
from Dilemme import game

class populationOfAi:
    
    def __init__(self):
        self.individuals = []
        self.histoPerf = []
    
    def __repr__(self):
        return "I have {} individuals\nHere's my historic \
        : {}".format(len(self.individuals), self.histoPerf)
            
    def fillWithRandomIndividuals(self, n):
        print("Emptying the individuals set")
        self.individuals = []
        print("Generating random Ais")
        for k in range(n):
            D = [random.random() for i in range(1000)]
            self.individuals.append(ai(D))
        print("GeneratedAll")
    
    def __getitem__(self,n):
        return self.individuals[n]
    
    def reproduct(self, first, second):
        D=[0 for j in range(1000)]
        for j in range(1000):
            D[j] = random.choice([first.decisions[j],second.decisions[j]])
        return ai(D)
    
    def makeThemPlay(self,stratlist):
        """Makes every individual play against every predetermined strategies"""
        print("starting to play against strats")
        for strat in stratlist:
            p1 = strat()
            for i in range(len(self.individuals)):
                g = game(p1,self.individuals[i])
                g.play(1000)
                p1.reinit()
                self.individuals[i].reinit()
            del p1
        print("played against all")
        
    def mutate(self, n):
        """mutate indivudual n, with a probability of 1/5
        'x-man' appears once every 500 times"""
        if random.randint(1,250)==1:
            D = [random.random() for i in range(1000)]
            self.individuals[n] = ai(D)
        else:
            t = self.individuals[n].decisions
            for k in range(len(t)):
                if random.randint(1,3) == 1:
                    i = t[k]
                    m = min(i, 1-i)
                    mutation = random.choice([-1,1]) \
                    * m * random.random() / 3
                    t[k] = i + mutation
                    
    def mutateAll(self):
        for i in range(len(self.individuals)):
            self.mutate(i)
            
    def selectBests(self,n):
        """selects the n best individuals"""
        print("selecting best individuals")
        l = self.individuals.copy()
        l.sort()
        return l[-n:]
        
    def createNewGeneration(self, n,stratlist):
        """n is the number of parents which will be chosen
            rember that the population will then be created will have
            (n*(n-1))/2"""
        self.mutateAll()
        self.makeThemPlay(stratlist)
        best = self.selectBests(n)
        self.histoPerf.append(sum(best[-1].histoScores))
        self.individuals = []
        print("starting to create new individuals")
        for i in range(n):
            for j in range(i+1,n):
                self.individuals.append(self.reproduct(best[i],best[j]))
        print("NewGeneration created") 
