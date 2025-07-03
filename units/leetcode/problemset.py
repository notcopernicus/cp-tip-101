#  Climbing Stairs Dynamic Programming Problem 
# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top of the staircase.

# I think that this problem is asking us to find out how many different ways can we incremement by 1 or 2 to reach n set of stairs
# To implement this we can Memoization to avoid unnessecary work 

def climbStairs(n):
    one, two = 1, 1 # initially our incrementors are both set to one

    for i in range (n -1): # we traverse n -1
        tmp = one
        one = one + two
        two = tmp
    return one

print(climbStairs(5))