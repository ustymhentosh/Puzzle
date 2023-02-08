# Puzzle


def validate_row(board):
    """
    Check rows
    >>> validate_row(["**** ****","***1 ****","**  3****","* 4 1****","     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    
    
    a = []
    for line in board:
        for x, j in enumerate (line):
            if j != '*' and j != ' ':
                a.append(j)
                
            for i in range(len(a)-1):
                for j in range(i+1, len(a)):
                    if a[i] ==a[j]:
                        return False
        a = []
    return True





def validate_columns(board):
  pass





def validate_colour(board):
  pass





def validate_board(board):
  pass
