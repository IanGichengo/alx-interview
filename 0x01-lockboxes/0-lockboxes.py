#!/usr/bin/python3
""" determines if all boxes can be opened """


def canUnlockAll(boxes):
    """ Number of boxes """
    n = len(boxes)

    opened = [False] * n

    queue = [0]

    opened[0] = True

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    return all(opened)
