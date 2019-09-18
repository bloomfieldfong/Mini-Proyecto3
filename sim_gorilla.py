# ------------------------------------- #
# Universidad del Valle de Guatemala    #
# Autoras:                              #
#   Michelle Bloomfield, 16803          #
#   Andrea Cordón, 16076                #
# sim_gorilla.py                        #
# ------------------------------------- #

# Simulacion de eventos para la empresa Gorilla
# Una hora de ejecucion

import random
import math
import sys
import time


### Arrival: Lambda = 2400 por minuto 
### Departure: Lambda = 6,000 por minuto
def generador(s, x):
    return s - (1/x)* math.log(random.random())

# # Variables de tiempo
# T = 0   # tiempo de cierre
# Tp = 0  # tiempo extra realizado por el servidor
# t = 0   # tiempo de la simulación

#     # Contadores
# Na = 0  # numero de llegadas al tiempo t
# Nd = 0  # numero de salidas al tiemop t
    
#     # Estado del sistema
# n = 0   # numero de solicitudes en el sistema en el tiempo t 

#     # Listas con tiempos
# A = []
# D = []

# Este servidor puede atender hasta 100 solicitudes por segundo
def cases():
    # Variables de tiempo
    T = 0   # tiempo de cierre
    Tp = 0  # tiempo extra realizado por el servidor
    t = 0   # tiempo de la simulación

        # Contadores
    Na = 0  # numero de llegadas al tiempo t
    Nd = 0  # numero de salidas al tiemop t
        
        # Estado del sistema
    n = 0   # numero de solicitudes en el sistema en el tiempo t 

        # Listas con tiempos
    A = []
    D = []

    # Se comienza la simulacion
    t = Na = Nd = 0
    t0 = generador(0, 2400)
    ta = t0
    td = float("inf")

    ### Caso 1
    if( ta <= td  and ta <= T ):
        t = ta
        Na += 1
        n += 1
        Tt = generador( tt, 6000 )
        ta = Tt
        if( n == 1 ): 
            Y = generador( t, 6000 ) 
            td = t + Y
        A.append(Na)

    ## Caso 2 
    if( td < ta and td <= T ): 
        t = td
        n -= 1
        Nd += 1
        if( n == 0 ):
            td = float("inf")
        else:  
            Y = generador( t, 6000 )
        D.append(Nd)

    ## Caso 3
    if(min(ta, td) > t and n > 0):
        t = td
        n -= 1
        Nd += 1
        if(n > 0):
            Y = generador(t, 6000)
            td = t + Y
        D.append(Nd)
        
    ## Caso 4
    if(min(ta, td) > T and n == 0):
        Tp = max(time.time() - T, 0)

    return Na, ta, td

cant_solicitudes, tiempo_arrivals, tiempo_departures = cases()
print(cant_solicitudes)
print(tiempo_arrivals)
print(tiempo_departures)