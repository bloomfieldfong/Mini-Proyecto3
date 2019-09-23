import math

x = [1,2,3,4]

print(min(x))

##Posicion del mas bajo
for i in range(len(x)): 
    if x[i] == min(x):
        pos = i
        print(str(pos)) 
            