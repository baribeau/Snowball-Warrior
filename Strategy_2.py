# Imports
import time
from random import *
import random
import math

# Function to be called in game app
def getMove( myScore,  mySnowballs,  myDucksUsed,  myMoveHistory, opponentsScore,  opponentsSnowballs,
             opponentsDucksUsed,  opponentMoveHistory ):

    if opponentsSnowballs == 0: # If they have no snowballs, don't duck

        if mySnowballs < 1: # Testing legality of throwing
            tVar = 0
            rVar = 100
        else:
            tVar = 5 * opponentsDucksUsed # Increases chances of throwing when opponent has fewer ducks
            rVar = 100 - tVar
            
        move = choice(rVar*["RELOAD"] + tVar*['THROW'])
           
    elif opponentsSnowballs == mySnowballs:
        if myDucksUsed < 5:
            
            # If opponent is close to winning, make throw more likely
            tVar= 40 * opponentsScore +10#so tVar is never 0
            dVar= 100 - tVar
                
            move = choice(dVar*["DUCK"] + tVar*['THROW'] )
            
        else: # If ducking is illegal
            if mySnowballs >= 1:
                move = "THROW"
            else:
                move = "RELOAD"
                
    else: # Most of the time, try to throw as much as we can to pull ahead
        if mySnowballs >= 1:
            move = "THROW"
        else:
            move = "RELOAD"

    if len(myMoveHistory) == 0: # First turn, reload has best chances
        move = choice(70*["RELOAD"] + 15*["THROW"] + 15*["DUCK"])

    if mySnowballs > 6: # Don't hoard more than 6 snowballs
        move = "THROW"
        
    if mySnowballs == 0 and opponentsSnowballs != 0:

        if myDucksUsed < 5:
            dVar = opponentsSnowballs * 15 # More likely to duck the more snowballs opponent has
            rVar = 100 - dVar
            move = choice(dVar*["DUCK"] + rVar*['RELOAD'])
            
        else:
            move = "RELOAD"

    # If opponent is one point from winning, be cautious (duck chances increase)
    if opponentsScore == 2 and myDucksUsed < 5 and opponentsSnowballs > 3:
        if mySnowballs >= 1:
            move = choice(10*["RELOAD"] + 40*["THROW"] + 50*["DUCK"])
        else:
            move = choice(40*["RELOAD"] + 60*["DUCK"])

    # Pattern recognition from 2-term patterns to 5-term patterns
    for i in range(2,6):
        if len(opponentMoveHistory) > 2*i:
            if opponentMoveHistory[-i:] == opponentMoveHistory[-(2*i):-i]:
                predMove = opponentMoveHistory[-i]

                if predMove == "THROW":
                    
                    if myDucksUsed < 5:
                        move = "DUCK"
                        
                    elif mySnowballs >= 1:
                        move = "THROW"

                    else:
                        move = "RELOAD"

                elif predMove == "RELOAD":
                    
                    if mySnowballs >= 1:
                        move = "THROW"
                    else:
                        move = "RELOAD"  

                else:
                    move = "RELOAD"

    return move
        


