def main():
	#getCertain()
	goto(getCurrentPos(), (0, 0), get_world_size())

	allUnlocks = (
		(Unlocks.Grass, None),
		(Unlocks.Speed, None),
		(Unlocks.Plant, Unlocks.Speed),
		(Unlocks.Expand, Unlocks.Speed),
		(Unlocks.Carrots, Unlocks.Plant),
		(Unlocks.Watering, Unlocks.Carrots),
		(Unlocks.Trees, Unlocks.Carrots),
		(Unlocks.Fertilizer, Unlocks.Watering),
		(Unlocks.Sunflowers, Unlocks.Watering),
		(Unlocks.Pumpkins, Unlocks.Trees),
		(Unlocks.Dinosaurs, Unlocks.Pumpkins),
		(Unlocks.Cactus, Unlocks.Pumpkins),
		(Unlocks.Mazes, Unlocks.Pumpkins),
		(Unlocks.Polyculture, Unlocks.Mazes),
		(Unlocks.Leaderboard, Unlocks.Simulation)
	)
	
	data = {
		"dinoPath": None,
		"size": get_world_size(),
		"upgrades": None,
		"treasure": None,
		"currentPos": getCurrentPos()
	}
	
	if data["dinoPath"] == None:
		data["dinoPath"] = updateDinoPath(data)

	while True:
		#if num_unlocked(Unlocks.Leaderboard) > 0:
			#break
		cheap = None
		cheapCost = 0
		
		# find first valid unlock
		for i in allUnlocks:
			checked = checkUnlock(i)
			
			cost = 0
			if checked[0]:
				for j in checked[1]:
					cost = max(cost, checked[1][j])
				cheap = i
				cheapCost = cost
				break
			
		if cheap == None:
			data["upgrades"] = []
			data = getAll(data)
			break
		
		# find cheapest unlock
		for i in allUnlocks:
			checked = checkUnlock(i)
			
			cost = 0
			if checked[0]:
				for j in checked[1]:
					cost = max(cost, checked[1][j])
				if cost < cheapCost:
					cheap = i
					cheapCost = cost
				
		data["upgrades"] = [cheap]
		
		quick_print(data["upgrades"])
		data = getAll(data)
		for upgrade in data["upgrades"]:
			unlock(upgrade[0])
			
			if data["size"] % 2 == 0 and upgrade[0] == Unlocks.Expand:
				unlock(upgrade[0])
			
			if upgrade[0] == Unlocks.Expand:
				data["size"] = get_world_size()
				
				data["dinoPath"] = updateDinoPath(data)
			elif upgrade[0] == Unlocks.Dinosaurs:
				if data["dinoPath"] == None:
					data["dinoPath"] = updateDinoPath(data)

		quick_print(" ")

	print("Done")

main()