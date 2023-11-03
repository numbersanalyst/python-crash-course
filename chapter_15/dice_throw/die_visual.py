from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

die = Die()

results = [die.roll() for _ in range(1_000)]

frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

x_values = list(range(1, die.num_sides + 1))

data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Results"}
y_axis_config = {"title": "Frequency of occurance values"}
my_layout = Layout(
    title="Result of throwing single die D6 one thousand times.",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot(
    {
        "data": data,
        "layout": my_layout,
    },
    filename="d6.html",
)
