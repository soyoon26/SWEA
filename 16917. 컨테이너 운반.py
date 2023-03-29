T = int(input())
#옮겨진 화물의 전체 무게
for tc in range(T):
    N, M = map(int,input().split())   #컨테이너, 트럭
    w_lst = [int(i) for i in input().split()]
    truck = [int(i) for i in input().split()]

    w_lst.sort(reverse=True)
    truck.sort(reverse=True)
    sum = 0
    for i in range(N):
        M = len(w_lst)
        for j in range(M):
            try:
                if truck[i] >= w_lst[j]:
                    sum += w_lst[j]
                    w_lst.pop(j)
                    break
                else :
                    pass
            except : pass

    print(f'#{tc+1} {sum}')
