def getAll():
	clear()
	do_a_flip()
	
	size = get_world_size()
	
	required = {
		Items.Hay: size * size,
		Items.Wood: size * size,
		Items.Carrot: size * size * 1.5,
		Items.Pumpkin: size * size * num_unlocked(Unlocks.Cactus) * 2,
		Items.Cactus: size * size,
		Items.Gold: 0,
		Items.Bone: 0,
		Items.Weird_Substance: size * num_unlocked(Unlocks.Mazes)
	}
	
	for upgrade in upgrades:
		cost = get_cost(upgrade)
		quick_print(cost)
		
		for item in cost:
			required[item] += cost[item]
	
	water = 0.3
	
	# quick_print([hayCount, woodCount, carrotCount, pumpkinCount, cactusCount, goldCount])
	quick_print(" ")
	quick_print(required)
	
	treasure = None
	
	while True:
		change_hat(Hats.Straw_Hat)
		#goto(0, 0)
		if num_items(Items.Hay) <= required[Items.Hay]:	
			replant(size, Entities.Grass, water)
		elif num_items(Items.Wood) <= required[Items.Wood] or num_items(Items.Weird_Substance) <= required[Items.Weird_Substance]:
			replant(size, Entities.Bush, water)
		elif num_items(Items.Carrot) <= required[Items.Carrot]:
			replant(size, Entities.Carrot, water)
		elif num_items(Items.Pumpkin) <= required[Items.Pumpkin]:
			replantPumpkin(size, Entities.Pumpkin)
		elif num_items(Items.Cactus) <= required[Items.Cactus]:
			#replant(size, Entities.Cactus, water)
			farmCactus()
		elif num_items(Items.Gold) <= required[Items.Gold]:
			treasure = startMaze(size, treasure)
		elif num_items(Items.Bone) <= required[Items.Bone]:
			change_hat(Hats.Dinosaur_Hat)
			if size % 2 == 0:
				getBonesComplex(size)
			else:
				getBonesSimple(size)
		else:
			break