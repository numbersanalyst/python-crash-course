import csv

from plotly import offline
from plotly.graph_objects import Scattergeo, Layout

data_limit = 5_000
iteration = 0

filename = "data/world_fires_7_day.csv"
with open(filename, encoding="utf8") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lons, lats, powers, dates = [], [], [], []
    for row in reader:
        lons.append(row[1])
        lats.append(row[0])
        powers.append(float(row[2]))
        dates.append(row[5])

        iteration += 1
        if iteration > data_limit:
            break


data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": dates,
    "marker": {
        "size": [0.05 * power for power in powers],
        "color": powers,
        "colorscale": "Hot",
        "reversescale": True,
        "colorbar": {"title": "brightness of the fire"}
    }
}]

my_layout = Layout(title=f"{data_limit} fires on the world in 2018")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="world_fires_map.html")