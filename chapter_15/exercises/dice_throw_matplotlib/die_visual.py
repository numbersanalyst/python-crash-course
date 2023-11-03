import matplotlib.pyplot as plt
from die import Die

die = Die()

fig, ax = plt.subplots()

results = [die.roll() for _ in range(1_000)]
frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

x_values = list(range(1, die.num_sides + 1))
ax.bar(x_values, frequencies)

ax.set_title("Result of throwing single die D6 one thousand times.")
ax.set_xlabel("number of dots")
ax.set_ylabel("frequency of occurance values")

plt.show()
