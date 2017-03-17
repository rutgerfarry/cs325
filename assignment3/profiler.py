import matplotlib.pyplot as plt
from numpy import sin, cos, pi
from shared import WeatherData
from forecast import create_weather_model

def collect_weather_data():
    raw_csv_data = open("Corvallis.csv").read()
    weather_data = [WeatherData(line) for line in raw_csv_data.splitlines()[1:]]
    return weather_data

def graph_warm_up():
    # Clear plot context
    plt.cla()
    plt.clf()

    points = [[1, 2, 3, 5, 7, 8, 10], [3, 5, 7, 11, 14, 15, 19]]

    # Create line of best fit
    slope = 1.7142857
    x_0 = 0
    y_0 = 1.8571429
    x_stop = 35
    y_stop = slope * (x_stop - x_0) + y_0

    # Create figure
    plt.title("Line of Best Fit")
    plt.axis([0, 12, 0, 20])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    # Plot line of best fit and data points
    plt.plot(points[0], points[1], 'ro')
    plt.plot([x_0, x_stop], [y_0, y_stop], 'b', label="1.714x + 1.857- y")

    plt.legend(loc='upper left')
    plt.savefig("docs/line_of_best_fit_plot.png")

def graph_forecast():
    # Clear plot context
    plt.cla()
    plt.clf()

    # Calculate line of best fit model
    dataset = collect_weather_data()
    x = create_weather_model(dataset)

    days = []
    observed_avg_temps = []
    line_of_best_fit_points = []
    linear_trend_points = [x[0], x[1] * dataset[-1].day]

    for data in dataset:
        d = data.day
        days.append(d)
        observed_avg_temps.append(data.avg_temp)
        line_of_best_fit_points.append(x[0]+x[1]*d \
            + x[2]*cos((2*pi*d)/365.25) \
            + x[3]*sin((2*pi*d)/365.25) \
            + x[4]*cos((2*pi*d)/365.25*10.7) \
            + x[5]*sin((2*pi*d)/365.25*10.7))

    # Create figure
    plt.figure(figsize=(16, 9))
    plt.title("Local Temperature Change")
    plt.xlabel("Days since May 1st, 1952")
    plt.ylabel("Temperature in degrees Celsius")

    # Plot observed temperatures using red +'s
    plt.plot(days, observed_avg_temps, "r+")

    # Plot line of best fit with blue line
    plt.plot(days, line_of_best_fit_points, "b")

    # Plot linear trendline with green dashes
    plt.plot([days[0], days[-1]], linear_trend_points, "g--")

    plt.savefig("docs/forecast_plot.png")

# Prevent running if imported as a module
if __name__ == "__main__":
    graph_warm_up()
    graph_forecast()
