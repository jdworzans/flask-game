import matplotlib.pyplot as plt

def odejmowanie(lista):
    #for i in lista:
        # i[0]-=0.5
        # i[1]-=0.5
    return lista


def rysuj(lista, col1, col2):
    lista = odejmowanie(lista)
    iksy, igreki = [], []
    for k in lista:
        iksy.append(k[0])
        igreki.append(k[1])
    fig, axis = plt.subplots(1,1)
    axis.scatter(iksy[0::2], igreki[0::2], s = 7000, c=col1)
    axis.scatter(iksy[1::2], igreki[1::2], s = 7000, c=col2)
    axis.set_xlim(0,3)
    axis.set_ylim(0,3)
    axis.set_xticks([1,2,3])
    axis.set_yticks([1,2,3])
    axis.tick_params(left = False, bottom = False)
    axis.grid()
    return fig 
