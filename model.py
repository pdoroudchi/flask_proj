# simple linear regression of salary against years of experience

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json

# import salary dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# split dataset into train and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# fit simple linear regression to train set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predict test set
y_pred = regressor.predict(X_test)

# save model with pickle
pickle.dump(regressor, open('model.pkl','wb'))

# load model to print prediction result for 5 years of experience
model = pickle.load( open('model.pkl','rb'))
print(model.predict([[5]]))
