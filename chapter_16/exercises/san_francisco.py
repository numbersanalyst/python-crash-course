import matplotlib.pyplot as plt

from datetime import datetime

import csv



filename = '../data/san_francisco_2015_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        date = datetime.strptime(row[1], "%Y-%m-%d")
        high = int(row[2])
        low = int(row[4])

        dates.append(date)
        highs.append(high)
        lows.append(low)

plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots(figsize=(10, 6))
fig.autofmt_xdate()

ax.set_title("The highest and the lowest temperature in San Francisco, 2015", fontsize=24)
ax.set_xlabel("Date occurrences", fontsize=16)
ax.set_ylabel("Temperature [F]", fontsize=16)

ax.plot(dates, highs, c="red")
ax.plot(dates, lows, c="blue")

ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.show()