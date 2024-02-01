from collections import defaultdict


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    hashmap = {}
    result = []
    # count the occurance for each item
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    # loop through hashmap and store count as index of list
    # we have a bounded list of max length k because in the worst case,
    # each item in k only occurs once
    bounded_list = defaultdict(list)
    for key, value in hashmap.items():
        bounded_list[value].append(key)
    # loop through list backewards (highest to lower) to see the most occuring
    # we don't care about 0 since nothing in the bounded_list will occur 0 times
    for i in range(len(nums), 0, -1):
        items = bounded_list[i]
        for item in items:
            result.append(item)
            if len(result) == k:
                return result


# O(n)
