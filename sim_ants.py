# ------------------------------------- #
# Universidad del Valle de Guatemala    #
# Autoras:                              #
#   Michelle Bloomfield, 16803          #
#   Andrea Cordón, 16076                #
# sim_ants.py                           #
# ------------------------------------- #


import math
import sys
import time
import random


### Arrival: Lambda = 2400 por minuto 
### Departure: Lambda = 6,000 por minuto
def generador(s, x):
    return s - (1/x)* math.log(random.random())
