from helpers import gotoDino
from helpers import getCurrentPos

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
		if i != 0:
			path.remove((i, 0))
		
	for x in range(size - 2, 0, -1):
		path.append((x, 0))
		
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
	
def getPathIndex(pos, path):
	for i in range(len(path)):
		if path[i] == pos:
			return i
	pass
	return 0
			
def getBones(data):
	clear()
	
	currentPos = (0, 0)
		
	change_hat(Hats.Dinosaur_Hat)
	
	data["currentPos"] = currentPos
	
	applePos = measure()
	snakeLen = 2
	lastIndex = 0
	index = 1
	appleIndex = getPathIndex(applePos, data["dinoPath"])
	pathLen = len(data["dinoPath"])
	
	while True:		
		canMove = gotoDino(currentPos, data["dinoPath"][index])
		
		# is trying to shortcut but can't
		if (lastIndex + 1) % pathLen != index and not canMove and data["size"] % 2 == 0:
			# try cycle
			currentPos = getCurrentPos()
			index = getPathIndex(currentPos, data["dinoPath"])
			index = (index + 1) % pathLen
			canMove = gotoDino(currentPos, data["dinoPath"][index])
			currentPos = data["dinoPath"][index]
		else:
			currentPos = data["dinoPath"][index]
		
		lastIndex = index
		
		if currentPos == applePos:
			applePos = measure()
			appleIndex = getPathIndex(applePos, data["dinoPath"])
			snakeLen += 1
		
		# only do optimisation at even sizes
		indexDist = appleIndex - index
		if data["size"] % 2 == 0 and applePos != None and indexDist > snakeLen and currentPos[1] != 0 and applePos[1] != 0:
			# apple in front snake in cycle and not y = 0
			if applePos[0] % 2 == 1 and currentPos[1] == data["size"] - 1:
				index = appleIndex
			elif applePos[0] % 2 == 0 and currentPos[1] == 1:
				index = appleIndex
			else:
				index += 1
		elif data["size"] % 2 == 0 and applePos != None and indexDist < 0:
			# apple behind snake in cycle
			indexDist = (pathLen - index) + appleIndex
			if currentPos[1] == 1 and indexDist > snakeLen:
				index = pathLen - currentPos[0]
			else:
				index += 1
		elif data["size"] % 2 == 0 and applePos != None and applePos[1] == 0:
			# apple in front snake in cycle and is y = 0
			if currentPos[1] == 1 and indexDist > snakeLen:
				index = pathLen - data["size"]
				
				if index != lastIndex:
					index += 1
			else:
				index += 1
		else:
			index += 1
		
		if not canMove or applePos == None:
			if snakeLen < data["size"] * data["size"]:
				quick_print(snakeLen)
				pass
			change_hat(Hats.Straw_Hat)
			break
		else:
			data["currentPos"] = currentPos
		
		if index >= pathLen:
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