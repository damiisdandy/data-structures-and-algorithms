def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # we solve this by multiplying every product on the left with the right
    prefix = 1
    result = [prefix]
    # default product prefix for first element is 1
    # loop through and multiple everything that is on the left (prefix)
    for i in range(1, len(nums)):
        prefix *= nums[i - 1]
        result.append(prefix)

    # for [1, 2, 3, 4] result is [1, 1, 2, 6]
    postfix = 1
    # we ignore the last element of the list since the answer is its prefix
    # loop backwards, multiple everything that is on the right (postfix)
    for i in range(len(nums) - 2, -1, -1):
        postfix *= nums[i + 1]
        # result at index i is the previously calculate prefix * postfix
        result[i] *= postfix
    return result


# O(n)
