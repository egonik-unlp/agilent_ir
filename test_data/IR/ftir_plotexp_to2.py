# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 17:46:45 2020

@author: eduar
"""
##Librerias
from os import listdir
from os.path import isfile, join

##Funciones

def plotter_ir(filename,Yi):
    d_crudos=list()
    for line in open(filename, encoding="utf8"):
        line=line.replace("\n", "")
        line = line.replace(",",".")
        d_crudos.append(line)
    trans=d_crudos[6:]    
    fin=float(d_crudos[2])
    ini=float(d_crudos[1])
    long=float(d_crudos[0])
    nus=list()
    paso=(ini - fin)/long
    ini_fal=ini
    
    for i in trans:
        nus.append(ini_fal)
        ini_fal-=paso
    trans_flo=list()
    
    for i in trans:
        trans_flo.append(float(i))
    esto=(nus,trans_flo)
    
    d2=filename+"_espectro.txt"
    d3 = filename+"_espectro.png"
    f=open(d2,"w")
    pu=list(range(len(trans)))
    for i in pu:
        u=int(i)
        f.write(str(nus[u])+"   "+str(trans_flo[u]) +"\n")
    import matplotlib.pyplot as plt
    if Yi == "y" or Yi == "Y":
        plt.plot(nus,trans_flo)
        plt.axis([4000,620,30,105])
        plt.savefig(d3)
        plt.show()
def cargar_folder():
    a = listdir()
    x = [i for i in a if ".asp" in i]
    return x    
#--------------------------------Programa-----------------------------------
X = cargar_folder()
print("Desea graficar los espectros [y/n] =")
Y = input()
for i in X:
    plotter_ir(i,Y)
print("todo exportado")
    
    