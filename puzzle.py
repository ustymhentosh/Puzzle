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


def validate_rows(board):
    pass





def validate_columns(board):
    pass



def validate_colour(board):
    for i in range(5):
        # print(i)
        if not validate_one_colour(board, i):
            return False
    return True




def validate_board(board):
    pass
