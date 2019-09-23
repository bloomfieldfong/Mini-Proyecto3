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

# Este servidor puede atender hasta 100 solicitudes por segundo
def cases(solicitudes):

    # Cantidad de solicitudes
    solicitudes_real = solicitudes/60

    # Variables de tiempo
    T = 3600   # tiempo de cierre
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
    t0 = generador(0, solicitudes_real)
    ta = t0
    td = 9999999999999

    while True:
        ### Caso 1
        if( ta <= td  and ta <= T ):
            t = ta
            Na = Na + 1
            n = n + 1
            Tt = generador( t, solicitudes_real )
            ta = Tt
            if( n == 1 ): 
                Y = generador( t, solicitudes_real ) 
                td = t + Y
            A.append(Na)

        ## Caso 2 
        if( td < ta and td <= T ): 
            t = td
            n = n - 1
            Nd = Nd + 1
            if( n == 0 ):
                td = 9999999999999#float("inf")
            else:  
                Y = generador( t, 100 )
            D.append(Nd)

        ## Caso 3
        if(min(ta, td) > t and n > 0):
            t = td
            n = n - 1
            Nd = Nd + 1
            if(n > 0):
                Y = generador( t, 100 )
                td = t + Y
            D.append(Nd)
            
        ## Caso 4
        if(min(ta, td) > T and n == 0):
            Tp = max(t - T, 0)
            break

    return n, Na, Nd, ta, td, A, D, Tp

#solicitudes = sys.argv[0]
#print(str(solicitudes))


# Cantidad de solicitudes
solicitudes_inicial = int(sys.argv[1])

# Ejecutar cases()
cant_solicitudes_reales, cant_solicitudes, cant_departures, tiempo_arrivals, tiempo_departures, multiple_arrivals, multiple_departures, tiempo_maximo = cases(solicitudes_inicial)

# Calcular tiempo idle
idle_time_list = []
idle_time = 0
for i in range(len(multiple_arrivals)):
    idle = multiple_departures[i] - multiple_arrivals[i]
    idle_time_list.append(idle)

for j in range(len(idle_time_list)):
    idle_time = idle_time + idle_time_list[i]

# Calcular tiempo ocupado
tiempo_ocupado = tiempo_departures - tiempo_arrivals

# Calcular tiempo en cola
arrivals_list = multiple_arrivals
arrivals_list.sort(reverse=True)
arrivals_time = 0

for k in range(len(arrivals_list)):
    arrivals_time = arrivals_time - arrivals_list[i]

# Calcular tiempo de cada solicitud en cola
tiempo_promedio = abs(arrivals_time/(solicitudes_inicial/60))

# Calcular cantidad de solicitudes por segundo


# Calcular momento de la ultima solicutud
last = len(multiple_departures)


# Imprimir resultados
print(" Cantidad de solicitudes atendidas por el servidor: ", cant_solicitudes, "\n",
      "Tiempo en que el servidor estuvo ocupado: ", tiempo_ocupado, "\n", 
      "Tiempo en idle: ", idle_time, "\n",
      "Tiempo en cola: ", abs(arrivals_time), "\n",
      "Tiempo promedio de cada solicitud en cola: ", tiempo_promedio, "\n",
      "Tiempo solicitudes en cola por segundo: ", tiempo_promedio/cant_solicitudes, "\n",
      "Momento de salida de la ultima solicitud: ", tiempo_maximo, "\n",)
