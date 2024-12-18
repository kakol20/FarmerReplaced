def replant(size, entity, water):
	for x in range(size):
		for y in range(size):
			if can_harvest():
				harvest()
				
				if entity == Entities.Carrot or entity == Entities.Cactus or entity == Entities.Sunflower:
					Till()
					
				if (entity == Entities.Bush or entity == Entities.Grass) and get_ground_type() == Grounds.Soil:
					till()
					
				if entity == Entities.Bush:
					if x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0:
						plant(Entities.Tree)
						useFertilizer()
				if entity != Entities.Grass:
					plant(entity)
					if get_water() <= water and num_items(Items.Water) >= water:
						use_item(Items.Water)
			elif get_entity_type() == None:
				if (entity == Entities.Bush or entity == Entities.Grass) and get_ground_type() == Grounds.Soil:
					till()
				plant(entity)
					
			move(North)
		move(East)
		
# -----
		
def replantPumpkin(size, entity):
	field = fieldGrid(size, False)
	
	for z in range(3):
		for x in range(size):
			for y in range(size):
				
				if get_entity_type() != entity:
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
	goto(0, 0)
	
def fillRemaining(size, entity, field):
	keepChecking = True
	while keepChecking:
		hasLeft = False
		for x in range(size):
			for y in range(size):
				if field[x][y] == True:
					hasLeft = True
					goto(x, y)
					
					if get_entity_type() != entity:
						Till()
						plant(entity)
						useFertilizer()
					elif can_harvest():
						field[x][y] = False
		keepChecking = hasLeft