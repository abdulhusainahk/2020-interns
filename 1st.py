import matplotlib.pyplot as plt
import pandas as pd
arr1,arr2=[],[]
dataset=pd.read_json('data.json')
df=sorted(dataset['rates'].items())
d=input("Enter the number of the month to plot eg[01,03,05,11,12])")
Curr1=input("Enter the currency on the x-axis")
Curr2=input("Enter the currency on the y-axis")
for item in df:
    x=str(item[0])
    if x[:8] == f'2019-{d}-':
        arr1.append(item[1][Curr1])
        arr2.append((item[1][Curr2]))
ti=Curr1+" vs "+Curr2
plt.title(ti)
plt.xlabel(Curr1)
plt.ylabel(Curr2)
plt.plot(arr2,arr1,c='red')
plt.scatter(arr2,arr1,c='blue')
plt.show()