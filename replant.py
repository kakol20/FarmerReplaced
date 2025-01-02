def replant(data, entity, water):
	if num_unlocked(Unlocks.Expand) <= 1:
		x = 0
		for y in range(data["size"]):
			if get_entity_type() != None:
				while not can_harvest():
					pass
				harvest()
			
			groundType = get_ground_type()
					
			if entity == Entities.Grass:
				if groundType == Grounds.Soil:
					till()
			elif entity == Entities.Bush and num_unlocked(Unlocks.Trees) > 0:
				if x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0:
					plant(Entities.Bush)
				else:
					plant(Entities.Tree)
					useFertilizer()
					useWater(water)
			else:
				if groundType != Grounds.Soil and entity != Entities.Bush:
					till()
				plant(entity)
				useFertilizer()
				useWater(water)
			if data["size"] > 1:
				move(North)
		return

	for x in range(data["size"]):
		for y in range(data["size"]):
			if get_entity_type() != None:
				while not can_harvest():
					pass
				harvest()
			
			groundType = get_ground_type()
					
			if entity == Entities.Grass:
				if groundType == Grounds.Soil:
					till()
			elif entity == Entities.Bush and num_unlocked(Unlocks.Trees) > 0:
				if x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0:
					plant(Entities.Bush)
				else:
					plant(Entities.Tree)
					useFertilizer()
					useWater(water)
			else:
				if groundType != Grounds.Soil and entity != Entities.Bush:
					till()
				plant(entity)
				useFertilizer()
				useWater(water)
				
			move(North)
		move(East)
		
# -----
		
def replantPumpkin(data, entity):
	data["currentPos"] = getCurrentPos()
	if not (data["currentPos"][0] == 0 and data["currentPos"][1] == 0):
		goto(data["currentPos"], (0, 0), data["size"])
		data["currentPos"] = (0, 0)
	
	field = fieldGrid(data["size"], True)
	for x in range(data["size"]):
		for y in range(data["size"]):
			below = get_entity_type()
			if below != entity:
				if below != None:
					while not can_harvest():
						pass
					harvest()
				Till()
				plant(entity)
				field[x][y] = True
			else:
				if can_harvest():
					field[x][y] = False
			move(North)
		move(East)
			
	data = fillRemaining(data, entity, field)
	harvest()
	return data
	
def fillRemaining(data, entity, field):
	keepChecking = True
	while keepChecking:
		hasLeft = False
		for x in range(data["size"]):
			for y in range(data["size"]):
				if field[x][y]:
					goto(data["currentPos"], (x, y), data["size"])
					data["currentPos"] = (x, y)
					
					if get_entity_type() != entity:
						Till()
						plant(entity)
						useFertilizer()
						field[x][y] = True
						hasLeft = True
					elif can_harvest():
						field[x][y] = False
					else:
						field[x][y] = True
						hasLeft = True
		#do_a_flip()
		keepChecking = hasLeft
	
	return data