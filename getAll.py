from helpers import getCurrentPos
from bones import updateDinoPath
from polyculture import checkPolyculture
from sunflower import farmSunflower
from replant import replantPumpkin
from sortable import farmSortable
from maze import startMaze
from bones import getBones

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
	
	carUnlocked = num_unlocked(Items.Carrot)
	pumUnlocked = num_unlocked(Items.Pumpkin)
	powUnlocked = num_unlocked(Items.Power)
	cacUnlocked = num_unlocked(Items.Cactus)
	aplUnlocked = num_unlocked(Entities.Apple)
	
	intHayCost = 0
	intWoodCost = 0
	if carPlCost != {} and carUnlocked > 0:
		intHayCost = size * size * carUnlocked * carPlCost[Items.Hay]
		intWoodCost = size * size * carUnlocked * carPlCost[Items.Wood]
		
	intCarrotCost = 0
	if puPlCost != {} and pumUnlocked > 0:
		intCarrotCost = size * size * pumUnlocked * puPlCost[Items.Carrot] * 2
	
	if sfPlCost != {} and powUnlocked > 0:
		intCarrotCost = max(intCarrotCost, size * size * powUnlocked * sfPlCost[Items.Carrot])
		
	intPumpkinCost = 0
	if cacPlCost != {} and cacUnlocked > 0:
		intPumpkinCost = size * size * cacUnlocked * cacPlCost[Items.Pumpkin]
		
	if apPlCost != {} and aplUnlocked > 0:
		intPumpkinCost = max(intPumpkinCost, size * size * aplUnlocked * apPlCost[Items.Pumpkin])
	
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
			
		if data["size"] % 2 == 0 and upgrade[0] == Unlocks.Expand:
			cost = get_cost(Unlocks.Expand, num_unlocked(Unlocks.Expand) + 1)
			for item in cost:
				required[item] += cost[item]
			
	for i in required:
		if i == Items.Weird_Substance:
			required[i] *= num_unlocked(Items.Fertilizer)
		else:
			required[i] *= num_unlocked(i)
		
	#if num_unlocked(Items.Fertilizer) > 0 and num_unlocked(Unlocks.Mazes) > 0:
		#quick_print(num_unlocked(Unlocks.Mazes))
		#pass
	
	water = 0.3

	#quick_print(" ")
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

	return data