T = int(input())
for tc in range(T):
    people = list(map(int,input()))
    people_l = (len(people))
    cnt = people[0]  #일어난 사람
    need = 0
    for i in range(1,people_l):
        if people[i] != 0 and i > cnt:
            need += i - cnt
            cnt = i
        cnt += people[i]
    print(f"#{tc+1}",need)

