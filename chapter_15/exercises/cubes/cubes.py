import matplotlib.pyplot as plt

x_values = range(1, 5000)
y_values = [num**3 for num in x_values]

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.hsv, s=5)

ax.set_xlabel("Values")
ax.set_ylabel("Cubes of values")
ax.set_title("Cubes of numbers")

ax.axis([0, 6000, 0, 135000000000])

plt.show()
