def main():
	#getCertain()
	goto(0,0)

	allUnlocks = [
		Unlocks.Plant,
		Unlocks.Expand,
		Unlocks.Speed,
		Unlocks.Watering,
		Unlocks.Fertilizer,
		Unlocks.Grass,
		Unlocks.Trees,
		Unlocks.Carrots,
		Unlocks.Pumpkins,
		Unlocks.Dinosaurs,
		Unlocks.Cactus,
		Unlocks.Mazes,
		Unlocks.Sunflowers,
		Unlocks.Leaderboard,
		Unlocks.Polyculture
	]

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
				
		upgrades = [cheap]
		quick_print(cheap)
		getAll(upgrades)
		for upgrade in upgrades:
			unlock(upgrade)
		quick_print(" ")

	print("Done")

main()