import numpy as np
from numpy.linalg import inv, solve
import matplotlib.pyplot as plt
f=lambda x:x**4*(1-3*x)
c,t=[],0
x=np.array([-1,-0.5,0,0.5,1])
cases=[f(i) for i in x]
order=2
plt.axvline(x=0,color='k'),plt.axhline(y=0,color='k'),plt.grid()
#Least Square Fitting Model
A=np.zeros(shape=(len(x),order+1))
for i in range(order+1):
    A[:,i]=x**i #A[start row:end row,start column:end column]
a=solve(A.T.dot(A),A.T.dot(cases)) #find factors of the polynomial using LSF
for i in range(len(x)):
    d=A[i,:].dot(a)
    c.append(d)
    plt.scatter(i,sum(c),color='red')
    
plt.show()
for i in list(a):
    print('a={}'.format(i))