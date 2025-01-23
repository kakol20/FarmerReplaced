from helpers import universalPlant

def replant(data, entity, water):
	if num_unlocked(Unlocks.Expand) <= 1:
		x = 0
		for y in range(data["size"]):
			plantEntity = entity
			if entity == Entities.Bush and num_unlocked(Unlocks.Trees) > 0:
				if y % 2 == 1:
					plantEntity = Entities.Bush
				else:
					plantEntity = Entities.Tree	
			
			universalPlant(plantEntity)		
			
			if data["size"] > 1:
				move(North)
		return

	for x in range(data["size"]):
		for y in range(data["size"]):
			plantEntity = entity
			if entity == Entities.Bush and num_unlocked(Unlocks.Trees) > 0:
				if (x % 2 == 0 and y % 2 == 1) or (x % 2 == 1 and y % 2 == 0):
					plantEntity = Entities.Bush
				else:
					plantEntity = Entities.Tree
			
			universalPlant(plantEntity)	
				
			move(North)
		move(East)
	return data
		
# -----
		
def replantPumpkin(data, entity):
	data["currentPos"] = getCurrentPos()
	if not (data["currentPos"][0] == 0 and data["currentPos"][1] == 0):
		goto(data["currentPos"], (0, 0), data["size"])
		data["currentPos"] = (0, 0)
	
	field = fieldGrid(data["size"], True)
	for x in range(data["size"]):
		for y in range(data["size"]):
			universalPlant(entity, False)
			field[x][y] = True
			
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
						universalPlant(entity)
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