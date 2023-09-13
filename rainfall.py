def compute_average(n, arr):
    sum = 0
    valid_day = 0
    for i in range(n):
        if arr[i] >= 0:
            sum += arr[i]
            valid_day += 1

    if valid_day == 0:
       return "INSUFFICIENT DATA"
    else:
       return int(sum/valid_day)

num = int(input())
days = list(map(int, input().split()))

if compute_average(num,days) == -1:
    print("INSUFFICIENT DATA")
else:
    print (compute_average(num,days))