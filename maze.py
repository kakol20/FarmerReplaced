from helpers import getCurrentPos

def startMaze(data):
	#clear()
	#data["currentPos"] = (0, 0)
	
	below = get_entity_type()
	if below == None or below == Entities.Grass:
		plant(Entities.Bush)
	elif below != Entities.Bush:
		while not can_harvest():
			pass
		harvest()
		plant(Entities.Bush)
	
	substanceNeed = data["size"] * num_unlocked(Unlocks.Mazes)
	
	if num_items(Items.Weird_Substance) < substanceNeed:
		#quick_print(num_items(Items.Weird_Substance))
		#pass
		return data
	
	use_item(Items.Weird_Substance, substanceNeed)
				
	return mazeOld(data)
	
def mazeOld(data):
	facing = 0
	directions = [North, East, South, West]
	treasure = data["treasure"]
	currentPos = data["currentPos"]
	
	if treasure != None:
		delta = (treasure[0] - currentPos[0], treasure[1] - currentPos[1])
		absDelta = (abs(delta[0]), abs(delta[1]))
		
		if absDelta[1] > absDelta[0]:
			if delta[1] > 0:
				facing = 0
			else:
				facing = 2
		else:
			if delta[0] > 0:
				facing = 1
			else:
				facing = 3
	else:
		facing = 0
	
	while get_entity_type() != Entities.Treasure:
		moved = move(directions[facing % 4])
		
		facing += 1
		if not moved:
			facing += 2
	
	#quick_print(measure())
	if treasure != None:
		data["currentPos"] = treasure
	data["treasure"] = measure()
	data["currentPos"] = getCurrentPos()
	harvest()
	return data