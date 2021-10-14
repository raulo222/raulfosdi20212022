from io import FileIO
from os import PRIO_PGRP


try:
    f = open ('coso.txt','r')
except FileNotFoundError:
    print("no es troba ficher coso.txt")
fx = open ('text.txt','w')
i=0
while i!=5:
    mensaje = f.readline()
    try:
        fx.readline
    except IndexError:
        print("El document esta vuit")
    vector =mensaje.split(" ")
    try:
        miniv= vector[2].split()
        if vector[1]=='+':
            print(vector[0],vector[1],miniv[0],"=",int(vector[0])+int(vector[2]))
            fx.write(vector[0])
            fx.write(vector[1])
            fx.write(miniv[0])
            fx.write("=")
            cositi=int(vector[0])+int(vector[2])
            fx.write(str(cositi))
            fx.write("\n")
            i=i+1
        if vector[1]=='-':
            print(vector[0],vector[1],miniv[0],"=",int(vector[0])-int(vector[2]))
            fx.write(vector[0])
            fx.write(vector[1])
            fx.write(miniv[0])
            fx.write("=")
            cositi=int(vector[0])-int(vector[2])
            fx.write(str(cositi))
            fx.write("\n")
            i=i+1
        if vector[1]=='X':
            print(vector[0],vector[1],miniv[0],"=",int(vector[0])*int(vector[2]))
            fx.write(vector[0])
            fx.write(vector[1])
            fx.write(miniv[0])
            fx.write("=")
            cositi=int(vector[0])*int(vector[2])
            fx.write(str(cositi))
            fx.write("\n")
            i=i+1    
    except IndexError:
        print("el document coso te algun problema")
f.close()
fx.close()