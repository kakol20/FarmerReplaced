# https://gist.github.com/zapakh/9a9b39a07964bbd27ab8cbd05ca35501
def startMaze(size, treasure):
	clear()
	plant(Entities.Bush)
	 
	while get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
		use_item(Items.Weird_Substance, size * num_unlocked(Unlocks.Mazes))
			
	return firstSolve(treasure)
	
def firstSolve(treasure):
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