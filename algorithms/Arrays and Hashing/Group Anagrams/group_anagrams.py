def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    hashmap = {}
    for s in strs:
        # sort word (all anagrams will look the same after sorting)
        s_sorted = "".join(sorted(s))
        if hashmap.get(s_sorted):
            hashmap[s_sorted].append(s)
        else:
            hashmap[s_sorted] = [s]

    result = [k for k in hashmap.values()]
    return result


# O(n * mlong(m)) where m is the lenght of the string
