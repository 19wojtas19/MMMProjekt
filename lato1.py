import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


# R = 1000
# C = 100e-9


# Z1 = R
# Z2 = -1j/(w*C)
# G = Z2/(Z1+Z2)
f = np.logspace(-1, 6, 1e3)
w = 2*np.pi*f
coeff = [3.2, 2, 1, 4, 5]
np.roots(coeff)

# print(np.roots(coeff)[0])
# A = np.roots(coeff)[0]
# print(A)

Y0 = 1
Y1 = 1j*w-np.roots(coeff)[0]
Y2 = 1j*w-np.roots(coeff)[1]
Y3 = 1j*w-np.roots(coeff)[2]
Y4 = 1j*w-np.roots(coeff)[3]
H = Y0/(Y1*Y2*Y3*Y4)
plt.figure(figsize=[12,3])
plt.subplot(121)
plt.semilogx(f,20*np.log10(abs(H)))
plt.show()
plt.grid(True,which='both')
plt.subplot(122)
plt.semilogx(f,np.angle(H)*180/np.pi)
plt.show()
plt.grid(True,which='both')




# cf = [3, 2, 4]
# np.roots(cf)
#
#
# def fun(x, a=1, b=-7, c=5, d=13):
#     return a * x ** 3 + b * x ** 2 + c * x + d
#
#
# x = np.linspace(-2, 7, 1000)
# sol = optimize.root(fun,)
# sol.x
#
#
# plt.plot(x, fun(x), lw=3)
# plt.plot(sol.x, fun(sol.x), 'd', ms=10)
# plt.axhline(0, color='red', lw=0.5)
# plt.show()



