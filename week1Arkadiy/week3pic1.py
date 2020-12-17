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
    date_base = []
    flux_base = []
    error_base = []
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
            # if( -float(space_split[1]) < 3000):
            if(True):
                date_base.append(float(space_split[0]))
                flux_base.append(-float(space_split[1]))
                error_base.append(float(space_split[2]))
    date_values = np.array( date_values)
    flux_values = np.array( flux_values)
    error_values = np.array( error_values)
    date_base = np.array( date_base)
    flux_base = np.array( flux_base)
    error_base = np.array( error_base)
    
    return date_values,flux_values,error_values,date_base,flux_base,error_base
def func(t , Fbase, t0, t12 ,F0 , A,B ,phi, w1, w2):
    Fbase = funcBase( t , A,B,Fbase ,phi, w1, w2 )
    F= Fbase +  F0/ np.sqrt( 1+ 12* np.power( (t- t0 )/ t12, 2 ) )
    return F

def funcBase( t , A,B,C ,phi, w1, w2 ):
    F = A * np.sin( t * w1+ phi)+ B *np.cos(w2*t) +C
    return F


locx=[1016.244447,401.147305,970.656195,368.242608]
locy=[378.910711,486.726583,1052.106262,750.385742]
name=['881','605','4771','5108']
# filename='./datalightcurve/'
filename='./example_lightcurve'
# filename='./lightcurve_all'
datanames=os.listdir(filename)
Data_num=len(datanames)
for i in range(0,1):
# for i in range(3,4):
    dataname=datanames[i]
    filename='./example_lightcurve'
    [date_values,flux_values,error_values,date_base,flux_base,error_base]\
        =getdata(os.path.join(filename,dataname))
    total_NUM=len(date_values)
    # plt.subplot(4,1,i+1)
    plt.xlabel('Modified Julian Date / day')
    plt.ylabel('Flux')
    plt.title(dataname)
    # a=plt.errorbar(date_values,flux_values,fmt="r.",yerr=error_values,label='example')
    a=plt.errorbar(date_base,flux_base,fmt="r.",yerr=error_base,label='example')
    # plt.show()
    popt, pcov = curve_fit(func, date_base, flux_base , maxfev = 1000000, \
        sigma = error_base*2  \
            ,p0=[-100 , 54000 , 100 , 15000 ,1470, 1000 ,0,2*np.pi/600, 2*np.pi/500])
        # ,bounds=([ \
        #     100 , -np.inf ,min(flux_base), 0, 0,0]\
        #     ,[\
        #         max(flux_base) - min(flux_base),  max(flux_base) - min(flux_base) ,max(flux_base), 2*np.pi, np.pi / 50, np.pi / 50]) )
    # po=np.polyfit(date_base , flux_base,10, w= 1/error_base)#
    # funpolyfit=np.poly1d(po)#
    
    date_x= np.linspace( np.ceil(min(date_values)),np.ceil(max(date_values)), 1000)
    plt.plot(date_x, func(date_x, *popt), 'r-', label='fit' )
    # plt.plot(date_x, funpolyfit(date_x), 'r-', label='fit' )
    # print(popt)
    # plt.show()
    # popt, pcov = curve_fit(func, date_values, flux_values-funpolyfit(date_values) , maxfev = 10000000000, \
    #     sigma = error_values*2  \
    #     ,bounds=([ min(flux_values),min( date_values) , 0, 0 ]\
    #         ,[max(flux_values) ,max(date_values) , max(date_values), max(flux_values)-min(flux_values)]) )
    
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

    # def funcBase( t , A,B,C ,phi, w1, w2 ):
    print( "A ", popt[4], perr[4])
    print( "B ",popt[5] , perr[5])
    
    print("phi", popt[6] , perr[ 6])
    print("w1 " , popt[7], perr[7])
    print("w2 " , popt[8], perr[8])
    
    # plt.plot(date_values, func(date_values, *popt), 'r-', label='fit' )
    





    filename='./datalightcurve/'
    dataname= 'lc' + name[i]+'.data'
    
    [date_values,flux_values,error_values,a,a,a]=getdata(os.path.join(filename,dataname))
    total_NUM=len(date_values)
    # plt.subplot(4,1,i+1)
    plt.xlabel('Modified Julian Date / day')
    plt.ylabel('Flux')
    plt.title(dataname)
    a=plt.errorbar(date_values,flux_values,fmt="b.",yerr=error_values,label='my result')

    plt.legend()
    plt.show()
