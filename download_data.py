#download 1 component stock data 

from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import numpy as np
import pylab as p

# dt(year,month,date)
start = dt(2010, 1, 1)
end = dt(2015, 5, 1)

# download Genting and FTSE KLCI daily data
data = DR("3182.KL", 'yahoo', start, end)
KLSE=DR("^KLSE", 'yahoo', start, end)

# making data frame into matrix
data_close=data['Close'].values

Sum=0
#finding the number of row
X=data_close.shape[0]

# making a zero array
Average = np.zeros((X+1-5,))

for i in range (X+1-5):
    for j in range (5):
        Sum=Sum + data_close[j+i];
    Average[i]=Sum/5
    Sum=0
    
Time=p.linspace(0,X+1-5,X+1-5)

p.xlabel('time, $t$',fontsize=16)
p.ylabel('Average Stock Price, S(t)',fontsize=16)
p.title('Moving Average Plot of Genting',fontsize=20)
p.plot (Time,Average);p.show()    

# calculating correlation
Alldata=['3182.KL','^KLSE']
closing=  DR(Alldata, 'yahoo', start, end)['Close']
correlate=closing.corr()

correlation=correlate['^KLSE'].values
msg='The correlation between Genting and FTSE KLCI is %.7f' %correlation [0]

print (correlate)
print (msg)