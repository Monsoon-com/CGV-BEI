import matplotlib.pyplot as plt

# DDA Algorithm Function
def dda(x1, y1, x2, y2):
    x_points = []
    y_points = []

    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points


# -------- USER INPUT --------
print("Enter the endpoints of the line:")
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Call DDA function
x, y = dda(x1, y1, x2, y2)

# Plot the line
plt.figure(figsize=(6, 6))
plt.plot(x, y, marker='o')
plt.title("DDA Line Drawing Algorithm (User Input)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
