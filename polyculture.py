def companion_planting(size, water, buySeeds):
    field = field_grid_init(size)
    while True:
        for x in range(size):
            for y in range(size):
	            companion = get_companion()
	            curCrop = field[x][y]
	            if can_harvest():
	            	harvest()
	            	if curCrop == Entities.Carrots:
	            		Till()
	            		checkSeeds(size, curCrop, buySeeds)
	            	plant(curCrop)

	            	if water > 0:
						if get_water() <= water:
							use_item(Items.Water_Tank)

	            	field[companion[1]][companion[2]] = companion[0]
	            else:
	           		plant_grass()
                move(North)
            move(East)