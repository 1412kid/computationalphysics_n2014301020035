from matplotlib.pyplot import*

g=-9.8;l=1;dt=0.04


#function(that shows different algorithms solving harmonic motion)starts
def h_motion_Emethod(end_time):
    ang1=[];ang1.append(0.05)
    ang1_v=[];t1=[]
    ang1_v.append(0);t1.append(0);
    for i in range(int(end_time/dt)):
        ang1_v_tmp=ang1_v[-1]+g/l*ang1[-1]*dt
        ang1_v.append(ang1_v_tmp)
        ang1_tmp=ang1[-1]+ang1_v[-2]*dt
        ang1.append(ang1_tmp)
        t1.append(dt*(i+1))
    line1=plot(t1,ang1,'g--',label='Euler Method')
    
def h_motion_ECmethod(end_time):
    ang2=[];ang2.append(0.05)
    ang2_v=[];t2=[]
    ang2_v.append(0);t2.append(0);
    for i in range(int(end_time/dt)):
        ang2_v_tmp=ang2_v[-1]+g/l*ang2[-1]*dt
        ang2_v.append(ang2_v_tmp)
        ang2_tmp=ang2[-1]+ang2_v[-1]*dt
        ang2.append(ang2_tmp)
        t2.append(dt*(i+1))
    line2=plot(t2,ang2,'r--',label='Euler-Cromer Method')
    

def h_motion_RKmethod(end_time):
    ang=[];ang_v=[];t=[]
    ang.append(0.05);ang_v.append(0);t.append(0)
    for i in range(int(end_time/dt)):
        angm=ang[-1]+1/2*dt*ang_v[-1]
        ang_vm=ang_v[-1]+g/l*dt*ang[-1]
        ang_tmp=ang[-1]+ang_vm*dt
        ang.append(ang_tmp)
        ang_v_tmp=ang_v[-1]+g/l*dt*angm
        ang_v.append(ang_v_tmp)
        t.append(dt*(i+1))
    line3=plot(t,ang,'b-.',label='Runge-Kutta Method')

    
def display_hmotion(et1,et2,et3):
    h_motion_Emethod(et1)
    h_motion_ECmethod(et2)
    h_motion_RKmethod(et3)
    legend(loc='upper left')
    xlabel("t/(s)");ylabel('angle/(rad)')
    title('The Comparision of  Three Algorithms')
    show()
#function(that shows different algorithms solving harmonic motion)ends


#function(that shows the periods of the oscillation with different amplitudes)starts
def h_motion_RKmethod1(index1,end_time1,ango1):
    ang=[];ang_v=[];t=[]
    ang.append(ango1);ang_v.append(0);t.append(0)
    for i in range(int(end_time1/dt)):
        angm=ang[-1]+1/2*dt*ang_v[-1]
        ang_vm=ang_v[-1]+g/l*dt*ang[-1]**index1
        ang_tmp=ang[-1]+ang_vm*dt
        ang.append(ang_tmp)
        ang_v_tmp=ang_v[-1]+g/l*dt*angm**index1
        ang_v.append(ang_v_tmp)
        t.append(dt*(i+1))
    line1=plot(t,ang,'r-',label='Amplitude=0.2')
    
def h_motion_RKmethod2(index2,end_time2,ango2):
    ang=[];ang_v=[];t=[]
    ang.append(ango2);ang_v.append(0);t.append(0)
    for i in range(int(end_time2/dt)):
        angm=ang[-1]+1/2*dt*ang_v[-1]
        ang_vm=ang_v[-1]+g/l*dt*ang[-1]**index2
        ang_tmp=ang[-1]+ang_vm*dt
        ang.append(ang_tmp)
        ang_v_tmp=ang_v[-1]+g/l*dt*angm**index2
        ang_v.append(ang_v_tmp)
        t.append(dt*(i+1))
    line2=plot(t,ang,'g-',label='Amplitude=0.4')

def h_motion_RKmethod3(index3,end_time3,ango3):
    ang=[];ang_v=[];t=[]
    ang.append(ango3);ang_v.append(0);t.append(0)
    for i in range(int(end_time3/dt)):
        angm=ang[-1]+1/2*dt*ang_v[-1]
        ang_vm=ang_v[-1]+g/l*dt*ang[-1]**index3
        ang_tmp=ang[-1]+ang_vm*dt
        ang.append(ang_tmp)
        ang_v_tmp=ang_v[-1]+g/l*dt*angm**index3
        ang_v.append(ang_v_tmp)
        t.append(dt*(i+1))
    line3=plot(t,ang,'b-',label='Amplitude=1.0')

def display_AT(A1,A2,A3):
    h_motion_RKmethod1(3,20,A1)
    h_motion_RKmethod2(3,20,A2)
    h_motion_RKmethod3(3,20,A3)
    legend(loc='upper right',fontsize=9.0)
    xlabel("t/(s)");ylabel('angle/(rad)')
    title('The Dependence of Period on Amplitudes')
    show()
#function(that shows the periods of the oscillation with different amplitudes)ends
    
display_hmotion(10,10,10)

display_AT(0.2,0.4,1.0) 
   
    
