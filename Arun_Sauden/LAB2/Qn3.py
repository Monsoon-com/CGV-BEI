#Extend the DDA program to draw rectangle given two opposite corners
import matplotlib.pyplot as plt
x1=int(input("Enter the value of X1:"))
y1=int(input("Enter the value of Y1:"))
x2=int(input("Enter the value of X2:"))
y2=int(input("Enter the value of Y2:"))
xcords=[x1,x2,x2,x1,x1]
ycords=[y1,y1,y2,y2,y1]
plt.plot(xcords,ycords,marker="o",linestyle="--",color="black")
plt.grid(True)
plt.axis('equal')
plt.show()