import numpy as np
import matplotlib.pyplot as plt
points=16
def lagrange(xo):
    global points
    x=np.array(range(0,points))
    f=lambda x:x**2 +5
    y=[f(i) for i in x]
    plt.plot(x,y,color='k')
    l,ll=1,[]
    for i in x:
        for j in x:
            if j!=i:
                l=l*((xo-j)/(i-j))
        ll.append(l*y[list(x).index(i)])
        l=1
    return sum(ll)
plt.plot(np.arange(0,points,0.01),lagrange(np.arange(0,points,0.01),),color='red')