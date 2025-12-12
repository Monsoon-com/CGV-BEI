import matplotlib.pyplot as plt
x1=float(input("Enter starting point of x axis:  "))
y1=float(input("Enter starting point of y axis:  "))
x2=float(input("Enter ending point of x axis:  "))
y2=float(input("Enter ending point of y axis:  "))
dx = x2-x1
dy = y2-y1
if(abs(dx)>=abs(dy)):
    steps=abs(dx)
else:
    steps=abs(dy)
Xinc=dx/steps
Yinc=dy/steps
x=x1
y=y1
x_coords = []
y_coords = []
for i in range(0, int(steps)):
    x_coords.append(round(x))
    y_coords.append(round(y))
    x=x+Xinc
    y=y+Yinc
plt.plot(x_coords, y_coords,marker ='o', linestyle='--', color='b')
plt.title('DDA Line Drawing Algorithm')
plt.axis ('equal')
plt.show()