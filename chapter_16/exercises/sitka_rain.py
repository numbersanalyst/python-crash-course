import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "../data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rains = [], []

    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        date.strftime("%d")
        rain = float(row[3])

        dates.append(date)
        rains.append(rain)

fig, ax = plt.subplots()

plt.style.use("seaborn-v0_8")
ax.plot(dates, rains, c="blue")

ax.set_title("Rainfall amount in Sitka 2018", fontsize=24)
ax.set_xlabel("measurement date", fontsize=16)
ax.set_ylabel("the amount of precipitation", fontsize=16)

ax.tick_params(axis="both", which="major", labelsize=16)
ax.fill_between(dates, rains, 0, facecolor="blue", alpha=0.4)

fig.autofmt_xdate()

plt.show()
