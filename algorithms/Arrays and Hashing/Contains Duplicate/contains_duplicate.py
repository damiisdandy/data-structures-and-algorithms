def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hashmap = {}
    for i in nums:
        # if it exists return true
        if hashmap.get(i):
            return True
        # if new, assign true
        else:
            hashmap[i] = True
    # if all numbers gets store and none is referenced, no duplicates where found
    return False


# O(n)
