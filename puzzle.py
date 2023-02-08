# Puzzle


def validate_rows(board):
  pass





def validate_columns(board):
    """
    Checks columns
    >>> validate_columns(["**** ****", "***1 ****", "**  3****", "* 4 1****","     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for i in range (9):
        newstring=""
        for k in range(9):
            if board[k][i]!=' ' or board[k][i]!='*':
                newstring+=board[k][i]
        for k in range(1,10):
            if newstring.count(str(k))>1:
                return False
    return True





def validate_colour(board):
  pass





def validate_board(board):
  pass
