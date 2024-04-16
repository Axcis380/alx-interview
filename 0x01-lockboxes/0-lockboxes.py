def canUnlockAll(boxes):
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
