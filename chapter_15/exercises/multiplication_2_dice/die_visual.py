from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

die1 = Die()
die2 = Die()

results = [die1.roll() * die2.roll() for _ in range(1_000)]

max_result = die1.num_sides * die2.num_sides

frequencies = [results.count(value) for value in range(1, max_result + 1)]

x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Results"}
y_axis_config = {"title": "Frequency of occurance values"}
my_layout = Layout(
    title="The result of multiplying the throws of two D6 dice one hundred times",
    xaxis=x_axis_config,
    yaxis=y_axis_config,
)
offline.plot(
    {
        "data": data,
        "layout": my_layout,
    },
    filename="d6_d6_multi.html",
)
