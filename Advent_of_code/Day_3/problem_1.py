"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?


Solution :

To be able to handle this problem, you need a stack to store the number, and you need to check each char in that number close to a symbol or not

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
    if c.isalnum() or c == ".":
        return False
    else: 
        return True



def check_char_near_symbol(matrix, i, j):
    try:
        # check left 
        if check_symbol(matrix[i][j-1]):
            return True
    except:
        print("this is the outliner")

    try:
        # check left top
        if check_symbol(matrix[i+1][j-1]):
            return True
    except:
        print("this is the outliner")

    try:
        # check top
        if check_symbol(matrix[i+1][j]):
            return True
    except:
        print("this is the outliner")

    try:
        # check top right
        if check_symbol(matrix[i+1][j+1]):
            return True
    except:
        print("this is the outliner")

    try:
        # check right 
        if check_symbol(matrix[i][j+1]):
            return True
    except:
        print("this is the outliner")

    try:
        # check bottom right 
        if check_symbol(matrix[i-1][j+1]):
            return True
    except:
        print("this is the outliner")

    try:
        # check bottom  
        if check_symbol(matrix[i-1][j]):
            return True
    except:
        print("this is the outliner")

    try:
        # check bottom left  
        if check_symbol(matrix[i-1][j-1]):
            return True
    except:
        print("this is the outliner")

    return False

def calculate_sum(matrix):
    sum_matrix = 0
    stack = []
    validate_stack = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].isdigit():
                stack.append(matrix[i][j])
                if check_char_near_symbol(matrix, i, j):
                    validate_stack = True
            else:
                if validate_stack == True:
                    str_stack = "".join([c for c in stack])
                    if str_stack != "":
                        sum_matrix = sum_matrix + int(str_stack)
                else:
                    validate_stack ==  True
                # empty stack
                stack = []
                # reset validate of stack
                validate_stack = False
    return sum_matrix
                

def main():
    # Your main code goes here
    matrix_line = load_input("input.txt")
    matrix_numpy = np.array(matrix_line)
    print(calculate_sum(matrix_numpy))

if __name__ == "__main__":
    main()
