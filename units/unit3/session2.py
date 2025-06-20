# Method to return True or False if all characters in a given string are (a-z)
str = 'test, test'
print(str.isalpha())

# Method to return True if all characters in a str are alphanumeric'
print(str.isalnum())

# Method to find the first occurence of a substring
print(str.find('es'))


# Method to count the freq if a the substring
print(str.count('es'))

# Instructor Demo - return a str seperated by spaces, reverse the order of the words, remove white spaces
def reverse_words(s):
    return ''.join(s.split()[::-1])
    # words = s.split() # remove extra spaces & split into words
    # rv = words[::-1] # reverse the  word order
    # return ' '.join(rv) # join words to a single string & return
print(reverse_words('  the sky   is blue'))
