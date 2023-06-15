#1.Split in Half
#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part.
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_in_half(s):
    length = len(s)
    half = length // 2
    odd = 0
    if length % 2:
        add = 1
    left = s[:half + odd]
    right = s[half + odd:]
    return right + left

test_string_odd = 'bbbbbcaaaaa'
test_string_even = 'aaaaabbbbbc'
print(split_in_half(test_string_odd))
print(split_in_half(test_string_even))

#2. Unique Characters in String
#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.

def unique_str(s):
    lenstr =len(s)
    lenset = len(set((s)))
    return lenset == lenstr

test_data_pos = 'abcde'
test_data_neg = 'aabcde'
print (unique_str(test_data_pos))
print (unique_str(test_data_neg))