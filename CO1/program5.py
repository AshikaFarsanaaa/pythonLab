numbers = input("Enter a list of integers separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]
result = ['over' if num > 100 else num for num in numbers_list]
print("Modified list:", result)
