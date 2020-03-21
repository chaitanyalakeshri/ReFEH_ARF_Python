from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


D=5
def ARF(aa):
    A=aa
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




x=np.arange(-10,11,0.1)
y=x.copy()

Z=np.zeros((x.shape[0],y.shape[0]))
xcount=0
for i in x:
    ycount=0
    for j in y:
        if i==0 and j==0:
            Z[xcount,ycount]=1
        elif (np.sqrt((i**2)+(j**2)))<10:
            area= (np.pi)*((i**2)+(j**2))
            Z[xcount,ycount]=ARF(area)
            
        else:
            Z[xcount,ycount]=np.nan #ARF((np.pi)*10*10)
        ycount=ycount+1
    xcount=xcount+1

X,Y=np.meshgrid(x,y)






fig = plt.figure()
ax = fig.gca(projection='3d')

surf = ax.plot_surface(X, Y, Z,cmap='viridis',vmin=0.85, vmax=1)
ax.set_xlabel('Dist from origin(km)')
ax.set_ylabel('Dist from origin(km)')
ax.set_zlabel('ARF (Aerial Reduction Factor')
#plt.zlabel("ARF (Aerial Reduction Factor")
#ax.set_zlim(-1.01, 1.01)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
