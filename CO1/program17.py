data = {}
n = int(input("How many items in dictionary? "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

asc = dict(sorted(data.items()))
print("Ascending:", asc)

desc = dict(sorted(data.items(), reverse=True))
print("Descending:", desc)
