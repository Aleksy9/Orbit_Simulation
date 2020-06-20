from Definitions import AU,m_earth,m_sun
import numpy as np
import matplotlib.pyplot as plt

G=6.67408*10**(-11)
dt=1
#Earth Initial Conditions
Px_earth=1*AU
Py_earth=0*AU
Vx_earth= 0
Vy_earth = 10000

#Sun Initial Conditions
Px_sun=0
Py_sun=0

x_array_earth=np.array([])
y_array_earth=np.array([])
x_array_sun=np.array([])
y_array_sun=np.array([])
t_array=np.array([])
t=0
for i in range(750000):
    t+=dt
    t_array=np.append(t_array,t)
    Dist_earth_sun=  np.sqrt(float(Px_earth-Px_sun)**2+float(Py_earth-Py_sun)**2)
    F0 = G*m_earth*m_sun/Dist_earth_sun**2

    #Earth body forces
        #Normalising distance vector
    dist_x_comp= Px_sun-Px_earth
    dist_y_comp= Py_sun-Py_earth
    norm_x = dist_x_comp/Dist_earth_sun
    norm_y = dist_y_comp/Dist_earth_sun

        #using normalised vector to get force components
    Fx_earth = norm_x*F0
    Fy_earth = norm_y*F0
    ax_earth= Fx_earth/m_earth
    ay_earth= Fy_earth/m_earth

    #Earth new velocity and positions
    x_array_earth=np.append(x_array_earth,Px_earth)
    y_array_earth=np.append(y_array_earth,Py_earth)
    Px_earth = ax_earth*dt**2/2 + Vx_earth*dt + Px_earth
    Py_earth = ay_earth*dt**2/2 + Vy_earth*dt + Py_earth
    Vx_earth = Vx_earth + ax_earth*dt
    Vy_earth = Vy_earth + ay_earth*dt

print('done')
'''
plt.plot(x_array_earth,y_array_earth)
plt.plot(0,0)
plt.show()'''