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
	
def distance(v1, v2):
	a = (v1[0] - v2[0])
	b = (v1[1] - v2[1])
	
	#return a + (0.5 * (b * b) * (1 / a)) # approximate
	#return a + b
	return approxSqrt(a * a + b * b)
	
def approxSqrt(x):
	yn = x
	i = 0
	while i < 4:
		temp = 0.5 * (yn + (x / yn))
		if yn == temp:
			yn = temp
			break
		
		yn = temp
		i += 1
			
	return yn