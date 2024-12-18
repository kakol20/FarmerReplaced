def main():
	#getCertain()
	goto(0,0)

	allUnlocks = [
		Unlocks.Watering,
		Unlocks.Fertilizer,
		Unlocks.Grass,
		Unlocks.Trees,
		Unlocks.Carrots,
		Unlocks.Pumpkins,
		Unlocks.Dinosaurs,
		Unlocks.Cactus,
		Unlocks.Mazes,
		Unlocks.Expand,
		Unlocks.Speed,
		Unlocks.Simulation
	]

	for repeat in range(2):
		cheap = Unlocks.Fertilizer
		cheapCosts = get_cost(cheap)
		cheapCost = 0
		for i in cheapCosts:
			cheapCost = max(cheapCost, cheapCosts[i])
			
		for i in allUnlocks:
			iCosts = get_cost(i)
			if iCosts == None:
				continue
				
			iCost = 0
			for j in iCosts:
				iCost = max(iCost, iCosts[j])
			
			if iCost < cheapCost:
				cheap = i
				cheapCosts = iCosts
				cheapCost = iCost

		upgrades = [cheap]

		quick_print(upgrades)

		getAll(upgrades)

		for upgrade in upgrades:
			unlock(upgrade)
		quick_print(" ")

	print("Done")

main()