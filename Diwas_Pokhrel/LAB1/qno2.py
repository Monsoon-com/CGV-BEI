import matplotlib.pyplot as plt
x1=int (input ("Enter x1: "))
y1=int (input ("Enter y1: "))
x2=int (input ("Enter x2: "))
y2=int (input ("Enter y2: "))
xcords=[x1,x2,x2,x1,x1] 
ycords=[y1,y1,y2,y2,y1]
plt.plot (xcords,ycords,marker="o",linestyle="-",color="green")
plt.grid(True)
plt.axis ('equal')
plt.show ()