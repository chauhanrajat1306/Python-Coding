size = int(input("Enter the size of the triangle: "))

for row in range(size):
    padding = " " * (size - row - 1)
    stars = " ".join("*" for _ in range(row + 1))
    print(padding + stars)
    