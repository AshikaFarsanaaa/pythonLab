li1 = input("Enter colors for list 1 (comma-separated): ").split(",")
li2 = input("Enter colors for list 2 (comma-separated): ").split(",")

result = []

for color in li1:
    if color not in li2:
        result.append(color)

print("Colors only in list 1:", result)
