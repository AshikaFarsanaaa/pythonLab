s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

new_s1 = s2[0] + s1[1:]
new_s2 = s1[0] + s2[1:]

final_string = new_s1 + " " + new_s2
print("Final string:", final_string)
