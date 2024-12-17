def goto(x, y):
	xDist = x - get_pos_x() # Positive if drone is east of the target space
	yDist = y - get_pos_y() # Positive if drone is north of the target space
	
	while get_pos_x() != x:
		if xDist > 0:
			move(East)
		elif xDist < 0:
			move(West)
		xDist = x - get_pos_x()
		
	while get_pos_y() != y:
		if yDist > 0:
			move(North) 
		elif yDist < 0:
			move(South)
		yDist = y - get_pos_y()

# -----
			
def fieldGrid(size, element):
	xArr = []
	for x in range(size):
		yArr = []
		for y in range(size):
			yArr.append(element)
		xArr.append(yArr)
	return xArr