def is_palindrome(s):
    # Remove all non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Sample test cases
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race car"))  # True
print(is_palindrome("hello"))  # False
