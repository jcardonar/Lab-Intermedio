
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import math

dataact1=np.loadtxt("Data3-1.txt", skiprows=1)

d=dataact1[:,1]
c=dataact1[:,2]

plt.figure(1)
plt.scatter(d,c)
plt.ylabel('Conteos')
plt.xlabel('Distancia [cm]')
plt.title('Conteos vs Distancia [cm]')
#plt.savefig("Lab2_fig2.png")

dd=[]

for i in range(len(d)):
	dd.append(1.0/(d[i]**2))

slope, intercept, r_value, p_value, std_err = stats.linregress(dd,c)

y = []
for i in range(len(dd)):
	y.append(dd[i]*slope + intercept)

plt.figure(2)
plt.scatter(dd, c)
plt.plot(dd, y)
plt.show()
