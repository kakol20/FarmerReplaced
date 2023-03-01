def createMaze():
    repeat = True
    while repeat:
        clear()
        plant(Entities.Bush)
        useFertilizer()
        repeat = findTreasure()
