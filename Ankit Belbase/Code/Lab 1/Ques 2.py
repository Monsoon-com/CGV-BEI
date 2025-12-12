import matplotlib.pyplot as plt

x1=float(input("Enter first corner x axis:  "))
y1=float(input("Enter first corner y axis:  "))
x2=float(input("Enter second corner x axis:  "))
y2=float(input("Enter second corner y axis:  "))
x3=float(input("Enter third corner x axis:  "))
y3=float(input("Enter third corner y axis:  "))
x4=float(input("Enter fourth corner x axis:  "))
y4=float(input("Enter fourth corner y axis:  "))

corners = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
all_x_coords = []
all_y_coords = []

for i in range(4):
    x_start, y_start = corners[i]
    x_end, y_end = corners[(i + 1) % 4]
    
    dx = x_end - x_start
    dy = y_end - y_start
    
    if(abs(dx) >= abs(dy)):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    Xinc = dx / steps
    Yinc = dy / steps
    
    x = x_start
    y = y_start
    
    for j in range(0, int(steps)):
        all_x_coords.append(round(x))
        all_y_coords.append(round(y))
        x = x + Xinc
        y = y + Yinc

all_x_coords.append(round(x1))
all_y_coords.append(round(y1))

plt.plot(all_x_coords, all_y_coords, marker='o', linestyle='-', color='b')
plt.title('DDA Line Drawing Algorithm for Rectangle')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.axis('equal')
plt.grid()
plt.show()






