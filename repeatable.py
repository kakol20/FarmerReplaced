def Till():
    if not is_over(Grounds.Soil):
        till()


def useFertilizer():
    trade(Items.Fertilizer)
    use_item(Items.Fertilizer)


def checkSeeds(size, entity, buySeeds):

    entityList = [Entities.Carrots, Entities.Pumpkin]
    seedsList = [Items.Carrot_Seed, Items.Pumpkin_Seed]
    inventory = get_inventory()

    seedCost = 1
    minCost = 50
    for i in range(len(entityList)):
        if entity == entityList[i]:
            seedCost = get_cost(seedsList[i])
            break

    for slot in inventory:
        item = slot[0]
        amount = slot[1]

        if entity == entityList[0]:  # For planting carrots
            if item == Items.Hay and amount <= seedCost[1][1] * minCost:
                runLoop(20, [size, Entities.Grass])
            elif item == Items.Wood and amount <= seedCost[0][1] * minCost:
                runLoop(20, [size, Entities.Bush])

        elif entity == entityList[1]:  # For planting pumpkins
            if item == Items.Carrot and amount <= seedCost[0][1] * minCost:
                runLoop(50, [size, Entities.Carrots])

    trade(seedsList[i], buySeeds)
