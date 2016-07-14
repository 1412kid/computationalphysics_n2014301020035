from math import*
from visual import*
from matplotlib.pyplot import*

class  Billiard():
    ''' An elliptical billiard table'''
def __init__(self,dt):
    self.dt=dt

def collision(self,theta0,run_t):
    x=[];v_x=[];y=[]
    t=arange(0,2*pi,0.1)
    curve(x=20*cos(t),y=10*sin(t),z=0,color=color.red)
    ball=sphere(pos=(10*sqrt(3),0,0),radius=1,color=color.blue)
    ball.velocity=vector(1*cos(theta0),1*sin(theta0),0)
    ball.trail=curve(color=ball.color)
    for i in range(int(run_t/self.dt)):
        rate(100000)
        ball.pos.x=ball.pos.x+ball.velocity.x*self.dt
        ball.pos.y=ball.pos.y+ball.velocity.y*self.dt
        ball.trail.append(pos=ball.pos)
        if fabs(ball.pos.y-0)<=0.001:
            x.append(ball.pos.x);v_x.append(ball.velocity.x)
        if fabs(0.0025*ball.pos.x**2+0.01*ball.pos.y**2-1)<0.001:
            norm=sqrt((4*ball.pos.y)**2+ball.pos.x**2)
            vect_n=vector(ball.pos.x/norm,4*ball.pos.y/norm)
            proj=fabs(dot(ball.velocity,vect_n))
            addon=sqrt(ball.velocity.x**2+ball.velocity.y**2-proj**2)
            if ball.velocity.y/ball.velocity.x>=0:
                if ball.velocity.x>=0:
                    if ball.pos.x>=0 and ball.pos.y>=0:
                        if -ball.pos.x/(4*ball.pos.y)<=ball.velocity.y/ball.velocity.x<=4*ball.pos.y/ball.pos.x:
                            vect_f=-ball.velocity+vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                            ball.velocity=vect_f
                        else:
                            vect_f=-ball.velocity-vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                            ball.velocity=vect_f
                    elif ball.pos.x<0 and ball.pos.y>0:
                        vect_f=-ball.velocity+vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                        ball.velocity=vect_f
                    elif ball.pos.x>0 and ball.pos.y<0:
                        vect_f=-ball.velocity-vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                        ball.velocity=vect_f
                else:
                    if ball.pos.x<0 and ball.pos.y<0:
                        if -ball.pos.x/(4*ball.pos.y)<=ball.velocity.y/ball.velocity.x<=4*ball.pos.y/ball.pos.x:
                            vect_f=-ball.velocity+vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                            ball.velocity=vect_f
                        else:
                            vect_f=-ball.velocity-vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                            ball.velocity=vect_f
                    elif ball.pos.x<0 and ball.pos.y>0:
                        vect_f=-ball.velocity-vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                        ball.velocity=vect_f
                    elif ball.pos.x>0 and ball.pos.y<0:
                        vect_f=-ball.velocity+vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                        ball.velocity=vect_f             
            else:
                if ball.velocity.x>=0:
                    if ball.pos.x>0 and ball.pos.y<0:
                        if 4*ball.pos.y/ball.pos.x<=ball.velocity.y/ball.velocity.x<=-ball.pos.x/(4*ball.pos.y):
                            vect_f=-ball.velocity-vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                            ball.velocity=vect_f
                        else:
                            vect_f=-ball.velocity+vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                            ball.velocity=vect_f
                    elif ball.pos.x>0 and ball.pos.y>0:
                        vect_f=-ball.velocity+vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                        ball.velocity=vect_f
                    elif ball.pos.x<0 and ball.pos.y<0:
                        vect_f=-ball.velocity-vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                        ball.velocity=vect_f         
                elif ball.velocity.x<0:
                    if ball.pos.x<0 and ball.pos.y>0:
                            if 4*ball.pos.y/ball.pos.x<=ball.velocity.y/ball.velocity.x<=-ball.pos.x/(4*ball.pos.y):
                                vect_f=-ball.velocity-vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                                ball.velocity=vect_f
                            else:
                                vect_f=-ball.velocity+vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                                ball.velocity=vect_f
                    elif ball.pos.x>0 and ball.pos.y>0:
                        vect_f=-ball.velocity-vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                        ball.velocity=vect_f
                    elif ball.pos.x<0 and ball.pos.y<0:
                        vect_f=-ball.velocity+vector(2*4*ball.pos.y/norm*addon,-2*ball.pos.x/norm*addon)
                        ball.velocity=vect_f
    return (x,v_x)                        
def phase_space(run_t):
    ball=Billiard()
    dt=0.001
    xx=[];v_xx=[]
    __init__(ball,0.001)
    lis=collision(ball,1,run_t)
    xx=lis[0];v_xx=lis[1]
    title('Elliptical phase_space')
    xlabel('x');ylabel('v_x')
    scatter(xx,v_xx,color='black',s=1,label='initial pos:focal point')
    legend(loc='upper right',fontsize=11)
    show()        
phase_space(1000)
        
        
    
