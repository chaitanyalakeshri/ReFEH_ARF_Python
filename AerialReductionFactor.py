import numpy as np

#area A in Km2
def ARF(A):
    A=200
    if A<=20:
        a=0.40-(0.0208*np.log(4.6-(np.log(A))))
        b=0.0394*A**0.354
    elif 20< A < 100:
        a=0.40-(0.00382*(4.6-(np.log(A)))**2)
        b=0.0394*A**0.354
    elif 100<= A <500:
        a=0.40-(0.00382*(4.6-(np.log(A)))**2)
        b=0.0627*A**0.254
    else True:
    return 1-b*D**(-a)


print(ARF(20))