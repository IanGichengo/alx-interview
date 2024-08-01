def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)

    # A list to track which boxes are opened
    opened = [False] * n

    # A queue to manage the boxes to explore
    queue = [0]

    # The first box is opened initially
    opened[0] = True

    while queue:
        # Get the next box to explore
        current_box = queue.pop(0)

        # Get all the keys in the current box
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                queue.append(key)

    # Return True if all boxes are opened, otherwise False
    return all(opened)
