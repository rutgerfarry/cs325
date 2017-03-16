import sys
from pulp import LpVariable, LpProblem, LpMinimize, LpStatus, value
from numpy import sin, cos, pi
from shared import WeatherData

def collect_weather_data():
    if len(sys.argv) == 2:
        raw_csv_data = open(sys.argv[1]).read()
    else:
        sys.exit("ERROR: No weather data filename supplied.\n"
                 "USAGE: $ python warming_up.py {WEATHER_DATA_CSV}")

    weather_data = [WeatherData(line) for line in raw_csv_data.splitlines()[1:]]
    return weather_data

def create_weather_model(dataset):
    """Creates a weather model for an area based on average temps over time.
    Returns a tuple containing regression coefficients x0...x5 for the model,
    followed by the PuLP status object, eg. `(x0,x1,x2,x3,x4,x5,PuLP_status)`
    
    :param dataset: A list of WeatherData objects representing data since 1952.
    """

    # Declare problem
    prob = LpProblem("warmingUp", LpMinimize)

    # Define variables
    dev = LpVariable("dev")
    x0 = LpVariable("x0")
    x1 = LpVariable("x1")
    x2 = LpVariable("x2")
    x3 = LpVariable("x3")
    x4 = LpVariable("x4")
    x5 = LpVariable("x5")

    # Define problem based on model by Robert Vanderbei found at:
    # http://www.princeton.edu/~rvdb/tex/LocalWarming/LocalWarming.pdf
    prob += dev

    for data in dataset:
        d = data.day

        prob += \
             x0+x1*d \
             + x2*cos((2*pi*d)/365.25) \
             + x3*sin((2*pi*d)/365.25) \
             + x4*cos((2*pi*d)/365.25*10.7) \
             + x5*sin((2*pi*d)/365.25*10.7) \
             - data.avg_temp \
             <= dev

        prob += -dev <= \
             x0+x1*d \
             + x2*cos((2*pi*d)/365.25) \
             + x3*sin((2*pi*d)/365.25) \
             + x4*cos((2*pi*d)/365.25*10.7) \
             + x5*sin((2*pi*d)/365.25*10.7) \
             - data.avg_temp
    status = prob.solve()

    return (value(x0), value(x1), value(x2), value(x3), value(x4), value(x5),
            status)

def print_weather_model(model):
    print "Status: " + LpStatus[model[6]]
    print "x0: " + str(model[0])
    print "x1: " + str(model[1])
    print "x2: " + str(model[2])
    print "x3: " + str(model[3])
    print "x4: " + str(model[4])
    print "x5: " + str(model[5])

# Prevent running if imported as a module
if __name__ == "__main__":
    WEATHER_DATA = collect_weather_data()
    weather_model = create_weather_model(WEATHER_DATA)
    print_weather_model(weather_model)
