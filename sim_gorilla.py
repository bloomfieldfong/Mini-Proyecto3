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
tp = 0

start_time = time.time()

A = []
D = []

def cases(ta, td, t):
    ### Caso 1
    if(ta<=td  and ta <= t):
        t = ta
        Na = Na + 1
        n = n + 1
        tt = generador(tt, 6000)
        ta = tt
        if n == 1: 
            y = generador(t, 6000) 
        A.append(t)

    ## Caso 2 
    if(td< ta and td <= t): 
        t = td
        n = n-1
        if n == 0:
            td = 999999
        else:  
            y = generador(t, 6000)
        D.append(t)

    ## Caso 3
    if(min(ta, td) > t and n > 0):
        t = td
        n -= 1
        Nd += 1
        if(n > 0):
            y = generador(t, 6000)
            td = t + y
        D.append(td)
        
    ## Caso 4
    if(min(ta, td) > t and n = 0):
        Tp = max(time.time() - t, 0)
        break

# Puede atender hasta 100 solicitudes por segundo
def gorilla_server():
    break

# Son 10 servidores
def ants_server():
    break