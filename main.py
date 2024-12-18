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
		cheap = None
		cheapCost = 0
		
		# find first valid unlock
		for i in allUnlocks:
			iCosts = get_cost(i)
			
			# checked if unlocked or max level
			if iCosts == {} or iCosts == None:
				continue
				
			# check if item not unlock
			invalid = False
			for j in iCosts:
				if num_unlocked(j) <= 0:
					invalid = True
					break	
			if invalid:
				continue
			
			cheap = i
			for j in iCosts:
				cheapCost = max(cheapCost, iCosts[j])
			break
			
		if cheap == None:
			break
		
		# find cheapest unlock
		for i in allUnlocks:
			iCosts = get_cost(i)
			# checked if unlocked or max level
			if iCosts == {} or iCosts == None:
				continue
			# check if item not unlock
			invalid = False
			for j in iCosts:
				if num_unlocked(j) <= 0:
					invalid = True
					break	
			if invalid:
				continue
				
			iCost = 0
			for j in iCosts:
				iCost = max(iCost, iCosts[j])
			
			if iCost < cheapCost:
				cheap = i
				cheapCost = iCost
				
		upgrades = [cheap]
		quick_print(cheap)
		getAll(upgrades)
		for upgrade in upgrades:
			unlock(upgrade)
		quick_print(" ")

	print("Done")

main()