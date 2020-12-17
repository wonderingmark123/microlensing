import numpy as np

u = [1, 0.1, 0.01] #given values for u

def original_A(u):
	A = ((u ** 2) + 2)/(u * np.sqrt((u ** 2) + 4))
	return A

def approximate_A(u):
	#if u is much less than 1, u ** 2 goes to 0
	A_approximate = 1/u
	print(1/u)
	return A_approximate

#compare the two equations
for element in u:
	print('Given u: ', element)
	print('Original A: ', original_A(element))
	print('Approximate A: ', approximate_A(element))
	print('') #to split the segments between each other

#the smaller u is, the better the approximation is


 
 
 