import ctypes
import matplotlib.pyplot as plt
import numpy as np


# Load the shared library into c types.

lib = ctypes.cdll.LoadLibrary('rk4.so')

x0 = float(0.0)
y0 = float(1.0)
xf = float(10)
h = float(0.1)
n = int((xf - x0)/h)

# Define the argument types.
rk4 = lib.rk4

analytic = lambda x: np.exp(-x**2/2)

def res(x0, y0, xf, h):
    n = int((xf - x0)/h)
    rk4.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
    rk4.restype = ctypes.POINTER(ctypes.c_double * n)
    x = np.arange(x0, xf, h)
    return x, np.array(rk4(x0, y0, xf, h).contents)[:n]

h = 5.0e-3
res1 = res(0, 1, 10, h)

plt.figure(1, figsize=(10, 8))

plt.plot(res1[0], res1[1], label='h=5e-3')
plt.plot(res1[0], analytic(res1[0]), '--',  label='Analytic')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r"$y'=-xy $ with $y(0)=1$")
plt.legend()

plt.savefig('rk4.png')

relative_error = np.abs((analytic(res1[0]) - res1[1])/analytic(res1[0]))
plt.figure(2, figsize=(10, 8))
plt.plot(res1[0], relative_error, label='Relative Error')
plt.xlabel('x')
plt.ylabel('Relative Error')
plt.title(r"Relative Error for $y'=-xy $ with $y(0)=1$ and h=5e-3")
plt.legend()

plt.savefig('rk4_error.png')

plt.show()