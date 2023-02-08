# Puzzle



def validate_one_colour(board, number_of_column):
    row = list(board[8 - number_of_column][number_of_column + 1 : number_of_column + 5])
    col = [i[number_of_column]  for i in board[: 8 - number_of_column] if i[number_of_column] != '*']
    # print(col, row)
    numbers_list = []
    for i in row:
        if i != ' ':
          numbers_list.append(int(i))
    for j in col:
        if j != ' ':
            numbers_list.append(int(j))
    # print(numbers_list)
    if len(set(numbers_list)) != len(numbers_list):
        return False
    return True


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
    for i in range(5):
        # print(i)
        if not validate_one_colour(board, i):
            return False
    return True



def validate_board(board):
    pass
