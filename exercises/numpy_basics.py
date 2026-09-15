import numpy as np

# Plain Python approach (list + loop)
numbers_list = [1, 2, 3, 4, 5]
doubled_list = []
for n in numbers_list:
    doubled_list.append(n * 2)

print("Python list result:", doubled_list)

# NumPy approach (no loop)
numbers_array = np.array([1, 2, 3, 4, 5])
doubled_array = numbers_array * 2

print("NumPy array result:", doubled_array)
print(numbers_list * 2)
data = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [4.9, 3.0, 1.4, 0.2],
    [6.2, 3.4, 5.4, 2.3]
])


print("Data:")
print(data)
print("Shape:", data.shape)

# Get a single row (row index 0 = the first row)
print("First row:", data[0])

# Get a single value (row 0, column 2)
print("Row 0, Col 2:", data[0, 2])

# Get a single column (all rows, column 1)
print("Second column:", data[:, 1])


numbers = np.array([10, 20, 30, 40, 50])

print("numbers[1:3]:", numbers[1:3])
print("numbers[:2]:", numbers[:2])
print("numbers[2:]:", numbers[2:])
print("numbers[:]:", numbers[:])


# All rows, all columns except the last one -> features (X)
X = data[:, 0:-1]

# All rows, only the last column -> label/target (Y)
Y = data[:, -1]

print("X (features):")
print(X)
print("Y (target):", Y)


print("Sum of all values:", data.sum())
print("Mean of all values:", data.mean())

print("Sum of each column (axis=0):", data.sum(axis=0))
print("Sum of each row (axis=1):", data.sum(axis=1))
