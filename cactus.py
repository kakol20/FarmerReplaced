# https://bit.ly/41E2sTg

def plantCactus():
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Cactus:
		if can_harvest():
			harvest()
		plant(Entities.Cactus)
		
def sowCactus():
	size = get_world_size()
	goto(0, 0)
	for i in range(size):
		for j in range(size):
			use_item(Items.Water)
			plantCactus()
			move(North)
		move(East)
		
def sortCactus():
	size = get_world_size()
	goto(0, 0)
	cactus_map = []
	
	for i in range(size):
		for j in range(size):
			x, y = get_pos_x(), get_pos_y()
			value = measure()
			cactus_map.append((x, y, value))
			move(North)
		move(East)
	
	sorted = False
	
	while not sorted:
		sorted = True
		
		for j in range(size - 1):
			for i in range(size):
				index = i * size + j
				neighbour = index + 1
				
				if cactus_map[index][2] > cactus_map[neighbour][2]:
					goto(cactus_map[index][0], cactus_map[index][1])
					swap(North)
					cactus_map[index] = get_pos_x(), get_pos_y(), measure()
					
					goto(cactus_map[neighbour][0], cactus_map[neighbour][1])
					cactus_map[neighbour] = get_pos_x(), get_pos_y(), measure()
					
					sorted = False
		
		for i in range(size - 1):
			for j in range(size):
				index = i * size + j
				neighbour = (i + 1) * size + j
				
				if cactus_map[index][2] > cactus_map[neighbour][2]:
					goto(cactus_map[index][0], cactus_map[index][1])
					swap(East)
					cactus_map[index] = get_pos_x(), get_pos_y(), measure()
					
					goto(cactus_map[neighbour][0], cactus_map[neighbour][1])
					cactus_map[neighbour] = get_pos_x(), get_pos_y(), measure()
					
					sorted = False
	harvest()
	
def farmCactus():
	sowCactus()
	sortCactus()
	