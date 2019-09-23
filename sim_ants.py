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
    return x - (1/lambda_)* math.log(random.random())\



def simulacion(no_server =10, tiempo_sim = 60, lambda_entrada = 40, lambda_salida = 10):

    ##Tiempos
    t = 0
    et = 0
    ## Ta = tiempo inicial de llegada de cliente
    ## Td = tiempo de salida 
    ta = generador(t, lambda_entrada)
    td = np.zeros(no_server) + 999999
    # Variables de tiempo
    t = 0   # tiempo de cierre
    # Contadores
    Na = 0  # numero de llegadas al tiempo t
    n = 0   #  clientes en el sistema
    # Listas con tiempos
    A = []
    D = []


    server = np.zeros(no_server)
    # clientes atendidos
    c = np.zeros(no_server)
    server_ocupado = np.zeros(no_server)
    colas_espera = []

    while t < tiempo_sim or n == 0:
        
        ## CASO 1: si ta es el minimo de los tiempos de salida 
        ##Se verifica si hay algun servidor que esta saliendo
        
        
        if ta == min(min(td), ta): 

            if t< tiempo_sim: 
                t = ta # avanzamos el tiempo al tiempo de llegada
                Na += 1 ##Contador de clientes
                ta = generador(t,lambda_entrada) # proxima llegada
                A.append(t)

                ##Se agrega un cliente a un servidor que no esta ocupado 
                if no_server > n: 
                    for i in range(0,no_server):
                        ##Si un verdor esta disponible
                        if server[i] == 0: 
                            server[i] = Na ## el cliente que llego sera atendido en la posicion i
                            ##calcula el tiempo de salida
                            td[i] = generador(t, lambda_salida)  
                            ##Tiempo en el que el servidor estuvo ocupado (se le resta la t ya que ese es el tiempo actual que tuve el proceso)
                            server_ocupado[i]+= td[i] -t
                            break
                else: 
                ##Catnidad de servidores que tuvieron que esperar 
                    et +=1
                    colas_espera.append(min(td)-t)

                    
            
                
                ##Entro un nuevo cliente           
                n += 1
                
        ## CASO 2 Y 3: verifica si el tiempo de salida es mayor al tiempo actual
        ##Si hay un tiempo de salida menor del tiempo actual entonces significa que termino 
        ##el proceso y se desocupo el servidor. Se agregara un nuevo servidor a la posicion que salio
        else:
            ##Posicion del mas bajo
            for i in range(0,len(td)): 
                if td[i] == min(td):
                    pos = i 
            ##avanzamos al tiempo de salida
            t = min(td)
            ##Agregamos el tiempo de salida
            D.append(t)
            ##se atendio cliente en este servidor 
            c[pos] += 1

            ##Si todavia hay clientes por atender hay que agregar uno nuevo a la posicion que se desocupo 
            if n >= no_server: 

                ##Se agrega al nuevo tiempo justo despues de que se va el 
                server[pos] =Na+ 1
                td[pos] = generador(t, lambda_salida)
                ##Tiempo en el que el servidor estuvo ocupado (se le suma la t ya que ese es el tiempo actual)
                server_ocupado[pos]+= td[pos] -t
        
            ##Si no hay clientes que atender entonces td[pos] = inf 
            else:  
                ## tiempo de salida  = inf
                td[pos] = 9999999999
                ##Servidor desocupado
                server[pos] = 0
            ##Se fue un cliente
            n -= 1
    print("\n##########################################")  
    print("#Servidores: "+str(no_server)+", Tiempo de simulacion: "+str(tiempo_sim)+"#")
    print("##########################################")      
    print("\nLos servidores atendieron "+ str(c))
    print("\nLos servidores estuvieron ocupados por: "+ str(server_ocupado))
    print("\nPromedio de server ocupado: "+str(np.sum(server_ocupado)/no_server))
    print("\nLos servidores estuvieron descoupados por: "+str(tiempo_sim - server_ocupado))
    print("\nLos procesos en cola tuviero que esperar: "+str(np.sum(colas_espera)))
    print("\nLa cantidad de procesos que tuvieron que esperar son:"+str(et))
    print("\nEl tiempo en que se atendio el ultimo proceso es de: "+str(D[-1])+" s")
    print("\nSe atendieron "+str(Na)+ " cantidad de procesos")
    





simulacion()
simulacion(10, 1000,40,10)
