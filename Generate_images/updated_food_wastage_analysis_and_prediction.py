#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the dataset
file_path = "Food_Wastage_sample.csv"  # Please adjust the file path as necessary
data = pd.read_csv(file_path)

# In[22]:

user_input_dining_area = input("Please enter the name of the dining area: ")

# Filter data based on user input
filtered_data = data[data['Location'] == user_input_dining_area]
filtered_data.head()


# Group by Week and Food, then sum the Amt_Consumed
weekly_food_sales = filtered_data.groupby(['Week', 'Food'])['Amt_Consumed'].sum().reset_index()

# Find the food with maximum Amt_Consumed for each week
highest_selling_food_per_week = weekly_food_sales.loc[weekly_food_sales.groupby('Week')['Amt_Consumed'].idxmax()]

# Visualize the highest selling food item and its quantity for each week
plt.figure(figsize=(12, 6))
plt.bar(highest_selling_food_per_week['Week'], highest_selling_food_per_week['Amt_Consumed'],
        color='skyblue', label='Amount Consumed')
plt.title('Highest Selling Food Item per Week in ' + user_input_dining_area)
plt.xlabel('Week')
plt.ylabel('Amount Consumed')
plt.xticks(highest_selling_food_per_week['Week'])
plt.legend()

# Annotate the bars with the corresponding food names
for idx, row in highest_selling_food_per_week.iterrows():
    plt.text(row['Week'], row['Amt_Consumed'], row['Food'], ha='center', va='bottom')

plt.show()

# Group by Week and sum the Wastage
weekly_wastage = filtered_data.groupby('Week')['Wastage'].sum().reset_index()

# Visualize the wastage of food for each week
plt.figure(figsize=(12, 6))
plt.plot(weekly_wastage['Week'], weekly_wastage['Wastage'], marker='o', linestyle='-', color='coral')
plt.title('Weekly Food Wastage in ' + user_input_dining_area)
plt.xlabel('Week')
plt.ylabel('Total Wastage')
plt.xticks(weekly_wastage['Week'])
plt.grid(True)
plt.show()

# Find the maximum week number in the dataset
max_week = filtered_data['Week'].max()

# Initialize a dictionary to store predicted values for each food
predicted_values = {}

# Iterate over each food item in the dataset
for food in filtered_data['Food'].unique():
    # Filter data for the specific food
    food_data = filtered_data[filtered_data['Food'] == food]
    
    # Group by Week and sum the Amt_Consumed
    weekly_food_consumed = food_data.groupby('Week')['Amt_Consumed'].sum().reset_index()
    
    # Prepare data for Linear Regression
    X = weekly_food_consumed['Week'].values.reshape(-1, 1)
    y = weekly_food_consumed['Amt_Consumed'].values
    
    # Train Linear Regression model
    model = LinearRegression().fit(X, y)
    
    # Predict the amount consumed for the next week (max_week + 1)
    predicted_amt = model.predict(np.array([[max_week + 1]]))[0]
    
    # Store the predicted value in the dictionary
    predicted_values[food] = predicted_amt

# Find the food item with the highest predicted value
predicted_highest_selling_item = max(predicted_values, key=predicted_values.get)
predicted_highest_selling_item, predicted_values[predicted_highest_selling_item]


# Add predicted value to the highest_selling_food_per_week dataframe
predicted_row = pd.Series({'Week': max_week + 1, 'Food': predicted_highest_selling_item, 'Amt_Consumed': predicted_values[predicted_highest_selling_item]})
highest_selling_food_per_week = highest_selling_food_per_week.append(predicted_row, ignore_index=True)

# Visualize the updated highest selling food item and its quantity for each week
plt.figure(figsize=(14, 7))
plt.bar(highest_selling_food_per_week['Week'], highest_selling_food_per_week['Amt_Consumed'],
        color=['skyblue' if week <= max_week else 'green' for week in highest_selling_food_per_week['Week']], label='Amount Consumed')
plt.title('Highest Selling Food Item per Week in ' + user_input_dining_area + ' (with Prediction)')
plt.xlabel('Week')
plt.ylabel('Amount Consumed')
plt.xticks(highest_selling_food_per_week['Week'])
plt.legend()

# Annotate the bars with the corresponding food names
for idx, row in highest_selling_food_per_week.iterrows():
    plt.text(row['Week'], row['Amt_Consumed'], row['Food'], ha='center', va='bottom')
    

# Save the plot as a PNG file
plt.savefig('C:\\Users\\sreer\\OneDrive\\Desktop\\Generate_images\\highest_selling_food_per_week.png', format='png', dpi=300)
plt.show()

# Train Linear Regression model for weekly wastage prediction
X_wastage = weekly_wastage['Week'].values.reshape(-1, 1)
y_wastage = weekly_wastage['Wastage'].values
wastage_model = LinearRegression().fit(X_wastage, y_wastage)

# Predict the wastage for the next week (max_week + 1)
predicted_wastage = wastage_model.predict(np.array([[max_week + 1]]))[0]

# Add predicted value to the weekly_wastage dataframe
predicted_wastage_row = pd.Series({'Week': max_week + 1, 'Wastage': predicted_wastage})
weekly_wastage = weekly_wastage.append(predicted_wastage_row, ignore_index=True)

# Visualize the updated weekly wastage with prediction for the upcoming week
plt.figure(figsize=(14, 7))
plt.plot(weekly_wastage['Week'], weekly_wastage['Wastage'], marker='o', linestyle='-', color='coral')
plt.scatter(max_week + 1, predicted_wastage, color='red', zorder=5)  # Highlight the predicted point
plt.title('Weekly Food Wastage in ' + user_input_dining_area + ' (with Prediction)')
plt.xlabel('Week')
plt.ylabel('Total Wastage')
plt.xticks(weekly_wastage['Week'])
plt.grid(True)

# Add a vertical line to separate actual data and prediction
plt.axvline(x=max_week + 0.5, color='k', linestyle='--', label='Prediction Boundary')

plt.legend()
plt.savefig('C:\\Users\\sreer\\OneDrive\\Desktop\\Generate_images\\food_wastage_per_week.png', format='png', dpi=300)
plt.show()
