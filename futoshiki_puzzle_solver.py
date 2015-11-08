# futoshiki puzzle solver:

import random


def print_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            print matrix[row][column],
        print ""


def possible_solutions_list(board_size):
    amount = [x for x in range(1, board_size + 1)]
    random.shuffle(amount) # shuffle list to allow potentially quicker solving
    return amount


def check_row(board, row_nr, next_possible):
    for checker in range(len(board)):
        if board[row_nr][checker] == next_possible:
            return False
    return True


def check_column(board, column_nr, next_possible):
    for checker in range(len(board)):
        if board[checker][column_nr] == next_possible:
            return False
    return True


def check_inequality(board, row, column, inequality_dict, next_possible):
    if (row, column) in inequality_dict:
        value_row, value_column = inequality_dict[(row, column)]

        if board[value_row][value_column] == 0:
            # if the other matrix element is 0 we just place next_possible on the board
            return True
        elif next_possible < board[value_row][value_column]:
            return True
        else:
            return False
    return True # no inequality, therefore you can place next_possible on the board


def check_valid(board, next_possible, inequality_dict):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:  # when we find an element containing 0, check if it can be replaced with next_possible.
                if check_row(board, row, next_possible) and check_column(board, column, next_possible) and check_inequality(board, row, column, inequality_dict, next_possible):
                    return True, row, column
                return False, -1, -1


def solve(board, prev_row, prev_column, inequality_dict, board_size):
    global counter
    counter += 1

    for checker in range(len(board)):
        # we are done solving when there are no more 0s (zeros) on the board.
        if not check_row(board, checker, 0) or not check_column(board, checker, 0):
            break
        elif checker == len(board) - 1:
            return True

    for next_possible in possible_solutions_list(board_size):
        next_possible_is_valid, row, column = check_valid(board, next_possible, inequality_dict)

        if next_possible_is_valid:
            board[row][column] = next_possible

            if solve(board, row, column, inequality_dict, board_size):
                return True

    """ 
    when we have gone through all possible numbers and no one worked
    then we remove the previously placed number from the board.
    """

    board[prev_row][prev_column] = 0
    return False


def main():
    print_matrix(board)
    print ""

    solve(board, -1, -1, inequality_dict, board_size)
    
    print_matrix(board)
    print "ran solve():", counter, "times."


counter = 0

board_size = 5
board = [[0 for x in range(board_size)] for y in range(board_size)]
board[0][0] = 2
board[0][2] = 1
board[3][4] = 5
board[4][4] = 1

inequality_dict = {(1, 1): (0, 1), (1, 2): (1, 1), (2, 3): (2, 2), (2, 4): (2, 3), (3, 2): (3, 1)}
#keys and values are matrix coordinates, 
#the integer in the key matrix element has to be less than the integer in the value matrix element.


if __name__ == "__main__":
    main()
