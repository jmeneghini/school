import ctypes
import matplotlib.pyplot as plt
import numpy as np


# Load the shared library into c types.

lib = ctypes.cdll.LoadLibrary('instability.so')

x0 = float(0.0)
y0 = float(1.0)
xf = float(10)
h = float(0.1)
n = int((xf - x0)/h)

# Define the argument types.
euler = lib.euler


def res(x0, y0, xf, a, h):
    euler = lib.euler
    n = int((xf - x0)/h)
    euler.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
    euler.restype = ctypes.POINTER(ctypes.c_double * n)
    x = np.arange(x0, xf, h)
    return x, np.array(euler(x0, y0, xf, a, h).contents)[:n]

a = 4; h = 1
res1 = res(0, 1, 10, a, h)
plt.plot(res1[0], res1[1], label='h=1')
h = 0.5
res3 = res(0, 1, 10, a, h)
plt.plot(res3[0], res3[1], label='h=0.5')
h = 0.1
res5 = res(0, 1, 10, a, h)
plt.plot(res5[0], res5[1], label='h=0.1')
h = 0.01
res6 = res(0, 1, 10, a, h)
plt.plot(res6[0], res6[1], label='h=0.01')
plt.plot(res6[0], np.exp(-a*res6[0]), label='Analytic')
plt.ylim(-1.1, 1.1)
plt.xlim(0, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title(r"$y'=e^{-\alpha x} $ with $y(0)=1$ and $\alpha = 4$ ")
plt.savefig('instability.png')

plt.show()




