import matplotlib.pyplot as plt

x1 = int(input("Enter the starting point of x: "))
y1 = int(input("Enter the starting point of y: "))
x2 = int(input("Enter the ending point of x: "))
y2 = int(input("Enter the ending point of y: "))

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

xinc = dx / steps
yinc = dy / steps

x = x1
y = y1

xcord = []
ycord = []

for i in range(steps):
    xcord.append(round(x))
    ycord.append(round(y))
    plt.plot(xcord, ycord, marker='o', linestyle='--', color='green')
    x += xinc
    y += yinc

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()