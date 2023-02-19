import ctypes
import matplotlib.pyplot as plt
import numpy as np


# Load the shared library into c types.
lib = ctypes.cdll.LoadLibrary('euler.so')

x0 = float(0.0)
y0 = float(1.0)
xf = float(10)
h = float(0.1)
n = int((xf - x0)/h)

# Define the argument types.
euler = lib.euler

euler.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
euler.restype = ctypes.POINTER(ctypes.c_double * n)

def res(x0, y0, xf, h):
    euler = lib.euler
    n = int((xf - x0)/h)
    euler.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
    euler.restype = ctypes.POINTER(ctypes.c_double * n)
    x = np.arange(x0, xf, h)
    return x, np.array(euler(x0, y0, xf, h).contents)[:n]

plt.plot(*res(0, 1, 10, 1), label='h=1')
plt.plot(*res(0, 1, 10, 0.5), label='h=0.5')
plt.plot(*res(0, 1, 10, 0.1), label='h=0.1')
plt.plot(*res(0, 1, 10, 0.01), label='h=0.01')
plt.plot(*res(0, 1, 10, 0.001), label='h=0.001')

plt.plot(res(0, 1, 10, 0.001)[0], 1/4 *(-2*res(0, 1, 10, 0.001)[0] + 3*np.exp(-2*res(0, 1, 10, 0.001)[0]) + 1), label='Analytic')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title("$y'=-2y - x$ with $y(0)=1$, ")
plt.savefig('euler.png')

plt.show()




