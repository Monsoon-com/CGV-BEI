import matplotlib.pyplot as plt 
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
dx=x2-x1
dy=y2-y1
if(abs(dx)>abs(dy)):
    steps=abs(dx)
else:
    steps=abs(dy)
xinc=dx/steps
yinc=dy/steps
x=x1
y=y1
xcord=[]
ycord=[]
for i in range (0,steps):
    xcord.append(round(x))
    ycord.append(round(y))
    x=x+xinc
    y=y+yinc
xcord.append(round(x2))
ycord.append(round(y2))
plt.plot(xcord,ycord,marker="o",linestyle="",color="black")
plt.grid(True)
plt.axis('equal')
plt.show()
