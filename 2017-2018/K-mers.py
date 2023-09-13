def k_mer(L, N, k, Q, line, patterns):
    
    pattern_dict = {pattern: 0 for pattern in patterns}

    window = line[:k]

    for i in range(Q):
        if window in patterns:
            pattern_dict[window] += 1 
        if i + k < N:
            window = window[1:] + line[i + k]
    return pattern_dict

L, N, k, Q = map(int, input().split())

line = ""
for i in range(L):
    line += input()

patterns  =  []
for row in range(Q):
    patterns .append(input())

result = k_mer(L, N, k, Q, line, patterns)

for pattern in patterns:
    print(pattern, " ", result[pattern])

# Takeaway:
# Substring operation is expensive, especially for long strings. It is often 
# better to slide the window and make minor adjustment on the subscript 