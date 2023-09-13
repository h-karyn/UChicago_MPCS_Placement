def usefulGene(numLine, sequence):
    gene = 0 
    usefulGene = 0 
    for line in sequence:
        for letter in line[0]:
            gene += 1 
            if letter == 'C' or letter == 'G':
                usefulGene += 1 
    return usefulGene/gene * 100

numLine = int(input())

sequence = []

for _ in range(numLine):
    sequence.append(list(input().split()))

print(usefulGene(numLine, sequence))



# 4
# GGGATA
# CCCATA
# AAAAAA
# TTTTTT
