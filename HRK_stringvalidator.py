if __name__ == '__main__':
    input_string = input().strip()


    print(any(c.isalnum() for c in input_string))  # Check for alphanumeric
    print(any(c.isalpha() for c in input_string))  # Check for alphabetical
    print(any(c.isdigit() for c in input_string))  # Check for digits
    print(any(c.islower() for c in input_string))  # Check for lowercase
    print(any(c.isupper() for c in input_string))  # Check for uppercase
