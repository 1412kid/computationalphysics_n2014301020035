from math import*
from matplotlib.pyplot import*
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from visual import*
from numpy import*
class Lorenz():
    '''Lorenz Model'''

def __init__(self,x0,y0,z0,sigma,r,b,dt):
    self.x=[x0]
    self.y=[y0]
    self.z=[z0]
    self.sigma=sigma
    self.r=r
    self.b=b
    self.t=[0.0]
    self.dt=dt
    

def flow(self,run_time):
    for i in range(int(run_time/self.dt)):
        x_med=self.x[-1]+self.sigma*(self.y[-1]-self.x[-1])*self.dt
        y_med=self.y[-1]+(-self.x[-1]*self.z[-1]+self.r*self.x[-1]-self.y[-1])*self.dt
        z_med=self.z[-1]+(self.x[-1]*self.y[-1]-self.b*self.z[-1])*self.dt
        self.x.append(x_med)
        self.y.append(y_med)
        self.z.append(z_med)

def plot_L_3D(self):
    fig=figure()
    ax=Axes3D(fig)
    x=self.x
    y=self.y
    z=self.z
    ax.plot(x,y,z)
    xlabel('x');ylabel('y');
    title('3D display of Lorenz Model')
    show()

def plot_zx(self):
    plot(self.x,self.z,'k-')
    title('Phase space plot   z v.s. x')
    xlabel('x')
    ylabel('z')
    show()

def plot_zy(self):
    plot(self.y,self.z,'k-')
    title('Phase space plot   z v.s. y')
    xlabel('y')
    ylabel('z')
    show()

def plot_phase_zx(self,run_t):
    z_store=[]
    x_store=[]
    for i in range(1,int(run_t/self.dt)):
        if fabs(self.y[i]-0)<=0.001:
            x_store.append(float(self.x[i]))
            z_store.append(float(self.z[i]))        
    scatter(x_store,z_store,color='k',s=1,label='Phase space plot   z v.s. x when y=0')
    xlabel('x')
    ylabel('z')
    legend()
    show()

def plot_phase_zy(self,run_t):
    z_store=[]
    y_store=[]
    for i in range(1,int(run_t/self.dt)):
        if fabs(self.x[i]-0)<=0.001:
            y_store.append(float(self.y[i]))
            z_store.append(float(self.z[i]))        
    scatter(y_store,z_store,color='k',s=1,label='Phase space plot   z v.s. y when x=0')
    xlabel('y')
    ylabel('z')
    legend(fontsize=11)
    show()

def period(self,run_t):
    z_med=[]
    t_med=[]
    dt=0.0001
    for i in range(int(run_t/dt)):
        z_med.append(self.z[i])
        t_med.append(i*dt)
    return (z_med,t_med)

def birds_finding(self,run_t):
    dt=0.0001
    for i in range(50000,int(run_t/dt)):
        if self.z[i]>230:
            print i
    
def hope(run_t):
    butterfly=Lorenz()
    __init__(butterfly,x0=1,y0=0,z0=0,sigma=10,r=163.6467,b=8./3,dt=0.0001)
    flow(butterfly,run_t)
    birds_finding(butterfly,run_t)
    period(butterfly,run_t)
    show()

def Lorenz_ball(self,run_t):
    ball=sphere(pos=(1,0,0),radius=5,color=color.red)
    ball.trail=curve(color=ball.color)
    for i in range(int(run_t/self.dt)):
        rate(1000)
        ball.pos.x=self.x[i]
        ball.pos.y=self.y[i]
        ball.pos.z=self.z[i]
        ball.trail.append(pos=ball.pos)
        
def subplots(run_t):
    butterfly=Lorenz()
    __init__(butterfly,x0=1,y0=0,z0=0,sigma=10,r=163.647,b=8./3,dt=0.0001)
    flow(butterfly,run_t)
    z_medi=[]
    t_medi=[]
    lis=period(butterfly,run_t)
    z_medi.extend(lis[0])
    t_medi.extend(lis[1])
    butt=Lorenz()
    __init__(butt,x0=1,y0=0,z0=0,sigma=10,r=163.646,b=8./3,dt=0.0001)
    flow(butt,run_t)
    z_media=[]
    t_media=[]
    liss=period(butt,run_t)
    z_media.extend(liss[0])
    t_media.extend(liss[1])
    p1=subplot(211)
    p1.plot(t_medi,z_medi,'k-',label='r=163.647')
    p1.set_title('Lorenz model z v.s. time')
    p1.set_ylabel('z')
    p1.set_xlabel('time')
    p1.legend()
    p2=subplot(212)
    p2.plot(t_media,z_media,'k-',label='r=163.646')
    p2.set_xlabel('time')
    p2.set_ylabel('z')
    p2.legend()
    show()
    
butterfly=Lorenz()
__init__(butterfly,x0=1,y0=0,z0=0,sigma=10,r=25,b=8./3,dt=0.0001)
flow(butterfly,1000)
plot_phase_zy(butterfly,1000)
    



















