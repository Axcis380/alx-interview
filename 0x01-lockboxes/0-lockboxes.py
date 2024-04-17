#!/usr/bin/python3
"""Function to check if all lockboxes can be opened"""

def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return False

    unlocked = set([0])  # Start with the key to the first box
    for box_id, box in enumerate(boxes):
        if box_id in unlocked:
            unlocked.update(box)  # Add keys from the current box to unlocked

    return len(unlocked) == n

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
