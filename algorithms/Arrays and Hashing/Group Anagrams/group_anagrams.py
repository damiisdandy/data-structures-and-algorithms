from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # hashmap = defaultdict(list)

    # for s in strs:
    #     # declaring a list for all characters in the alphabet
    #     char_count = [0] * 26  # 26 characters in the alphabet

    #     # for each characters in the string count its occurance
    #     # and map it to the index in `char_count`
    #     for c in s:
    #         # we are subtracting the unicode values since if "a" is 80, then (80 - 80) index[0] ("a"),
    #         # (81 - 80) index[1] ("b") , etc..
    #         # we use only lowercase letters because the constraint stats the words are in lowercase
    #         char_count[ord(c) - ord("a")] += 1
    #     # get the unique character count config for the word and its anagrams
    #     hashmap[tuple(char_count)].append(s)
    # return a list of values which are the grouped list of anagrams
    # result = [k for k in hashmap.values()]
    # return result

    # 0(nm) where m is the lenght of the string

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


# O(n * mlog(m)) where m is the lenght of the string
# technically O(nm) is faster than O(n * mlog(m)) but due to the constraints for the questions
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
#
# we are sorted words of length at most 100 characters in length, also the new to convert to a tuple and
# convert to a list from a dict_value (the return value) makes it not only memory inefficient but slightly slower than
# the O(n * mlog(m)) solution
