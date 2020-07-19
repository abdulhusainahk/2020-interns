import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
arr1,arr2,arr3,arr4=[],[],[],[]
dataset=pd.read_json('data.json')
df=sorted(dataset['rates'].items())
d=input("Enter the number of the month to plot eg[01,03,05,11,12])")
Curr1,Curr2=input("Enter the two currencies on the x-axis seperated by '-' eg[INR-USD]").strip().split('-')
Curr3=input("Enter the currency on the y-axis")
for item in df:
    x=str(item[0])
    if x[:8] == f'2019-{d}-':
        arr1.append(item[1][Curr1])
        arr2.append(item[1][Curr2])
        arr3.append(item[1][Curr3])
        arr4.append(x[8:10])
arr5=np.add(np.array(arr1),np.array(arr2))/2
arr3=np.array(arr3)
xlabel=Curr1+"-"+Curr2
ti="("+Curr1+"-"+Curr2+") vs "+Curr3
plt.title(ti)
plt.xlabel(xlabel)
plt.ylabel(Curr3)
plt.plot(arr5,arr3,c='red')
for i,j,k in zip(arr5,arr3,arr4):
    plt.scatter(i,j,c='blue')
    plt.annotate(k,xy=(i,j),xytext=(5, 2),textcoords='offset points',ha='right',va='bottom')
plt.show()
