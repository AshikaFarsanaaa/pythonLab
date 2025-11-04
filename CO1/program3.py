
numbers = [-4, 8, 3, -6, 0, 7, 9]

positive_numbers = [num for num in numbers if num > 0]
print(f"Positive numbers: {positive_numbers}")


n_numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in n_numbers]
print(f"Squared numbers: {squared_numbers}")


word = "hello Ashika"
vowels = "aeiouAEIOU"
vowel_list = [char for char in word if char in vowels]
print(f"List of vowels: {vowel_list}")

word_to_convert = "python"
ordinal_values = [ord(char) for char in word_to_convert]
print(f"Ordinal values: {ordinal_values}")
