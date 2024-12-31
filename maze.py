def startMaze(size, treasure, old):
	clear()
	plant(Entities.Bush)
	while get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
		use_item(Items.Weird_Substance, size * num_unlocked(Unlocks.Mazes))
				
	if old:
		return mazeOld(treasure)
	else:
		return mazeNew(treasure)
	
def mazeOld(treasure):
	facing = 0
	directions = [North, East, South, West]
	
	if treasure != None and treasure[0] > treasure[1]:
		facing = 1
	else:
		facing = 0
	
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

# https://gist.github.com/zapakh/9a9b39a07964bbd27ab8cbd05ca35501
def mazeNew(treasure):
	currentPos = getCurrentPos()
	goal = treasure
	
	opp = {
		North: South,
		East: West,
		South: North,
		West: East
	}
	d = {
		North: (0, 1),
		East: (1, 0),
		South: (0, -1),
		West: (-1, 0)
	}
	
	stack = [([North, East, South, West], None)]
	visited = {currentPos}
	
	while get_entity_type() != Entities.Treasure:
		peak = stack[-1]
		dirs = peak[0]
		back = peak[1]
		
		old = currentPos
		dir = None
		
		while len(dirs) > 0:
			dir = dirs.pop()
			currentPos = (old[0] + d[dir][0], old[1] + d[dir][1])
			
			if currentPos in visited or not move(dir):
				dir = None
				continue
			else:
				break
			
		if dir == None:
			stack.pop()
			if back == None:
				print("Can't find path")
				while True:
					do_a_flip()
			move(back)
			currentPos = (old[0] + d[back][0], old[1] + d[back][1])
		else:
			visited.add(currentPos)
			stack.append((
				getRankedDirs(currentPos, goal, opp[dir]),
				opp[dir]))
	treasure = measure()
	harvest()
	return treasure
			
def getRankedDirs(pos, goal, exclude=None):
	if goal == None:
		allDirs = [(1, North), (2, East), (3, South), (4, West)]
	else:
		allDirs = [
			(goal[1] - pos[1] + 0.1, North),
			(goal[0] - pos[0] + 0.2, East),
			(pos[1] - goal[1] + 0.3, South),
			(pos[0] - goal[0] + 0.4, West)]
		
	rankedDirs = []
	for i in range(len(allDirs)):
		worstDir = min(allDirs)
		allDirs.remove(worstDir)
		if worstDir[1] != exclude:
			rankedDirs.append(worstDir[1])	
	return rankedDirs