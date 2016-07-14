# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:10:06 2016
@author: AF
"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

class baseball_normal:
    def __init__(self, v, theta, w, y0, z0, x1, y1, z1):
        ###------- position of the picher -----------
        self.y0 = y0  
        self.z0 = z0
        ###------- position of the home plate -------
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        ###------------------------------------------
        self.dt = 0.01
        self.v = v*0.44704
        self.theta = theta
        self.w = w*2*np.pi

        
    def calculate(self):
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = np.sqrt(vx[i - 1]**2+vy[i - 1]**2+vz[i - 1]**2)
            B = 0.0039 + 0.0058/(1 + np.e**((v - 35)/5))
            vx.append(vx[i - 1] - B*self.dt*v*vx[i - 1] - 0.00041*vy[i - 1] * self.w*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*vy[i - 1] + 0.00041*vx[i - 1] * self.w*self.dt)
            vz.append(vz[i - 1])
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z  
        
    def plot2D(self):
        data = (raw_input("please input the two variables you want to plot from (x,y,z):").split(' '))
        notation = {'x': self.x, 'y':self.y,'z':self.z}
        plt.figure()
        plt.xlabel(data[0]+' (m)')
        plt.ylabel(data[1]+' (m)')
        plt.plot(notation[data[0]],notation[data[1]])
        plt.show()
        return 0    
    
    def plot3D(self):
        fig = plt.figure
        ax = fig.gca(projection='3d')
        ax.set_xlabel('x (m)', fontsize = 12)
        ax.set_ylabel('z (m)', fontsize = 12)
        ax.set_zlabel('y (m)', fontsize = 12)
        ax.plot(self.x,self.z,self.y)
        plt.show()
        return 0
    
    def store(self):           #### save the calculculate datas            
        data_file = open('data_2_19.txt','w')
        for i in range(len(self.x)):
                data_file.write(str(self.x))
                data_file.write(' ')
                data_file.write(str(self.y))
                data_file.write(' ')
                data_file.write(str(self.z))
                data_file.write('\n')
        print "all the datum have been written in file: data_2_19.txt"
            
    
class baseball_fullspin(baseball_normal):
    def calculate(self, w_x, w_y, w_z):
        w_x = w_x * 2 * np.pi
        w_y = w_y * 2 * np.pi
        w_z = w_z * 2 * np.pi
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = np.sqrt(vx[i - 1]**2+vy[i - 1]**2+vz[i - 1]**2)
            B = 0.0039 + 0.0058/(1 + np.e**((v - 35)/5))
            vx.append(vx[i - 1] - B*self.dt*v*vx[i - 1] + 0.00041*(w_y*vz[i - 1] - w_z*vy[i - 1])*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*vy[i - 1] +0.00041*(w_z*vx[i - 1] - w_x*vz[i - 1])*self.dt)
            vz.append(vz[i - 1] - B*self.dt*v*vz[i - 1] + 0.00041*(w_x*vy[i - 1] - w_y*vx[i - 1])*self.dt)
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z

class baseball_rough(baseball_normal):
    def calculate(self):
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = np.sqrt(vx[i - 1]**2+vy[i - 1]**2+vz[i - 1]**2)
            B = (0.0013 + 0.0084/(1 + np.e**((v - 21)/2.5)))*(-(3 - np.e**(0.5*(v - 39)))/(1 + np.e**(0.5*(v - 39))) + 4)
            vx.append(vx[i - 1] - B*self.dt*v*vx[i - 1] - 0.00041*vy[i - 1] * self.w*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*vy[i - 1] + 0.00041*vx[i - 1] * self.w*self.dt)
            vz.append(vz[i - 1])
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z
        
class baseball_smooth(baseball_normal):
    def calculate(self):
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = np.sqrt(vx[i - 1]**2+vy[i - 1]**2+vz[i - 1]**2)
            B = 0.0013 + 0.0084/(1 + np.e**((v - 65)/4))
            vx.append(vx[i - 1] - B*self.dt*v*vx[i - 1] - 0.00041*vy[i - 1] * self.w*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*vy[i - 1] + 0.00041*vx[i - 1] * self.w*self.dt)
            vz.append(vz[i - 1])
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z
        
class baseball_wind(baseball_normal):
    
    def module(self,vx,vy,vx_w,vy_w):
        delta_vx = vx - vx_w
        delta_vy = vy - vy_w
        return np.sqrt(delta_vx**2 + delta_vy**2)
    
    def calculate(self,vx_w, vy_w):
        vx = []
        vy = []
        vz = []
        vx.append( self.v * np.cos(self.theta*np.pi/180))
        vy.append( self.v * np.sin(self.theta*np.pi/180))
        vz.append(0)
        t = []
        self.x = []       ### forward and backward
        self.y = []       ### up and down
        self.z = []       ### left and right
        t.append(0)
        self.x.append(0)
        self.y.append(self.y0)
        self.z.append(0)
        i = 1
        while ( self.y[-1] >= self.y1 ):
            v = self.module(vx[i - 1], vy[i - 1], vx_w, vy_w)
            B = 0.0039 + 0.0058/(1 + np.e**((v - 35)/5))
            vx.append(vx[i - 1] - B*self.dt*v*(vx[i - 1] - vx_w) - 0.00041*vy[i - 1] * self.w*self.dt)
            vy.append(vy[i - 1] - 9.8*self.dt - B*self.dt*v*(vy[i - 1] - vy_w) + 0.00041*vx[i - 1] * self.w*self.dt)
            vz.append(vz[i - 1])
            self.x.append(self.x[i - 1] + 0.5*(vx[i - 1] + vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(vy[i - 1] + vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(vz[i - 1] + vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        return self.x, self.y, self.z
        

fig = plt.figure(figsize = (8,6))
plt.title('Trajectory of cannon shell')
plt.xlabel('Horizontal distance (m)', fontsize = 12)
plt.ylabel('Vertical height (m)', fontsize = 12)
## ---------------- full spin ---------------------
A = baseball_fullspin(100,40,33,1,0,0,0,0)
record_fullspin = A.calculate(0,0,33)
ax = fig.gca(projection='3d')
ax.set_xlabel('Horizontal distance (m)', fontsize = 12)
ax.set_ylabel('z axis (m)', fontsize = 12)
ax.set_zlabel('Vertical height (m)', fontsize = 12)
ax.plot(record_fullspin[0],record_fullspin[2],record_fullspin[1], label = 'Omege vector (0,0,33)')
record_fullspin = A.calculate(0,10,31)
ax.plot(record_fullspin[0],record_fullspin[2],record_fullspin[1], label = 'Omege vector (0,10,31)')
record_fullspin = A.calculate(20,20,17)
ax.plot(record_fullspin[0],record_fullspin[2],record_fullspin[1], label = 'Omege vector (20,20,17)')
record_fullspin = A.calculate(0,30,0)
ax.plot(record_fullspin[0],record_fullspin[2],record_fullspin[1], label = 'Omege vector (0,30,0)')
record_fullspin = A.calculate(30,0,0)
ax.plot(record_fullspin[0],record_fullspin[2],record_fullspin[1], label = 'Omege vector (30,0,0)')
ax.legend()
## ---------------- normal -------------------------  
'''A = baseball_normal(100, 40, 33, 1, 0, 0, 0, 0)
record_normal = A.calculate()
print record_normal[0][-1]
plt.plot(record_normal[0], record_normal[1], label = 'normal ball')
## --------------- rough ---------------------------
B = baseball_rough(100, 40, 33, 1, 0, 0, 0, 0)
record_rough = B.calculate()
print record_rough[0][-1]
plt.plot(record_rough[0], record_rough[1], label = 'rough ball')
## -----------------smooth --------------------------
C = baseball_smooth(100, 40, 33, 1, 0, 0, 0, 0)
record_smooth = C.calculate()
print record_smooth[0][-1]
plt.plot(record_smooth[0], record_smooth[1], label = 'smooth ball')'''
## ---------------- different angle -----------------
'''data_w = [10,20,30,35,40,45,50,60]
for degree in range(8):
    A = baseball_normal(100,data_w[degree],33,1,0,0,0,0)
    record_normal = A.calculate()
    plt.plot(record_normal[0], record_normal[1], label = 'angle ='+str(data_w[degree])+'degree')
    degree-=1'''
## ---------------- different angular velocity ----------------------
'''data_w = [-30,0,33,60,200,300]
for degree in range(6):
    A = baseball_normal(100,40,data_w[degree],1,0,0,0,0)
    record_normal = A.calculate()
    plt.plot(record_normal[0], record_normal[1], label = 'angular velocity ='+str(data_w[degree])+'rps')
    degree-=1
'''
## --------- find the furthest distance-----------------
'''distance = []
w_record = []
for i in range(30,60):
    A = baseball_normal(100,i,33,1,0,0,0,0)
    record_normal = A.calculate()
    distance.append(record_normal[0][-1])
    w_record.append(i)
for j in range(len(distance)):
    if (distance[0] < distance[j]):
        distance[0] = distance[j]
        w_record[0] = w_record[j]
    else:
        pass
print distance[0]
print w_record[0]'''
## -------------- wind --------------------------------
### -------------- backspin ---------------------------
'''plt.subplot(121)
plt.title('Trajectory of cannon shell (Backspin)')
plt.xlabel('Horizontal distance (m)', fontsize = 12)
plt.ylabel('Vertical height (m)', fontsize = 12)
A = baseball_wind(100,40,33,1,0,0,0,0)
record_wind = A.calculate(4.47,0)
plt.plot(record_wind[0], record_wind[1], label = 'Backspin: tailwind')
record_wind = A.calculate(0,0)
plt.plot(record_wind[0], record_wind[1], label = 'Backspin: no wind')
record_wind = A.calculate(-4.47,0)
plt.plot(record_wind[0], record_wind[1], label = 'Backspin: headwind')
plt.legend(loc = 'upper left', fontsize = 9)
### ------------- np spin -----------------------------
plt.subplot(122)
plt.title('Trajectory of cannon shell (No spin)')
plt.xlabel('Horizontal distance (m)', fontsize = 12)
plt.ylabel('Vertical height (m)', fontsize = 12)
plt.ylim(0,40)
plt.xlim(0,140)
A = baseball_wind(100,40,0,1,0,0,0,0)
record_wind = A.calculate(4.47,0)
plt.plot(record_wind[0], record_wind[1],'-.',linewidth = 3, label = 'No spin: tailwind')
record_wind = A.calculate(0,0)
plt.plot(record_wind[0], record_wind[1],'-.',linewidth = 3, label = 'No spin: no wind')
record_wind = A.calculate(-4.47,0)
plt.plot(record_wind[0], record_wind[1],'-.',linewidth = 3, label = 'No spin: headwind')'''
##-------------------------------------------------------
'''plt.legend(loc = 'upper right', fontsize = 9)
plt.savefig('chapter2.19_ball.png', dpi = 144)'''
## -------------- argprase ------------------------------
'''parser = argparse.ArgumentParser()
parser.add_argument("velocity", type = float, help= "display a square of a given number")
parser.add_argument("theta", type = float, help= "the initial batting angle")
parser.add_argument("omega", type = float, help = "the angular velocity of spin")
parser.add_argument("height", type = float, help = "the height of batting point")
group1 = parser.add_mutually_exclusive_group()
group1.add_argument("-r", "--radian", action="store_true", default = 0, help = "unit of theta")
group1.add_argument("-d", "--degree", action="store_true", default = 1, help = "unit of theta")
group2 = parser.add_mutually_exclusive_group()
group2.add_argument("-mph", "--mile_per_hour", action="store_true", default = 0, help="unit of velocity")
group2.add_argument("-mps", "--meter_per_second", action="store_true", default = 1,help = "unit of velocity")
group3 = parser.add_mutually_exclusive_group()
group3.add_argument("-rps", "--revolution_per_second", action="store_true", default = 1,help= "unit of angular velocity")
group3.add_argument("-rpm", "--revolution_per_minute", action="store_true", default = 0, help = "unit of angular velocity")
parser.add_argument("-s", "--store", action = "store_true", default = 1, help = "store the datum you have calculated in a file")
parser.add_argument("-p", "--plot", choices=['2d','3d'], default = '3d', help = "plot the datum you have calculated")
args = parser.parse_args()
## -----------------------------------------
if args.radian:
    args.theta = args.theta*180/np.pi
elif args.degree:
    pass
if args.mile_per_hour:
    pass
elif args.meter_per_second:
    args.velocity = args.velocity/0.44704
if args.revolution_per_second:
    pass
elif args.revolution_per_minute:
    args.omega = args.omega/60
## =========================================
A = baseball_normal(args.velocity, args.theta, args.omega, args.height,0,0,0,0)
record = A.calculate()
##  -------- plot --------------------------
if args.plot == '2d':
    A.plot2D()
else:
    A.plot3D()
## ---------- store ------------------------
if args.store:
    A.store()
else:
    pass'''

