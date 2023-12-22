"""

--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

"""

import numpy as np

def load_input(file):
    # Open the file in read mode ('r')
    lines = []
    with open(file, 'r') as file:
        # Read all lines and store them in a list
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = [[c for c in line] for line in lines]
    return lines


def check_symbol(c):
    if c == "*":
        return True
    else: 
        return False
    
def check_char_near_symbol(matrix, i, j):
    try:
        # check left 
        if check_symbol(matrix[i][j-1]):
            pos_i, pos_j = i, j-1
            return True, pos_i, pos_j
    except:
        print("this is the outliner")

    try:
        # check left top
        if check_symbol(matrix[i+1][j-1]):
            pos_i, pos_j = i+1, j-1
            return True, pos_i, pos_j
    except:
        print("this is the outliner")

    try:
        # check top
        if check_symbol(matrix[i+1][j]):
            pos_i, pos_j = i+1, j
            return True, pos_i, pos_j
    except:
        print("this is the outliner")

    try:
        # check top right
        if check_symbol(matrix[i+1][j+1]):
            pos_i, pos_j = i+1, j+1
            return True, pos_i, pos_j
    except:
        print("this is the outliner")

    try:
        # check right 
        if check_symbol(matrix[i][j+1]):
            pos_i, pos_j = i, j+1
            return True, pos_i, pos_j
    except:
        print("this is the outliner")

    try:
        # check bottom right 
        if check_symbol(matrix[i-1][j+1]):
            pos_i, pos_j = i-1, j+1
            return True, pos_i, pos_j
    except:
        print("this is the outliner")

    try:
        # check bottom  
        if check_symbol(matrix[i-1][j]):
            pos_i, pos_j = i-1, j
            return True, pos_i, pos_j
    except:
        print("this is the outliner")

    try:
        # check bottom left  
        if check_symbol(matrix[i-1][j-1]):
            pos_i, pos_j = i-1, j-1
            return True, pos_i, pos_j
    except:
        print("this is the outliner")

    return False, 0, 0


def calculate_sum(matrix):
    stack = []
    validate_stack = False
    list_symbol = []
    dict_symbol = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit():
                stack.append(matrix[i][j])
                bool_char_near_symbol, pos_i, pos_j = check_char_near_symbol(matrix, i, j) 
                if bool_char_near_symbol:
                    validate_stack = True
                    list_symbol = [stack, str(pos_i)+str(pos_j)]
            else:
                if validate_stack == True:
                    str_stack = "".join([c for c in stack])
                    if str_stack != "":
                        if list_symbol[1] not in dict_symbol.keys():
                            dict_symbol[list_symbol[1]] = []
                            dict_symbol[list_symbol[1]].append(list_symbol[0])
                        else:
                            dict_symbol[list_symbol[1]].append(list_symbol[0])        
                else:
                    validate_stack ==  True
                # empty stack
                stack = []
                # reset validate of stack
                validate_stack = False
    return dict_symbol 

def calculate_dict(dict_matrix):
    sum_dict = 0
    for key in dict_matrix.keys():
        if len(dict_matrix[key]) == 2:
            mul = 1
            for x in dict_matrix[key]:
                int_x = int("".join([c for c in x]))
                mul = mul * int_x
            sum_dict = sum_dict + mul
    return sum_dict


def main():
    # Your main code goes here
    matrix_line = load_input("input.txt")
    matrix_numpy = np.array(matrix_line)
    dict_symbol = calculate_sum(matrix_numpy)
    print(calculate_dict(dict_symbol))

if __name__ == "__main__":
    main()