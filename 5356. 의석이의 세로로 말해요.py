T = int(input())
for tc in range(T):
    board = []
    max = 0
    for i in range(5):
        board.append(list(input()))
        if max < len(board[i]):
            max = len(board[i])
    for i in range(5):
        if len(board[i]) < max:
            board[i] += ['empty']*(max-len(board[i]))

    board_t = list(map(list,zip(*board)))
    print(f"#{tc+1}", end=' ')
    for i in range(max):
        for j in range(5):
            if board_t[i][j] != 'empty':
                print(board_t[i][j],end = '')
    print()
