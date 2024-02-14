def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # amount = 0
    # length = len(height)
    # max_left=[0]*length
    # max_right=[0]*length
    # for i in range(length):
    #     if i > 0:
    #         # max left at i is the maximum between, current max left `max_left[i - 1]`
    #         # and previous list value
    #         max_left[i] = max(max_left[i - 1], height[i - 1])
    #         # max right at i is the maximum between, current max right `max_right[i + 1]`
    #         # and foward list value
    #         backwards_index = length - i - 1
    #         max_right[backwards_index] = max(max_right[backwards_index + 1], height[backwards_index + 1])
    # # calculating the amount of water that can be stored is
    # # boundary = min(max_left[i], max_right[i]))
    # # amount of water = boundary - height[i]
    # for i in range(length):
    #     boundary = min(max_left[i], max_right[i])
    #     # we use max here because we don't want to have negative amount of water
    #     amount += max((boundary - height[i]), 0)

    # return amount

    amount = 0
    l, r = 0, len(height) - 1
    max_left = height[l]
    max_right = height[r]
    while l < r:
        # since mex_left is smaller, it'll be the boundary
        if max_left < max_right:
            # notice we did not consider index 0 this is because the water contained is 0, it has no left boundary
            # lets calculate the water for the following (next) index (+1)
            l += 1
            # update max left if the height is greater
            max_left = max(max_left, height[l])
            # we never get a negative value since we are subtracting from the maximum
            # amount of water at that index is the max left minus the current height
            # max left either gets updated to be greater meaning the max_height and height arer equal
            # therefore no water can be stored at that point
            # if max left isn't updated then height is smaller then water can be stored
            amount += max_left - height[l]
        else:
            # notice we did not consider the last index this is because the water contained is 0, it has no right boundary
            r -= 1
            max_right = max(max_right, height[r])
            amount += max_right - height[r]
    return amount
