#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Filename: c:\Users\wondering\Desktop\lab-Semester5\week1Arkadiy\page5_q1.py
# Path: c:\Users\wondering\Desktop\lab-Semester5\week1Arkadiy
# Created Date: Tuesday, November 17th 2020, 2:16:47 pm
# Author: Haotian Song
# 
# Copyright (c) 2020 Your Company
###

from matplotlib import pyplot as plt 
import numpy as np
from math import cos

 

#DATA
blist=[-33, -44, -4, -22] #degrees
llist=[280, 303, 1, 121] #degrees
Dslist=[50, 60, 8, 780] #kpc
Dlstep=0.001 #incriment, in kpc
name=['LMC','SMC','The Galactic Bulge','The Andromeda Galaxy']

 

#CONSTANTS
kpc=3.09e19 #m
Msun=1.99e30 #kg
G=6.67e-11 #N * m**2 * kg**(-2)
c=3e8 #m/s
f=1 #restriction is tau <= 10**(-7), so I just tried severl values to get tau to be less than the limit
a=5 #kpc
R0=8 #kpc
rho_0 = 0.01 * Msun * 1000**3 #kg per KILOparsec
tE=20 #days
Ns=10e6 #stars
T=365*5 #days

 

for i in range(0,4):
    b=blist[i]/180*np.pi #to rads
    l=llist[i]/180*np.pi #to rads
    Ds=Dslist[i]
    Dl=np.arange(0, Ds, Dlstep)

 

    r_sqrd = R0**2 + Dl**2 - 2*cos(l)*cos(b)*R0*Dl #kpc^2
    rho = f * rho_0 * (a**2 + R0**2)/(a**2 + r_sqrd) #in kg per kpc

 

    dtau=(4*np.pi*G)/(c**2 * kpc) * (Ds-Dl) * Dl/Ds * rho * Dlstep #dimentionless (kpc in G is for the correct units)
    tau=np.sum(dtau) #imitating integration

 

    Nev=2/np.pi * tau/tE * Ns * T
    print('Object: ', name[i])
    print('Optical depth tau: ', tau)
    print('Number of possible events: ', Nev)
    pri'''
Filename: c:\Users\wondering\Desktop\lab-Semester5\week1Arkadiy\page5_q1.py
Path: c:\Users\wondering\Desktop\lab-Semester5\week1Arkadiy
Created Date: Tuesday, November 17th 2020, 2:16:47 pm
Author: 皓日普照

Copyright (c) 2020 Your Company
'''
'''
Filename: c:\Users\wondering\Desktop\lab-Semester5\week1Arkadiy\page5_q1.py
Path: c:\Users\wondering\Desktop\lab-Semester5\week1Arkadiy
Created Date: Tuesday, November 17th 2020, 2:16:47 pm
Author: 皓日普照

Copyright (c) 2020 Your Company
'''
nt('')
#print('f = '+str(1/5.6022))