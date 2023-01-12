import sys


def calculate_number_of_characters():
    input_data = input("Write down any string and I will try to count the number of characters in the string: ")
    print(f"Number of characters in the `{input_data}` string is: {len(input_data)}")
    print(f"Size of string in bytes: {sys.getsizeof(input_data)}")


calculate_number_of_characters()
