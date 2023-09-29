input_list_str = input("Enter a list of numbers separated by spaces: ")
input_list = list(map(int, input_list_str.split()))

square = lambda x: x ** 2

result = list(map(square, input_list))

print("Original list of numbers:", input_list)
print("Square of list elements:", result)