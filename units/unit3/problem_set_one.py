# Problem 1 take a list of strings and return the sum of these strings as an int
def sum_of_str (nums):
    sumo = 0
    for num in nums:
        sumo += int(num)
    return sumo
    # # return sum(int(nums) for num in nums)
    # return (sum(map(int, nums)))

print (sum_of_str(['111', '223', '332']))

# problem 2 remove duplicates of numbers

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
print(remove_duplicates([1, 2, 2, 2, 3, 4, 5]))



# problem 3 reverse a chars in a string s, but keep all non letter chars in place

def reverse(s):
    # extract letters andsd reverse them
    letters = [c for c in s if c.isalpha()][::-1]
    
    result = []
    # traverse s and find all non letter chars
    for char in s:
        if char.isalpha():
            result.append(letters.pop(0)) # reversed letter
        else:
            result.append(char) # non letter char 
    return ''.join(result)

print(reverse('a-bC-dEf-ghIj'))