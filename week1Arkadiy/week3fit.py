import numpy as np
import matplotlib.pyplot as plt
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
    mag_values = []
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

        #  remove the larger time 
        # if(float(space_split[0]) < 2300 +2452000):
        #     continue
        # if(float(space_split[0]) > 2800 +2452000):
        #     continue
        if space_split != ['']: #to make sure it won't care about empty lines
            
            
            date_values.append(float(space_split[0]))
            mag_values.append(float(space_split[1]))
            error_values.append(float(space_split[2]))
        
    date_values = np.array( date_values)
    mag_values = np.array( mag_values)
    error_values = np.array( error_values)
    return date_values,mag_values,error_values


def func(t,t0,Mpsf,fb,te,u0):
    u=np.sqrt( np.power(u0,2) + np.power(((t - t0) / te),2) )
    A=(  np.power(u , 2 ) + 2 )/ u/ np.sqrt( np.power(u , 2 ) + 4 )
    # A= 1/u
    
    # M10 =10 ** Mpsf /10** 2.5 / ( A *fb + (1- fb ) ) 
    for a in A:
        if   a * fb + 1 - fb <= 0:
            print(a,fb,u0,t0)
    M = Mpsf - 2.5 * np.log10(  A * fb + 1 - fb )
    # M= np.nan_to_num(M)
    return M

for filename in {"micro-1.dat","micro-2.dat"}:
    [date_values,mag_values,error_values]=getdata(filename)
    date_values=date_values - 2452000 
    #  plot the light curve 
    plt.xlabel('Modified Julian Date / day')
    plt.ylabel('Flux')
    plt.title(filename)
    mag10=np.power( 10, mag_values )
    a=plt.errorbar(date_values,-mag_values,fmt="b.",yerr=error_values,label=filename)
    
    # plt.show() 
    
    popt, pcov = curve_fit(func, date_values, mag_values , maxfev = 10000000000, \
        sigma =error_values  \
        ,bounds=([min( date_values)  , min(mag_values) , 0, 0 ,0]\
            ,[max(date_values) ,max(mag_values) , 1, max(date_values), 1]) )
    # t0,Mpsf,fb,te,u0
    perr = np.sqrt(np.diag(pcov))
    print( "t0" , popt[0], perr[0])
    print( "Mpsf" , popt[1] , perr[1])
    print( "fb" , popt[2] , perr[2])
    print( "te" , popt[3] , perr[3])
    print( "u0" , popt[4] , perr[4])
    # popt = [2500,  18.8 , 0.5, 10, 0.1 ]
    plt.plot(date_values,- func(date_values, *popt), 'r-', label='fit' )
    plt.legend()
    plt.show()
