def getBonesComplex(size):
	path = []
	#path.append((0, 0))
	
	for i in range(0, size, 2):
		for j in range(size):
			path.append((i, j))
		for j in range(size - 1, -1, -1):
			path.append((i + 1, j))
		
	#path.append(path[0])
	
	for i in range(0, size - 1, 1):
		path.remove((i, 0))
		
	#quick_print(path)
	
	index = 1
	while True:
		canMove = goto(path[index][0], path[index][1])
		if not canMove:
			change_hat(Hats.Straw_Hat)
			break
		
		index += 1
		
		if index >= len(path):
			index = 0