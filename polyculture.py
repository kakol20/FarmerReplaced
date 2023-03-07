def polyculture(size, water, buySeeds):
    field = fieldGrid(size, Entities.Grass)
    while True:
        for x in range(size):
            for y in range(size):
	            companion = get_companion()
	            entity = field[x][y]
	            if can_harvest():
	            	harvest()
	            	if entity == Entities.Carrots:
	            		Till()
	            		checkSeeds(size, entity, buySeeds)
	            	plant(entity)

	            	if water > 0:
				if get_water() <= water:
				use_item(Items.Water_Tank)

	            	field[companion[1]][companion[2]] = companion[0]
	            else:
	           	plant_grass()
                move(North)
            move(East)
