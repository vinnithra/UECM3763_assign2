import pylab as p

n_path = 5; n = n_partitions = 1000; t = 1.0;
alpha = 1; tita = 0.064; X0 = 3.0;

#To create the brownian motion
dt=t/n; T = p.linspace(0,t,n+1)
dB = p.randn(n_path, n+1)*p.sqrt(dt); dB[:,0]=0;
B = dB.cumsum(axis=1);
X = p.zeros_like(B)

X[:,0] = X0

#the solution of the mean reversal
for col in range (n):
    X[:,col+1] = X[:,col] + alpha*(tita-X[:,col])*dt + [0.27 * X[:,col]]*dB[:,col+1]

R = X.transpose()

p.title('Mean Reversal Model')
p.xlabel('Time,$t$',fontsize=16)
p.ylabel('R(t)',fontsize=16)
p.plot(T,R)
p.show()

#expected value of R(1)
R1 = R[-1,:]
E = R1.sum() / n_path
msg = 'The expected value of R(1) is %.13f' %E
print(msg)

# P[R(1)>2]
count = 0

for i in range (5):
    if R1[i] > 2:
        count = count + 1
        
count2 = count / n_path
msg = 'The probability that R(1) is more than 2 is %.13f' %count2
print(msg)