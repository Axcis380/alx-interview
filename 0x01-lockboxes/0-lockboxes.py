#!/usr/bin/python3
"""Function to check if all lockboxes can be opened"""


def canUnlockAll(boxes):
    unlocked = set()

    for box_id in range(len(boxes) - 1, -1, -1):
        box = boxes[box_id]
        if len(box) == 0 or box_id in unlocked:
            unlocked.add(box_id)
        for key in box:
            if key < len(boxes):
                unlocked.add(key)
        if len(unlocked) == len(boxes):
            return True
    return False
