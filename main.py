def start():
    clear()
    do_a_flip()

    treasure = False

    poly = False

    size = get_world_size()
    entity = Entities.Pumpkin
    water = 0.3
    buySeeds = size * size

    while True:
        if treasure == True:
            startMaze()
        elif poly == True:
            companion_planting(size, water, 1)
        else:
            if entity == Entities.Pumpkin:
                replantPumpkin(size, entity, 0, buySeeds)
            else:
                replant(size, entity, water, buySeeds)
