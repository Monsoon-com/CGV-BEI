# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 3, 6, 5]

# plt.plot(x, y)
# plt.title("Simple Line Graph")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# #Bar GRaph
# subjects = ["Math", "Science", "English", "Computer", "Nepali"]
# marks = [85, 90, 78, 92, 88]

# plt.bar(subjects, marks)
# plt.title("Marks of 5 Subjects")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 5, 2, 6, 4]

plt.figure()
plt.plot(x, y)
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

subjects = ["Math", "Science", "English", "Computer", "Nepali"]
marks = [85, 90, 78, 92, 88]

plt.figure()
plt.bar(subjects, marks)
plt.title("Marks of 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
