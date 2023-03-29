T = int(input())
for tc in range(T):
    time_lst = []
    possible = []
    N = int(input()) #신청서
    for i in range(N):
        time_lst.append(list(map(int,input().split())))    #작업시간, 종료시간

    time_lst.sort(key=lambda x: x[1])
    possible.append(time_lst.pop(0))

    for i in range(N):
        try:
            if possible[-1][1] <= time_lst[i][0]:
                possible.append(time_lst[i])
            else:
                pass
        except:
            pass
    print(f'#{tc+1} {len(possible)}')