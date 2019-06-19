'''
Define a function is_palindrome() that recognizes palindromes 
(i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.
'''

word = input("Please enter a word and I will tell you if it is palindrome or not: ")

def is_palindrome():
    string = ''
    for i in range(len(word)-1,-1,-1):
        string += word[i]
    if word == string:
        return True
    else:
        return False

if is_palindrome() == True:
    print("Word is palindrome.")
else:
    print("Word is NOT palindrome.")
    