from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate

from scipy.integrate import fixed_quad
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time

start = time.process_time()

nn = 10                         # Gaussian Quadrature 积分时取的根的个
                                # 数
beta = 100                      # 温度的倒数
er = 1e-6                       # 积分从零开始时, 为避免发散, 从一个非
                                # 常小的数值开始积
R = 1/30                        # 参数 k_epsilon R 的取值
epsabs = 1e-1                   # 用 integrate.quad 积分时限定的绝对误
                                # 差 

#定义用到的函数
def xi(k, mu):
    return k**2 - mu
def n(k, mu):
    x = xi(k,mu)
    n =  1 / (np.exp(beta*x) - 1)
    return n
def z(omega, q, mu):
    return omega - q**2/2 + 2*mu


def pi(omega, q, k, mu):
    """没有积分时的 PI"""
    pi = 1 + n(k+q/2, mu) + n(-k+q/2, mu)
    pi = pi / (xi(k+q/2, mu) + xi(-k+q/2, mu) -omega)
    pi = pi * k**4
    pi = pi -k**2/2 - z(omega, q, mu)/4
    pi = pi*2 / np.pi**2
    return pi

def PI(omega, q, mu):
    """将函数 PI 中的 k 积分掉"""
    zz = z(omega, q, mu)
    if zz<0:
        PI, err = fixed_quad(lambda x: pi(omega, q, x, mu), er, 10,
                             n=nn) 
    else:
        a = np.sqrt(zz/2)
        PI1, err = fixed_quad(lambda x: pi(omega, q, x, mu), er, a-er,
                              n=nn) 
        PI2, err = fixed_quad(lambda x: pi(omega, q, x, mu), a+er,
                              10, n=nn)
        PI = PI1 + PI2
    PI = PI * R
    return PI

def delta(omega, q, rkv, mu):
    """函数 delta^p"""
    zz = z(omega, q, mu)
    if zz<0:
        img = 0
    else:
        k = np.sqrt(zz/2)
        img = 1 + n(k+q/2, mu) + n(-k+q/2, mu)
        img = img * R/(2*np.pi)
        img = img * k**3
    rel = PI(omega, q, mu)
    rel = rel + rkv/(4*np.pi)
    rel = rel +zz/(4*np.pi)
    delta = np.angle(rel + 1j*img) - np.pi
    return delta

NNN = 100
mu = -.5

rkv = 1
q = np.linspace(-4, 4, NNN)
omega = np.linspace(-1, 8, NNN)
#q, omega = np.meshgrid(q, omega)
zzz = np.zeros(NNN*NNN)
zzz.shape = (NNN, NNN)
for i in range(NNN):
    for j in range(NNN):
        zzz[i, j] = delta(omega[i], q[j], rkv, mu)

co = np.zeros(NNN)
cp = np.zeros(NNN)
for i in range(NNN-1):
    for j in range(NNN):
        if zzz[i, j]>-1 and zzz[i+1, j]<-3:
            co[j] = i
y = np.linspace(-1, 3, NNN)
for i in range(NNN):
    c = int(co[i])
    y[i] = omega[c]

plt.plot(q, y, 'r')
oo = q**2/2 - 2*mu -rkv
plt.plot(q, oo, 'b')
plt.show()

q, omega = np.meshgrid(q, omega)
fig = plt.figure()
ax = Axes3D(fig)

ax.plot_surface(omega, q, zzz, cmap=cm.rainbow)

plt.show()
