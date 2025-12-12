import matplotlib.pyplot as plt
width = float(input("Enter width: "))
height = float(input("Enter height: "))
x = [0, width, width, 0, 0]
y = [0, 0, height, height, 0]
plt.plot(x, y, marker='o')
plt.title("Rectangle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()