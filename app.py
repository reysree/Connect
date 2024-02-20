from flask import Flask, render_template, request, send_file
import os
import nbconvert
import nbformat

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dining_area = request.form.get("dining_area")
        run_notebook(dining_area)
        # Render a template and pass the file path of the generated image
        return render_template("result.html", image_file=f"{dining_area}_graph_name.png")
    return render_template("index.html")

def run_notebook(dining_area):
    # Load notebook
    with open("updated_food_wastage_analysis_and_prediction.ipynb", "r", encoding="utf-8") as nb_file:
        notebook = nbformat.read(nb_file, as_version=4)
    # Set user_input_dining_area in the notebook
    for cell in notebook.cells:
        if "user_input_dining_area = " in cell.source:
            cell.source = f"user_input_dining_area = '{dining_area}'"
    # Convert notebook
    exporter = nbconvert.NotebookExporter()
    body, resources = exporter.from_notebook_node(notebook)
    # Save output notebook
    with open("output_notebook.ipynb", "w", encoding="utf-8") as output_file:
        output_file.write(body)

if __name__ == "__main__":
    app.run(debug=True)
