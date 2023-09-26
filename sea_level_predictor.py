import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    fig, ax = plt.subplots()
    df.plot(kind="scatter", x="Year", y="CSIRO Adjusted Sea Level")
    # Create first line of best fit
    x1 = df["Year"]
    y1 = df["CSIRO Adjusted Sea Level"]
    predicted_x1 = np.arange(1880, 2051)
    plt.xticks(np.arange(1850, 2075, 25, dtype=float))
    mask_x = df["Year"] >= 2000
    x = df[mask_x]["Year"]
    predicted_x = np.arange(2000, 2051)
    y = df[mask_x]["CSIRO Adjusted Sea Level"]
    slope, intercept, r_value, p_value, std_err = linregress(x1, y1) 
    predicted_y = slope * predicted_x1 + intercept
    plt.plot(predicted_x1, predicted_y)
    # Create second line of best fit
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x, y)
    predicted_y2 = slope2 * predicted_x + intercept2
    plt.plot(predicted_x, predicted_y2)
    plt.xticks(np.arange(1850, 2100, 25, dtype=float))
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
    # Add labels and title

    # plt.show() 
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()