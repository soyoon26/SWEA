T= int(input())
for tc in range(T):
    N = int(input())
    sheep = []
    num = 0
    while len(sheep) < 10:
        sheep = list(sheep)
        num += 1
        sheep += list(str(N*num))
        sheep = set(sheep)
    print(f"#{tc+1}",num*N)