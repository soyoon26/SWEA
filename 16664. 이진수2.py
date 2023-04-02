T= int(input())
for tc in range(T):
    N = float(input())
    def sol(N):
        ans=[]
        for i in range(1,13):
            while N :
                if (1/2)**i <= N:
                    N = N-((1/2)**i)
                    ans+=[1]
                else:
                    ans+=[0]
                break
        if N == 0:
            print(f'#{tc+1} ',*ans,sep='')
        else:
            print(f'#{tc+1} overflow')
    sol(N)
