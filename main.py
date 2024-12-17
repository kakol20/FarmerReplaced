#getCertain()

#set_execution_speed(10)

upgrades = [
	#Unlocks.Fertilizer, 
	Unlocks.Cactus, 
	Unlocks.Dinosaurs,
	Unlocks.Mazes
]

quick_print(num_unlocked(Unlocks.Cactus))

getAll()

for upgrade in upgrades:
	unlock(upgrade)

print("Done")