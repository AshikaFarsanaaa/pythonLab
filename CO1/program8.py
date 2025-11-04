def replace_char_user_defined():
    s = input("Enter a string: ")
    first_char = s[0]
    new_str = first_char + s[1:].replace(first_char, '$')
    print("Modified string:", new_str)

replace_char_user_defined()
