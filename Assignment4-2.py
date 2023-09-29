input_list_str = input("Enter a list of integers separated by spaces: ")
input_list = list(map(int, input_list_str.split()))

triple = lambda x: x * 3

result = list(map(triple, input_list))

print("Original list of numbers:", input_list)
print("Triple of list numbers:", result)