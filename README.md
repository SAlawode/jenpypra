# Palindrome Finder

This is a simple Python script to find palindromes in a given list of words. A palindrome is a word that reads the same backward as forward, such as "level" or "radar".

## How It Works

The script defines two functions:
1. `is_palindrome(word)`: Checks if a given word is a palindrome.
2. `find_palindromes(words)`: Finds and returns a list of palindromes from a given list of words.

## Prerequisites

Make sure you have Python installed on your machine. This script works with Python 3.x.

## Usage

1. Clone this repository or download the `palindrome_finder.py` file.

2. Run the script with a list of words to find palindromes.

### Example

```python
# palindrome_finder.py

def is_palindrome(word):
    return word == word[::-1]

def find_palindromes(words):
    palindromes = [word for word in words if is_palindrome(word)]
    return palindromes

# Example usage:
words = ["level", "world", "radar", "python", "madam", "hello", "racecar"]
palindromes = find_palindromes(words)
print("Palindromes found:", palindromes)
