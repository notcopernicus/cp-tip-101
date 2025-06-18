# Tuesday June 17 Session One Unit 3: Focused on Strings

# Method for printing everything in lowercase
str = "Copernic"
str2 = str.lower()
print(str2)
print(str.lower())

print()
# Method for printing everything in uppercase
str3 = 'Umar'
str4 = str3.upper()
print(str4)
print(str3.upper())

print()
# Method for seperating a string into a list of strings
str4 = 'Today is technical interview prep'
str5 = str4.split()
print(str5)
str4 = 'Today x there x are x exes'
print(str4.split('x'))

print()
# Method for joining iems in a list seperated by some parameter x, into a string
my_list = ['The', 'brown', 'lazy', 'dog', 'jumped', 'over']
my_joined = '-'.join(my_list)
print(my_joined)
print(' '.join(my_list))

print()
# Method for removing whitespace or some specified char param at the front/end of a string
str5 = "codepath                 "
str6 = str5.strip()
print(str6)
print("??????yes".strip('?'))
print()



# Problem 1 - 
print()
def count_mississippi(limit):
    for num in range(1, limit):
	    print(f"{num} mississippi") 
(count_mississippi(6))



print()
# Problem 2 Write a function that accepts a str as a parameter and returns a new string where the first and last char are swapped
def swap (name):
    # convert to mutable list
    lst = list(name)

    # swap the first and last chars
    lst[0], lst[-1] = lst[-1], lst[0]

    # join back as a string and return
    return ''.join(lst)

name = 'boat'
print(swap(name))
print()
          








# Problem 3: 
# Instructor Demo - Write a function to determine wheter a given sentence is a panagram
sentence = "The quick brown fox jumps over the lazy brown dog"
def is_panagram(sentence):
    # make everything lowercase
    sentence = sentence.lower()
    # remove all non alpha chars
    letters = set(char for char in sentence if char.isalpha())
    print(letters)
    # since there are twenty-six letters in the alphabet, return true
    return len(letters) == 26
print(is_panagram(sentence))
print()








# Problem 4: Write a function that takes any string and reverses it
def reverse_str (str):
     return str[::-1] # this is the syntax trick for reversing any string in python
    # this works because we start at the end of the string and move backwards torward str[0] with each step -1
str20 = 'reverse of Copernic is'
print('reverse of Copernic is ' + reverse_str(str20[11:19]))
# note: slicing allows you to manipulate some string. the index to the right of the colon is non-inclusive and the left index is inclusive 
# remember that  –– string [start : stop : step]

# you can also do this another way
def reversedstr(name):
    reversedstring = ''
    for char in range (len(name)-1, -1, -1):
          reversedstring += name[char]
    return reversedstring
name = 'umar'
print('reversed is ' + reversedstr(name))
print()






#Problem 5
def first_unique_char(my_str):
    for i, char in enumerate (my_str):
        if my_str.count(char) == 1:
             return i
    return -1
     
my_str = "iloveloveleetcode"
print('the first unique char in problem 5 is ' f'{first_unique_char(my_str)}')
print()







# Problem 6 Write a fucntion that takes as a list of words and returns the minimum distance between word1 and word2, if each increment is 1

def find_min_dst(words, word1, word2):
     # set a tracker variable for each word to store index positions
     tracker1, tracker2 = -1, -1 # -1 meaning not found

     # set a minimum distance variable that will be updated
     min_dst = float('inf') # for now just set it to some big number
     
     print(words)
     print("word 1 is: " + word1 + " , word 2 is: " + word2)

     # loop through the words
     for index, word in enumerate (words):
        # check to see if the current words equals word 1
        if word == word1:
               # if it does, set word1's tracker to this current index pos
               tracker1 = index
               print("word 1 is at index " +  f"{tracker1}")
               # also, check to see if we have seen word2 so far
               if tracker2 != -1:
                    # if we have then we can recalculate the minimum distance by subtracting the two positions
                    min_dst = min(min_dst, tracker1 - tracker2) # if it hasn't we can just move on and concurrently repeat for word2
        elif word == word2:
            tracker2 = index
            print('word 2 is at index ' + f'{tracker2}')
            if tracker1 != -1:
                min_dst = min(min_dst, tracker2 - tracker1)


    # finally, return the minimum distance or -1 once we get out of the for loop
     return min_dst
                
     
# note: the order of our x, y values in min matter becauses distances can't be negative. 

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = find_min_dst(words, "the", "brown")
print('the distance between the two words is ' + f'{dist1}')