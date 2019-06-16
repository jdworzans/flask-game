import matplotlib.pyplot as plt

def odejmowanie(lista):
    wynik = []
    for i in lista:
        wynik.append([i[0]-0.5, i[1]-0.5])
    return wynik


def rysuj(lista, col1, col2):
    nowa = odejmowanie(lista)
    iksy, igreki = [], []
    for k in nowa:
        igreki.append(k[0])
        iksy.append(k[1])
    fig, axis = plt.subplots(1,1)
    axis.scatter(iksy[0::2], igreki[0::2], s = 7000, c=col1)
    axis.scatter(iksy[1::2], igreki[1::2], s = 7000, c=col2)
    axis.set_xlim(0,3)
    axis.set_ylim(0,3)
    axis.vlines([1,2],0,3)
    axis.hlines([1,2],0,3)
    axis.set_xticks([0.5, 1.5, 2.5])
    axis.set_xticklabels(["A", "B", "C"])
    axis.set_yticks([0.5, 1.5, 2.5])
    axis.set_yticklabels(["1", "2", "3"])
    axis.tick_params(left = False, bottom = False)
    return fig