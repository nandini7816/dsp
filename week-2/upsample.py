x = [1, 2, 3, 4, 5]

def ds(x, a):
    y = []
    if a < 1:
        for i in range(0, len(x)):
             index = int(a * i)
             if index < len(x):  # Check if the index is within bounds of list
                y.append(x[index])
    return y

y = ds(x, 1/2)
print(y)  # Output: [1, 1, 2]