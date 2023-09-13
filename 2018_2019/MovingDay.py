def is_big_enough(num, target, boxes):

    biggest_volumn = 0 
    biggest_index = 0 

    for i in range(num):
        volumn = boxes[i][0] * boxes[i][1] * boxes[i][2]
        if volumn >= biggest_volumn:
            biggest_volumn = volumn
            biggest_index = i

    return  (boxes[biggest_index][0] * boxes[biggest_index][1] * boxes[biggest_index][2]) - target


num, target = map(int, input().split())

boxes = []

for _ in range(num):
    row = list(map(int, input().split()))
    boxes.append(row)

print(is_big_enough(num, target, boxes))
