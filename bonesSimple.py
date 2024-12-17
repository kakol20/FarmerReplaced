def getBonesSimple(size):
	vertical = North
	horizontal = East
	nextApple = (size, size)
	while True:	
		if get_entity_type() == Entities.Apple:
			nextApple = measure()
			#quick_print(nextApple)
			diffX = nextApple[0] - get_pos_x()
			#quick_print(diffX)
			
			if diffX > 0:
				horizontal = East
			elif diffX < 0:
				horizontal = West
	
		if not move(vertical):
			if vertical == North:
				vertical = South
			else:
				vertical = North
			
			if not move(horizontal):
				if horizontal == East:
					horizontal = West
				else:
					horizontal = East
				move(horizontal)
			
			if not move(vertical):
				break