import numpy as np
import matplotlib.pyplot as plt

def plotVectors(vecs, cols, alpha=1):
    """
    Plot set of vectors.

    Parameters
    ----------
    vecs : array-like
        Coordinates of the vectors to plot. Each vectors is in an array. For
        instance: [[1, 3], [2, 2]] can be used to plot 2 vectors.
    cols : array-like
        Colors of the vectors. For instance: ['red', 'blue'] will display the
        first vector in red and the second in blue.
    alpha : float
        Opacity of vectors

    Returns:

    fig : instance of matplotlib.figure.Figure
        The figure of the vectors
    """
    plt.figure()
    plt.axvline(x=0, color='#A9A9A9', zorder=0)
    plt.axhline(y=0, color='#A9A9A9', zorder=0)

    for i in range(len(vecs)):
        x = np.concatenate([[0,0],vecs[i]])
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy', scale_units='xy', scale=1, color=cols[i],
                  alpha=alpha)

#funcao para calcular angulo entre vetores
def ang2Vet(v, u):
    
    #calculando o produto escalar entre v e u
    vInternoU = v.dot(u)
    
    #calculando os modulos de v e u
    vModulo = np.linalg.norm(v)
    uModulo = np.linalg.norm(u)
    
    #calculando o cosseno do angulo entre v e u
    r = vInternoU/(vModulo*uModulo)
    
    #angulo em radianos
    ang = np.arccos(r)
    
    #retornando em graus
    return (180/np.pi)*ang

#criando vetores
u = np.array([0,1])
v = np.array([1, 0])

#definindo as cores dos vetores para plotar o grafico
red = 'red'
blue = 'blue'

#usando funcao do matplotlib para plotar vetores
plotVectors([u, v], [red, blue])

plt.xlim(-5, 10)
plt.ylim(-5, 5)

plt.show()

#usando a funcao criada para calcular o angulo entre u e v
angulo = ang2Vet(u, v)
print(angulo)