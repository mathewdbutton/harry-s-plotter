class Graph:
  def __init__(self, title="", y_axis=[], x_axis={}, header_row=1, filename="", show=False):
    self.x_axis = x_axis
    self.y_axis = y_axis
    self.filename = filename
    self.title = title
    self.header_row = header_row
    self.show = show

  def y_axis_columns(self):
    return [set['heading'] for set in self.y_axis["sets"]]

  @staticmethod
  def from_yaml(data):
    return Graph(title=data['title'],
          y_axis=data['y-axis'],
          x_axis=data['x-axis'],
          filename=data['name'],
          header_row=data["header_row"],
          show=data['show']
            )
