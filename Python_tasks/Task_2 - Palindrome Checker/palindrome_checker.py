def is_palindrome(string):
    string = string.replace(" ", "").lower() # i have replaced spaces with no spaces and converted to lower case
    return string == string[::-1]  # Compare the string with its reverse


print(is_palindrome(":abba:"))