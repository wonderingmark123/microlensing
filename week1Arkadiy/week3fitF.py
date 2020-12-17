#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# Filename: c:\Users\wondering\Desktop\lab-Semester5\week1Arkadiy\week2Thu.py
# Path: c:\Users\wondering\Desktop\lab-Semester5\week1Arkadiy
# Created Date: Thursday, November 26th 2020, 7:37:58 pm
# Author: Haotian Song
# 
# Copyright (c) 2020 Your Company
###
from matplotlib import pyplot as plt
import numpy as np
import os
from scipy.optimize import curve_fit
from math import log10, sqrt



def getdata(filename):
    """
    get the data from .data files
    """
    # f=open(os.path.join(filename,dataname))
    f=open(filename)
    content = f.read() #reading the contents
    line_split = content.split('\n') #splitting into a line-by-line matrix

    date_values = []
    flux_values = []
    error_values=[]
    i=0
    for line in line_split: #reading line by line
        #space_split[1] - date  /day
        #space_split[3] - difference flux
        #space_split[5] - error

        # skip empty lines
        if(line == ''):
            continue
        space_split = line.split()
        
        # delete nan data
        if(np.isnan(float(space_split[0]))):
                continue
        if(np.isnan(float(space_split[1]))):
                continue
        if(np.isnan(float(space_split[2]))):
                continue
        if(float(space_split[1])>1e4):
            continue
        # if(float(space_split[2])+float(space_split[1]) < 0):
        #     continue
        if space_split != ['']: #to make sure it won't care about empty lines
            
            
            date_values.append(float(space_split[0]))
            flux_values.append(-float(space_split[1]))
            error_values.append(float(space_split[2]))
    date_values = np.array( date_values)
    flux_values = np.array( flux_values)
    error_values = np.array( error_values)
    return date_values,flux_values,error_values
def func(t , Fbase, t0, t12 ,F0 ):
    F= Fbase +  F0/ np.sqrt( 1+ 12* np.power( (t- t0 )/ t12, 2 ) )
    return F




locx=[1016.244447,401.147305,970.656195,368.242608]
locy=[378.910711,486.726583,1052.106262,750.385742]
name=['881','605','4771','5108']
# filename='./datalightcurve/'
filename='./example_lightcurve'
# filename='./lightcurve_all'
datanames=os.listdir(filename)
Data_num=len(datanames)
# for i in range(0,Data_num):
for i in range(3,4):
    dataname=datanames[i]
    filename='./example_lightcurve'
    [date_values,flux_values,error_values]=getdata(os.path.join(filename,dataname))
    total_NUM=len(date_values)
    # plt.subplot(4,1,i+1)
    plt.xlabel('Modified Julian Date / day')
    plt.ylabel('Flux')
    plt.title(dataname)
    a=plt.errorbar(date_values,flux_values,fmt="r.",yerr=error_values,label='example')

    popt, pcov = curve_fit(func, date_values, flux_values , maxfev = 10000000000, \
        sigma = error_values*2  \
        ,bounds=([ min(flux_values),min( date_values) , 0, 0 ]\
            ,[max(flux_values) ,max(date_values) , max(date_values), max(flux_values)-min(flux_values)]) )
    
    # u0 = popt[0] / popt[3]
    u0 = 0.1 
    tE = popt[2]/2/sqrt(3) / u0
    perr = np.sqrt(np.diag(pcov))
    # def func(t , Fbase, t0, t12 ,F0 ):
    print( "Fbase" , popt[0], perr[0])
    print( "t0" , popt[1] , perr[1])
    print( "t_{1/2}" , popt[2] , perr[2])
    print( "\Delta F0" , popt[3] , perr[3])
    print( " u0 ", u0)
    print( "tE ", tE )
    plt.plot(date_values, func(date_values, *popt), 'r-', label='fit' )





    filename='./datalightcurve/'
    dataname= 'lc' + name[i]+'.data'
    
    [date_values,flux_values,error_values]=getdata(os.path.join(filename,dataname))
    total_NUM=len(date_values)
    # plt.subplot(4,1,i+1)
    plt.xlabel('Modified Julian Date / day')
    plt.ylabel('Flux')
    plt.title(dataname)
    a=plt.errorbar(date_values,flux_values,fmt="b.",yerr=error_values,label='my result')

    plt.legend()
    plt.show()
