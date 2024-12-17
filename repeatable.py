def Till():
	if get_ground_type() != Grounds.Soil:
		till()

# -----

def useFertilizer():
	if num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)

# -----
	
def runLoop(times, list):
	for i in range(times):
		replant(list[0], list[1])