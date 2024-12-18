def polyculture(size, water, startEntity):
	field = fieldGrid(size, startEntity)
	
	if startEntity == Entities.Bush and num_unlocked(Unlocks.Trees) > 0:
		for x in range(size):
			for y in range(size):
				if x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0:
					field[x][y] = Entities.Bush
				else:
					field[x][y] = Entities.Tree
	
	for x in range(size):
		for y in range(size):
			companion = get_companion()
			entity = field[x][y]
			if can_harvest():
				harvest()
				if entity == Entities.Carrot:
					Till()
				elif entity == Entities.Tree and num_unlocked(Unlocks.Trees) == 0:
					entity = Entities.Bush
				
				field[x][y] = entity
				plant(entity)
				useWater(water)
				if entity == Entities.Tree:
					useFertilizer()

				#quick_print(companion)
				#quick_print(field)
				
				field[companion[1][0]][companion[1][1]] = companion[0]
			elif get_entity_type() == None:
				plant(entity)
			move(North)
		move(East)
		
def checkPolyculture(size, water, entity):
	if num_unlocked(Unlocks.Polyculture) > 0:
		polyculture(size, water, entity)
	else:
		replant(size, entity, water)