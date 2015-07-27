import pylab as p
import numpy as np

#Setup parameters
alpha = 1 ; sigma=0.27; tita=0.064;R0=3;
n_path=1000 ; n = n_partitions=1000;t=1.0;

dt=t/n; T=p.linspace(0,t,n+1)
dB=p.randn(n_path,n+1) * p.sqrt (dt); dB[:,0]=0;
B=dB.cumsum(axis=1);
R=p.zeros_like(B)


R[:,0]=R0
for col in range (n):
    R[:,col+1] = R[:,col]+alpha*(tita-R[:,col])*dt+R[:,col]*0.27*dB[:,col]

#pick 5 path randomly
R_random_row=np.random.randint(n_path,size=5)
R1=R[R_random_row,:]

p.xlabel('time, $t$', fontsize=16)
p.ylabel('R(t)',fontsize=16)
p.title('Mean Reversal Process' , fontsize=20)
p.plot(T,R1.transpose());p.show();

Z=R.transpose()
C=Z[-1,:]
total = 0
count=0

for i in range (n_path):    
    total=total +C[i]
    
expected_R1=total / n_path
msg1='The expected value of R(1) is %.13f' %expected_R1
print (msg1)

for i in range (n_path):
    if C[i]>2:
        count=count+1
        
prob=count/n_path
msg2='P(R(1)>2 is %.3f)' %prob
print (msg2)