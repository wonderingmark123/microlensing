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
        
        # if(float(space_split[2])+float(space_split[1]) < 0):
        #     continue
        if space_split != ['']: #to make sure it won't care about empty lines
            
            if( float(space_split[1]) < -1000):
                continue
            if( float(space_split[1])  > 1e4):
                continue
            date_values.append(float(space_split[0]))
            flux_values.append(float(space_split[1]))
            error_values.append(float(space_split[2]))
    return date_values,flux_values,error_values


locx=[1016.244447,401.147305,970.656195,368.242608]
locy=[378.910711,486.726583,1052.106262,750.385742]
name=[5108,881,4771,605]
# filename='./datalightcurve/'
# filename='./example_lightcurve'
filename='./lightcurve_all'
datanames=os.listdir(filename)
Data_num=len(datanames)
for i in range(300,Data_num):
    dataname=datanames[i]
    dataname = 'lc1011.data'
    f=open(os.path.join(filename,dataname))

    content = f.read() #reading the contents
    line_split = content.split('\n') #splitting into a line-by-line matrix

    date_values = []
    flux_values = []
    error_values=[]
    i=0
    num_lag=0
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
        
        # if(float(space_split[2])+float(space_split[1]) < 0):
        #     continue
        if space_split != ['']: #to make sure it won't care about empty lines
            
            if( float(space_split[1]) < -1e4):
                continue
            if( float(space_split[1])  > 1e4):
                continue
            if( np.abs( float(space_split[1])) > 1000):
                num_lag += 1
            date_values.append(float(space_split[0]))
            flux_values.append(-float(space_split[1]))
            error_values.append(float(space_split[2]))
    if(len(flux_values)<10):
        continue
    total_NUM=len(date_values)
    # plt.subplot(4,1,i+1)
    plt.xlabel('Modified Julian Date / day')
    plt.ylabel('Flux')
    plt.title(dataname)
    a=plt.errorbar(date_values,flux_values,fmt="bo",yerr=error_values)
    if( num_lag > 10):
        plt.show()
    
    
# plt.show()

    # plt.plot(date_values,flux_values,'.')
    # plot the hist for different values
    # plt.subplot(4,1,1)
    # plt.hist(error_values)
    # plt.title('error')
    # plt.subplot(4,1,2)
    # plt.hist(date_values)
    # plt.title('date')
    # plt.subplot(4,1,3)
    # plt.hist(flux_values,log=True)
    # plt.title('flux')