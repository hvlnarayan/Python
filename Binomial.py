__author__ = 'HVLNARAYAN'
# H V Lakshminarayan, Jan 2015, European call using binomial tree
from math import exp, sqrt
import numpy as np
def ec(s,k,r,t,sigma,n):
    '''
    s= stock price; k = strike price; r = cont comp riskfree rate; t= time to expiry;
     sigma is the vol; n= number of steps
    '''
    dt=t/n
    u=exp(sigma*sqrt(dt))
    d=1/u
    p=(exp(r*dt)-d)/(u-d)
    v=np.zeros((1, n+1), dtype=np.float64)

    for j in range(0,n+1,1):
        v[0,j] = s*(u**j)*(d**(n-j))

    for j in range(0,n+1,1):
        v[0,j]=max(v[0,j]-k,0)

    for i in range(n,0,-1):
        for j in range(0,i,1):
            v[0,j]= exp(-r*dt)*(p*v[0,j+1]+(1-p)*v[0,j])

    return v[0,0]








