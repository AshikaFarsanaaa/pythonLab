numbers = list(map(int, input("Enter numbers: ").split()))
result = []

for num in numbers:
    if num % 2 != 0:
        result.append(num)

print("List after removing even numbers:", result)
