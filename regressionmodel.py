# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:18:45 2023
"""

import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt

file_path = "starcraft_player_data.csv"
df = pd.read_csv(file_path)

# Handle missing values
df = df.replace('?', float('nan'))  # Replace '?' with NaN
df = df.dropna()  # Remove rows with missing values

# Convert columns to numeric data types
df['Age'] = pd.to_numeric(df['Age'])
df['HoursPerWeek'] = pd.to_numeric(df['HoursPerWeek'])

# Independent variables
X = df[['Age', 'HoursPerWeek', 'TotalHours', 'APM', 'SelectByHotkeys', 'AssignToHotkeys',
        'UniqueHotkeys', 'MinimapAttacks', 'MinimapRightClicks', 'NumberOfPACs',
        'GapBetweenPACs', 'ActionLatency', 'ActionsInPAC', 'TotalMapExplored',
        'WorkersMade', 'UniqueUnitsMade', 'ComplexUnitsMade', 'ComplexAbilitiesUsed']]

# Dependent variable
y = df['LeagueIndex']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

plt.scatter(y_test, y_pred)
plt.xlabel('Actual LeagueIndex')
plt.ylabel('Predicted LeagueIndex')
plt.title('Linear Regression - Actual vs Predicted')
plt.show()

