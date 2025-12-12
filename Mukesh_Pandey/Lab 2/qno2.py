import matplotlib.pyplot as plt
xcord1 , ycord1 = [], []
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
dx = abs(x2-x1)
dy = abs(y2-y1)
dx_s = x2 - x1
dy_s = y2 - y1

# Bresenham's Line Algorithm
if x2 >= x1:
        sx = 1 
else:
        sx = -1
if y2 >= y1:
        sy = 1 
else:
        sy = -1
x = x1
y = y1
if dx >= dy:
    p = 2 * dy - dx
    for _ in range(dx + 1):
        xcord1.append(x)
        ycord1.append(y)
        x += sx
        if p >= 0:
            y += sy
            p += 2 * dy - 2 * dx
        else:
            p += 2 * dy
else:
    p = 2 * dx - dy
    for _ in range(dy + 1):
        xcord1.append(x)
        ycord1.append(y)
        y += sy
        if p >= 0:
            x += sx
            p += 2 * dx - 2 * dy
        else:
            p += 2 * dx

# DDA Line Algorithm

if(abs(dx_s)>abs(dy_s)):
    steps=abs(dx_s)
else:
    steps=abs(dy_s)

xcord=[]
ycord=[]
if steps == 0:
    xcord = [x1]
    ycord = [y1]
else:
    xinc=dx_s/steps
    yinc=dy_s/steps
    x=x1
    y=y1
    for i in range (0,steps):
        xcord.append(round(x))
        ycord.append(round(y))
        x=x+xinc
        y=y+yinc
    xcord.append(round(x2))
    ycord.append(round(y2))

plt.plot(xcord1,ycord1,marker='o',linestyle='-',color='blue',label='Bresenham')
plt.plot(xcord,ycord,marker='.',linestyle='--',color='black',label='DDA')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()