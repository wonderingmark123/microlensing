

from math import sqrt


# te= 20.629971754843453 *24 *60*60
te=20.01180497486381 *24 *60*60
# te = 199 *24 *60*60
teerr=0.5956137707616701


v=50*1e3 # m/s
verr= 30 *1e3 
c=3e8
kpc=3.09e19 # m
Msun=1.99e30
G=6.67e-11


Ds=8 * kpc  # m
Dl= 5 *kpc
Dlerr=2 * kpc
M = c**2 /4 /G * ( te * v )**2 * Ds *Dl/(Ds-Dl)**3 /Msun
print(M)

DM=M* sqrt( 4* ( ( teerr / te ) **2 + ( verr / v ) ) + (( Ds + Dl *2 ) /(Ds - Dl) * Dlerr /Dl)**2 )
print(DM) 