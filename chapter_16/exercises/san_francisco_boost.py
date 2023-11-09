import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from datetime import datetime

import csv


def get_data(filename, dates, highs, lows, avg):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
 
        title_idx = header_row.index('city')
        date_idx = header_row.index('Date')
        tmin_idx = header_row.index('Min.TemperatureF')
        tmax_idx = header_row.index('Max.TemperatureF')
        tmean_idx = header_row.index('Mean.TemperatureF')

        for row in reader:
            date = datetime.strptime(row[date_idx], '%Y-%m-%d')

            if not 'title' in locals():
                title = row[title_idx] + ' ' + str(date.year)

            try:
                high = int(row[tmax_idx])
                low = int(row[tmin_idx])
                avgtemp = int(row[tmean_idx])
            except ValueError:
                print(f'**** Not data found for {date}.')
            except Exception as err:
                print(f'**** Error: {err}.')
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)
                avg.append(avgtemp)

    return title



filename = "../data/san_francisco_2015_full.csv"
dates, highs, lows, avg = [], [], [], []

title = (get_data(filename, dates, highs, lows, avg))



plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots(figsize=(10, 6))
fig.autofmt_xdate()

ax.set_title(title, fontsize=24)
ax.set_xlabel("Date occurrences", fontsize=16)
ax.set_ylabel("Temperature [F]", fontsize=16)

ax.plot(dates, highs, c="red", linewidth=0.7)
ax.plot(dates, avg, c="magenta", alpha=0.4, linewidth=0.4)
ax.plot(dates, lows, c="blue", linewidth=0.7)

ax.fill_between(dates, highs, lows, facecolor="gray", alpha=0.1, hatch='///', edgecolor="gray")

red_patch = mpatches.Patch(color='red', label='highest temperature')
blue_patch = mpatches.Patch(color='blue', label='lowest temperature')
magenta_patch = mpatches.Patch(color='magenta', label='avg temperature')
ax.legend(handles=[red_patch, blue_patch,magenta_patch])

plt.show()