def minesweeper(arr):
    
    x = arr[0]
    y = arr[1]
    original_mtx = arr[2]
    
    result = []
    for i in range(x):
        row = []
        for j in range(y):
            count = 0 
            #check if bomb 
            if original_mtx[i][j] == 1:
                row.append("X")
            else:
                # count 8 cornors 
                if i > 0: #up
                    if original_mtx[i-1][j] == 1:
                        count += 1 
                if i < x-1: #down
                    if original_mtx[i+1][j] == 1:
                        count += 1 
                if j > 0: #left 
                    if original_mtx[i][j-1] == 1:
                        count += 1 
                if j <= y-2: #right 
                    if original_mtx[i][j+1] == 1:
                        count += 1 
                if i > 0 and j > 0: # up-left 
                    if original_mtx[i-1][j-1] == 1:
                        count += 1 
                if i < x-1 and j > 0: # bottom-left 
                    if original_mtx[i+1][j-1] == 1:
                        count += 1 
                if i >0 and j < y-1: # top-right 
                    if original_mtx[i-1][j+1] == 1:
                        count += 1 
                if i < x-1 and j < y-1: # bottom-right 
                    if original_mtx[i+1][j+1] == 1:
                        count += 1      
                if count ==0:
                    row.append("-")
                else:
                    row.append(count)
        result.append(row)
    return result
    
    
# Read the dimensions of the minefield
n, m = map(int, input().split())

# Initialize an empty minefield as a list of lists
minefield = []

# Read each line of the minefield and append it to the minefield list
for _ in range(n):
    row = list(map(int, input().split()))
    minefield.append(row)
    
# Call the minesweeper function and print the result
result = minesweeper([n, m, minefield])
for row in result:
    print("".join(map(str, row)))
