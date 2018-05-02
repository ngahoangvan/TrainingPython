def is_anagram(firstString, secondString):
    return sorted(firstString) == sorted(secondString)

print(is_anagram('abc','cab'))

print(is_anagram('abc','cag'))