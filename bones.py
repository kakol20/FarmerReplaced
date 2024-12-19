def getBonesEven(size):
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
	
	currentPos = (0, 0)
	index = 1
	while True:
		canMove = gotoDino(currentPos, path[index])
		currentPos = path[index]
		index += 1
		
		if not canMove:
			change_hat(Hats.Straw_Hat)
			break
		
		if index >= len(path):
			index = 0

def getBonesOdd(size):
	path1 = []
	for i in range(0, size, 2):
		for j in range(size):
			path1.append((i, j))
		for j in range(size - 1, -1, -1):
			path1.append((i + 1, j))
	
	for i in range(0, size, 1):
		if i != 0:
			path1.remove((i, 0))
		path1.remove((i, size - 1))
		path1.remove((size, i))
		
	path1.append((size - 1, size - 1))
	#path1.append((0, size - 1))
	
	path2 = []
	for i in range(0, size, 2):
		for j in range(size - 1, -1, -1):
			path2.append((i, j))
		for j in range(size):
			path2.append((i + 1, j))
			
	for i in range(0, size, 1):
		if i != 0:
			path2.remove((i, size - 1))
		path2.remove((i, 0))
		path2.remove((size, i))
	
	path2.append((size - 1, 0))
	
	for i in path2:
		path1.append(i)	
	
	#quick_print(path1)
	
	currentPos = (0, 0)
	index = 1
	while True:		
		canMove = gotoDino(currentPos, path[index])
		currentPos = path[index]
		index += 1
		
		if not canMove:
			change_hat(Hats.Straw_Hat)
			break
		
		if index >= len(path1):
			index = 0