T = int(input())
for tc in range(T):
    N, M, K = map(int,input().split())  # 손님수,M초의 시간 K개의 붕어빵
    arrive = sorted(list(map(int,input().split())))
    ans = "Possible"


                        #2,2,2
    for i in range(N):   #3,4
        fish = ((arrive[i]//M)*K)-i  #도착시에 구워져있는 붕어빵 수
        if fish <= 0 :
            ans = "Impossible"
            break
    print(f"#{tc+1}",ans)