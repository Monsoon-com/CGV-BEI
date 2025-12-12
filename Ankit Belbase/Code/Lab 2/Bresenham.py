import matplotlib.pyplot as plt
x1 = int(input("Enter starting point of x-axis: "))
x2 = int(input("Enter ending point of x-axis: "))
y1 = int(input("Enter starting point of y-axis: "))
y2 = int(input("Enter ending point of y-axis: "))
dx = abs(x2 - x1)
dy = abs(y2 - y1)
if(x1<x2):
    sx =+1
else:
    sx = -1
if(y1<y2):
    sy = +1
else:
    sy = -1
xes , yes = [], []
x=x1
y=y1
if(dx>dy):
    p=2*dy-dx
    for i in range(dx+1):
        xes.append(x)
        yes.append(y)
        if(p>=0):
            y=y+sy
            p=p+2*dy-2*dx
        else:
            p=p+2*dy
      

else :
    p=2*dx-dy
    for i in range(dy+1):
        xes.append(x)
        yes.append(y)
        if(p>=0):
            x=x+sx
            p=p+2*dx-2*dy
        else:
            p=p+2*dx
plt.plot(xes,yes , marker='o', color='b',linestyle='--')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bresenham's Line Drawing Algorithm")
plt.axis ('equal')
plt.show()
