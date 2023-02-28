T = 10
for tc in range(T):
    N = int(input())
    board = [[int(i) for i in input().split()]for _ in range(100)]
    # print(board)
    cnt = 0  #스택 마지막부터
    for i in range(100):
        stack = []
        for j in range(100):
            if not stack:
                if board[j][i] == 1:
                    stack.append(board[j][i])

            if stack: #스택
                if board[j][i] == 2:
                    stack.pop()
                    cnt += 1
    print(f"#{tc+1}",cnt)
