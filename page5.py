from matplotlib import pyplot as plt 
import numpy as np

from math import *
t=np.arange(-5,5,0.01)
kpc=3.09e19
Msun=1.99e30
G=6.67e-11
c=3e8
tE=20

rho0=0.01
a=5
u0line = [1,0.3,0.1,0.03]
t0=0
for i in [1,2,3,4]:
    u0=u0line[i-1]
    u=np.sqrt(u0**2+(t-t0)**2)
    A=(u**2+2)/u/np.sqrt(u**2+4)
    plt.plot(t,A)
    plt.xlabel('t/t_E')
    plt.ylabel('A')
    plt.title('u0='+str(u0))
    
plt.show()