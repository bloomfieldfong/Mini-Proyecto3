##Simulacion de eventos para la empresa Gorilla
## Una hora de ejecucion

import random
import math


### Arrival: Lambda = 2400 por minuto 
### Departure: Lambda = 6,000 por minuto
def generador(s, x):
    return s - (1/x)* math.log(random.random())

t = Na = Nd = 0
ES = 0 

to = generador(0, 2400)

ta = to 
td = 999999

A = []

### Caso 1
if ta<=td  and ta <= t:
    t = ta
    Na = Na + 1
    n = n + 1
    tt = generador(tt, 6000)
    ta = tt
    if n == 1: 
        y = generador(t, 6000) 
    A.append(t)

