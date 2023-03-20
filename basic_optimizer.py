import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.optimize import minimize, NonlinearConstraint

def intpen (x0, u0, roh):
    k=0
    x = x0
    u = u0
    convergence = 1
    while convergence > 1e-6:
        res = minimize(eff,x, u)
        # print(res)
        xold = x
        u = roh*u
        x = res.x
        k = k+1
        convergence = abs(x-xold)
    return x, k


def eff(x, u):
    if x> 50:
        return 10000000000
    else:
        p = m.log(-(x-50))
        f = fun(x)
        return f-(u*p)

#Function for testing below
def fun(x):
    return 2*x[0]**2 - 3*(2*x[0] + x[0]**2)

x = 20 #initial guess
u = 20 #initial penalty parameter
p = .9 #penalty decrease factor

ex, it = intpen(x,u,p)

print (ex)
print(it)

thebounds ={(1,25)}
res = minimize(fun, x, bounds=thebounds, tol=1e-6)
print(res)