# ------------------------------------- #
# Universidad del Valle de Guatemala    #
# Autoras:                              #
#   Michelle Bloomfield, 16803          #
#   Andrea Cordón, 16076                #
# sim_ants.py: simular tiempo de n      #
# servidores en paralelo                #
# ------------------------------------- #

import math
import random
import numpy as np 


def generador(x, lambda_):
    return x - (1/lambda_)* math.log(random.random())




def simulacion(no_server =10, tiempo_sim = 100, lambda_ = 4500,):

        ##Tiempos
    t = 0
    ## Ta = tiempo inicial de llegada de cliente
    ## Td = tiempo de salida 
    ta = generador(t, lambda_)
    td = np.zeros(no_server) + 999999
        # Variables de tiempo
    t = 0   # tiempo de cierre
    Tp = 0  # tiempo extra realizado por el servidor

        # Contadores
    Na = 0  # numero de llegadas al tiempo t
    Nd = np.zeros(no_server)   # numero de servidores atendidos al tiempo t 
    n = 0   #  clientes en el sistema
    # Listas con tiempos
    A = []
    D = []

    server = np.zeros(no_server)
    # clientes atendidos
    C = np.zeros(no_server)

    for i in range(tiempo_sim):

        ## CASO 1: si ta es el minimo de los tiempos de salida 

        if ta == min(ta, min(td)): 
            t = ta # avanzamos el tiempo al tiempo de llegada
            Na += 1 ## llego un cliente
            ta = generador(t,lambda_) # proxima llegada
            A[Na] = t

            ##Se agrega un cliente a un servidor que no esta ocupado 
            if no_server > n: 
                for i in rane(no_server):
                    if server[i] == 0: 
                        server[i] = Na ## el cliente que llego sera atendido en la posicion i
                        ##calcula el tiempo de salida
                        td[i] = generador(t, lambda_)
                        break
            n += 1

        else: 
            ##Buscamos el td menor de todos los que se ingresaron 
            t = min(td)

            ##Posicion del mas bajo
            for i in range(len(td)): 
                if td[i] == min(td)
                    pos = i 
            
            ##se atendio un nuevo cliente en este servidor 
            c[pos] += 1

            ##Si todavia hay clientes por atender hay que agregar uno nuevo a la pos que se desocupo 
        