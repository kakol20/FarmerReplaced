def startMaze(size, treasure):
	clear()
	plant(Entities.Bush)
	 
	while get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
		use_item(Items.Weird_Substance, size * num_unlocked(Unlocks.Mazes))
			
	treasure = solveMaze(size, treasure)
	return treasure
		
def solveMaze(size, treasure):
	if treasure == None:
		treasure = firstSolve()
	else:
		treasure = firstSolve()
		#treasure = secondSolve(treasure)
	
	return treasure
	
def firstSolve():
	facing = 0
	directions = [North, East, South, West]
	
	while get_entity_type() != Entities.Treasure:
		x = get_pos_x()
		y = get_pos_y()
		
		move(directions[facing % 4])
		
		facing += 1
		if x == get_pos_x() and y == get_pos_y():
			facing += 2
	
	#quick_print(measure())
	treasure = measure()
	harvest()
	return treasure

# A* Pathfinding
def secondSolve(treasure):
	dir = [North, East, South, West]
	opDir = [South, West, North, East]
	
	open = [] # the set of squares to be evaluated
	closed = [] # the set squars alread evaluated
	
	startPos = (get_pos_x(), get_pos_y())
	#startH = abs(treasure[0] - get_pos_x()) + abs(treasure[1] - get_pos_y())
	startH = distance(startPos, treasure)
	
	open.append({
		"pos": startPos,
		"g": 0,
		"h": startH,
		"f": startH,
		"parent": {"pos": startPos}
	})
	
	while True:
		lowestOpen = 0
		lowestF = open[0]["f"]
		for i in range(1, len(open), 1):
			if open[i]["f"] < lowestF:
				lowestF = open[i]["f"]
				lowestOpen = i
		current = open[lowestOpen]
		open.pop(lowestOpen)
		closed.append(current)
		
		gotoNode(current, closed)
		
		if get_entity_type() == Entities.Treasure: # path has been found
			treasure = measure()
			harvest()
			return treasure
		
		for d in range(len(dir)):
			if move(dir[d]): # is traversable
				nPos = (get_pos_x(), get_pos_y())
				nG = current["g"] + 1
				#nG = distance(nPos, closed[0]["pos"])
				nH = distance(nPos, treasure)
				neighbour = {
					"pos": nPos,
					"g": nG,
					"h": nH,
					"f": nH + nG,
					"parent": current
				}
				move(opDir[d])
				checkClosed = checkNeighbour(neighbour["pos"], closed)
				if not checkClosed[0]: # neighbour is not in closed
					checkOpen = checkNeighbour(neighbour["pos"], open)
					
					if checkOpen[0]: # is in open set
						if neighbour["f"] < open[checkOpen[1]]["f"]: # new path to neighbour is short
							open[checkOpen[1]] = neighbour
					else: # is not in open set
						open.append(neighbour)
	
def checkNeighbour(neighbourPos, nodeSet): # checks if neighbour in open/closed set
	for i in range(len(nodeSet)):
		if nodeSet[i]["pos"] == neighbourPos:
			return [True, i]
	return [False, 0]
	
def gotoNode(node, closed):
	currentPos = (get_pos_x(), get_pos_y())
	
	if currentPos == node["parent"]["pos"]:
		goto(node["pos"][0], node["pos"][1])
		return

	toNodePath = []
	backtrack = []
	
	# fill toNodePath
	tempNode = node
	toNodePath.append(node)
	while True:
		toAppend = tempNode["parent"]
		toNodePath.append(toAppend)
		
		tempNode = toAppend
		
		if toAppend["pos"] == tempNode["parent"]["pos"]:
			break
		
	# fill backtrack
	tempIndex = checkNeighbour(currentPos, closed)[1]
	tempNode = closed[tempIndex]
	while True:
		toAppend = tempNode["parent"]
		backtrack.append(toAppend)
		
		tempNode = toAppend
		
		if toAppend["pos"] == tempNode["parent"]["pos"]:
			break

	tempI = 0
	startI = len(toNodePath) - 1
	endWhile = False
	while not endWhile:
		for i in range(len(toNodePath)):
			if backtrack[tempI]["pos"] == toNodePath[i]["pos"]:
				startI = i
				i = len(toNodePath)
				endWhile = True
		goto(backtrack[tempI]["pos"][0], backtrack[tempI]["pos"][1])
		tempI += 1
	
	for i in range(startI, -1, -1):
		goto(toNodePath[i]["pos"][0], toNodePath[i]["pos"][1])