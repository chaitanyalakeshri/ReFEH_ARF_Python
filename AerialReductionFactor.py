import matplotlib.pyplot as plt
import numpy as np
#D is design storm duration
#D= Tp*(1+(SAAR/1000))
D=5

#area A in Km2
def ARF(A):
    if A<=20:
        a=0.40-(0.0208*np.log(4.6-(np.log(A))))
        b=0.0394*A**0.354
    elif 20< A < 100:
        a=0.40-(0.00382*(4.6-(np.log(A)))**2)
        b=0.0394*A**0.354
    elif 100<= A <500:
        a=0.40-(0.00382*(4.6-(np.log(A)))**2)
        b=0.0627*A**0.254
    elif 500<=A<1000:
        a=0.40-(0.0208*(np.log(np.log(A)-4.6)))
        b=0.0627*A**0.254
    elif 1000<=A:
        a=0.40-(0.0208*(np.log(np.log(A)-4.6)))
        b=0.1050*A**0.180
    else:
        print ("Area should be a positive number")

    return 1-b*D**(-a)

print(ARF(1))
print(ARF(100))

area=np.arange(1,1001,1)
ARF_mat=np.zeros_like(area,dtype=float)
count=0
for i in area:
    ARF_mat[count]=ARF(i)
    count=count+1
#print(ARF_mat)
plt.plot(area,ARF_mat)
plt.show()