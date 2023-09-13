def hailstones(num):
    sum = 0
    if num == 1:
        sum += 1 
    elif num % 2 == 0: 
        sum += hailstones(num/2) + num
    else:
        sum += hailstones(3*num + 1) + num

    return int(sum)

n =  int(input())

result = hailstones(n)

print(result)