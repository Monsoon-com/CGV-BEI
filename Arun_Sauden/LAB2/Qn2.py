import matplotlib.pyplot as plt


# m < 1  (gentle positive slope)
x1 = [0, 10]
y1 = [0, 5]

# m > 1  (steep positive slope)
x2 = [0, 5]
y2 = [0, 10]

# Horizontal line (slope = 0)
x3 = [0, 10]
y3 = [5, 5]

# Vertical line (undefined slope)
x4 = [5, 5]
y4 = [0, 10]

# Negative slope (m < 0)
x5 = [0, 10]
y5 = [10, 0]

plt.plot(x1, y1, label="m < 1")
plt.plot(x2, y2, label="m > 1")
plt.plot(x3, y3, label="Horizontal (m = 0)")
plt.plot(x4, y4, label="Vertical (undefined)")
plt.plot(x5, y5, label="Negative slope (m < 0)")

plt.title("Lines with Different Slopes")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()
plt.show()
