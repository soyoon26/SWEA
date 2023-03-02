T = int(input())
for tc in range(T):
    N = int(input())
    board = [[i for i in input()]for _ in range(N)]
    ans = "NO"
    di = [0,1,1,1]
    dj = [1,-1,0,1]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for k in range(4):
                    dx = i + di[k]
                    dy = j + dj[k]
                    if 0 <= dx < N and 0 <= dy < N: #범위를 벗어나지 않을 때
                        if board[dx][dy] == 'o':
                            cnt = 1
                            for l in range(1,5): #오목이니까 다음 2,3,4,5를 탐색하기 위해서
                                lx = i + di[k]*l #k는 위에 쓰인 k랑 같으니까
                                ly = j + dj[k]*l
                                if 0 <= lx < N and 0 <= ly < N:
                                    if board[lx][ly] == 'o':
                                        cnt += 1
                                    else:
                                        cnt = 0
                            if cnt >= 5:
                                ans = "YES"
                                break

    print(f"#{tc+1}",ans)


