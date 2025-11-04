def count_a(names):
    """Counts the total number of 'a' letters in a list of names."""
    return sum(name.lower().count('a') for name in names)

names = input("Enter first names separated by spaces: ").split()
total_a = count_a(names)

print("List of names:", names)
print("Total occurrences of 'a':", total_a)
