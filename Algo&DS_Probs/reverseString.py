"""""
Given a string of words, reverse all the words in the string

start - "This is the best"
finish - "best the is The"
"""

def reverse(s):
    s = s.split()
    s.reverse()
    str = ""
    for words in s:
        str += words + " "

    
    return str

print(reverse("this is the best "))