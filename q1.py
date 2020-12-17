kpc=3.09e19
Msun=1.99e30
G=6.67e-11
c=3e8
Re=sqrt(6.67*1.99d19)/3e8*sqrt(8*kpc * 0.3)
 
Re=sqrt(G.*Msun)./c.*sqrt(8 * 3.09d19 .* 0.3)./kpc
thetaE=Re/8
 
 
theta_obs=pi/180/3600;
 
m=0.3*(thetaE./theta_obs)
u=[1 0.1 0.01];
A=u.^2+2./u./sqrt(u.^2+4)
A_bar=1./u+3./8.*u
 
 
