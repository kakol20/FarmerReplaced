
def replantPumpkin(size, entity, water, buySeeds):
    for z in range(3):  # go over 3 times to ensure all pumpkins grown
        for x in range(size):
            for y in range(size):

                if not is_over(entity):
                    Till()
                    if buySeeds:
                        checkSeeds(size, entity)
                    plant(entity)

                if water > 0:
                    if get_water() <= water:
                        use_item(Items.Water_Tank)

                move(North)
            # y end
            move(East)
        # x end
    # z end
    harvest()


def replant(size, entity, water, buySeeds):
    for x in range(size):
        for y in range(size):

            if can_harvest():
                harvest()
                if entity == Entities.Carrots:
                    Till()
                    if buySeeds:
                        checkSeeds(size, entity)

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
