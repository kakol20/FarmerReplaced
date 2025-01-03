def debug():
	#clear()
	
	unlocks = {}
	items = {}
	
	unlocks = Unlocks
	#items = {Items.Weird_Substance: 999999}
	
	globals = {}
	seed = -1
	
	size = get_world_size()
	water = 0.5
	
	clear()
	data = {
		"dinoPath": None,
		"size": get_world_size(),
		"upgrades": None,
		"treasure": None,
		"currentPos": getCurrentPos()
	}
	
	if data["dinoPath"] == None:
		data["dinoPath"] = updateDinoPath(data)
	
	#pass
	
	#simulate("main", unlocks, items, globals, seed, 1)
	simulate("testAll", unlocks, items, globals, seed, 1)

	
debug()
print("Debug Done")