from visual import*
from math import*
dt=0.05;GM=5000
p1=sphere(pos=(-100,0,0),radius=5,color=color.red)
p2=sphere(pos=(100,0,0),radius=5,color=color.green)
p3=sphere(pos=(0,0,100*sqrt(3)),radius=5,color=color.blue)
p1.velocity=vector(2.5,0,-2.5*sqrt(3));p2.velocity=vector(2.5,0,2.5*sqrt(3));p3.velocity=vector(-5,0,0)
p4=sphere(pos=(0,0,0),radius=3,color=color.white)

p1.trail=curve(color=p1.color)

R12=sqrt((p1.pos.x-p2.pos.x)**2+(p1.pos.y-p2.pos.y)**2+(p1.pos.z-p2.pos.z)**2)
R13=sqrt((p1.pos.x-p3.pos.x)**2+(p1.pos.y-p3.pos.y)**2+(p1.pos.z-p3.pos.z)**2)
R23=sqrt((p3.pos.x-p2.pos.x)**2+(p3.pos.y-p2.pos.y)**2+(p3.pos.z-p2.pos.z)**2)
Epi=-GM*R12**(-1)-GM*R13**(-1)-GM*R23**(-1)
Eki=0.5*(p1.velocity.x**2+p1.velocity.y**2+p1.velocity.z**2+p2.velocity.x**2+p2.velocity.y**2+p2.velocity.z**2+p3.velocity.x**2+p3.velocity.y**2++p3.velocity.z**2)
Ei=Epi+Eki
print R12,Ei

for i in range(30000):
    rate(1000)
    R12=sqrt((p1.pos.x-p2.pos.x)**2+(p1.pos.y-p2.pos.y)**2+(p1.pos.z-p2.pos.z)**2)
    R13=sqrt((p1.pos.x-p3.pos.x)**2+(p1.pos.y-p3.pos.y)**2+(p1.pos.z-p3.pos.z)**2)
    R23=sqrt((p3.pos.x-p2.pos.x)**2+(p3.pos.y-p2.pos.y)**2+(p3.pos.z-p2.pos.z)**2)
    
    
    p1posxm=p1.pos.x+1/2*dt*p1.velocity.x
    p1velocityxm=p1.velocity.x+dt*(p2.pos.x-p1.pos.x)*GM*R12**(-3)+dt*(p3.pos.x-p1.pos.x)*GM*R13**(-3)
    p1posym=p1.pos.y+1/2*dt*p1.velocity.y
    p1velocityym=p1.velocity.y+dt*(p2.pos.y-p1.pos.y)*GM*R12**(-3)+dt*(p3.pos.y-p1.pos.y)*GM*R13**(-3)
    p1poszm=p1.pos.z+1/2*dt*p1.velocity.z
    p1velocityzm=p1.velocity.z+dt*(p2.pos.z-p1.pos.z)*GM*R12**(-3)+dt*(p3.pos.z-p1.pos.z)*GM*R13**(-3)

    p2posxm=p2.pos.x+1/2*dt*p2.velocity.x
    p2velocityxm=p2.velocity.x+dt*(p1.pos.x-p2.pos.x)*GM*R12**(-3)+dt*(p3.pos.x-p2.pos.x)*GM*R23**(-3)
    p2posym=p2.pos.y+1/2*dt*p2.velocity.y
    p2velocityym=p2.velocity.y+dt*(p1.pos.y-p2.pos.y)*GM*R12**(-3)+dt*(p3.pos.y-p2.pos.y)*GM*R23**(-3)
    p2poszm=p2.pos.z+1/2*dt*p2.velocity.z
    p2velocityzm=p2.velocity.z+dt*(p1.pos.z-p2.pos.z)*GM*R12**(-3)+dt*(p3.pos.z-p2.pos.z)*GM*R23**(-3)

    p3posxm=p3.pos.x+1/2*dt*p3.velocity.x
    p3velocityxm=p3.velocity.x+dt*(p1.pos.x-p3.pos.x)*GM*R13**(-3)+dt*(p2.pos.x-p3.pos.x)*GM*R23**(-3)
    p3posym=p3.pos.y+1/2*dt*p3.velocity.y
    p3velocityym=p3.velocity.y+dt*(p1.pos.y-p3.pos.y)*GM*R13**(-3)+dt*(p2.pos.y-p3.pos.y)*GM*R23**(-3)
    p3poszm=p3.pos.z+1/2*dt*p3.velocity.z
    p3velocityzm=p3.velocity.z+dt*(p1.pos.z-p3.pos.z)*GM*R13**(-3)+dt*(p2.pos.z-p3.pos.z)*GM*R23**(-3)
    
    p1.pos.x=p1.pos.x+p1velocityxm*dt
    p1.pos.y=p1.pos.y+p1velocityym*dt
    p1.pos.z=p1.pos.z+p1velocityzm*dt
    p1.velocity.x=p1.velocity.x+dt*(p2posxm-p1posxm)*GM*R12**(-3)+dt*(p3posxm-p1posxm)*GM*R13**(-3)
    p1.velocity.y=p1.velocity.y+dt*(p2posym-p1posym)*GM*R12**(-3)+dt*(p3posym-p1posym)*GM*R13**(-3)
    p1.velocity.z=p1.velocity.z+dt*(p2poszm-p1poszm)*GM*R12**(-3)+dt*(p3poszm-p1poszm)*GM*R13**(-3)

    p2.pos.x=p2.pos.x+p2velocityxm*dt
    p2.pos.y=p2.pos.y+p2velocityym*dt
    p2.pos.z=p2.pos.z+p2velocityzm*dt
    p2.velocity.x=p2.velocity.x+dt*(p1posxm-p2posxm)*GM*R12**(-3)+dt*(p3posxm-p2posxm)*GM*R23**(-3)
    p2.velocity.y=p2.velocity.y+dt*(p1posym-p2posym)*GM*R12**(-3)+dt*(p3posym-p2posym)*GM*R23**(-3)
    p2.velocity.z=p2.velocity.z+dt*(p1poszm-p2poszm)*GM*R12**(-3)+dt*(p3poszm-p2poszm)*GM*R23**(-3)

    p3.pos.x=p3.pos.x+p3velocityxm*dt
    p3.pos.y=p3.pos.y+p3velocityym*dt
    p3.pos.z=p3.pos.z+p3velocityzm*dt
    p3.velocity.x=p3.velocity.x+dt*(p1posxm-p3posxm)*GM*R13**(-3)+dt*(p2posxm-p3posxm)*GM*R23**(-3)
    p3.velocity.y=p3.velocity.y+dt*(p1posym-p3posym)*GM*R13**(-3)+dt*(p2posym-p3posym)*GM*R23**(-3)
    p3.velocity.z=p3.velocity.z+dt*(p1poszm-p3poszm)*GM*R13**(-3)+dt*(p2poszm-p3poszm)*GM*R23**(-3)

    p1.trail.append(pos=p1.pos)
    
R12=sqrt((p1.pos.x-p2.pos.x)**2+(p1.pos.y-p2.pos.y)**2+(p1.pos.z-p2.pos.z)**2)
R13=sqrt((p1.pos.x-p3.pos.x)**2+(p1.pos.y-p3.pos.y)**2+(p1.pos.z-p3.pos.z)**2)
R23=sqrt((p3.pos.x-p2.pos.x)**2+(p3.pos.y-p2.pos.y)**2+(p3.pos.z-p2.pos.z)**2)
Epf=-GM*R12**(-1)-GM*R13**(-1)-GM*R23**(-1)
Ekf=0.5*(p1.velocity.x**2+p1.velocity.y**2+p1.velocity.z**2+p2.velocity.x**2+p2.velocity.y**2+p2.velocity.z**2+p3.velocity.x**2+p3.velocity.y**2++p3.velocity.z**2)
Ef=Epf+Ekf
print R12,Ef
   
    
