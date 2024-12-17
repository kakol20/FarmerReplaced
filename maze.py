def startMaze(size):
	clear()
	plant(Entities.Bush)
	 
	while get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
		use_item(Items.Weird_Substance, size * num_unlocked(Unlocks.Mazes))
			
	solveMaze()
		
def solveMaze():
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
	harvest()
	
def findTreasure():
	been = []
	path = [[get_pos_x(), get_pos_y()]]
	
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			break
			
		posX = get_pos_x()
		posY = get_pos_y()
		pos = [posX, posY]
		freedom = getBranching()
		moved = False
		
		for direction in freedom:
			dirpos = direction[1]
			pathContains = False
			beenContains = False
			
			for p in path:
				if (p[0] == dirpos[0]) and (p[1] == dirpos[1]):
					pathContains = True
			for p in been:
				if (p[0] == dirpos[0]) and (p[1] == dirpos[1]):
					beenContains = True
					
			if (beenContains == False) and (pathContains == False):
				move(direction[0])
				moved = True
				break
				
		if moved == False:
			a = path.pop()
			if len(freedom) == 2:
				been.pop()
			been.append(pos)
			backtrack(a, posX, posY)
		
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
		
		wall =  initX == newX and initY == newY
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