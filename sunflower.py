def farmSunflower(size, water):
	clear()
	sorted_list = []
	
	for x in range(size):
		for y in range(size):
			if can_harvest():
				harvest()
				Till()
				plant(Entities.Sunflower)
				if get_water() <= water and num_items(Items.Water) >= water:
					use_item(Items.Water)
			elif get_entity_type() == None:
				Till()
				plant(Entities.Sunflower)
				
			value = measure()
			while value == None:
				if get_entity_type() != Entities.Sunflower:
					Till()
					plant(Entities.Sunflower)
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
		
	for i in sorted_list:
		goto(i["pos"][0], i["pos"][1])
		while not can_harvest():
			do_a_flip()
		harvest()