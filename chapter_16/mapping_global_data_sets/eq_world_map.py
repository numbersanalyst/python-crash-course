import json

from plotly import offline
from plotly.graph_objs import Layout

filename = "data/eq_data_30_day_m1_fresh.json"
with open(filename, encoding="utf8") as f:
    all_eq_data = json.load(f)

layout_title = all_eq_data["metadata"]["title"]
all_eq_dicts = all_eq_data["features"]

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    hover_texts.append(eq_dict["properties"]["title"])

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "text": hover_texts,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Power"},
        },
    }
]
my_layout = Layout(title=layout_title)

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")
