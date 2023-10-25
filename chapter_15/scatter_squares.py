import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [num**2 for num in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.twilight)

ax.set_title('Squares of numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Value of squares', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0,1100,0,1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
