import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split

data=pd.read_csv('original.csv')
data1=data.head(50)
#data2=(data[['Collection','Genre','Budget','Num_multiplex']])
#plt.plot('Genre','Budget',ls='--',data=data1)
#plt.show()
#print(data2.info())
#train_data,test_data=data.
##bins=(27000,45000,60000)
#group_names=['good','bad']
#data1['Collection']=pd.cut(data1['Collection'],bins=bins,labels=group_names)
#data1['Collection'].unique()
#print(data1['Collection'])
#label=LabelEncoder()
#data1['Collection']=label.fit_transform(data1['Collection'])
x=data1.drop('Collection',axis=1)                                                   #separating dataset as responces and future variables
y=data1['Collection']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=10)       #SPLITTING DATA
#applying scalling
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
print(x_train)



"""
iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,test_size = 0.3, random_state = 1
)
print(iris.values())
print(X_train.shape)
print(X_test.shape)

print(y_train)
print(y_train.shape)
print(y_test.shape)"""



