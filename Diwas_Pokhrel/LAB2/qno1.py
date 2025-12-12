import matplotlib .pyplot as plt
xcord,ycord =[],[]
x1=int(input("Enter x1:"))
y1=int(input("Enter y1:")) 
x2=int(input("Enter x2:")) 
y2=int(input("Enter x2:"))    
dx = abs(x2 - x1)
dy = abs(y2 - y1)
if x2 >= x1:
        sx=1
else:
        sy=-1
if y2 >= y1:
        sy=1
else:
        sy=-1
x=x1
y=y1
if dx>=dy:
        p=2*dy-dx
        for _ in range(dx+1):
            xcord.append(x)
            ycord.append(y)
            x+=sx 
            if p>=0:
                y+=sy 
                p+=2*dy-2*dx
        else: 
            p+=2*dy
else:
        p =2* dx-2* dy
        for _ in range(dy+1):
          xcord.append(x)
          ycord.append(y) 
          y+=sy 
        if p >=0:  
                x+=sx 
                p+=2*dx-2*dy
        else: 
                p+=2*dx
plt.plot(xcord,ycord,marker='o',linestyle='-',color='blue')
plt.grid(True)
plt.show()