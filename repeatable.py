def Till():
	if get_ground_type() != Grounds.Soil:
		till()
		
def useFertilizer():
	if num_items(Items.Fertilizer) > 0 and num_unlocked(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)
		
def useWater(water):
	if get_water() <= water and num_items(Items.Water) >= water and num_unlocked(Items.Water) > 0:
		use_item(Items.Water)