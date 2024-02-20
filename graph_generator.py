import matplotlib.pyplot as plt
import pandas as pd

def generate_graph(dining_area):
    # Your data processing and graph generation code here
    # For illustration, let’s create a simple bar graph
    data = {'Food Item': ['Pizza', 'Burger', 'Pasta'], 'Sales': [100, 150, 80]}
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(10,6))
    plt.bar(df['Food Item'], df['Sales'], color=['red', 'green', 'blue'])
    plt.title(f'Highest Selling Food Items in {dining_area}')
    plt.xlabel('Food Item')
    plt.ylabel('Sales')
    
    # Save the graph as an image file
    plt.savefig(f'static/{dining_area}_sales_graph.png')
