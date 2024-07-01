import matplotlib.pyplot as plt
import numpy as np

# Rod
M = 5
R = 200

# Ball
m = 2
vel = 4

d = np.linspace(0,R+20,100)
va = (d*m*vel)/(1/3*M*R*R + m*d*d)

xmax = d[np.argmax(va)]
ymax = va.max()

plt.plot(xmax, ymax, 'r*')
plt.annotate("Best distance: " + str(round(xmax,1)), (0, ymax))

plt.plot(d,va)
plt.show()
