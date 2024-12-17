# https://github.com/eyyMinda/FarmerReplaced
def getCertain():
	clear()
	do_a_flip()
	
	treasure = False
	
	poly = False
	
	size = get_world_size()
	entity = Entities.Cactus
	water = 0.3
	buySeeds = size * size
	
	while True:
		if treasure == True:
			# startMaze()
			do_a_flip()
		elif poly == True:
			# polyCulture(size, water, 1)
			do_a_flip()
		else:
			if entity == Entities.Pumpkin:
				replantPumpkin(size, entity)
				# do_a_flip()
			elif entity == Entities.Cactus:
				farmCactus()
			else:
				replant(size, entity, water)
				# do_a_flip()