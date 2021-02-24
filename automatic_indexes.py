import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


sitka_file = open("data/sitka_weather_07-2018_simple.csv", "r")
death_valley_file = open("data/death_valley_2018_simple.csv", "r")

csv_reader1 = csv.reader(sitka_file, delimiter=",")
csv_reader2 = csv.reader(death_valley_file, delimiter=",")

header_row1 = next(sitka_file)
header_row2 = next(death_valley_file)

high = []
low = []
date = []

for index, column_header in enumerate(header_row1):
    if column_header == "TMAX":
        h = index
    elif column_header == "TMIN":
        l = index
    elif column_header == "DATE":
        d = index
