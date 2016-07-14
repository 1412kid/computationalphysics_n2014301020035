import numpy as np
from visual import *
class baseball_state:
    def __init__(self, v, theta, w_x, w_y, w_z, y0, z0, x1, y1, z1):
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
        self.w_x = w_x*2*np.pi
        self.w_y = w_y*2*np.pi
        self.w_z = w_z*2*np.pi

        
    def calculate(self):
        self.vx = []
        self.vy = []
        self.vz = []
        self.vx.append( self.v * np.cos(self.theta*np.pi/180))
        self.vy.append( self.v * np.sin(self.theta*np.pi/180))
        self.vz.append(0)
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
            v = np.sqrt(self.vx[i - 1]**2+self.vy[i - 1]**2+self.vz[i - 1]**2)
            B = 0.0039 + 0.0058/(1 + np.e**((v - 35)/5))
            self.vx.append(self.vx[i - 1] - B*self.dt*v*self.vx[i - 1] + 0.00041*(self.w_y*self.vz[i - 1] - self.w_z*self.vy[i - 1])*self.dt)
            self.vy.append(self.vy[i - 1] - 9.8*self.dt - B*self.dt*v*self.vy[i - 1] + 0.00041*(self.w_z*self.vx[i - 1] - self.w_x*self.vz[i - 1])*self.dt)
            self.vz.append(self.vz[i - 1] - B*self.dt*v*self.vz[i - 1] + 0.00041*(self.w_x*self.vy[i - 1] - self.w_y*self.vx[i - 1])*self.dt)
            self.x.append(self.x[i - 1] + 0.5*(self.vx[i - 1] + self.vx[i])*self.dt)
            self.y.append(self.y[i - 1] + 0.5*(self.vy[i - 1] + self.vy[i])*self.dt)
            self.z.append(self.z[i - 1] + 0.5*(self.vz[i - 1] + self.vz[i])*self.dt)
            t.append(t[i - 1] + self.dt)
            i+= 1
        self.x[-1] = self.x[-2]+(self.y1 - self.y[-2])*(self.x[-2] - self.x[-1])/(self.y[-2] - self.y[-1])
        self.z[-1] = self.z[-2]+(self.y1 - self.y[-2])*(self.z[-2] - self.z[-1])/(self.y[-2] - self.y[-1])
        self.y[-1] = self.y1
        self.vx[-1] = 0.5*(self.vx[-1] + self.vx[-2])
        self.vy[-1] = 0.5*(self.vy[-1] + self.vy[-2])
        self.vz[-1] = 0.5*(self.vy[-1] + self.vz[-2])
        return 0
   
    def vplot(self):
        ball = sphere(pos=(0,self.y0,0), radius=2, color=color.white)
        t = 0
        deltat = 0.01
        i = 0
        ball.trail = curve(color = ball.color)
        while i < len(self.vx):
            rate(50)
            ball.velocity = vector(self.vx[i], self.vy[i], 10*self.vz[i])
            ball.pos = ball.pos + ball.velocity*deltat
            ball.trail.append(pos = ball.pos)
            t = t + deltat
            i+=1

           
### -----------------------------------------------------------------------------------------------------------
baseball = baseball_state(100,40,20,-20,300,1,0,0,0,0)
baseball.calculate()
arrow(pos = (0, 0, 0), axis = (100, 0, 0), shaftwidth = 1, color = color.blue)
label(text = 'Horizontal distance', pos = (100, 0, 0))
arrow(pos = (0, 0, 0), axis = (0, 100, 0), shaftwidth = 1, color = color.blue)
label(text = 'Vertical distance', pos = (0, 100, 0))
arrow(pos = (0, 0, 0), axis = (0, 0, 100), shaftwidth = 1, color = color.blue)
label(text = 'Z axis', pos = (0, 0, 100))
while 1:
    baseball.vplot()
