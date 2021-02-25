import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


sitka_file = open("data/sitka_weather_2018_simple.csv", "r")
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

for index, column_header in enumerate(header_row2):
    if column_header == "TMAX":
        h = index
    elif column_header == "TMIN":
        l = index
    elif column_header == "DATE":
        d = index

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
        print(low, high)
fig, ax = plt.subplots(2, 1, figsize=(13, 10))

fig.suptitle(
    "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US",
    fontsize=14,
)

ax[0].set_title("SITKA AIRPORT, AK US", fontsize=12)
ax[0].plot(dates_1, highs_1, c="red")
ax[0].plot(dates_1, lows_1, c="blue")
ax[0].fill_between(dates_1, highs_1, lows_1, facecolor="blue", alpha=0.1)
ax[1].set_title("DEATH VALLEY, CA US", fontsize=12)
ax[1].plot(dates_2, highs_2, c="red")
ax[1].plot(dates_2, lows_2, c="blue")
ax[1].fill_between(dates_2, highs_2, lows_2, facecolor="blue", alpha=0.1)
fig.autofmt_xdate()
plt.show()
