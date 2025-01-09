# Creating an array using a list
arr = [1, 2, 3, 4, 5]

# Accessing elements
print("First element:", arr[0])
print("Last element:", arr[-1])

# Adding an element
arr.append(6)
print("Array after append:", arr)

# Removing an element
arr.remove(3)  # Removes the first occurrence of 3
print("Array after removing 3:", arr)

# Updating an element
arr[2] = 10
print("Array after update:", arr)

# Iterating through the array
print("Elements in the array:")
for element in arr:
    print(element)
