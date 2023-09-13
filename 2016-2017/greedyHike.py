def greedyHike(X, Y, x_s, y_s, graph):

    elevation_change = 0 

    while x_s + 1 != X:
        current_ele = graph[x_s][y_s]        
        right_ele_change = abs(graph[x_s + 1][y_s] - current_ele)
        if y_s - 1 >= 0:
            up_ele_change = abs(graph[x_s + 1][y_s - 1])
        if y_s + 1 < Y:
            down_ele_change = abs(graph[x_s + 1][y_s + 1])
        
        min_change = up_ele_change
        min_pos = (x_s + 1, y_s - 1)
        if down_ele_change < up_ele_change:
            min_change = down_ele_change
            min_pos = (x_s + 1, y_s + 1)
        if right_ele_change < down_ele_change:
            min_change = right_ele_change
            min_pos = (x_s + 1, y_s)
        
        elevation_change += min_change
        
        #update pos
        x_s = min_pos[0]
        y_s = min_pos[1]

    return x_s, y_s, elevation_change




X, Y = map(int, input().split())
x_s, y_s = map(int, input().split())

graph = []

for _ in range(X):
    graph.append(list(map(int, input().split())))

result = greedyHike(X, Y, x_s, y_s, graph)

print(" ".join(map(str, result)))