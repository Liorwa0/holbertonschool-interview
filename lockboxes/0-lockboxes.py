#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    unlocked = set([0])
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == n
