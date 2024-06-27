from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

# Load the dataset
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
iris_data = pd.read_csv('iris.data', header=None, names=column_names)

@app.route('/')
def index():
    # Histograms
    histograms = []
    for column in iris_data.columns[:-1]:
        fig = px.histogram(iris_data, x=column, title=f'Histogram of {column}', marginal="box")
        histograms.append(fig.to_html(full_html=False))

    # Pair plot
    pair_fig = px.scatter_matrix(iris_data, dimensions=iris_data.columns[:-1], color="class")
    pair_plot = pair_fig.to_html(full_html=False)

    return render_template('index.html', histograms=histograms, pair_plot=pair_plot)

if __name__ == '__main__':
    app.run(debug=True)
