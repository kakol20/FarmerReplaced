def goto(x, y):
    yDist = get_pos_y() - y  # Positive if drone is north of the target space
    xDist = get_pos_x() - x  # Positive if drone is east of the target space
    halfWorldSize = get_world_size()/2
    while get_pos_y() != y:
        if yDist >= halfWorldSize or (-halfWorldSize <= yDist and yDist < 0):
            move(North)
        else:
            move(South)
    while get_pos_x() != x:
        if xDist >= halfWorldSize or (-halfWorldSize <= xDist and xDist < 0):
            move(East)
        else:
            move(West)
