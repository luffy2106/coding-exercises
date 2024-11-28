

def remaining_leaves_chatGPT(width: int, height: int, leaves: list, winds: str) -> int:
    """  
    This is the solution from chatGPT and it's wrong
    """
    for wind in winds:
        if wind == 'U':  # Up
            for col in range(width):
                for row in range(1, height):
                    leaves[row - 1][col] += leaves[row][col]
                    leaves[row][col] = 0
        elif wind == 'D':  # Down
            for col in range(width):
                for row in range(height - 2, -1, -1):
                    leaves[row + 1][col] += leaves[row][col]
                    leaves[row][col] = 0
        elif wind == 'L':  # Left
            for row in range(height):
                for col in range(1, width):
                    leaves[row][col - 1] += leaves[row][col]
                    leaves[row][col] = 0
        elif wind == 'R':  # Right
            for row in range(height):
                for col in range(width - 2, -1, -1):
                    leaves[row][col + 1] += leaves[row][col]
                    leaves[row][col] = 0

    # Calculate the total remaining leaves
    remaining = sum(sum(row) for row in leaves)
    return remaining



def remaining_leaves(width, height, leaves, winds):
    """
    Solution come up after 40 minutes, while required time is 20 minutes. Pay attention to the following things :
    - pay attention to how matrix change, it will be row by row and col by col
    - pay attention to how range(height-1,-1,-1) work : start :height-1, end : 0, step = -1
    """
    for wind in winds:
        if wind == "U":
            for row in range(height):
                for col in range(width):
                    if row < height -1:
                        leaves[row][col] = leaves[row+1][col]
                    else:
                        leaves[row][col] = 0
        elif wind == "D":
            for row in range(height-1,-1,-1):
                for col in range(width):
                    if row > 0:
                        leaves[row][col] = leaves[row-1][col]
                    else:
                        leaves[row][col] = 0
        elif wind == "R":
            for row in range(height):
                for col in range(width-1,-1,-1):
                    if col > 0:
                        leaves[row][col] = leaves[row][col-1]
                    else :
                        leaves[row][col] = 0
        elif wind == "L":
            for row in range(height):
                for col in range(width):
                    if col < width - 1:
                        leaves[row][col] = leaves[row][col+1]
                    else :
                        leaves[row][col] = 0
                        

    remaining = sum(sum(row) for row in leaves)
                
    return remaining





width = 4
height = 4
leaves = [
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 1, 1],
    [0, 2, 3, 0]
]
winds = "RRD"

print(remaining_leaves(width, height, leaves, winds))
# expected output = 1