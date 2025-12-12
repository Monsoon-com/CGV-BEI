#Use DDA to draw the axes of a simple coordinate system(X and Y axes) using matplotlibb in python
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

# X-axis from (-10,0) to (10,0)
x_axis_x, x_axis_y = dda(-10, 0, 10, 0)

# Y-axis from (0,-10) to (0,10)
y_axis_x, y_axis_y = dda(0, -10, 0, 10)

plt.plot(x_axis_x, x_axis_y, label="X-axis")
plt.plot(y_axis_x, y_axis_y, label="Y-axis")

plt.title("Coordinate Axes using DDA Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.axhline(0, color='black', linewidth=0.5) 
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
