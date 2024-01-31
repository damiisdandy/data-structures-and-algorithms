def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # hashmap to store number and their indexes
    hashmap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        # check if difference doesn't exists, it means we've not come across a value that adds up in the past
        if hashmap.get(diff) is None:
            hashmap[nums[i]] = i
        # if difference exists, return the index of that difference and the current index
        else:
            return [hashmap[diff], i]
