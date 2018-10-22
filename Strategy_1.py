# Imports
import time
from random import *
import random
import math

# Function to be called in game app
def getMove( myScore,  mySnowballs,  myDucksUsed,  myMoveHistory, opponentsScore,  opponentsSnowballs,
             opponentsDucksUsed,  opponentMoveHistory ):

    if opponentsSnowballs == 0: # If they have no snowballs, don't duck
        
        if opponentsDucksUsed < 2: # If they have most of their ducks left, don't waste a throw
            move = "RELOAD"
        else:
            if mySnowballs >= 1: # Testing legality of throwing
                move = "THROW"
            else:
                move = "RELOAD"

    elif opponentsSnowballs == mySnowballs:
        if myDucksUsed < 5 and opponentsSnowballs > 2: # They will probably throw, test legality of ducking
            move = "DUCK"
        else:
            if mySnowballs >= 1:
                move = "THROW"
            else:
                move = "RELOAD"
                
    else: # Most of the time, try to throw as much as we can to pull ahead
        if mySnowballs >= 1:
            move = "THROW"
        else:
            move = "RELOAD"

    if len(myMoveHistory) == 0: # Reload as opening move
        move = "RELOAD"

    if mySnowballs > 6: # Don't hoard more than 6 snowballs
        move = "THROW"
        
    if mySnowballs == 0: 
        if opponentsSnowballs >= 4:
            if myDucksUsed < 4:
                move = "DUCK" # Play it safe if they have many snowballs, we have none, and ducking is legal
            else:
                move = "RELOAD"
        else:
           move = "RELOAD"

    if opponentsScore >= 2 and myDucksUsed < 4 and opponentsSnowballs > 2: # If opponent is one point from winning, be cautious 
        move = "DUCK"

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
    
