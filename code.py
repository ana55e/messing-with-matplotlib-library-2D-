import numpy as np
import matplotlib.pyplot as plt
plt.ion()
phi = np.linspace(0, 2*np.pi, 200000)
for r in range(1,58):

    x = r*np.cos(phi)-np.log(r*phi)
    y = r*np.sin(phi)+np.cos(phi**r)
    plt.plot(x,np.log(np.sin(x)+1/x))
    plt.draw()
    plt.pause(0.1)

for r in range(1,200):

    x = r*np.cos(phi)-np.log(1+r**phi)
    y = r*np.sin(phi)+np.tan(x)
    plt.plot(x,y)
    plt.draw()
    plt.pause(0.1)

plt.show(block=True) 
