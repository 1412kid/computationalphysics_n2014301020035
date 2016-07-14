# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:37:59 2016
@author: AF
"""
v = 700

import ode as solving_ode
import math
import matplotlib.pyplot as plt

def correct(string):           ##### delete all the data of (x,y) where y<0
    while True:
        if (string[1][2][-1] < 0):
            if (string[1][2][-1] < 0 and string[1][2][-2] > 0):
                x_record = string[1][0][-1] 
                y_record = string[1][2][-1]
            del string[1][0][-1]
            del string[1][2][-1]
        else:
            r = - string[1][2][-1]/y_record
            string[1][0].append((string[1][0][-1]+ r *x_record)/(r + 1))
            string[1][2].append(0)
            break
    return string
    

def scan1(theta,delta,ran):
    theta = theta - ran
    theta_record = []
    x = []
    theta_record.append(theta)
    for i in range(int(ran*2/delta)):
        vx_0 = v * math.cos(theta*math.pi/180)
        vy_0 = v * math.sin(theta*math.pi/180)
        A = solving_ode.ode(0.1,0,200,(0,vx_0,0,vy_0))
        A.set_fx(['v_x','-0.00004*v_x*math.sqrt(v_x**2+v_y**2)*math.e**(-y/10000)','v_y','-9.8-0.00004*math.sqrt(v_x**2+v_y**2)*v_y*math.e**(-y/10000)'],['t','x','v_x','y','v_y'])
        x.append(correct(A.euler()[:])[1][0][-1])
        theta = theta + delta
        theta_record.append(theta)
    for j in range(len(x)):
        if ( x[0] < x[j]):
            x[0] = x[j]
            theta_record[0] = theta_record[j]
    return theta_record[0]
    
def scan2(theta,delta,ran):
    theta = theta - ran
    theta_record = []
    x = []
    theta_record.append(theta)
    for i in range(int(ran*2/delta)):
        vx_0 = v * math.cos(theta*math.pi/180)
        vy_0 = v * math.sin(theta*math.pi/180)
        A = solving_ode.ode(0.1,0,200,(0,vx_0,0,vy_0))
        A.set_fx(['v_x','-0.00004*math.sqrt(v_x**2+v_y**2)*v_x*(1-(0.0065*y)/280)**2.5','v_y','-9.8-0.00004*math.sqrt(v_x**2+v_y**2)*v_y*(1-(0.0065*y)/280)**2.5'],['t','x','v_x','y','v_y'])
        x.append(correct(A.euler()[:])[1][0][-1])
        theta = theta + delta
        theta_record.append(theta)
    for j in range(len(x)):
        if ( x[0] < x[j]):
            x[0] = x[j]
            theta_record[0] = theta_record[j]
    return theta_record[0]

def scan3(theta,delta,ran):
    theta = theta - ran
    theta_record = []
    x = []
    theta_record.append(theta)
    for i in range(int(ran*2/delta)):
        vx_0 = v * math.cos(theta*math.pi/180)
        vy_0 = v * math.sin(theta*math.pi/180)
        A = solving_ode.ode(0.1,0,200,(0,vx_0,0,vy_0))
        A.set_fx(['v_x','-0.00004*math.sqrt(v_x**2+v_y**2)*v_x','v_y','-9.8-0.00004*math.sqrt(v_x**2+v_y**2)*v_y'],['t','x','v_x','y','v_y'])
        x.append(correct(A.euler()[:])[1][0][-1])
        theta = theta + delta
        theta_record.append(theta)
    for j in range(len(x)):
        if ( x[0] < x[j]):
            x[0] = x[j]
            theta_record[0] = theta_record[j]
    return theta_record[0]
         

##---------------- Isothermal ---------------------------------
#theta = 45
#theta = scan1(scan1(scan1(scan1(45,5,20),2,10),0.5,2),0.01,0.3)
theta = scan2(scan2(scan2(scan2(45,5,20),2,10),0.5,2),0.01,0.3)
plt.figure(figsize = (8,6))
#plt.subplot(131)
vx_0 = v * math.cos(theta*math.pi/180)
vy_0 = v * math.sin(theta*math.pi/180)
plt.title('Trajectory of cannon shell (Isothermal Correction)')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
A = solving_ode.ode(0.1,0,200,(0,vx_0,0,vy_0))
#A.set_fx(['v_x','-0.00004*v_x*math.sqrt(v_x**2+v_y**2)*math.e**(-y/10000)','v_y','-9.8-0.00004*math.sqrt(v_x**2+v_y**2)*v_y*math.e**(-y/10000)'],['t','x','v_x','y','v_y'])
A.set_fx(['v_x','-0.00004*math.sqrt(v_x**2+v_y**2)*v_x*(1-(0.0065*y)/280)**2.5','v_y','-9.8-0.00004*math.sqrt(v_x**2+v_y**2)*v_y*(1-(0.0065*y)/280)**2.5'],['t','x','v_x','y','v_y'])
cannon_record = correct(A.euler()[:])
x_max = cannon_record[1][0][-1]
print x_max
print theta
plt.plot(cannon_record[1][0],cannon_record[1][2],linewidth = 3, label=str(theta))
#for i in range(6):
#    vx_0 = v * math.cos(theta*math.pi/180)
#    vy_0 = v * math.sin(theta*math.pi/180)
#    A = solving_ode.ode(0.1,0,200,(0,vx_0,0,vy_0))
#    A.set_fx(['v_x','-0.00004*v_x*math.sqrt(v_x**2+v_y**2)*math.e**(-y/10000)','v_y','-9.8-0.00004*v_y*math.sqrt(v_x**2+v_y**2)*math.e**(-y/10000)'],['t','x','v_x','y','v_y'])
#    cannon_record = correct(A.rgkt_3()[:])
#    plt.plot(cannon_record[1][0],cannon_record[1][2],linewidth = 3, label=str(theta))
#    theta = theta +5
#plt.legend(fontsize = 13)
#plt.plot(25000,10000)
##---------------- Adiabatic -----------------------------------
'''theta = scan2(scan2(scan2(scan2(45,2,20),2,10),0.5,2),0.01,0.3)
theta = 30
#plt.subplot(132)
plt.title('Trajectory of cannon shell (Adiabatic Correction)')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
for j in range(6):
    vx_0 = v * math.cos(theta*math.pi/180)
    vy_0 = v * math.sin(theta*math.pi/180)
    A = solving_ode.ode(0.1,0,200,(0,vx_0,0,vy_0))
    A.set_fx(['v_x','-0.00004*v_x*math.sqrt(v_x**2+v_y**2)*(1-(0.0065*y)/280)**2.5','v_y','-9.8-0.00004*math.sqrt(v_x**2+v_y**2)*v_y*(1-(0.0065*y)/280)**2.5'],['t','x','v_x','y','v_y'])
    cannon_record = correct(A.euler()[:])
    plt.plot(cannon_record[1][0],cannon_record[1][2],linewidth = 3, label=str(theta))
    theta = theta +5
plt.legend(fontsize = 13)
plt.plot(25000,10000)'''
##---------------- no density correction ---------------------------------
#theta = scan3(scan3(scan3(scan3(45,5,20),2,10),0.5,2),0.01,0.3)
#theta = 30
#plt.subplot(133)
#plt.title('Trajectory of cannon shell (without density correction)')
#plt.xlabel('x(m)')
#plt.ylabel('y(m)')
#for k in range(6):
#    vx_0 = v * math.cos(theta*math.pi/180)
#    vy_0 = v * math.sin(theta*math.pi/180)
#    A = solving_ode.ode(0.1,0,200,(0,vx_0,0,vy_0))
#    A.set_fx(['v_x','-0.00004*700*v_x*math.sqrt(v_x**2+v_y**2)','v_y','-9.8-0.00004*700*v_y*math.sqrt(v_x**2+v_y**2)'],['t','x','v_x','y','v_y'])
#    cannon_record = correct(A.euler()[:])
#    plt.plot(cannon_record[1][0],cannon_record[1][2],linewidth = 3, label=str(theta))
#    theta = theta +5
#plt.legend(fontsize = 13)
#plt.plot(25000,10000)
##------------------ error analysis ---------------------------------------
'''plt.title('Trajectory of cannon shell (without density correction)')
plt.xlabel('x(m)')
plt.ylabel('y(m)')
theta = 38
vx_0 = v * math.cos(theta*math.pi/180)
vy_0 = v * math.sin(theta*math.pi/180)
A = solving_ode.ode(0.5,0,200,(0,vx_0,0,vy_0))
A.set_fx(['v_x','-0.00004*700*v_x','v_y','-9.8-0.00004*700*v_y'],['t','x','v_x','y','v_y'])
cannon_euler_5 = correct(A.euler()[:])
plt.plot(cannon_euler_5[1][0],cannon_euler_5[1][2],':',linewidth = 3, label='Simple Euler method with time step = 0.5s')
cannon_rgkt_5 = correct(A.rgkt_3()[:])
plt.plot(cannon_rgkt_5[1][0],cannon_rgkt_5[1][2], label='3rd Runge-Kutta method with time step = 0.5s')
B = solving_ode.ode(0.1,0,200,(0,vx_0,0,vy_0))
B.set_fx(['v_x','-0.00004*700*v_x','v_y','-9.8-0.00004*700*v_y'],['t','x','v_x','y','v_y'])
cannon_euler_1 = correct(B.euler()[:])
plt.plot(cannon_euler_1[1][0],cannon_euler_1[1][2], label='Simple Euler method with time step = 0.1s')
cannon_rgkt_1 = correct(B.rgkt_3()[:])
plt.plot(cannon_rgkt_1[1][0],cannon_rgkt_1[1][2], label='3rd Runge-Kutta method with time step = 0.1s')
C = solving_ode.ode(0.05,0,200,(0,vx_0,0,vy_0))
C.set_fx(['v_x','-0.00004*700*v_x','v_y','-9.8-0.00004*700*v_y'],['t','x','v_x','y','v_y'])
cannon_euler_05 = correct(C.euler()[:])
plt.plot(cannon_euler_05[1][0],cannon_euler_05[1][2],':',linewidth = 3, label='Simple Euler method with time step = 0.05s')
cannon_rgkt_05 = correct(C.euler()[:])
plt.plot(cannon_rgkt_05[1][0],cannon_rgkt_05[1][2],':',linewidth = 1, label='3rd Runge-Kutta method with time step = 0.05s')
plt.legend(loc='upper left')'''
plt.savefig('chapter2_2.9.png',dpi = 256)
plt.show()
        
     
