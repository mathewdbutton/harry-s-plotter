import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import yaml
from graph import Graph

def load_data(filename, header=1):
  return pd.read_csv(filename, header=header)

def load_graph_settings(filename="./graph_settings.yml"):
  with open(filename, 'r') as stream:
    try:
        return(yaml.safe_load(stream))
    except yaml.YAMLError as e:
        print(f"Can't read {filename} - {e}")

def generate(data_path, output_path):
    data = load_data(data_path)
    settings = load_graph_settings()
    for graph in settings['graphs']:
      graph_model = Graph(graph)
      x_axis = graph_model.x_axis

      y_axis_columns = [set['heading'] for set in graph['y-axis']['sets'] ]
      df = pd.DataFrame(data, columns=[x_axis['heading'], *y_axis_columns])

      # # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
      fig, ax = plt.subplots()  # Create a figure and an axes.
      for column in graph['y-axis']['sets']:
        ax.plot(df[x_axis['heading']], df[column['heading']], label=column['name'])  # Plot some data on the axes.

      ax.set_xlabel(graph['x-axis']['name'])  # Add an x-label to the axes.
      ax.set_ylabel(graph['y-axis']['name'])  # Add a y-label to the axes.
      ax.set_title(graph['title'])  # Add a title to the axes.
      ax.legend()  # Add a legend.
      if 'show' in graph:
        plt.show()
      fig.set_size_inches(18.5, 10.5)
      fig.savefig(f"{output_path}{graph['name']}.png", bbox_inches='tight')
