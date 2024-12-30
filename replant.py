def replant(size, entity, water):
	for x in range(size):
		for y in range(size):
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
		
def replantPumpkin(size, entity):
	field = fieldGrid(size, False)
	for z in range(3):
		for x in range(size):
			for y in range(size):
				entityType = get_entity_type()
				if entityType != entity:
					if entityType != None:
						while not can_harvest():
							pass
						harvest()
					Till()
					plant(entity)
					
					if z > 0:
						field[x][y] = True
				else:
					if z > 0 and can_harvest():
						field[x][y] = False
				move(North)
			move(East)
			
	fillRemaining(size, entity, field)
	harvest()
	#goto(0, 0)
	
def fillRemaining(size, entity, field):
	keepChecking = True
	while keepChecking:
		hasLeft = False
		for x in range(size):
			for y in range(size):
				if field[x][y] == True:
					hasLeft = True
					goto(getCurrentPos(), (x, y), size)
					
					if get_entity_type() != entity:
						Till()
						plant(entity)
						useFertilizer()
					elif can_harvest():
						field[x][y] = False
		keepChecking = hasLeft