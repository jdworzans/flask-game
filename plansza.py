import matplotlib.pyplot as plt 
import numpy as np

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
    plt.scatter(iksy[0::2], igreki[0::2], s = 7000, c="pink")
    plt.scatter(iksy[1::2], igreki[1::2], s = 7000, c="blue")
    plt.plot()
    ax = plt.gca()
    #ax.set_xticks([1,2,3])
    #ax.set_yticks([1,2,3])
    plt.xlim(0,3)
    plt.ylim(0,3)
    ax.tick_params(left = False, bottom = False)
    plt.grid()
    plt.show()

rysuj(próba)