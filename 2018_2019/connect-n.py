def connect_n(x, y, n, arr):
    for i in range(x):
        for j in range(y):

            found_n = False
            head = arr[i][j]

            if head != "O":

                # check down 
                if i+n-1 < x: # check i+n exsit 
                    consecutive = True
                    for k in range(n):
                        consecutive = consecutive & (head == arr[i+k][j])
                    if consecutive:
                        found_n = True

                # check diagonal - bottom right 
                if i+n-1 < x  and j+n-1 <  y: # check i+n exsit 
                    consecutive = True
                    for k in range(n):
                        consecutive = consecutive & (head == arr[i+k][j+k])
                    if consecutive:
                        found_n = True

                # check diagonal - bottom left 
                if i + n - 1 < x and j - n + 1 >= 0:  # check i+n exists and j-n doesn't go out of bounds

                    consecutive = True
                    for k in range(n):
                        consecutive = consecutive & (head == arr[i+k][j-k])
                    if consecutive:
                        found_n = True

                # check right  
                if j+n-1 <  y: # check i+n exsit 
                    consecutive = True
                    for k in range(n):
                        consecutive = consecutive & (head == arr[i][j+k])
                    if consecutive:
                        found_n = True

            if found_n:
                return arr[i][j]
    return None

x, y, n = map(int, input().split())

board = []
for _ in range(x):
    row = list(input().split())
    board.append(row)

result = connect_n(x, y, n, board)

if result == None:
    print("None") 
elif result =="B":
    print("BLUE WINS")
else: 
    print("RED WINS")
