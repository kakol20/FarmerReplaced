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
		
	return path

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
	
	return path1
			
def getBones(data):
	currentPos = (0, 0)
	data["currentPos"] = currentPos
	index = 1
	while True:		
		canMove = gotoDino(currentPos, data["dinoPath"][index])
		currentPos = data["dinoPath"][index]
		index += 1
		
		if not canMove:
			change_hat(Hats.Straw_Hat)
			break
		else:
			data["currentPos"] = currentPos
		
		if index >= len(data["dinoPath"]):
			index = 0
	return data
			
def updateDinoPath(data):
	if num_unlocked(Unlocks.Dinosaurs) == 0:
		return None
	out = []
	if data["size"] % 2 == 0:
		out = getBonesEven(data["size"])
	else:
		out = getBonesOdd(data["size"])
		
	return out