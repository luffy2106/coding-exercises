"""
We will check each rule one by one. Pay attention on how to access row and col from list of list
"""


class Solution:
    def check_row(self, board: List[List[str]]):
        rows = len(board)
        for i in range(rows):
            row_i = board[i][:]
            print(row_i)
            set_row = set()
            for element in row_i:
                if element == ".":
                    continue
                else:
                    if element not in set_row:
                        set_row.add(element)
                    else:
                        print("invalid row")
                        return False
        print("\n")
        return True

    def check_col(self, board: List[List[str]]):
        cols = len(board[0])
        for j in range(cols):
            col_j = [element[j] for element in board]
            print(col_j)
            set_col = set()
            for element in col_j:
                if element == ".":
                    continue
                else:
                    if element not in set_col:
                        set_col.add(element)
                    else:
                        print("invalid col")
                        return False
        return True
    
    def check_box(self, board: List[List[str]]):
        rows = len(board)
        cols = len(board[0])
        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                set_box = set()
                box = [box_row[j:j+3] for box_row in board[i:i+3]] 
                # print(box)
                for i_box in range(len(box)):
                    box_i_box = box[i_box]
                    for j_box in range(len(box_i_box)):
                        if box[i_box][j_box] == ".":
                            continue
                        else:
                            if box[i_box][j_box] not in set_box:
                                set_box.add(box[i_box][j_box])
                            else:
                                print("invalid box at box {}".format(box))
                                return False
        return True




    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.check_box(board) and self.check_row(board) and self.check_col(board):
            return True
        else:
            return False




                    




















