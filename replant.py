#---------- General

def replant(size, entity, water, buySeeds):
    for x in range(size):
        for y in range(size):

            if can_harvest():
                harvest()
                if entity == Entities.Carrots:
                    Till()
                    if buySeeds > 0 and x == 0 and y == 0:
                        checkSeeds(size, entity, buySeeds)

                if entity == Entities.Bush:
                    if x % 2 == 0 and y % 2 == 1 or x % 2 == 1 and y % 2 == 0:
                        plant(Entities.Tree)
                        useFertilizer()

                if entity != Entities.Grass:
                    plant(entity)

                    if get_water() <= water:
                        use_item(Items.Water_Tank)
            # y end
            move(North)
        # x end
        move(East)


#-------- Pumpkins

def replantPumpkin(size, entity, buySeeds):
    field = fieldGrid(size, False)

    for z in range(3):
        for x in range(size):
            for y in range(size):

                if not is_over(entity):
                    Till()
                    if buySeeds > 0 and z == 0 and x == 0 and y == 0:
                        checkSeeds(size, entity, buySeeds)
                    plant(entity)

                    if z > 0:
                        field[x][y] = True
                else:
                    if z > 0 and can_harvest():
                        field[x][y] = False

                move(North)
            # y end
            move(East)
        # x end
    # z end
    fillRemaining(size, entity, field)

    harvest()
    goto(0, 0)


def fillRemaining(size, entity, field):
    keepChecking = True
    while keepChecking:
        hasLeft = False
        for x in range(size):
            for y in range(size):
                if field[x][y] == True:
                    hasLeft = True
                    goto(x, y)
                    if not is_over(entity):
                        Till()
                        plant(entity)
                        useFertilizer()
                    elif can_harvest():
                        field[x][y] = False

        keepChecking = hasLeft
