def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # area = (r - l) * min(height[l],height[r])
    max_area = 0
    # we start from the widest possible area, to MAXIMISE area
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        max_area = max(max_area, area)
        # we move the pointer with the smallest height since, it is the bottle neck
        if height[r] < height[l]:
            r -= 1
        else:
            l += 1
    return max_area
