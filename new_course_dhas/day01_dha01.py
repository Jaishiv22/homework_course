import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
y= x*x
plt.plot(x,y,"b*--")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Parabola")


plt.show()