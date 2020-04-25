'''
24. Write a Python program to test whether a passed letter is a vowel or not.
'''

#Actual Solution
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

#MT Solution
def VowelOrNot(char):
    all_vowels = 'aeiou'
    #below will return true if vowel if found, False if not
    if(char in all_vowels != True):
        print("\nVowel found: " + char)
    else:
        print("\nNo vowel found")

VowelOrNot('a')
VowelOrNot('e')
VowelOrNot('i')
VowelOrNot('o')
VowelOrNot('u')

VowelOrNot('b')
VowelOrNot('c')
VowelOrNot('z')
