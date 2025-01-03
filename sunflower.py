def farmSunflower(data, water):
	#clear()
	sorted_list = []
	data["currentPos"] = getCurrentPos()
	if data["currentPos"][0] != 0 or data["currentPos"][1] != 0:
		goto(data["currentPos"], (0, 0), data["size"])
		data["currentPos"] = (0, 0)
	currentPos = data["currentPos"]
	
	for x in range(data["size"]):
		for y in range(data["size"]):		
			universalPlant(Entities.Sunflower)
				
			value = measure()
			while value == None:
				value = measure()
			
			item = {
				"pos": (x, y),
				"value": value
			}
			inserted = False
			for i in range(len(sorted_list)):
				if item["value"] > sorted_list[i]["value"]:
					sorted_list.insert(i, item)
					inserted = True
					break
			if not inserted:
				sorted_list.append(item)
			
			move(North)
		move(East)
	
	currentPos = (0, 0)
	for i in sorted_list:
		goto(currentPos, i["pos"], data["size"])
		currentPos = i["pos"]
		while not can_harvest():
			pass
		harvest()
	data["currentPos"] = currentPos
	return data