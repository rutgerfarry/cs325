import time
import random
import argparse
from sys import argv
import numpy as np
import matplotlib
matplotlib.use('Agg') # Because Miles don't have a display :(
import matplotlib.pyplot as plt

from shared import WeatherData

def collect_weather_data():
    raw_csv_data = open("Corvallis.csv").read()
    weather_data = [WeatherData(line) for line in raw_csv_data.splitlines()[1:]]
    return weather_data


def graph_warm_up():

    points = np.array([[1, 2, 3, 5, 7, 8 , 10], [3,5,7,11,14,15,19]])

    # Create the best fit line - skills
    slope = 1.7142857
    x_0 = 0
    y_0 = 1.8571429
    x_stop = 35
    y_stop = slope * (x_stop - x_0) + y_0

    plt.title("Line of Best Fit")
    plt.axis([0, 12, 0, 20])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    plt.plot(points[0], points[1], 'ro') 
    plt.plot([x_0, x_stop], [y_0, y_stop], 'b', label="1.714x + 1.857- y")

    plt.legend(loc='upper left')
    plt.savefig("docs/lineOBF_plot.png")

def graph_forecast():
    x0 = 10.135061
    x1 = 0.00010095409
    x2 = 5.2564156
    x3 = 8.7514693
    x4 = 1.8864462
    x5 = -0.38240757

    plt.title("Local Temperature Change")
    plt.xlabel("d")
    plt.ylabel("T")


    plt.savefig("docs/lineOBF_plot.png")



def main():
    graph_warm_up()
    graph_forecast()
    

main()
