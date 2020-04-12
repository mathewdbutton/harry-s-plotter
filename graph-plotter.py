import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

data = pd.read_csv(r'/Users/mathew/Downloads/129RD_E_1_devc.csv', header=1)


df = pd.DataFrame(data, columns=['Time', 'RAD DOWN_24', 'RAD DOWN_25', 'RAD DOWN_26'])

# # Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(df["Time"], df["RAD DOWN_24"], label='farts')  # Plot some data on the axes.
ax.plot(df["Time"], df["RAD DOWN_25"], label='RAD DOWN_25')  # Plot some data on the axes.
ax.plot(df["Time"], df["RAD DOWN_26"], label='RAD DOWN_26')  # Plot some data on the axes.

ax.set_xlabel('Time in seconds')  # Add an x-label to the axes.
ax.set_ylabel('RHF')  # Add a y-label to the axes.
ax.set_title("Things on fire - a plot by harry")  # Add a title to the axes.
ax.legend()  # Add a legend.

plt.savefig('foo.png')
