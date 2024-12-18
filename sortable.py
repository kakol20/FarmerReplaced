# https://bit.ly/41E2sTg

def plantSortable(entity):
	Till()
	if get_entity_type() != entity:
		if get_entity_type() != None:
			while not can_harvest():
				do_a_flip()
			harvest()
		plant(entity)
		
def sowSortable(entity):
	size = get_world_size()
	clear()
	for i in range(size):
		for j in range(size):
			useWater(0.3)
			plantSortable(entity)
			move(North)
		move(East)
		
def sortSortable(size):
	size = get_world_size()
	goto(0, 0)
	sort_map = []
	
	for i in range(size):
		for j in range(size):
			x, y = get_pos_x(), get_pos_y()
			while not can_harvest():
				do_a_flip()
			value = measure()
			sort_map.append((x, y, value))
			move(North)
		move(East)
	
	sorted = False
	
	while not sorted:
		sorted = True
		
		for j in range(size - 1):
			for i in range(size):
				index = i * size + j
				neighbour = index + 1
				
				if sort_map[index][2] > sort_map[neighbour][2]:
					goto(sort_map[index][0], sort_map[index][1])
					swap(North)
					sort_map[index] = get_pos_x(), get_pos_y(), measure()
					
					goto(sort_map[neighbour][0], sort_map[neighbour][1])
					sort_map[neighbour] = get_pos_x(), get_pos_y(), measure()
					
					sorted = False
		
		for i in range(size - 1):
			for j in range(size):
				index = i * size + j
				neighbour = (i + 1) * size + j
				
				if sort_map[index][2] > sort_map[neighbour][2]:
					goto(sort_map[index][0], sort_map[index][1])
					swap(East)
					sort_map[index] = get_pos_x(), get_pos_y(), measure()
					
					goto(sort_map[neighbour][0], sort_map[neighbour][1])
					sort_map[neighbour] = get_pos_x(), get_pos_y(), measure()
					
					sorted = False
	goto(size - 1, size - 1)
	harvest()
	
def farmSortable(entity, size):
	sowSortable(entity)
	sortSortable(size)
	