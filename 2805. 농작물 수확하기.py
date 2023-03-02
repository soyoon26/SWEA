from pprint import pprint
T = int(input())
for tc in range(T):
    N = int(input())
    farm = [[int(i) for i in input()]for _ in range(N)]
    sum = 0
    for i in range((N//2)+1):   #중간까지는
        for j in range((N//2)-i,(N//2)+i+1):
            sum += farm[i][j]

    for i in range((N//2)+1,N):
        for j in range((N//2)-N+i+1,(N//2)+N-i):
            sum += farm[i][j]
    print(f"#{tc+1}",sum)