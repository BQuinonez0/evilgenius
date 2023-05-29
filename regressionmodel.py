# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:18:45 2023
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_selection import RFECV
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt

file_path = "starcraft_player_data.csv"
df = pd.read_csv(file_path)

# Handle missing values
df = df.replace('?', float('nan'))  # Replace '?' with NaN
df = df.dropna()  # Remove rows with missing values

# Independent variables
X = df[['Age', 'HoursPerWeek', 'TotalHours', 'APM', 'SelectByHotkeys', 'AssignToHotkeys',
        'UniqueHotkeys', 'MinimapAttacks', 'MinimapRightClicks', 'NumberOfPACs',
        'GapBetweenPACs', 'ActionLatency', 'ActionsInPAC', 'TotalMapExplored',
        'WorkersMade', 'UniqueUnitsMade', 'ComplexUnitsMade', 'ComplexAbilitiesUsed']]

# Dependent variable
y = df['LeagueIndex']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create a linear regression model
model = LinearRegression()

# Perform recursive feature elimination with cross-validation
rfecv = RFECV(estimator=model)
rfecv.fit(X_train_scaled, y_train)

# Get the optimal number of features
optimal_num_features = rfecv.n_features_

# Select the top features
X_train_selected = rfecv.transform(X_train_scaled)
X_test_selected = rfecv.transform(X_test_scaled)

# Fit the final model using the selected features
model.fit(X_train_selected, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test_selected)

# Calculate mean squared error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Print the optimal number of features
print("Optimal Number of Features:", optimal_num_features)

# Print the MLR equation with selected features
selected_feature_indices = rfecv.support_
selected_features = X.columns[selected_feature_indices]
coefficients = model.coef_
intercept = model.intercept_

equation = f"LeagueIndex = {intercept:.2f} + "
for feature, coefficient in zip(selected_features, coefficients):
    equation += f"({coefficient:.2f} * {feature}) + "

equation = equation.rstrip(" + ")
print("MLR Equation:", equation)

# Plot the predicted values vs. the actual values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual LeagueIndex')
plt.ylabel('Predicted LeagueIndex')
plt.title('Linear Regression - Actual vs. Predicted')
plt.show()
