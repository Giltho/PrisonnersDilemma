# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 22:01:51 2014
PROJECT : TIPE_DILEMME
@author: Sacha
"""

from random import choice

class strategy:
    """Mother class strategy, completly abstract, can't be used as such"""
    def __init__(self):
        self.points=0
        self.moves=[]
        self.cooperated = 0
        self.name = "Abstract"
    
    def addpoints(self, pts):
        self.points += pts
        
    def reinit(self):
        self.__init__()
    
    def __repr__(self):
        s = ""
        s += "I am a {} strategy".format(self.name)
        s += "\nRight now, I have {} points and I have played\
        {} moves".format(self.points,len(self.moves))
        return s
    


class pavlov(strategy):
    """Cooperate at first, and then, if last turns it won 3 points or more,
    it repeats last move, else it changes"""
    def __init__(self):
        self.lastpointsadded = None
        strategy.__init__(self)
        self.name = "Pavlov"
    
    def getmove(self,opponent):
        if self.moves == []:
            self.cooperated += 1
            self.moves.append(True)
            return True
        else:
            if self.lastpointsadded >= 3:
                mv = self.moves[-1]
            else:
                mv = not self.moves[-1]
            if mv:
                self.cooperated +=1
            self.moves.append(mv)
            return mv
    
    def addpoints(self, pts):
        self.points += pts
        self.lastpointsadded = pts

class spiteful(strategy):
    """Will always cooperate untill opponent betrays once, then will always
    betray"""
    def __init__(self):
        strategy.__init__(self)
        self.name = "Spiteful"
        self.coop = True
    
    def getmove(self,opponent):
        if not self.coop:
            self.moves.append(False)
            return False
        else:
            if opponent.moves==[]:
                a=True
            else:
                a=opponent.moves[-1]
            if a:
                self.cooperated += 1
            self.coop = a
            self.moves.append(a)
            return a  

class periodicBBC(strategy):
    """Will periodically play 'Betray Betray Cooperate' """
    def __init__(self):
        strategy.__init__(self)
        self.name = "Periodical BBC"
        self.round = 0
        self.m = [False,False,True]
        
    def getmove(self,opponent):
        a=self.m[self.round]
        self.moves.append(a)
        self.round += 1
        self.round = self.round % 3
        if a:
            self.cooperated += 1
        return a
        
class periodicCCB(strategy):
    """Will periodically play 'Cooperate Cooperate Betray' """
    def __init__(self):
        strategy.__init__(self)
        self.name = "Periodical CCB"
        self.round = 0
        self.m = [True, True, False]
        
    def getmove(self,opponent):
        a=self.m[self.round]
        self.moves.append(a)
        self.round += 1
        self.round = self.round % 3
        if a:
            self.cooperated +=1
        return a



class nicemajority(strategy):
    """Play what the opponent played most, on the first move or when the
    opponent cooperated as many times as he betrayed, nicemajority will
    cooperate"""

    def __init__(self):
        strategy.__init__(self)
        self.name = "Majority with a cooperating first move"

    
    def getmove(self,opponent):
        coop = len([i for i in opponent.moves if i==True])
        betr = len(opponent.moves)-coop
        if coop < betr :
            self.moves.append(False)
            return False
        else:
            self.cooperated += 1
            self.moves.append(True)
            return True
            
class badmajority(strategy):
    """Play what the opponent played most, on the first move or when the
    opponent cooperated as many times as he betrayed, badmajority will
    betray"""
    
    def __init__(self):
        strategy.__init__(self)  
        self.name = "Majority with a betraying first move"

    
    def getmove(self,opponent):
        coop = len([i for i in opponent.moves if i==True])
        betr = len(opponent.moves)-coop
        if coop > betr :
            self.cooperated += 1
            self.moves.append(True)
            return True
        else:
            self.moves.append(False)
            return False
            
class nicecopycat(strategy):
    """niceopycat strategy will cooperate the first time and then
    copy the opponent's last move"""
    
    def __init__(self):
        strategy.__init__(self)
        self.name = "Copycat with a cooperating first move"        
        
    def getmove(self, opponent):
        if opponent.moves==[]:
            self.moves.append(True)
            self.cooperated += 1
            return True
        mv = opponent.moves[-1]
        self.moves.append(mv)
        if mv : 
            self.cooperated += 1
        return mv

class gradual(strategy):
    def __init__(self):
        strategy.__init__(self)
        self.name = "Gradual"
        self.betrayed = 0
        self.leftToBetray = 0
    
    def getmove(self, opponent):
        if opponent.moves == []:
            self.moves.append(True)
            return True
        else:
            if opponent.moves[-1] == False:
                self.betrayed += 1
                self.leftToBetray = self.betrayed
            if self.leftToBetray > 0:
                self.leftToBetray -= 1
                self.moves.append(False)
                return False
            else:
                self.cooperated += 1
                self.moves.append(True)
                return True
            
                

class badcopycat(strategy):
    """niceopycat strategy will betray the first time and then
    copy the opponent's last move"""
    
    def __init__(self):
        strategy.__init__(self)
        self.name = "Copycat with a betraying first move"    
        
    def getmove(self, opponent):
        if opponent.moves==[]:
            self.moves.append(False)
            return False
        mv = opponent.moves[-1]
        self.moves.append(mv)
        if mv:
            self.cooperated +=1
        return mv
        
class randomstrat(strategy):
    """Will just play randomly"""

    def __init__(self):
        strategy.__init__(self)
        self.name = "Random"        
    
    def getmove(self, opponent):
        a = choice([True,False])
        self.moves.append(a)
        if a:
            self.cooperated += 1
        return a
        
        
class badguy(strategy):
    """The 'badguy' strategy will always betray"""
    
    def __init__(self):
        strategy.__init__(self)
        self.name = "Badguy"        
    
    def getmove(self, opponent):
        self.moves.append(False)
        return False


class niceguy(strategy):
    """The 'niceguy' strategy will always cooperate"""
    
    def __init__(self):
        strategy.__init__(self)
        self.name = "Niceguys"    
        
    def getmove(self,opponent):
        self.cooperated += 1
        self.moves.append(True)
        return True
    



    


