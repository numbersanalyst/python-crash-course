import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "data/death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"No data found for {date}.")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)


plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax.set_title(
    "The highest and the lowest day temperature - 2018\nDeath Valley, California",
    fontsize=24,
)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()
