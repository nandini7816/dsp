x = [1, 2, 3, 4, 5]
def ds(x, a):
    if a > 1:
        y = []
        for i in range(0, len(x)):
            if a * i < len(x):  # Check if the index is within bounds of list x
                y.append(x[a * i])
        return y
    else:
        return []  # Return an empty list if a <= 1

y = ds(x,2)
print(y)