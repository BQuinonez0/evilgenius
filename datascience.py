# -*- coding: utf-8 -*-
"""
Created on Sat May 27 15:14:50 2023

@author: Britney
"""


import pandas as pd
import matplotlib.pyplot as plt




file_path = "starcraft_player_data.csv"

df = pd.read_csv(file_path)

# Filter the data for 'LeagueIndex' equals 1
subset = df[df['LeagueIndex'] == 1]

# Calculate the mean age for each unique age within the subset
mean_age = subset.groupby('Age')['Age'].count()

# Plotting the mean age for category 'Age'
mean_age.plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Players for Age Category with LeagueIndex 1')
plt.show()


# Filter the data for 'LeagueIndex' equals 2
subset = df[df['LeagueIndex'] == 2]

# Calculate the mean age for each unique age within the subset
mean_age = subset.groupby('Age')['Age'].count()

# Plotting the mean age for category 'Age'
mean_age.plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Players for Age Category with LeagueIndex 2')
plt.show()


# Filter the data for 'LeagueIndex' equals 3
subset = df[df['LeagueIndex'] == 3]

# Calculate the mean age for each unique age within the subset
mean_age = subset.groupby('Age')['Age'].count()

# Plotting the mean age for category 'Age'
mean_age.plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Players for Age Category with LeagueIndex 3')
plt.show()


# Filter the data for 'LeagueIndex' equals 4
subset = df[df['LeagueIndex'] == 4]

# Calculate the mean age for each unique age within the subset
mean_age = subset.groupby('Age')['Age'].count()

# Plotting the mean age for category 'Age'
mean_age.plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Players for Age Category with LeagueIndex 4')
plt.show()



# Filter the data for 'LeagueIndex' equals 5
subset = df[df['LeagueIndex'] == 5]

# Calculate the mean age for each unique age within the subset
mean_age = subset.groupby('Age')['Age'].count()

# Plotting the mean age for category 'Age'
mean_age.plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Players for Age Category with LeagueIndex 5')
plt.show()


# Filter the data for 'LeagueIndex' equals 6
subset = df[df['LeagueIndex'] == 6]

# Calculate the mean age for each unique age within the subset
mean_age = subset.groupby('Age')['Age'].count()

# Plotting the mean age for category 'Age'
mean_age.plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Players for Age Category with LeagueIndex 6')
plt.show()


# Filter the data for 'LeagueIndex' equals 7
subset = df[df['LeagueIndex'] == 7]

# Calculate the mean age for each unique age within the subset
mean_age = subset.groupby('Age')['Age'].count()

# Plotting the mean age for category 'Age'
mean_age.plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Players for Age Category with LeagueIndex 7')
plt.show()


# Filter the data for 'LeagueIndex' equals 8
subset = df[df['LeagueIndex'] == 8]

# Calculate the mean age for each unique age within the subset
mean_age = subset.groupby('Age')['Age'].count()

# Plotting the mean age for category 'Age'
mean_age.plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Count of Players for Age Category with LeagueIndex 8')
plt.show()

