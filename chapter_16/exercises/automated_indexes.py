import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from datetime import datetime

import csv


def get_data(filename, dates, highs, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
 
        title_idx = header_row.index('NAME')
        date_idx = header_row.index('DATE')
        tmin_idx = header_row.index('TMIN')
        tmax_idx = header_row.index('TMAX')

        for row in reader:
            date = datetime.strptime(row[date_idx], '%Y-%m-%d')

            if not 'title' in locals():
                title = row[title_idx] + ' ' + str(date.year)

            try:
                high = int(row[tmax_idx])
                low = int(row[tmin_idx])
            except ValueError:
                print(f'**** Not data found for {date}.')
            except Exception as err:
                print(f'**** Error: {err}.')
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)

    return title



filename = "../data/death_valley_2018_simple.csv"
dates, highs, lows = [], [], []

title = (get_data(filename, dates, highs, lows))



plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots(figsize=(10, 6))
fig.autofmt_xdate()

ax.set_title(title, fontsize=24)
ax.set_xlabel("Date occurrences", fontsize=16)
ax.set_ylabel("Temperature [F]", fontsize=16)

ax.plot(dates, highs, c="red")
ax.plot(dates, lows, c="blue")

ax.fill_between(dates, highs, lows, facecolor="gray", alpha=0.1, hatch='///', edgecolor="gray")

red_patch = mpatches.Patch(color='red', label='The highest temperature')
blue_patch = mpatches.Patch(color='blue', label='The lowest temperature')
ax.legend(handles=[red_patch, blue_patch])

plt.show()