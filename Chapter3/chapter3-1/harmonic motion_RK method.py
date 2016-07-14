from matplotlib.pyplot import*

g=-9.8;l=1;dt=0.04;

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
    plot(t,ang,'r-')
    
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
    plot(t,ang,'g-')

def h_motion_RKmethod3(index3,end_time3,ango3):
    ang=[];ang_v=[];t=[]
    ang.append(ango3);ang_v.append(0);t.append(0)
    for i in range(int(end_time3/dt)):
        angm=ang[-1]+1/2*dt*ang_v[-1]
        ang_vm=ang_v[-1]+1*g/l*dt*ang[-1]**index3
        ang_tmp=ang[-1]+ang_vm*dt
        ang.append(ang_tmp)
        ang_v_tmp=ang_v[-1]+g/l*dt*angm**index3
        ang_v.append(ang_v_tmp)
        t.append(dt*(i+1))
    plot(t,ang,'b-')

def display_AT(A1,A2,A3):
    h_motion_RKmethod1(3,20,A1)
    h_motion_RKmethod2(3,20,A2)
    h_motion_RKmethod3(3,20,A3)
    show()

display_AT(0.2,0.4,1.0)
