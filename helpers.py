def goto(x, y):
	xDist = x - get_pos_x() # Positive if drone is east of the target space
	yDist = y - get_pos_y() # Positive if drone is north of the target space
	
	while get_pos_x() != x:
		if xDist > 0:
			if not move(East):
				return False
		elif xDist < 0:
			if not move(West):
				return False
		xDist = x - get_pos_x()
		
	while get_pos_y() != y:
		if yDist > 0:
			if not move(North):
				return False
		elif yDist < 0:
			if not move(South):
				return False
		yDist = y - get_pos_y()
		
	return True

# -----
			
def fieldGrid(size, element):
	xArr = []
	for x in range(size):
		yArr = []
		for y in range(size):
			yArr.append(element)
		xArr.append(yArr)
	return xArr

def harvestClear(size):
	goto(0,0)
	if get_entity_type() == Entities.Grass:
		return
	elif get_entity_type() == None:
		return

	for x in range(size):
		for y in range(size):
			entity = get_entity_type()
			while not can_harvest():
				do_a_flip()
			harvest()
			move(North)
		move(East)
	goto(0,0)