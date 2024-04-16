#!/usr/bin/python3

"""Lockboxes Contains method that finds the keys to
open other lockboxes
"""

def canUnlockAll(boxes):
    """
    Determines if all lockboxes can be opened.
    Args:
        boxes (list): A list of lists representing lockboxes and their keys.
    Returns:
        bool: Tru if all lockboxes can be opened, False otherwise.
    """
    unlocked = set()
    num_boxes = len(boxes)

    for box_id, box in enumerate(boxes):
        if not box or box_id == 0:
            unlocked.add(box_id)
        for key in box:
            if 0 <= key < num_boxes and key != box_id:
                unlocked.add(key)
        if len(unlocked) == num_boxes:
            return True
    
    return False
