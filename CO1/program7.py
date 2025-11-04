def compare_lists(list1, list2):

    same_length = len(list1) == len(list2)    
    same_sum = sum(list1) == sum(list2)    
    common_values = set(list1).intersection(list2)
    
    
    print("\nResults:")
    print(f"(a) Same length: {same_length}")
    print(f"(b) Same sum: {same_sum}")
    if common_values:
        print(f"(c) Common values: {common_values}")
    else:
        print("(c) No common values.")

list1 = list(map(int, input("Enter the first list of integers (space-separated): ").split()))
list2 = list(map(int, input("Enter the second list of integers (space-separated): ").split()))

compare_lists(list1, list2)
