#
import pandas as pd  
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt  
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_csv("data/BergDecompData.csv", sep = ",")

sns.scatterplot(df.MAT, df.Percloss)  
plt.title('Percloss in function MAT')  
plt.xlabel('MAT')  
plt.ylabel('Percloss')  
plt.show()

X = df['MAT'].values.reshape(-1,1)
y = df['Percloss'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

m1 = LinearRegression()  
m1.fit(X_train, y_train)
LinearRegression(copy_X=True, fit_intercept=True, normalize=False)

print(m1.intercept_)

print(m1.coef_)

y_pred = m1.predict(X_test)

df = pd.DataFrame({'Origin': y_test.flatten(), 'Pred': y_pred.flatten()})
print(df.head())

print('The value mean absolute error is: ', metrics.mean_absolute_error(y_test, y_pred))  
print('The value mean squared error is: ', metrics.mean_squared_error(y_test, y_pred))  
print('The value root mean squared srror is: ', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

r_squared = metrics.r2_score(y_test, y_pred)

print("The value R squared is: ", r_squared)

plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, color='black', linewidth=2)
plt.title('Percloss in function MAT')  
plt.xlabel('MAT')  
plt.ylabel('Percloss')  
plt.show()