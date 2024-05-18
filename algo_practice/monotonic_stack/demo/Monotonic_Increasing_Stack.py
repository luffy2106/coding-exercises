"""
Question :
Given the array, take a subset of that array such as all element in that subset is on increasing/decreasing order. Do it with the
complexity O(N)
"""



def monotonic_increasing(nums):
    stack_increase = []
    # result = []

    for num in nums:
        while len(stack_increase)>0  and stack_increase[-1] > num:
            stack_increase.pop()
        stack_increase.append(num)

    return stack_increase


def monotonic_decreasing(nums):
    stack_increase = []
    # result = []

    for num in nums:
        while len(stack_increase)>0  and stack_increase[-1] < num:
            stack_increase.pop()
        stack_increase.append(num)

    return stack_increase





# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6]
result_monotonic_increasing = monotonic_increasing(nums)
result_monotonic_decreasing = monotonic_decreasing(nums)
print("Monotonic increasing stack:", result_monotonic_increasing)
print("Monotonic decreasing stack:", result_monotonic_decreasing)