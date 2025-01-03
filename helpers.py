def goto(currentPos, targetPos, size):
	xDist = targetPos[0] - currentPos[0]
	yDist = targetPos[1] - currentPos[1]
	
	xDistA = abs(xDist)
	yDistA = abs(yDist)
	
	xDistW = min(size - xDistA, xDistA)
	yDistW = min(size - yDistA, yDistA)
	
	if xDistW != xDistA:
		xDist *= -1
	
	if yDistW != yDistA:
		yDist *= -1
	
	for i in range(xDistW):
		if xDist > 0:
			move(East)
		elif xDist < 0:
			move(West)
	
	for i in range(yDistW):	
		if yDist > 0:
			move(North)
		elif yDist < 0:
			move(South)
	
def gotoDino(currentPos, targetPos):
	xDist = targetPos[0] - currentPos[0]
	yDist = targetPos[1] - currentPos[1]
	
	for i in range(abs(xDist)):
		if xDist > 0:
			if not move(East):
				return False
		elif xDist < 0:
			if not move(West):
				return False
	
	for i in range(abs(yDist)):
		if yDist > 0:
			if not move(North):
				return False
		elif yDist < 0:
			if not move(South):
				return False
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
	
def getCurrentPos():
	return (get_pos_x(), get_pos_y())

def harvestClear(size):
	goto(getCurrentPos(), (0, 0), size)
	if get_entity_type() == Entities.Grass:
		return
	elif get_entity_type() == None:
		return

	for x in range(size):
		for y in range(size):
			entity = get_entity_type()
			while not can_harvest():
				pass
			harvest()
			move(North)
		move(East)
	goto(getCurrentPos(), (0, 0), size)
	
def checkUnlock(unlock_):
	# check if parent is unlocked
	if unlock_[1] != None and num_unlocked(unlock_[1]) <= 0:
		return (False, None)
	
	costs = get_cost(unlock_[0])
	
	# check if unlocked or max level
	if costs == {} or costs == None:
		return (False, costs)
		
	# check if item not unlocked
	invalid = False
	for i in costs:
		if num_unlocked(i) <= 0:
			invalid = True
			break
	if invalid:
		return (False, costs)
	return (True, costs)
	
def universalPlant(entity, useFert = True):
	if get_entity_type() != None:
		while not can_harvest():
			pass
		harvest()
		
	groundType = get_ground_type()
	if entity == Entities.Grass:
		if groundType == Grounds.Soil:
			till()
	elif not (entity == Entities.Bush or entity == Entities.Tree):
		if groundType == Grounds.Grassland:
			till()
			
	if entity != Entities.Grass:
		
		plant(entity)
	
	if not (entity == Entities.Bush or entity == Entities.Tree or entity == Entities.Grass):
		useWater(0.3)
		
	if not (entity == Entities.Bush or entity == Entities.Grass):
		if useFert:
			useFertilizer()