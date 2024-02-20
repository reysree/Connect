import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

def generate_graphs(dining_area):
    data = pd.read_csv('Food_Wastage_sample.csv')
    data = data[data['Location'] == dining_area]
    # Example: Weekly Highest Selling Item Analysis
    weekly_data = data.groupby(['Week', 'Food'])['Amt_Consumed'].sum().reset_index()
    highest_selling_food_per_week = weekly_data.loc[weekly_data.groupby('Week')['Amt_Consumed'].idxmax()]

    # Train a model for prediction (Example: Linear Regression)
    model = LinearRegression()
    model.fit(highest_selling_food_per_week[['Week']], highest_selling_food_per_week['Amt_Consumed'])

    # Make Predictions
    next_week = highest_selling_food_per_week['Week'].max() + 1
    prediction = model.predict(np.array([[next_week]]))[0]

    # Visualization: Highest Selling Item per Week (Replace this with actual visualization code)
    plt.figure(figsize=(10,6))
    plt.bar(highest_selling_food_per_week['Week'], highest_selling_food_per_week['Amt_Consumed'], color='skyblue')
    plt.title(f'Highest Selling Food Item per Week in {dining_area}')
    plt.xlabel('Week')
    plt.ylabel('Amount Consumed')
    
    # Save the graph as an image file
    plt.savefig(f'static/{dining_area}_highest_selling_item.png')

    # Additional graphs and analysis can be added here
    # ...

# Sample function call (You can remove this line in the actual script)
generate_graphs('Globes')
