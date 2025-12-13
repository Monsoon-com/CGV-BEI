import matplotlib.pyplot as plt

def dda(x1, y1, x2, y2):
    x_list, y_list = [], []
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1

    for i in range(steps + 1):
        x_list.append(round(x))
        y_list.append(round(y))
        x += x_inc
        y += y_inc

    return x_list, y_list

x, y = dda(2, 2, 10, 5)

plt.plot(x, y, marker='o')
plt.title("DDA Line (Slope m < 1)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
