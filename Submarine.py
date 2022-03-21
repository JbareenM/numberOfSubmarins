import numpy as np

"""
numberOfSubmarines
Parameters:
    seaArr: is a Matrix that contains a Submarine that shows by 'X'
The function count the number of submarines inside the matrix.
every submarine is in shape (N*M).
"""


def numberOfSubmarines(seaArr):
    counter = 0  # start the counter with 0 as a value
    for i in range(0, len(seaArr)):  # loop for the rows
        for j in range(0, len(seaArr[0])):  # loop for the columns
            if seaArr[i][j] == 'X':  # check if the value equals to 'X'
                if i > 0 and seaArr[i - 1][j] == 'X':
                    # if the row is not the first row and the upper square is 'X' it mean it belongs to another submarine
                    continue
                if j > 0 and seaArr[i][j - 1] == 'X':
                    # if the column is not the first one and the left square is 'X' it mean it belongs to another submarine
                    continue
                counter = counter + 1
                # if (i == 0 or seaArr[i - 1][j] != 'X') and (j == 0 or seaArr[i][j - 1] != 'X'):
                #     # check the borders if the 'X' value contains to another submarine or it's a new Submarine
                #     # if it's a border is a water (empty value or 0) so it's referred to new submarine start
                #     counter = counter + 1
    return counter


"""
numberOfSubmarines_withModify_inMatrix
Parameters:
    seaArr: is a Matrix that contains a Submarine that shows by 'X'
The function count the number of submarines inside the matrix.
every submarine is in shape (N*M).
"""


def numberOfSubmarines_withModify_inMatrix(seaArr):
    seaSubmarines_copy = seaArr.copy()  # copy the matrix because it will change the values of the input
    counter = 0  # start the counter with 0 as a value
    for i in range(0, len(seaSubmarines_copy)):  # loop for the rows
        for j in range(0, len(seaSubmarines_copy[0])):  # loop for the columns
            if seaSubmarines_copy[i][j] == 'X':  # check if the value equals to 'X'
                counter = counter + 1
                modifyMatrix(seaSubmarines_copy, i, j)
    return counter


def modifyMatrix(seaArr, i, j):
    if i < 0 or i >= len(seaArr) or j < 0 or j >= len(seaArr[0]) or seaArr[i][j] != 'X':
        return
    seaArr[i, j] = ' '
    modifyMatrix(seaArr, i + 1, j)
    modifyMatrix(seaArr, i, j + 1)


if __name__ == "__main__":
    seaSubmarines = np.array(
        [['X', 'X', 'X', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', 'X', ' ', ' '],
         [' ', ' ', ' ', ' ', 'X', ' ', 'X'],
         [' ', ' ', ' ', ' ', 'X', ' ', ' '],
         ['X', 'X', 'X', ' ', ' ', ' ', ' '],
         ['X', 'X', 'X', ' ', ' ', ' ', ' '],
         ['X', 'X', 'X', ' ', ' ', ' ', ' ']])
    print('the sea matrix is: \n', seaSubmarines, '\nThe number of Submarines is:', numberOfSubmarines(seaSubmarines))
    print('the sea matrix is: \n', seaSubmarines, '\nThe number of Submarines is:',
          numberOfSubmarines_withModify_inMatrix(seaSubmarines))
