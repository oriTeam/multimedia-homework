
import numpy as np
import matplotlib.pyplot as plt

f= 10
fs=8000
N = 10
A = 1
n= 100
pi = np.pi

try:
    x = np.arange(0,float(N)/f,float(1)/fs)
except ZeroDivisionError:
    x=0
i = 0
y = A*np.sin(2*pi*f*x)
z = 0
while i< 2*n +1:
    z+= A/( (2*i+1)*(2*i+1) ) * np.sin( 2 * (2*i+1) * pi * f * x )
    i+=1

plt.subplot(2,1,1)
plt.plot(x, y, '-', lw=2)
plt.title('Figure 1')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

plt.subplot(2,1,2)
plt.plot(x, z, '-', lw=2)
plt.title('Figure 2')
plt.xlabel('Time')
plt.ylabel('Amplitude ')
plt.grid(True, which='both')
plt.axhline(y=0, color='k')

plt.tight_layout()
plt.show()
