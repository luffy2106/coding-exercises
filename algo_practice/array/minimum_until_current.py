
"""
Question :
For each number in the list, find the minimum/maximum of each number until current number.
Ex : nums = [3,1,4,2]
=> 
min_until_current = [3, 1, 1, 1]
max_until_current = [3, 3, 4, 4] 

The complexity:
- Since we use only one loop, so the complexity is O(n)
"""





def find_minimum_until_current(nums):
    """For each number in the list, find the minimum of each number until current number

    Args:
        nums (list): list of numbers

    Returns:
        list: list of element where each element is the minimum until this current number
    """
    
    min_so_far = float('inf')
    result = []
    for num in nums:
        min_so_far = min(min_so_far, num)
        result.append(min_so_far)

    return result

def find_maximum_until_current(nums):
    """For each number in the list, find the minimum of each number until current number

    Args:
        nums (list): list of numbers

    Returns:
        list: list of element where each element is the minimum until this current number
    """
    
    min_so_far = -float('inf')
    result = []
    for num in nums:
        min_so_far = max(min_so_far, num)
        result.append(min_so_far)

    return result


nums = [3,1,4,2]
print(find_minimum_until_current(nums))
print(find_maximum_until_current(nums))