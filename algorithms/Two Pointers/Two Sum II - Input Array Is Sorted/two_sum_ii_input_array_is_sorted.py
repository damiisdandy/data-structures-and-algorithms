def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    i = 0
    j = len(numbers) - 1
    while i < j:
        total = numbers[i] + numbers[j]
        # if total is greater than target reduce the possible total
        if total > target:
            j -= 1
        # if total is less than target increase the possible total
        elif total < target:
            i += 1
        # if it is equal to target return the indexes
        else:
            return [i + 1, j + 1]
