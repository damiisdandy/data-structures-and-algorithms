from collections import defaultdict


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    hashmap = defaultdict(int)
    # if lengths aren't equal then it can't be valid
    # also to handle edgecases where all elements of t is in s
    if len(s) != len(t):
        return False
    # store the count of each occurance
    for i in s:
        hashmap[i] += 1
    # if found subtract, it not found of element count is 0 return False
    for j in t:
        if hashmap[j]:
            hashmap[j] -= 1
        else:
            return False
    return True


# O(n)
