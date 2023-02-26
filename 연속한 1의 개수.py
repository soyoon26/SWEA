T = int(input())
for tc in range(T):
    N = int(input())  #수열 길이
    nums = list(map(int,input()))
    max_lst = []
    cnt = 0
    for i in range(N-1):
        if nums[i] == 1:
            if nums[i] == nums[i+1]:
                cnt += 1
                if i == N-2:
                    max_lst.append(cnt+1)
            elif nums[i] != nums[i+1]:
                max_lst.append(cnt+1)
                cnt = 0
    print(f"#{tc+1}",max(max_lst))

