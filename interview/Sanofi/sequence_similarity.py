"""
Implementing Sequence similarity by Dynamic Programming. 

The input give you the formular and the example, see the details in here:


https://levelup.gitconnected.com/dynamic-programming-for-sequence-similarity-ccc26472912e

Solution provided by chatGPT(need to do it by yourself):

def solution(source, target, ins_cost, del_cost, rep_cost):
    m = len(source)
    n = len(target)

    # Initialize a matrix to store the distances
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the matrix
    for i in range(m + 1):
        dp[i][0] = i * del_cost
    for j in range(n + 1):
        dp[0][j] = j * ins_cost

    # Fill in the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = rep_cost
            dp[i][j] = min(dp[i - 1][j] + del_cost, dp[i][j - 1] + ins_cost, dp[i - 1][j - 1] + cost)

    return dp[m][n]

# Example usage
source = "kitten"
target = "sitting"
ins_cost = 1
del_cost = 1
rep_cost = 2

result = solution(source, target, ins_cost, del_cost, rep_cost)
print(result)


"""


def solution(source, target, ins_cost, del_cost, rep_cost):
    return




