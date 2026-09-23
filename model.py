# import numpy as np
#import pandas as pd
#from sklearn.model_selection import train_test_split
# from sklearn import svm
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import StandardScaler
#
# # load the diabetes data
#
# ls
#
# # group the data by outcome to get a sense of the distribution
#
# diabetes = pd.read_csv('diabetes.csv')
# diabetes.head()
# diabetes.shape
# diabetes.info()
# diabetes['Outcome'].value_counts()
#
# # split the data into input and target variables
#
# X = diabetes.drop('Outcome', axis=1)
# Y = diabetes['Outcome']
# X.shape
# Y.shape
# diabetes.describe()
#
# # scale the input variables using standardscaler
#
# scaler = StandardScaler()
# scaler.fit(X)
# standard_data = scaler.fit_transform(X)
# X = standard_data
# X
#
# # split the data into training and testing sets
#
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, stratify=Y, random_state=1)
# X_train.shape
# X_test.shape
#
# # create an SVM model with a linear kernel
#
# svc = svm.SVC(kernel='linear')
#
# # train the model on the training set
#
# svc.fit(X_train, Y_train)
#
# # make prediction on the training and testing sets
#
# train_y_pred = svc.predict(X_train)
# test_y_pred = svc.predict(X_test)
#
# # calculate the accuracy of the model on the training and testing sets
#
# train_accuracy = accuracy_score(train_y_pred, Y_train)
# test_accuracy = accuracy_score(test_y_pred, Y_test)
# print(train_accuracy)
# print(test_accuracy)
# input_data =(1,189,60,23,846,30.1,0.398,59)
# np_array_data = np.asarray(input_data)
# reshaped_data = np_array_data.reshape(1,-1)
# std_data = scaler.transform(reshaped_data)
# prediction = svc.predict(std_data)
# print(prediction)
#
# if prediction == 1:
#   print('The person is diabetic')
# else:
#   print('The person is not diabetic')
# diabetes.head(4)

import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#load the dataset
data = pd.read_csv('diabetes.csv')

# split the data into features adn labels
X= data.iloc[:, :-1] # features
y = data.iloc[:, -1] # labels

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create the model
model = RandomForestClassifier()

# train the model
model.fit(X_train, y_train)

# make predictions on test data
# prediction = model.predict(X_test, y_test)

pickle.dump(model, open('model.pkl', 'wb'))











