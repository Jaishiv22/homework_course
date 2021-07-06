import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7]
y_product1 = [100,200,230,120,500,210,400]
y_product2 = [212,323,124,213,102,222,320]


plt.plot(x,y_product1)
plt.plot(x,y_product2)
plt.xlabel("days of week")
plt.ylabel("sales of the day")
plt.legend(["y_product1","y_product2"])

plt.title("salesof product1 and product2 graph")










plt.show()