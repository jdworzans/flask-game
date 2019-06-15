import matplotlib.pyplot as plt 
import numpy as np
from matplotlib.figure import Figure
próba = [[1,2], [1,1], [2,3]]
def odejmowanie(lista):
    for i in lista:
        i[0]-=0.5
        i[1]-=0.5
    return lista



def rysuj(lista):
    lista = odejmowanie(lista)
    iksy = []
    igreki = []
    for k in lista:
        iksy.append(k[0])
        igreki.append(k[1])
    #print(lista)
    #print(iksy, igreki)
    fig, axis = plt.subplots(1,1)
    # axis = fig.add_axes()
    axis.scatter(iksy[0::2], igreki[0::2], s = 7000, c="pink")
    axis.scatter(iksy[1::2], igreki[1::2], s = 7000, c="blue")
    axis.set_xlim(0,3)
    axis.set_ylim(0,3)
    axis.tick_params(left = False, bottom = False)
    axis.grid()
    return fig 

rysuj(próba)