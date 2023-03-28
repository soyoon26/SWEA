T = int(input())

for tc in range(T):
    card_lst = list(map(int,input().split()))
    p1 = []
    p2 = []
    answer = 0
    def solve(lst,ans):
        global answer, flag
        if j+2 < len(lst):
            if lst[j] == lst[j + 1] and lst[j] == lst[j + 2]:
                answer = ans
                flag = 1

            elif lst[j] + 1 == lst[j + 1] and lst[j] + 2 == lst[j + 2]:
                answer = ans
                flag = 1
        if j+3 < len(lst):
            if lst[j] + 1 == lst[j + 1] and lst[j] + 2 == lst[j + 3]:
                answer = ans
                flag = 1

    flag = 0
    for i in range(6): #0,1,2,3,4,5
        p1.append(card_lst[i*2])  #0,2,4,6,8,10
        p1.sort()
        for j in range(len(p1)):
            solve(p1,1)
        if flag == 1:
            break
        p2.append(card_lst[(i*2)+1])    #1,3,5,7,9,11
        p2.sort()
        for j in range(len(p2)):
           solve(p2,2)
        if flag == 1:
            break

    print(f"#{tc+1} {answer}")

    #1223일 경우 반례