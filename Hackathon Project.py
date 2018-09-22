#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 19:07:10 2018

@author: chrisvo
"""

# written by using Spyder, python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('raw_data_update3.csv')
# not all the independent variables are relevant for prediction ()
X = dataset.iloc[:, 5:10].values
y = dataset.iloc[:, 10].values

#we have categorical data so we need to encode it
# Encoding categorical data
# in this dataset, there are 2 categorical variables
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# first categorical vairable
# 0 corresonds to female , 1 to male
labelencoder_X_1 = LabelEncoder()
X[:, 0] = labelencoder_X_1.fit_transform(X[:, 0])

#University of Delaware is 1 and Penn State is 0
labelencoder_X_2 = LabelEncoder()
X[:, 1] = labelencoder_X_2.fit_transform(X[:, 1])

# multiple variables
#onehotencoder = OneHotEncoder(categorical_features = [1])
#X = onehotencoder.fit_transform(X).toarray()
#remove one dummy variable column to not fall into dummy variable trap
#X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
# can use model selection instead of cross validation
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
#necessary because there will be many many calculations
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Phase 2 - Now let's make the ANN

# importing the Keras libraries and packages
import keras
# intialize our Neural network
from keras.models import Sequential
# creating the layers in our ANN
from keras.layers import Dense

#Initializing the ANN
#defining as a sequence of layers
# we will define the layers step by step later , so nothing in parethesis
classifier = Sequential()

#randomly initialize the weights close to 0
#the number of input nodes = number of independent variables, in this case 11
#Neuron activated by activation function
#the higher the activation function in the neuron the greater the impact in the ANN
# choose activation function - the best one is the rectifier function for the hidden layers
#sigmoid function is good for output layer -probablity that the customer leaves the bank can be determined
#we will decide how many epoch at the end

#Adding the input layer and the first hidden layer
# there is not really an optimal number of nodes in the hidden layer - can experiment with the number of hidden layers and the number of nodes in each layer
# tip: choose the number of nodes in the hidden layer by finding the average of the input and output layers
# in our case it will be 3, randomly intialize the weights according to a uniform distribution
#implement rectifier activation function
# the number of independent variables/nodes is necessary to mention - 5 hidden layer should expect 5 input nodes
classifier.add(Dense(activation="relu", units=3, kernel_initializer="uniform", input_dim = 5))

# add a second hidden layer (if needed)
# only change input_dim layer, don't need to specify
#still keep the units value the same if we don't want to make things complicated
classifier.add(Dense(activation="relu", units=3, kernel_initializer="uniform"))

#Adding the output layer
# just change some of the parameters
# 1 output node, need to use the sigmoid activation function - to have probablities for the outcomes
#if there are 3 categories for our output, input 3 and then use softmax for dependent variable that has more than 2 variables
classifier.add(Dense(activation="sigmoid", units=1, kernel_initializer="uniform"))

# Compiling the ANN -appying the Stochastic gradient descent algorithm
# find optimal set of weights using optimizer to make nn powerful
# loss function in the adam algorithm - need to optimize to find the optimal weights
#loss function is sum of (y-yhat) squared - this is the C
#perceptron - 1 neuron as the hidden layer between inputs and output
#logarthmic loss function dependent variable has 2 options (binary)
#metrics arguement used to evaluate model - accuracy used to improve the model until reaching the best accuracy
#metrics list will contain only one element
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
# add two additional elements
# specify the batch size before updating the weights
#epoch - round of when the whole training set passed through ANN 
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)


# Phase 3 - Making the predictions and evaluating the model

# Predicting the Test set results
#gives the probabilities for each customer in the test set
y_pred = classifier.predict(X_test)
# convert probablities to true/false
#predict 1 over the threshold, predict 0 under the threshold
# 1 corresponds to going to not being a donor in the future, 0 means they will be predicted to be a continued donor
#0.5 is the threshold
#if y_pred is greater than 0.5, true is returned
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix - by looking at this, we can determine the number of correct predictions within the test set
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

"""Predict if the customer with the folowing information will leave the bank:
Gender: Female (0)
Credit Score: Univeristy of Delaware (1)
Age: 35
Num_Donation: 3
Donation_Amt: 175
Is_Donor? If false returned then they will stay a donor, if true is returned, they will not be a donor in the future
"""

# example prediction and extracting this information
new_prediction = classifier.predict(sc.transform(np.array([[0, 1, 35, 3, 175]])))
new_prediction = (new_prediction > 0.5)

# True corresponds to prediction being correct
# 1 corresonds to True, in fact, the user will not be a donar going forward



