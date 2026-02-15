from math import *
import matplotlib.pyplot as plt

h = 0.001
x_values = []
derivative_values = []
cos_values = []

x = -pi
count = 0

while x <= pi:
    d = (sin(x + h) - sin(x)) / h
    c = cos(x)
    if count < 20:
        print(x, d, c)
    x_values.append(x)
    derivative_values.append(d)
    cos_values.append(c)
    x += 0.001
    count += 1

plt.plot(x_values, derivative_values)
plt.plot(x_values, cos_values)
plt.show()
