from graph import Graph

def from_template(template_name, data):
  template_lookup = {
    "rad": rad_graph
  }

  template_function = template_lookup.get(template_name, None)
  if template_function == None:
    print("Trying to use default template")
    return Graph.from_yaml(data)

  return template_function(data)


def rad_graph(data):

  y_axis = {
    "name": "Radiant Heat Flux (kW/m2)",
    "sets": list()
  }

  for suffix in data['column_suffix']:
    set = {
      "name": f"{suffix * 10} m downstream",
      "heading": f"{data['column_prefix']}{str(suffix).rjust(2,'0')}"
      }
    y_axis["sets"].append(set)

  x_axis = {
    "name": "Time (s)",
    "sets": list([{"name": "Time", "heading": "Time"}])
  }

  return Graph(title=data["title"], filename=data["name"], show=data['show'], header_row=1, y_axis=y_axis, x_axis=x_axis)
