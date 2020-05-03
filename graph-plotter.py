import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import yaml

def load_data(filename, header=1):
  return pd.read_csv(filename, header=header)

def load_graph_settings(filename="./graph_settings.yml"):
  with open(filename, 'r') as stream:
    try:
        return(yaml.safe_load(stream))
    except yaml.YAMLError:
        print(f"Can't read {filename}")

def main():
    data = load_data(r'/Users/mathew/Downloads/129RD_E_1_devc.csv')
    settings = load_graph_settings()
    for graph in settings['graphs']:

      x_axis = graph['x-axis']['sets'][0]

      y_axis_columns = [set['heading'] for set in graph['y-axis']['sets'] ]
      df = pd.DataFrame(data, columns=[x_axis['heading'], *y_axis_columns])

      # # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
      fig, ax = plt.subplots()  # Create a figure and an axes.
      for column in graph['y-axis']['sets']:
        ax.plot(df[x_axis['heading']], df[column['heading']], label=column['name'])  # Plot some data on the axes.

      ax.set_xlabel(graph['x-axis']['name'])  # Add an x-label to the axes.
      ax.set_ylabel(graph['y-axis']['name'])  # Add a y-label to the axes.
      ax.set_title(graph['name'])  # Add a title to the axes.
      ax.legend()  # Add a legend.
      plt.savefig(f"{graph['name']}-foo.png")
      if 'show' in graph:
        plt.show()


if __name__ == "__main__":
    main()
