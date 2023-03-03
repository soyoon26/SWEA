T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    board = [[int(i) for i in input().split()] for i in range(N)]

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    max = 0
    for i in range(N):
        for j in range(M):
            flower = board[i][j]
            for k in range(4):
                dx = i + di[k]
                dy = j + dj[k]
                if 0 <= dx < N and 0 <= dy < M:
                    flower += board[dx][dy]
            if max < flower :
                max = flower
    print(f'#{tc+1}',max)