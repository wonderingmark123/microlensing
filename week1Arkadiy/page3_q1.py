from scipy.optimize import fmin
import numpy as np

#CONSTANTS
kpc = 3.09e19 #metres
M_sun = 1.99e30 #kg
G = 6.67e-11 #N * m**2 * kg**(-2)
c = 3e8 #m/s

#VARIABLES
M = 0.3 * M_sun #mass of our lens
initial_D_l = 1 * kpc #distance to the lens that we're trying to optimise
D_s = 8 * kpc #distance to the source

def d_function(D_l):
	D = D_s * D_l / (D_s - D_l)
	return D

def theta_E_function(D):
	theta_E = np.sqrt((4*G*M) / (c**2 * D))
	return theta_E

def inverted_Re_function(D_l):
	D = d_function(D_l)
	theta_E = theta_E_function(D)
	Re = theta_E*D_l
	return (1/Re)

#trying to minimise 1/Re
fit_results = fmin(inverted_Re_function, initial_D_l, full_output = True)
optimised_D_l = fit_results[0][0]
print('Optimised D_l is ', optimised_D_l, ' m; ', optimised_D_l/kpc, ' kpc.')

D = d_function(optimised_D_l)
theta_E = theta_E_function(D) 
print('Theta_E is ', theta_E, ' radians.')

new_Re = 1/inverted_Re_function(optimised_D_l)
print('Max Re is ', new_Re, 'm.')



observed_theta = np.pi/(180*3600) #1 arcsecond in rads
mass = (observed_theta ** 2) * (c ** 2) * d_function(optimised_D_l) / (4 * G) #assuming the lens stays at the same point
print('Theoretical mass for a 1-arcsec image resolution is ', mass/M_sun, 'solar masses.') #huge!!!


 
 
 