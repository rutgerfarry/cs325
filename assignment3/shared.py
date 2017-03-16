from datetime import date

class WeatherData(object):
    """Represents a day of weather data obtained from:
    http://www.ncdc.noaa.gov/cdo-web/search
    Assumes data is a line of a csv in the form of:
    `STATION;DATE;TMAX;TMIN;year;month;day;average;day`

    Attributes:
        max_temp (float): Max temp ever recorded that day of the year (Celsius)
        min_temp (float): Min temp ever recorded that day of the year (Celsius)
        avg_temp (float): Average temp recorded that day of the year (Celsius)
        day (int): Number of days since May 1st, 1952
        date (datatime.date): Date obj representing the recording's date

    """

    def __init__(self, data_string):
        data = data_string.split(";")

        self.max_temp = float(data[2]) / 10
        self.min_temp = float(data[3]) / 10
        self.avg_temp = float(data[7])
        self.day = int(data[8])

        cal_year = int(data[4])
        cal_month = int(data[5])
        cal_day = int(data[6])
        self.date = date(cal_year, cal_month, cal_day)

    def __repr__(self):
        return "{0}: min: {1}, max: {2}, avg: {3}".format(
            self.date,
            self.min_temp,
            self.max_temp,
            self.avg_temp)
