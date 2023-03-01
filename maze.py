def createMaze():
	repeat = True
	while repeat:
		clear()
		plant(Entities.Bush)
		useFertilizer()
		repeat = findTreasure()


def findTreasure():
	if not is_over(Entities.Hedge):
        return True

    visited = []
    route = [[0, 0]]

    while True:
        if is_over(Entities.Treasure):
            harvest()
            break

        currX = get_pos_x()
        currY = get_pos_y()
        pos = [currX, currY]
        branches = getBranching()
        moved = False
        found_unvisited = False

        for dir in branches:
            dirpos = dir[1]
            visitedContains = False
            routeContains = False

            for p in route:
                if p[0] == dirpos[0] and p[1] == dirpos[1]:
                    routeContains = True

            for p in visited:
                if p[0] == dirpos[0] and p[1] == dirpos[1]:
                    visitedContains = True

            if not visitedContains and not routeContains:
                move(dir[0])
                route.append(pos)
                moved = True
                break

            if not moved:
                for dir in branches:
                    dirpos = dir[1]
                    visitedContains = False
                    routeContains = False

                    for p in route:
                        if p[0] == dirpos[0] and p[1] == dirpos[1]:
                            routeContains = True

                    for p in visited:
                        if p[0] == dirpos[0] and p[1] == dirpos[1]:
                            visitedContains = True

                    if not visitedContains and not routeContains:
                        found_unvisited = True
                        break

                if not found_unvisited:
	                a = route.pop()
	                visited.append(pos)
	                backtrack(a, currX, currY)
					
	return False

def getBranching():
    directions = [North, East, South, West]
    branching = []
    ind = 0
    for direction in directions:
        initX = get_pos_x()
        initY = get_pos_y()
        move(direction)
        newX = get_pos_x()
        newY = get_pos_y()
        wall = initX == newX and initY == newY
        if not wall:
            backInd = ind
            if ind >= 2:
                backInd -= 2
            else:
                backInd += 2
            move(directions[backInd])
            branching.append([direction, [newX, newY]])
        ind += 1
    return branching

def backtrack(route, x, y):
	if x > route[0]:
		move(West)
	elif x < route[0]:
		move(East)
	elif y > route[1]:
		move(South)
	elif y < route[1]:
		move(North)