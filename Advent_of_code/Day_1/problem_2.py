

def load_input(file):
    # Open the file in read mode ('r')
    lines = []
    with open(file, 'r') as file:
        # Read all lines and store them in a list
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines


def standardize_digit_line(line, dict_digit):
    """
    Convert line to new line with all digit in number format in one way
    """
    stack = ""
    for c in line:
        stack = stack + c
        for key in dict_digit.keys():
            if key in stack :
                stack = stack.replace(key, dict_digit[key])
    return stack


def sum_line_two_pointer(line):
    left, right = 0, len(line) - 1
    two_digit = 0
    while left <= right:
        if line[left].isdigit():
            # stat looking for digit from the right
            while True:
                if line[right].isdigit():
                    two_digit = int(line[left] + line[right]) 
                    return two_digit
                else:
                    right-=1
        else:
            left+=1
    return two_digit


def main():
    input = "input.txt"
    dict_digit = {
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    


    lines = load_input(input)
    sum = 0
    for line in lines:
        standard_line = standardize_digit_line(line, dict_digit)
        # right_digit_line = standardize_digit_line(left_digit_line[::-1], dict_digit)
        # standard_line = right_digit_line[::-1]
        sum += sum_line_two_pointer(standard_line)
    print(sum)



if __name__ == "__main__":
    main()