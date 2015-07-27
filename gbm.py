import pylab as p
import numpy as np

#Setup parameters
mu = 0.1 ; sigma=0.26; S0=39;
n_path=1000 ; n = n_partitions=1000;period=3;

#Create Brownian paths
t=p.linspace(0,3,n+1);
dB=p.randn(n_path,n+1) / p.sqrt (n/period); dB[:,0]=0;
B=dB.cumsum(axis=1);

#Calculating stock prices
nu= mu - sigma*sigma/2.0
S=p.zeros_like(B);S[:,0]=S0
S[:,1:]=S0*p.exp(nu*t[1:]+sigma*B[:,1:])

#calculate the theoretical expectation and variance
TheoExp_S3=S0*p.exp(mu*3)
TheoVar_S3=(S0**2)*(p.exp(2*mu*3))*(p.exp(sigma*sigma*3)-1)

msg5='The theoretical expectation of S(3) is %.13f' %TheoExp_S3
msg6='The theoretical variance of S(3) is %.13f'%TheoVar_S3
print ( msg5 )
print ( msg6 )

#pick 5 path randomly
S_random_row=np.random.randint(n_path,size=5)
S1=S[S_random_row,:]

#plot the graph
p.xlabel('time, $t$',fontsize=16)
p.ylabel('Stock Price at time t, S(t)',fontsize=16)
p.title('Geometric Brownian Motion',fontsize=20)
p.plot(t,S1.transpose ());p.show();


Z=S.transpose()
#to get the last value of the vector
C=Z[-1,:]
total = 0

for i in range (n_path):    
    total=total +C[i]
    
#to find the expected value of S(3)
expected_S3=total / n_path

#print the msg
msg1='Expected Value of S(3) based on the simulation is %.13f' %expected_S3
print (msg1)

#to calculate the variance
C_square=C*C

total_square=0
for i in range (n_path):
    total_square=total_square + C_square[i]

Var_S3=(total_square-((total**2)/n_path))/(n_path-1)
msg2='Variance of S(3) based on the simulation is %.13f' %Var_S3
print (msg2)

count = 0
Total=0
for i in range (n_path):
    if C[i]>39:
        count=count+1
        Total=Total + C[i]

#find probability of S3>39
Prob=count/n_path
msg3='P(S(3)>39 is %.3f)'%Prob
print (msg3)

#to find the conditional expectation 
cond_exp=Total/count
msg4='E[S(3)|S(3)>39] is %.13f' %cond_exp
print (msg4)