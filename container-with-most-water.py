def maxArea(height):
    """
    height: List[int]
    rVal: int
    """
    # The minimum of the two heights can be discarded after getting
    # the area because it will never support a higher water level
    # and no longer needs to be considered.
    
    # Start pointers from left and right and close in while discarding
    # lines that will no longer be useful.
    
    # Calculate area by multiplying (j - i), the width if the current
    # container by the minimum of the heights
    
    i, j = 0, len(height) - 1
    area = 0
    while i < j:
        area = max(area, (j - i) * min(height[i], height[j]))
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return area