from pprint import pprint
T = int(input())
for tc in range(T):
    board = []
    len_lst = []
    for i in range(5):
        board.append(list(input()))
        len_lst.append(len(board[i]))
    max_len = max(len_lst)

    for i in range(5):
        if max_len - len_lst[i] > 0:
            for j in range(max_len - len_lst[i]):
                board[i] +=['empty']

    board_1 = list(map(list,zip(*board)))

    # for i in range(max_len):
        # for j in range(5):
            # if board_1[i][j] != 'empty':
                # print(board_1[i][j],end='')
    ans = []
    for i in range(max_len):
        for j in range(5):
            if board[j][i] != 'empty':
                ans += (board[j][i])
    print(f'#{tc+1}',''.join(ans))