def getAll(data):
	#clear()
	#do_a_flip()
	
	#quick_print(get_cost(Entities.Carrot))
	
	size = data["size"]
	
	carPlCost = get_cost(Entities.Carrot)
	puPlCost = get_cost(Entities.Pumpkin)
	sfPlCost = get_cost(Entities.Sunflower)
	cacPlCost = get_cost(Entities.Cactus)
	apPlCost = get_cost(Entities.Apple)
	
	intHayCost = 0
	intWoodCost = 0
	if carPlCost != {}:
		intHayCost = size * size * num_unlocked(Items.Carrot) * carPlCost[Items.Hay]
		intWoodCost = size * size * num_unlocked(Items.Carrot) * carPlCost[Items.Wood]
		
	intCarrotCost = 0
	if puPlCost != {}:
		intCarrotCost = size * size * num_unlocked(Items.Pumpkin) * puPlCost[Items.Carrot] * 2
	
	if sfPlCost != {}:
		intCarrotCost = max(intCarrotCost, size * size * num_unlocked(Items.Power) * sfPlCost[Items.Carrot])
		
	intPumpkinCost = 0
	if cacPlCost != {}:
		intPumpkinCost = size * size * num_unlocked(Items.Cactus) * cacPlCost[Items.Pumpkin]
		
	if apPlCost != {}:
		intPumpkinCost = max(intPumpkinCost, size * size * num_unlocked(Entities.Apple) * apPlCost[Items.Pumpkin])
	
	required = {
		Items.Hay: intHayCost,
		Items.Wood: intWoodCost,
		Items.Carrot: intCarrotCost,
		Items.Pumpkin: intPumpkinCost,
		Items.Cactus: 0,
		Items.Gold: 0,
		Items.Bone: 0,
		Items.Weird_Substance: size * num_unlocked(Unlocks.Mazes)
	}
	
	for upgrade in data["upgrades"]:
		cost = get_cost(upgrade[0])
		quick_print(cost)
		
		for item in cost:
			required[item] += cost[item]
			
	for i in required:
		required[i] *= num_unlocked(i)
	
	water = 0.5

	#quick_print(" ")
	quick_print(required)
	
	while True:
		if num_unlocked(Unlocks.Dinosaurs) > 0:
			change_hat(Hats.Straw_Hat)
		
		if num_items(Items.Weird_Substance) < required[Items.Weird_Substance] and num_unlocked(Items.Fertilizer) > 0:
			if num_items(Items.Hay) < intHayCost:
				data = checkPolyculture(data, water, Entities.Grass)
			elif num_items(Items.Wood) < intWoodCost or num_unlocked(Items.Carrot) <= 0:
				data = checkPolyculture(data, water, Entities.Bush) 
			else:
				data = checkPolyculture(data, water, Entities.Carrot)
		elif num_items(Items.Power) < size * size and num_unlocked(Items.Power) > 0:
			while num_items(Items.Power) < size * size * 30:
				if num_items(Items.Hay) < intHayCost:
					data = checkPolyculture(data, water, Entities.Grass)
				elif num_items(Items.Wood) < intWoodCost:
					data = checkPolyculture(data, water, Entities.Bush) 
				elif num_items(Items.Carrot) < intCarrotCost:
					data = checkPolyculture(data, water, Entities.Carrot)
				else:
					data = farmSunflower(data, water)
		else:
			if num_items(Items.Hay) < required[Items.Hay]:
				data = checkPolyculture(data, water, Entities.Grass)
			elif num_items(Items.Wood) < required[Items.Wood]:
				data = checkPolyculture(data, water, Entities.Bush)
			elif num_items(Items.Carrot) < required[Items.Carrot]:
				data = checkPolyculture(data, water, Entities.Carrot)
			elif num_items(Items.Pumpkin) < required[Items.Pumpkin]:
				data = replantPumpkin(data, Entities.Pumpkin)
			elif num_items(Items.Cactus) < required[Items.Cactus]:
				data = farmSortable(Entities.Cactus, data)
			elif num_items(Items.Gold) < required[Items.Gold]:
				#clear()
				data = startMaze(data)
			elif num_items(Items.Bone) < required[Items.Bone]:
				clear()
				change_hat(Hats.Dinosaur_Hat)
				data = getBones(data)
			else:
				break
	return data