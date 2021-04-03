# Leetcode problem: 1779. Find Nearest Point That Has the Same X or Y Coordinate
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = float("inf")
        ptr = None

        # Go through each point and unpack index, x, y at the same time
        for i, (px, py) in enumerate(points):
            if px != x and py != y:
                continue
            if abs(px - x) + abs(py - y) < dist:
                dist = abs(px - x) + abs(py - y)
                ptr = i
        return -1 if ptr is None else ptr
