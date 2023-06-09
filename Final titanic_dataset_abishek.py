# -*- coding: utf-8 -*-
"""TiTanic DataSet Abishek.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kCyxBxkNROv9bfa_okbtrpQwm4NJD38E

# **About Titanic Dataset**
The Titanic dataset is a famous dataset that contains information about passengers aboard the Titanic ship, which sank in 1912 after colliding with an iceberg. The dataset is often used in data science and machine learning education and competitions as a starting point for exploring data analysis and predictive modeling techniques.

The Titanic dataset contains information about **1309** passengers, including their age, gender, ticket class, cabin, port of embarkation, and whether they survived or not. The goal of many analyses and models built on the Titanic dataset is to predict whether a given passenger would have survived the disaster.

The variables in the Titanic dataset are as follows:
**PassengerId: Unique identifier for each passenger
Survived: Whether the passenger survived (0 = No, 1 = Yes)
Pclass: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
Name: Passenger name
Sex: Passenger gender
Age: Passenger age
SibSp: Number of siblings/spouses aboard the Titanic
Parch: Number of parents/children aboard the Titanic
Ticket: Ticket number
Fare: Passenger fare
Cabin: Cabin number
Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)**
As mentioned earlier, the main objective of many analyses and models built on the Titanic dataset is to predict whether a given passenger would have survived the disaster, based on their demographic and travel information. This is a **binary classification problem**, where the target variable is **Survived** and the predictors are the other variables in the dataset.
"""



from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

"""# Importing Libraries"""

import pandas as pd
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

"""# Data Loading"""

data=pd.read_csv('/content/titanic.csv')
data.head(5)

"""# Data shuffling"""

data = data.sample(frac=1, random_state=42)

data.tail(5)

"""# Data Dimention:- No. of Rows and Columns"""

data.shape

print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])

data.info()

"""# Get Overall Statistics About The Dataframe"""

data.describe(include='all')

"""# Data Preprocessing & Data Cleaning

## Data Filtering
"""

data.columns

data[['Name','Age']]

sum(data['Sex']=='male')

data[data['Sex']=='male'].head()

sum(data['Survived']==1)

"""## Check Missing (Null) Values In The *Dataset*"""

data.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(data.isnull())

per_missing = data.isnull().sum() * 100 / len(data)

"""## Drop the Column"""

data.drop('Cabin', axis=1,inplace=True)

data.isnull().sum()

"""## Handle Missing Values"""

data['Embarked'].mode()

data['Embarked'].fillna('S',inplace=True)

data.isnull().sum()

data['Age']

data['Age'].fillna(data['Age'].mean(), inplace = True)

data.isnull().sum()



data.isnull().sum()

data['Fare'].fillna(data['Fare'].mean(), inplace = True)

data.head()

data['Sex'].unique()

data['Gender']=data['Sex'].map({'male':1, 'female':0})

data.head(5)

"""# Data Encoding"""

x=data['Sex'].map({'male':1, 'female':0})

data['Embarked'].unique()

pd.get_dummies(data,columns=['Embarked'])

data1=pd.get_dummies(data,columns=['Embarked'],drop_first=True)

data1.head(1)

"""# Visual Analysis

## How Many People Survived And How Many Died?
"""

data['Survived'].value_counts()

import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='Survived',data=data)

"""## How Many Passengers Were In First Class, Second Class, and Third Class?"""

data['Pclass'].value_counts()

sns.countplot(x='Pclass', data=data)

"""## Number of Male And Female Passengers"""

data['Sex'].value_counts()

sns.countplot(x ='Sex', data = data)

plt.hist(data['Age'])

"""#**12. Bivariate Analysis**

## How Has Better Chance of Survival Male or Female?
"""

sns.barplot(x='Sex',y='Survived',data=data)

"""## Which Passenger Class Has Better Chance of Surviva(First, Second, Or Third Class)?"""

sns.barplot(x="Pclass", y="Survived",data=data)

# Convert categorical variables to numeric
data = pd.get_dummies(data, columns=['Sex', 'Embarked'])
data.head(5)

data=data.drop(['PassengerId', 'Name', 'Ticket'], axis=1)

"""## Dataset Splitting into test and train"""

# Split the data into training and testing sets
X = data.drop('Survived', axis=1)
y = data['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""## Data Scaling"""

# Scale the numeric features
scaler = StandardScaler()
X_train[['Age', 'Fare']] = scaler.fit_transform(X_train[['Age', 'Fare']])
X_test[['Age', 'Fare']] = scaler.transform(X_test[['Age', 'Fare']])



"""# Model 1: Logistic regression using ANN"""

# Define the model
model = Sequential()
model.add(Dense(1, input_shape=(X_train.shape[1],), activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Model Fitting with 100 epochs and 32 batch_size
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

# Evaluate the model on the test data
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print('Logistics regressionn Accuracy: %.2f' % (accuracy*100))

"""# Model 2: 64-32-16-8-1 using ANN


"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define a more complex model with more layers and neurons
model1 = Sequential()
model1.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model1.add(Dense(32, activation='relu'))
model1.add(Dense(16, activation='relu'))
model1.add(Dense(8, activation='relu'))
model1.add(Dense(1, activation='sigmoid'))

# Compile the model
model1.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model for a large number of epochs
history = model1.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), verbose=0)

import matplotlib.pyplot as plt

# Plot the training and validation loss and accuracy
train_loss = history.history['loss']
val_loss = history.history['val_loss']
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.plot(train_loss, label='train')
plt.plot(val_loss, label='val')
plt.legend()
plt.title('Loss')

plt.subplot(1, 2, 2)
plt.plot(train_acc, label='train')
plt.plot(val_acc, label='val')
plt.legend()
plt.title('Accuracy')
plt.show()



# Evaluate the model on the test data
loss, accuracy = model1.evaluate(X_test, y_test, verbose=0)
print('Model 2 Accuracy: %.2f' % (accuracy*100))

"""# *Model 3: (32-16-8-1) ANN*"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define a more complex model with more layers and neurons
model_3 = Sequential()
model_3.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))
model_3.add(Dense(16, activation='relu'))
model_3.add(Dense(8, activation='relu'))
model_3.add(Dense(1, activation='sigmoid'))

# Compile the model
model_3.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model for a large number of epochs
history = model_3.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), verbose=0)

import matplotlib.pyplot as plt

# Plot the training and validation loss and accuracy
train_loss = history.history['loss']
val_loss = history.history['val_loss']
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.plot(train_loss, label='train')
plt.plot(val_loss, label='val')
plt.legend()
plt.title('Loss')

plt.subplot(1, 2, 2)
plt.plot(train_acc, label='train')
plt.plot(val_acc, label='val')
plt.legend()
plt.title('Accuracy')
plt.show()

# Evaluate the model on the test data
loss, accuracy = model_3.evaluate(X_test, y_test, verbose=0)
print('Model 3 Accuracy: %.2f' % (accuracy*100))

"""# Model 4:(16-8-1) ANN

"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define a more complex model with more layers and neurons
model_4 = Sequential()
model_4.add(Dense(16, input_dim=X_train.shape[1], activation='relu'))
model_4.add(Dense(8, activation='relu'))
model_4.add(Dense(1, activation='sigmoid'))

# Compile the model
model_4.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model for a large number of epochs
history = model_4.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), verbose=0)

import matplotlib.pyplot as plt

# Plot the training and validation loss and accuracy
train_loss = history.history['loss']
val_loss = history.history['val_loss']
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.plot(train_loss, label='train')
plt.plot(val_loss, label='val')
plt.legend()
plt.title('Loss')

plt.subplot(1, 2, 2)
plt.plot(train_acc, label='train')
plt.plot(val_acc, label='val')
plt.legend()
plt.title('Accuracy')
plt.show()

# Evaluate the model on the test data
loss, accuracy = model_4.evaluate(X_test, y_test, verbose=0)
print('Model 4 Accuracy: %.2f' % (accuracy*100))

"""# **Model 5: 8-1 ANN**"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define a more complex model with more layers and neurons
model_5 = Sequential()
model_5.add(Dense(8, input_dim=X_train.shape[1], activation='relu'))
model_5.add(Dense(1, activation='sigmoid'))

# Compile the model
model_5.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model for a large number of epochs
history = model_5.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), verbose=0)

import matplotlib.pyplot as plt

# Plot the training and validation loss and accuracy
train_loss = history.history['loss']
val_loss = history.history['val_loss']
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.plot(train_loss, label='train')
plt.plot(val_loss, label='val')
plt.legend()
plt.title('Loss')

plt.subplot(1, 2, 2)
plt.plot(train_acc, label='train')
plt.plot(val_acc, label='val')
plt.legend()
plt.title('Accuracy')
plt.show()

# Evaluate the model on the test data
loss, accuracy = model_5.evaluate(X_test, y_test, verbose=0)
print('Model 5 Accuracy: %.2f' % (accuracy*100))

"""# Model 6: (4-1) ANN"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define a more complex model with more layers and neurons
model_6 = Sequential()
model_6.add(Dense(4, input_dim=X_train.shape[1], activation='relu'))
model_6.add(Dense(1, activation='sigmoid'))

# Compile the model
model_6.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model for a large number of epochs
history = model_6.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), verbose=1)

import matplotlib.pyplot as plt

# Plot the training and validation loss and accuracy
train_loss = history.history['loss']
val_loss = history.history['val_loss']
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.plot(train_loss, label='train')
plt.plot(val_loss, label='val')
plt.legend()
plt.title('Loss')

plt.subplot(1, 2, 2)
plt.plot(train_acc, label='train')
plt.plot(val_acc, label='val')
plt.legend()
plt.title('Accuracy')
plt.show()

# Evaluate the model on the test data
loss, accuracy = model_6.evaluate(X_test, y_test, verbose=0)
print('Model 6 Accuracy: %.2f' % (accuracy*100))

"""# Model 7:2-1 ANN"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define a more complex model with more layers and neurons
model_7 = Sequential()
model_7.add(Dense(2, input_dim=X_train.shape[1], activation='relu'))
model_7.add(Dense(1, activation='sigmoid'))

# Compile the model
model_7.compile(optimizer='SGD', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model for a large number of epochs
history = model_7.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), verbose=1)

import matplotlib.pyplot as plt

# Plot the training and validation loss and accuracy
train_loss = history.history['loss']
val_loss = history.history['val_loss']
train_acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.plot(train_loss, label='train')
plt.plot(val_loss, label='val')
plt.legend()
plt.title('Loss')

plt.subplot(1, 2, 2)
plt.plot(train_acc, label='train')
plt.plot(val_acc, label='val')
plt.legend()
plt.title('Accuracy')
plt.show()

# Evaluate the model on the test data
loss, accuracy = model_7.evaluate(X_test, y_test, verbose=0)
print('Model 7 Accuracy: %.2f' % (accuracy*100))

"""# Model 8: Logistic regression using SKLEARN"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd


# Create a logistic regression model
model_8 = LogisticRegression()

# Fit the model to the training data
model_8.fit(X_train, y_train)

# Predict the target variable for the test data
y_pred = model_8.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print('Logistic Regression Accuracy:%.2f'% (accuracy*100))

"""# Model 9: Random Forest"""

from sklearn.ensemble import RandomForestClassifier
# Create a random forest classifier
model_9 = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
# Fit the model to the training data
model_9.fit(X_train, y_train)

# Predict the target variable for the test data
y_pred = model_9.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print('Random forest Accuracy:%.2f'% (accuracy*100))

