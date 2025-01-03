# https://bit.ly/41E2sTg

def sowSortable(entity, data):
	#currentPos = getCurrentPos()
	#goto(currentPos, (0, 0), size)
	if data["currentPos"] != (0, 0):
		goto(data["currentPos"], (0, 0), data["size"])
		data["currentPos"] = (0, 0)
	
	for i in range(data["size"]):
		for j in range(data["size"]):
			universalPlant(entity)
			move(North)
		move(East)
		
	return data
		
def sortSortable(data):
	size = data["size"]
	
	currentPos = data["currentPos"]
	if data["currentPos"] != (0, 0):
		goto(data["currentPos"], (0, 0), data["size"])
		data["currentPos"] = (0, 0)
	
	sort_map = []
	
	for x in range(size):
		for y in range(size):
			#while not can_harvest():
				#pass
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
					nextPos = (sort_map[index][0], sort_map[index][1])
					goto(currentPos, nextPos, size)
					currentPos = nextPos
					
					swap(North)
					sort_map[index] = currentPos[0], currentPos[1], measure()
					
					nextPos = (sort_map[neighbour][0], sort_map[neighbour][1])
					goto(currentPos, nextPos, size)
					currentPos = nextPos
					
					sort_map[neighbour] = currentPos[0], currentPos[1], measure()
					
					sorted = False
		
		#currentPos = getCurrentPos()
		for i in range(size - 1):
			for j in range(size):
				index = i * size + j
				neighbour = (i + 1) * size + j
				
				if sort_map[index][2] > sort_map[neighbour][2]:
					nextPos = (sort_map[index][0], sort_map[index][1])
					goto(currentPos, nextPos, size)
					currentPos = nextPos
					
					swap(East)
					sort_map[index] = currentPos[0], currentPos[1], measure()
					
					nextPos = (sort_map[neighbour][0], sort_map[neighbour][1])
					goto(currentPos, nextPos, size)
					currentPos = nextPos
					
					sort_map[neighbour] = currentPos[0], currentPos[1], measure()
					
					sorted = False
					
	#currentPos = getCurrentPos()
	#goto(currentPos, (size - 1, size - 1), size)#
	data["currentPos"] = currentPos
	harvest()
	return data
	
def farmSortable(entity, data):
	data = sowSortable(entity, data)
	data = sortSortable(data)
	return data