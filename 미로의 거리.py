from pprint import pprint
T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int,input()))for _ in range(N)]
    visited = [[0 for i in range(N)] for i in range(N)]


    si = sj = gi= gj = 0 #시작지점 찾기
    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j
                maze[si][sj] = 1 #시작지점 1로 바꾸기
            if maze[i][j] == 3:
                gi = i
                gj = j
            if maze[i][j] == 1:
                visited[i][j] = 1

    q = [[si,sj,-1]] #큐 생성
    di = [0,0,1,-1] #위아래
    dj = [-1,1,0,0] #좌우
    dx_lst = []
    while q:
        ci, cj, cnt = q.pop(0)
        if gi == ci and gj == cj:
            ans = cnt
            break
        for k in range(4):
            dx = ci + di[k]
            dy = cj + dj[k]
            if 0 <= dx < N and 0 <= dy < N:
                if visited[dx][dy] == 0:   # 범위 안에 있고 방문하지 않은 거리라면
                    visited[dx][dy] = 1
                    q.append([dx, dy, cnt+1])


    print(f"#{tc+1}",ans)











