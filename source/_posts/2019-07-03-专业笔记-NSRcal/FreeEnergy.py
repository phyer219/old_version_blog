from matplotlib import pyplot as plt
import numpy as np
from scipy import integrate
zero = 1e-1
cutoff = 1
err = 1.49e-1
mu = 0
beta = 1
R = 1/30
omega = 1
eps = .1                        # infinite small imaginary part 
rkv = 0                         # 2R_p/(k_n^2 v_p)
def xi(k, mu=mu):
    xi = k**2 - mu
    return xi
def n(p, beta=beta):
    n = 1 / (np.exp(beta*xi(p)) - 1)
    return n
def z(omega, q, mu=mu):
    z = omega - 2*q - 2*mu
    return z

def PI(omega, q, eps=eps, mu=mu, zero=zero, cutoff=cutoff,
       err=err):
    def a(k):
        a = (1 + n(k+q/2) + n(-k+q/2))
        return a
    def b(k):
        b = (xi(k+q/2) + xi(-k+q/2) - omega)
        return b
    Irel, error = integrate.quad(lambda k: k**4*(a(k)*b(k)/(b(k)**2 +
                                                            eps**2)), 
                                 zero, cutoff, epsabs=err)
    Iimg, error = integrate.quad(lambda k: k**4*(a(k)*eps**2/(b(k)**2 +
                                                               eps**2)), 
                                 zero, cutoff, epsabs=err)
    I = Irel -1j * Iimg
    PI = 2/(np.pi**2) * I
    return PI
def PIr(q, omega, R=R, mu=mu, zero=zero, cutoff=cutoff, err=err):
    I, error = integrate.quad(lambda k: k**2, zero, cutoff, epsabs=err)
    PIr = -1/(np.pi**2) * I
    I, error = integrate.quad(lambda k: 1, zero, cutoff, epsabs=err)
    PIr = PIr - z(omega, q)/(2*np.pi**2) * I
    PIr = PIr + PI(omega, q)
    PIr = R * PIr
    return PIr

def delta(omega, q, rkv):
    delta = rkv/(4*np.pi) + z(omega, q) + PIr(q, omega)
    delta = np.angle(delta)
    return delta

def omegaInt(rkv, mcutoff=-cutoff, pcutoff=cutoff, cutoff=cutoff):
    f = lambda q, omega: 3 * q**2 * n(omega) * delta (q, omega, rkv)
    omegaInt, error = integrate.dblquad(f, mcutoff, pcutoff, lambda
                                        omega: 0, lambda omega: cutoff
                                        , epsabs=err) 
    return omegaInt



print(omegaInt(0))

