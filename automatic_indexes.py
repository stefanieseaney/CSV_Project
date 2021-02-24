import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


sitka_file = open("data/sitka_weather_07-2018_simple.csv", "r")
death_valley_file = open("data/death_valley_2018_simple.csv", "r")

csv_reader1 = csv.reader(sitka_file, delimiter=",")
csv_reader2 = csv.reader(death_valley_file, delimiter=",")

header_row1 = next(csv_reader1)
header_row2 = next(csv_reader2)

highs_1, lows_1, dates_1 = [], [], []

for index, column_header in enumerate(header_row1):
    if column_header == "TMAX":
        h = index
    elif column_header == "TMIN":
        l = index
    elif column_header == "DATE":
        d = index

for header_row1 in csv_reader1:
    highs_1.append(int(header_row1[h]))
    lows_1.append(int(header_row1[l]))
    dates_1.append(datetime.strptime(header_row1[d], "%Y-%m-%d"))

highs_2, lows_2, dates_2 = [], [], []

for header_row2 in csv_reader2:
    try:
        high = int(header_row2[h])
        low = int(header_row2[l])
        date = datetime.strptime(header_row2[d], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates_2.append(date)
        highs_2.append(high)
        lows_2.append(low)
