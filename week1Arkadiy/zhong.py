#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:57:54 2020

@author: zhongduyi
"""
# degenerate difference flux fit

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import curve_fit
        
def fluxfit(t, to, dFo, Fbase, t_half): 
    F = dFo/ np.sqrt((1+12*np.power((t-to)/t_half , 2)))
    Ft = Fbase + F
    # print(to, dFo, Fbase, t_half )
    return Ft

date, flux_raw, error, twotimeserror = [], [], [], []
file = open('C:\\Users\\wondering\\Desktop\\lab-Semester5\\week1Arkadiy\\lc1053.data','r')
for line in file: 
    splitUp=line.split()
    if not np.isnan(float(splitUp[0])) and not np.isnan(float(splitUp[1])) and not np.isnan(float(splitUp[2])):
        if float(splitUp[0]) != 0 and float(splitUp[1]) != 0 and float(splitUp[2]) != 0:
           if float(splitUp[0]) > 54000 and float(splitUp[1]) <-  3890:
               continue
           if float(splitUp[1]) > 1000:
               continue
           date.append(float(splitUp[0]))
           flux_raw.append(float(splitUp[1]))
           error.append(abs(float(splitUp[2])))
           twotimeserror.append(abs(float(splitUp[2]))*2)
file.close();

flux = []
for i in range(0, len(flux_raw)):
    if flux_raw[i] < -200:
        flux.append(abs(flux_raw[i]))
    else:
        flux.append(flux_raw[i])
        
# fit curve
xdata = np.linspace(np.min(date), np.max(date), 5000)
date_array = np.asarray(date,float)
flux_array = np.asarray(flux,float)

# popt, pcov = curve_fit(fluxfit, date_array, flux_array, bounds =([min(date), min(flux), min(flux), min(date)],[max(date), max(flux), max(flux), max(date)]), sigma = twotimeserror)
popt, pcov = curve_fit(fluxfit, date_array, flux_array, p0=( 53994, 15000, 1000, 100), sigma = twotimeserror ,maxfev = 1000000000)
# print(popt[0])
fig = plt.figure(figsize=(36,6))
ax = fig.add_subplot(1,1,1)
ax.errorbar(date_array, flux_array, xerr = None, yerr = error, label="flux with errorbar for event ii", fmt=".", mfc='darkblue', ms=5, ecolor='lightblue')
ax.legend(loc='upper left', fontsize=24)
ax.plot(xdata, fluxfit(xdata, *popt), 'g--')
ax.set_xlim([min(date)-1, max(date)+1])  
ax.set_ylim([-200, max(flux)+100])
ax.set_xlabel('Time (modified Julian date in days)', fontsize=24)     
ax.set_ylabel('Brightness (Flux)', fontsize=24) 
#plt.gca().invert_yaxis()
plt.grid(True)    
plt.draw()                
plt.show()