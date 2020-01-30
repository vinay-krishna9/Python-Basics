def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def win_check(board, mark):
    return ( (board[1]==board[2]==board[3]==mark)or
             (board[4]==board[5]==board[6]==mark)or
             (board[7]==board[8]==board[9]==mark)or
             (board[1]==board[4]==board[7]==mark)or
             (board[2]==board[5]==board[8]==mark)or
             (board[3]==board[6]==board[9]==mark)or
             (board[1]==board[5]==board[9]==mark)or
             (board[3]==board[5]==board[7]==mark) )


def player_marker(board, marker):
    check = win_check(board, marker)

    if not check:
        pos = int(input('Where do you want to place your marker: '))
        board[pos] = marker
        display_board(board)
        player_marker(board,marker)
    else:
        print('Congratulations!')


# Starting board
start_board = ['']*10
display_board(start_board)

# Ask player to select X or O
p1, p2 = player_input()
print(p1, p2)

# Ask player input
player_marker(start_board, p1)






