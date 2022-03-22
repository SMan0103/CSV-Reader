# importing libraries
#for versions checkout requirements.txt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing and reading data sets
data = pd.read_csv("data.csv")



#reading into variables
X = data.iloc[:, :-1].values
Y = data.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,Y, test_size = 20, random_state = 0)

#import linear regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

#fitting the model
lr.fit(X_train,y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

# Predicting the Test set results
y_pred = lr.predict(X_test)

#traininig set
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, lr.predict(X_train), color = 'blue')
plt.title('Life Expectancy vs BMI (Training set)')
plt.xlabel('Life Expectancy')
plt.ylabel('BMI')
plt.show()