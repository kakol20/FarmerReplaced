def goto(x, y):
	yDist = get_pos_y() - y  # Positive if drone is north of the target space
	xDist = get_pos_x() - x  # Positive if drone is east of the target space
	halfWorldSize = get_world_size() / 2
	
	while get_pos_y() != y:
		if yDist >= halfWorldSize or (-halfWorldSize <= yDist and yDist < 0):
			if not move(North):
				return False
		else:
			if not move(South):
				return False
	
	while get_pos_x() != x:
		if xDist >= halfWorldSize or (-halfWorldSize <= xDist and xDist < 0):
			if not move(East):
				return False
		else:
			if not move(West):
				return False
			
	return True
	
def gotoDino(x, y):
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
	
def checkUnlock(unlock_):
	# check if parent is unlocked
	if unlock_[1] != None and num_unlocked(unlock_[1]) <= 0:
		return [False, None]
	
	costs = get_cost(unlock_[0])
	
	# check if unlocked or max level
	if costs == {} or costs == None:
		return [False, costs]
		
	# check if item not unlocked
	invalid = False
	for i in costs:
		if num_unlocked(i) <= 0:
			invalid = True
			break
	if invalid:
		return [False, costs]
	return [True, costs]