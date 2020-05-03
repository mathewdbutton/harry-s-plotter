class Graph:
  def __init__(self, graph_settings):
    self.settings = graph_settings
    self.x_axis = self.settings['x-axis']['sets'][0]
    self.y_axes = self.settings['y-axis']['sets']
    self.filename = self.settings['name']
    self.title = self.settings['title']
