def start():
    clear()
    do_a_flip()

    size = get_world_size()
    entity = Entities.Pumpkin
    water = 0
    buySeeds = True

    while True:
        if entity == Entities.Pumpkin:
            replantPumpkin(size, entity, 0, buySeeds)
        else:
            replant(size, entity, water, buySeeds)


def runLoop(times, list):
    for i in range(times):
        replant(list[0], list[1], 0.8, True)
