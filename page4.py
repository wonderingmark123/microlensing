from matplotlib import pyplot as plt 
import numpy as np

from math import cos,pi,sin,log

blist=[-33,-44,-4,-22]
llist=[280,303,1,121]
Dslist=[50 ,60, 8 ,780]
kpc=3.09e19
Msun=1.99e30
G=6.67e-11
c=3e8
f=1
a=5
R0=8
tE=20
Ns=10e6
T=365*5
Dlstep=0.0001
name=['LMC','SMC','The Galactic Bulge','The Andromeda Galaxy']
for i in range(0,4):
    b=blist[i]/180*pi
    l=llist[i]/180*pi
    Ds=Dslist[i]

    Dl=np.arange(0,Ds,Dlstep)
    
    rho=f*0.01*(a**2 + R0**2 ) /( a**2 + R0**2 + Dl**2 -2 * cos(l) *cos(b) *R0*Dl )
    dtau=G*Msun/c**2 *4*pi*Dl*(Ds-Dl)/Ds * rho *Dlstep *1e9 /kpc
    tau=np.sum(dtau)
    Nev=2/pi*tau/tE*Ns*T
    print(name[i])
    print(tau)
    print(Nev)
print('f = '+str(1/5.6022))