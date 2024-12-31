def startMaze(data):
	#clear()
	plant(Entities.Bush)
	while get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
		use_item(Items.Weird_Substance, data["size"] * num_unlocked(Unlocks.Mazes))
				
	return mazeOld(data)
	
def mazeOld(data):
	facing = 0
	directions = [North, East, South, West]
	treasure = data["treasure"]
	currentPos = data["currentPos"]
	
	if treasure != None:
		delta = (treasure[0] - currentPos[0], treasure[1] - currentPos[1])
		absDelta = (abs(delta[0]), abs(delta[1]))
		
		if delta[0] > 0 and absDelta[0] > absDelta[1]:
			facing = 1
		elif delta[0] < 0 and absDelta[0] > absDelta[1]:
			facing = 3
		elif delta[1] < 0 and absDelta[1] > absDelta[0]:
			facing = 2
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
	harvest()
	return data