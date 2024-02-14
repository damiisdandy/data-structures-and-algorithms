def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    # hashmap = {}
    # result = set()
    # for idx, value in enumerate(nums):
    #     hashmap[value] = idx
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i == j:
    #             continue
    #         # iv + jv + kv = 0
    #         k = -nums[i] - nums[j]
    #         if k in hashmap:
    #             if i == hashmap[k] or j == hashmap[k]:
    #                 continue
    #             output = [nums[i], nums[j], k]
    #             output.sort()
    #             result.add(tuple(output))
    # return [list(v) for v in result]

    nums.sort()
    result = []
    for idx, k in enumerate(nums):
        # avoid duplicates for starting value
        if idx > 0 and nums[idx] == nums[idx - 1]:
            continue
        # use two pointers for the rest of the array and avoid duplication
        left, right = idx + 1, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right] + k
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                result.append([k, nums[left], nums[right]])
                # we only need to update one pointer since the conditions
                # above will help us update the rest
                left += 1
                # avoid inner duplicates
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result
