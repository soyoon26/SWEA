T = int(input())
for tc in range(T):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]

    for i in range(E):
        f, t = map(int,input().split())
        graph[f].append(t)
        graph[t].append(f)

    S, G = map(int,input().split())
    visited = [S] #중복방지, 다녀온 곳
    queue = [[S,0]] #0은 지나갈 선 수
    ans = 0
    while queue:
        S,cnt = queue.pop(0)
        for i in graph[S]:
            if i not in visited:
                queue.append([i,cnt+1])
        visited += graph[S] #다녀온 노드 표시
        if S == G:
            ans = cnt

    print(f"#{tc+1}",ans)


