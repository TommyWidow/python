import math
import matplotlib.pyplot as plt
import numpy as np

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

D = b**2 - 4 * a * c

x1 = (-b - math.sqrt(D))/ (2 * a)
x2 = (-b + math.sqrt(D))/ (2 * a)

print(f"x1 = {x1}")
print(f"x2 = {x2}")

# x = np.linspace(-30, 30, 20)
# y = a*x**2 + b*x + c
#
# plt.plot(x, y)
# plt.plot([x1, x2], [0, 0], 'ro')
#
# plt.grid(True)
# plt.title('График квадратного уравнения')
#plt.show()
