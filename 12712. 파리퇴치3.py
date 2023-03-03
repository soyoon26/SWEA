T = int(input())
for tc in range(T):
    N, M = map(int,input().split()) #N*N배열, M은 화력
    fly_board = [[int(i) for i in input().split()] for _ in range(N)]

    #상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    max_fly = 0
    for i in range(N):
        for j in range(N):
            fly = fly_board[i][j]
            for k in range(4):
                for l in range(1,M):
                    dx = i + di[k]*l
                    dy = j + dj[k]*l
                    if 0 <= dx < N and 0 <= dy < N:
                        fly += fly_board[dx][dy]
            if max_fly < fly:
                max_fly = fly

    #대각선
    dii = [-1,-1,1,1]
    djj = [-1,1,-1,1]
    for i in range(N):
        for j in range(N):
            fly = fly_board[i][j]
            for k in range(4):
                for l in range(1,M):
                    dxx = i + dii[k]*l
                    dyy = j + djj[k]*l
                    if 0 <= dxx < N and 0 <= dyy < N:
                        fly += fly_board[dxx][dyy]
            if max_fly < fly:
                max_fly = fly
    print(f'#{tc+1}',max_fly)
