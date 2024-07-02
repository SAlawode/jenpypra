def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(words):
    palindromes = [word for word in words if is_palindrome(word)]
    return palindromes

# Example usage:
words = ["level", "world", "radar", "python", "madam", "hello", "racecar"]
palindromes = find_palindromes(words)
print("Palindromes found:", palindromes)
