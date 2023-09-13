def batter_up(hit, scores):
    valid_hit = 0 
    total = 0 
    for i in range(hit):
        if scores[i] != -1:
            valid_hit += 1 
            total += scores[i]

    return total/valid_hit

hit = int(input())

scores = list(map(int, input().split()))
print(batter_up(hit, scores))