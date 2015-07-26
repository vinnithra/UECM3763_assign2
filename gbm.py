import pylab as p

#Setup parameteres
mu = 0.1; sigma = 0.26; S0 = 39; t = 3;
n_path = 5; n = n_partitions = 1000;

#finding the theoritical values for the expectation and variance
Exp_S3=S0*p.exp(mu*t)
Var_S3=(S0**2)*p.exp(2*mu*t+(sigma**2)*t)*(p.exp((sigma**2)*t)-1)
print(Exp_S3)
print(Var_S3)

#Create Brownian paths
t = p.linspace(0,t,n+1);
dB = p.randn(n_path, n+1)/p.sqrt(n); dB[:,0]=0;
B = dB.cumsum(axis=1);

#Calculate Stock Price
nu = mu - sigma*sigma/2.0
S = p.zeros_like(B); S[:,0]=S0
S[:,1:]=S0*p.exp(nu*t[1:]+sigma*B[:,1:])
print(S)
p.title('Brownian Motion')
p.xlabel('t',fontsize=16)
p.ylabel('x',fontsize=16)
p.plot(t,S.transpose());p.show;

#to fing the expected value of s(3)
Z=S.transpose()
C=Z[-1]
total = 0

for i in range(5):
    total = total + C[i]

expected_S3=total/n_path

msg1 = 'Expexted Value of S(3) based on the simulation is %.30f' %expected_S3
print(msg1)

#to calculate the variance
C_square=C*C

total_square=0
for i in range(5):
    total_square=total_square+C_square[i]
    
Var_S3=(total_square-(expected_S3**2)/n_path)/(n_path-1)

msg2='Variance of S(3) based on the simulation is %.30f' %Var_S3
print(msg2)

#to calculate the probability
count = 0
Total=0

for i in range(5):
    if C[i]>39:
        count = count+1
        Total=Total+C[i]
        
#find probability of S3>39
Prob=count/n_path        
        
msg3 = 'The p(S(3)) > 39 is %f' %Prob
print(msg3)

#to find the conditional expectation
cond_exp=Total/count
msg4 ='The answer for the conditional expectation is %.13f' %cond_exp
print(msg4)





