nums = []

for i in range(5):
    number = float(input(f"Enter number {i+1}: "))
    nums.append(number)

largest = max(nums)
print("The largest number is:", largest)