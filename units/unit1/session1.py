""" # problem one : hello world
def hello_world():
    print ("hello world")
hello_world()

# problem two: today's mood
def todays_mood():
    mood = "🥱"
    print("Today's mood: " + mood)
todays_mood()

#problem three:
def print_menu():
    print("Today's menu: pizza")
print_menu()

#problem 4 sum of two integers

def sum(a,b):
    return a + b
print(sum(12,3))

#problem 5: product of two integers:
def product(a, b):
    return a * b
print(product(12,4))


in class problem june 5
UMPIRE
understand, match, plan, implement, review, expand

lst = [1,2,3,4,5]
threshold = 2

def above_t(lst, threshold):
    lst2 = []
    for i in lst:
        if (i > threshold):
            lst2.append(i)
    return lst2
print (above_t(lst,threshold))


Understand: I think this problem is asking us to print out each number or string in a list
Plan: 
for loop to call each element in the list
    print it out

Implementation:"""
"""
# breakout room problem 1
lst = ["suman", "copernic", "genesis", "abdullahi"]
def print_list(lst):
    for str in lst:
        print(str)
print_list(lst) 
"""
# breakout room problem 2
lst = [3,5,8]
def double(lst):
    for i in lst:
        print(i*2)
double(lst)

#breakout room problem 3
lst = [1,-2,-3,4]
def flip_sign(lst):
    for i in lst:
        print(-i)
flip_sign(lst)
