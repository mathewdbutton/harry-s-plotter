import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import yaml

from graph_type_manager import from_template
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
    for graph in [from_template(graph_data.get('type',None), graph_data) for graph_data in settings['graphs'] ]:
      x_axis = graph.x_axis['sets'][0]

      dataFrame = pd.DataFrame(data, columns=[x_axis['heading'], *graph.y_axis_columns()])

      fig, ax = plt.subplots()
      for column in graph.y_axis['sets']:
        ax.plot(dataFrame[x_axis['heading']], dataFrame[column['heading']], label=column['name'])  # Plot some data on the axes.

      ax.set_xlabel(graph.x_axis['name'])
      ax.set_ylabel(graph.y_axis['name'])
      ax.set_title(graph.title)
      ax.legend()
      if graph.show:
        plt.show()
      fig.set_size_inches(18.5, 10.5)
      fig.savefig(f"{output_path}{graph.filename}.png", bbox_inches='tight')
