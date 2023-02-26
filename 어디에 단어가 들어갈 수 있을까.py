from pprint import pprint
T = int(input())
for tc in range(T):
    N, K = map(int,input().split())  #N*N , 단어 길이 K
    puzzle = [[int(i) for i in input().split()] for _ in range(N)]
    space = 0
    def search(lst):
        global space
        cnt = 0
        for i in range(N):
            for j in range(N-1):
                if lst[i][j] == 1:
                    if lst[i][j+1] == 1:
                        cnt += 1
                        if j+2 == N:
                            if cnt +1 == K:
                                space += 1
                            cnt = 0
                    elif lst[i][j+1] != 1:
                        if cnt +1 == K:
                            space += 1
                        cnt = 0
    puzzle_t = list(map(list,zip(*puzzle)))
    search(puzzle)
    search(puzzle_t)
    print(f"#{tc+1}",space)

