colors_input = input("Enter color names separated by commas: ")
colors = [color.strip() for color in colors_input.split(',') if color.strip().isalpha()]

print("Cleaned color list (without numbers):", colors)

if colors:
    print("First color:", colors[0])
    print("Last color:", colors[-1])
else:
    print("No valid colors (all contained numbers).")
