
T = int(input())
for tc in range(T):
    N, input_num = input().split()
    lst16 = ['A','B','C','D','E','F']
    ans = []

    def sol(num):
        global ans
        answer = []
        while num:
            a = int(num % 2)
            answer += [a]
            num = num//2
        answer = answer[::-1]
        if len(answer) <= 3:
            answer = [0]*(4-len(answer))+answer
        ans+=answer



    for i in input_num:
        try:
            i = int(i)
            sol(i)
        except:
            for j in range(6):
                if i == lst16[j]:
                    sol(j+10)

    print(f'#{tc+1} ',*ans,sep='')