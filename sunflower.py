def farmSunflower(size, water):
	#clear()
	sorted_list = []
	goto(getCurrentPos(), (0, 0), size)
	
	for x in range(size):
		for y in range(size):
			belowEntity = get_entity_type()
			
			if belowEntity != None:
				while not can_harvest():
					pass
				harvest()
			
			Till()
			plant(Entities.Sunflower)
			useWater(water)
				
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
		
	#for i in range(len(sorted_list)):
		#quick_print(sorted_list[i]["pos"])
		#for j in range(len(sorted_list)):
			#if j != i:
				#quick_print(sorted_list[i]["pos"] == sorted_list[j]["pos"])
	
	currentPos = getCurrentPos()
	for i in sorted_list:
		goto(currentPos, i["pos"], size)
		currentPos = i["pos"]
		while not can_harvest():
			pass
		harvest()