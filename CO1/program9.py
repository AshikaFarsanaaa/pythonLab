def exchange_first_last(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]

string = input("Enter a string: ")
new_string = exchange_first_last(string)

print("String after exchanging first and last character:", new_string)
