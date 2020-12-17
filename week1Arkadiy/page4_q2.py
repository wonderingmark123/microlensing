from matplotlib import pyplot as plt
import math
import numpy as np

t = np.arange(-5, 5, 0.01)
t0 = 0
tE = 1 #as we are using units of t_E

fig = plt.figure(1, figsize = (10, 8))
data = fig.add_subplot(111)

data.set_title('Lighcurves for PSPL microlensing events', size = 25)
data.tick_params(labelsize=15)
data.set_xlabel('Time t (units of t_E)', size = 20)
data.set_ylabel('Magnification A', size = 20)

for u0 in [1, 0.3, 0.1, 0.03]:
	u = np.sqrt(u0**2+((t-t0)/tE)**2)
	A = (u**2+2)/(u*np.sqrt(u**2+4))
	data.plot(t, A, label = ('u0=' + str(u0)))

data.legend(loc='upper right', shadow=False, fontsize='15')
plt.show()