from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)

# Load your data
data = pd.read_csv('Food_Wastage_sample.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        # Filter data for selected location
        location_data = data[data['Location'] == location]
        
        # Generate the graphs (you need to replace this with your actual graph generation code)
        # Example: Total wastage per week
        plt.figure(figsize=(10, 6))
        plt.plot(location_data['Week'], location_data['Wastage'], marker='o')
        plt.title(f'Total Wastage per Week at {location}')
        plt.xlabel('Week')
        plt.ylabel('Total Wastage')
        plt.grid(True)
        
        # Convert plot to PNG image
        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        
        # Add your other graph generation and prediction code here
        
        return render_template('graphs.html', plot_url=plot_url)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
