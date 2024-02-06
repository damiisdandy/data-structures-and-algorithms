def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_set = set(nums)
    length = 0
    # loop through the set so we do not do the same operation twice
    for num in nums_set:
        # check if number is first in it's sequence
        # meaning it has no previous value
        prev_value = num - 1
        if prev_value not in nums_set:
            count = 1
            # while is has a next consecutive value
            while num + count in nums_set:
                count += 1
            # set length to the maximum it has seen
            length = max(length, count)
    return length
