'''
4. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first
char itself.

Sample String : 'restart'
Expected Result : 'resta$t'
'''

def CharReplace(str):
    d = ''
    index = 0
    streplace = ""

    for s in str:
        if index != 0: #if its anything other than the first character of the string
            if(s == d): #if the letter being examined is exactly the same as the first character
                streplace += '$' #replace it with $
            else:
                streplace += s #otherwise leave the character as is and save it as is
        else: #gets and saves the first character of the string
            d = s
            streplace += s

        index = index + 1
    print("\n")
    print(streplace)

CharReplace("restart")
