import copy


def generateParenthesis(n):
    ans = []
    original_str = '()'*n
    original_list = [c for c in original_str]
    ans.append(original_str)
    for i in range(len(original_str)):
        for j in range(i+1, len(original_str)):
            if original_str[i] == ")" and original_str[j] == "(":
                swap_list = copy.deepcopy(original_list)
                swap_list[i], swap_list[j] = swap_list[j], swap_list[i]
                swap_str = "".join(e for e in swap_list)
                ans.append(swap_str)
    return ans


if __name__ == "__main__":
    n = int(input())
    output = generateParenthesis(n)
    output.sort()
    print('["%s"]' % '","'.join(map(str, output)))