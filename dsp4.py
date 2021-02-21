import scipy.io
from matplotlib import pyplot as plt
from scipy.io import wavfile
import numpy as np
x=[1,2,3,4,5]
w=np.arange(-np.pi,np.pi,0.01*np.pi)
l=len(x)
y=[]
for i in range(0,len(w)):
        s=0
        for n in range(0,(l-1)):
                s=s+x[n]*np.exp(-1*1j*w[i]*n);
        y.append(s)
plt.subplot(211)
plt.stem(w,np.abs(y))
plt.subplot(212)
plt.stem(w,np.angle(y))
plt.show()
