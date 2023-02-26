T = int(input())
for tc in range(T):
    N = int(input())
    price = list(map(int,input().split()))
    stack = [price[-1]]
    sum = 0

    for i in range(N-1,-1,-1):
        if price[i] < stack[-1]:
            sum += (stack[-1]-price[i])
        if price[i] > stack[-1]:
            stack.pop()
            stack.append(price[i])
    print(f"#{tc+1}",sum)








