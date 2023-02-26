T = int(input())
for tc in range(T):
    N, M = map(int, input().split())  # 화덕크기 N, 피자 개수 M
    Ci = list(map(int, input().split()))
    Ci_num = list(enumerate(Ci, start=1))
    oven = []  # 화덕 크기만큼 받아줌

    for i in range(N):  # 처음 빈 화덕에 넣어주기
        oven.append(Ci_num.pop(0))

    while oven:
        if oven:
            num, ch = oven.pop(0)
            ch = ch // 2
            if ch != 0:
                oven.append((num, ch))
            else:  # 0이면
                if Ci_num:
                    oven.append(Ci_num.pop(0))

    print(f"#{tc + 1}", num)