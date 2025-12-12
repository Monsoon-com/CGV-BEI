#Implement the DDA algorithm as a functon that return x and y coordinate lists in python
import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    x = []
    y = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x_curr = x1
    y_curr = y1

    for _ in range(steps + 1):
        x.append(x_curr)
        y.append(y_curr)
        x_curr += x_inc
        y_curr += y_inc

    return x, y


x_points, y_points = dda(2, 3, 10, 8)

print("X coordinates:", x_points)
print("Y coordinates:", y_points)

plt.plot(x_points, y_points, marker='o')
plt.title("Line Using DDA Algorithm")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()
