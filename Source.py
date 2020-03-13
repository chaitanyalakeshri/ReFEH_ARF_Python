import numpy as np
SAAR= 1981
Dt=0.5
Tp=2.26


#D is design storm Duration
D=(Tp*(1+(SAAR/1000)))
d=D
D=d-(D%Dt)
print(D)

y is gumbels reduced variate
y=(-np.log(-np.log(1-(1/T))))

if D<=12:
    R=np.exp( (c*y + d1) + np.log(D) +(e*y) + f )
elif 12<D<=48:
    R=np.exp()
