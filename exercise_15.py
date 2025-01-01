def is_palindrome(value):
    # Convert the value to a string
    value_str = str(value)
    # Check if the string is equal to its reverse
    if value_str == value_str[::-1]:
        return True
    else:
        return False

# Main program
if __name__ == "__main__":
    input_value = input("Enter a string or number to check if it's a palindrome: ")
    if is_palindrome(input_value):
        print(f"'{input_value}' is a palindrome.")
    else:
        print(f"'{input_value}' is not a palindrome.")
