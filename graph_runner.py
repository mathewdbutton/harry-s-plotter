#!/usr/bin/env python

import argparse
import graph_plotter
import os.path

def main():
  parser = argparse.ArgumentParser(description='Build them graphs')
  parser.add_argument("-p", "--path", required=True, type=str, help="The path to the CSV file")
  parser.add_argument("-o", "--output", required=False, type=str, help="The path to output graph image. It'll default to the path of the CSV file")

  args = vars(parser.parse_args())
  path = args["path"]

  output_path = args["output"]+"/"
  if output_path == None:
    output_path = str(os.path.dirname(path))

  graph_plotter.generate(path, output_path)

if __name__ == "__main__":
    main()
