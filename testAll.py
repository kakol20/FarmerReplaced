def testAll():
	data = {
		"dinoPath": None,
		"size": get_world_size(),
		"upgrades": None,
		"treasure": None,
		"currentPos": getCurrentPos()
	}
	
	if data["dinoPath"] == None:
		data["dinoPath"] = updateDinoPath(data)
			
	size = data["size"]
	water = 0.3

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
		Items.Hay: max(intHayCost, 10000),
		Items.Wood: max(intWoodCost, 10000),
		Items.Carrot: max(intCarrotCost, 10000),
		Items.Pumpkin: max(intPumpkinCost, 10000),
		Items.Cactus: 10000,
		Items.Gold: 10000,
		Items.Bone: 10000,
		Items.Weird_Substance: size * num_unlocked(Unlocks.Mazes)
	}
	
	quick_print(required)
	
	while True:
		if num_unlocked(Unlocks.Dinosaurs) > 0:
			change_hat(Hats.Straw_Hat)
		
		if num_items(Items.Power) < size * size and num_unlocked(Items.Power) > 0:
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
				if num_items(Items.Weird_Substance) <= required[Items.Weird_Substance] and num_unlocked(Items.Fertilizer) > 0:
					if num_items(Items.Hay) < intHayCost:
						data = checkPolyculture(data, water, Entities.Grass)
					else:
						data = checkPolyculture(data, water, Entities.Bush)
				else:
					data = startMaze(data)
			elif num_items(Items.Bone) < required[Items.Bone]:
				#clear()
				data = getBones(data)
			else:
				break

testAll()
pass