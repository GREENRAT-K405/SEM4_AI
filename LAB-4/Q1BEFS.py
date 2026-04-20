

def BeFS(graph, start, goal):   #non heuristic version
    #non heuristic meaning is that no info about city to goal city is given

    open_list = []   # [cost,current_city,path]
    reached = []    # this is same as visited[]

    open_list.append([0, start, [start]])
    reached.append(start)

    explored = 0    #this is to count no. of cities we eill take to reach the end state

    while open_list:   #till it is not empty
        # choose node with smallest cost
        open_list.sort()
        cost, current, path = open_list.pop(0)
        explored += 1

        if current == goal:
            return path, cost, explored

        # find neighbors
        for row in graph:
            if row[0] == current:

                for i in range(1, len(row)):
                    neighbor = row[i][0]
                    step_cost = row[i][1]

                    if neighbor not in reached:
                        reached.append(neighbor)
                        open_list.append([
                            cost + step_cost,
                            neighbor,
                            path + [neighbor]
                        ])

    return None, None, explored


#assignment 1 map
#adjacency list
graph = [
 ["Chicago", ["Detroit",283], ["Cleveland",345], ["Indianapolis",182]],
 ["Detroit", ["Chicago",283], ["Cleveland",169], ["Buffalo",256]],
 ["Cleveland", ["Chicago",345], ["Detroit",169], ["Columbus",144], ["Pittsburgh",134], ["Buffalo",189]],
 ["Indianapolis", ["Chicago",182], ["Columbus",176]],
 ["Columbus", ["Indianapolis",176], ["Cleveland",144], ["Pittsburgh",185]],
 ["Buffalo", ["Detroit",256], ["Cleveland",189], ["Syracuse",150]],
 ["Pittsburgh", ["Cleveland",134], ["Columbus",185], ["Baltimore",247], ["Philadelphia",305], ["Syracuse",215]],
 ["Baltimore", ["Pittsburgh",247], ["Philadelphia",101]],
 ["Philadelphia", ["Baltimore",101], ["Pittsburgh",305], ["New York",97]],
 ["New York", ["Philadelphia",97], ["Providence",181], ["Boston",215], ["Syracuse",254]],
 ["Providence", ["New York",181], ["Boston",50]],
 ["Boston", ["Providence",50], ["New York",215], ["Portland",107]],
 ["Portland", ["Boston",107]],
 ["Syracuse", ["Buffalo",150], ["Pittsburgh",215], ["New York",254], ["Boston",312]]
]

start = "Syracuse"
goal = "Chicago"

path, total_cost, explored = BeFS(graph, start, goal)

print("Best First Path:", path)
print("Total Cost:", total_cost)
print("Nodes Explored:", explored)