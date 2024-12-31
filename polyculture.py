def polyculture(data, water, startEntity):
	field = fieldGrid(data["size"], startEntity)
	
	if startEntity == Entities.Bush and num_unlocked(Unlocks.Trees) > 0:
		for x in range(data["size"]):
			for y in range(data["size"]):
				if x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0:
					field[x][y] = Entities.Bush
				else:
					field[x][y] = Entities.Tree				
					
	for x in range(data["size"]):
		for y in range(data["size"]):
			companion = get_companion()
			entity = field[x][y]
			below = get_entity_type()
			
			if below != None:
				while not can_harvest():
					pass
				harvest()
			
			if entity == Entities.Tree and num_unlocked(Unlocks.Trees) == 0:
				entity = Entities.Bush
				
			field[x][y] = entity
							
			groundType = get_ground_type()
			if entity == Entities.Grass:
				if groundType == Grounds.Soil:
					till()
			elif entity == Entities.Carrot:
				Till()
				
			if entity != Entities.Grass:
				plant(entity)
				
			useWater(water)
			if entity == Entities.Tree:
				useFertilizer()
				
			if companion != None:
				companionPos = (companion[1][0], companion[1][1])
				#field[companion[1][0]][companion[1][1]] = companion[0]
				# check neighbour if tree
				if companion[0] == Entities.Tree:
					if polyIsValidTree(companionPos, field,  size):
						field[companionPos[0]][companionPos[1]] = Entities.Tree
					else:
						field[companionPos[0]][companionPos[1]] = startEntity
				else:
					field[companionPos[0]][companionPos[1]] = companion[0]
			
			move(North)
		move(East)
		
def checkPolyculture(data, water, entity):
	#currentPos = data["currentPos"]
	#if data["currentPos"] != (0, 0):
		#goto(data["currentPos"], (0, 0), data["size"])
		#data["currentPos"] = (0, 0)
		
	if num_unlocked(Unlocks.Polyculture) > 0:
		polyculture(data, water, entity)
	else:
		replant(data, entity, water)
	return data
		
def polyIsValidTree(pos, field, size):
	if pos[0] - 1 >= 0:
		if field[pos[0] - 1][pos[1]] == Entities.Tree:
			return False
			
	if pos[0] + 1 < size:
		if field[pos[0] + 1][pos[1]] == Entities.Tree:
			return False
			
	if pos[1] - 1 >= 0:
		if field[pos[0]][pos[1] - 1] == Entities.Tree:
			return False
			
	if pos[1] + 1 < size:
		if field[pos[0]][pos[1] + 1] == Entities.Tree:
			return False
			
	return True