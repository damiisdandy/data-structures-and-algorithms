# class Solution:
#     def encode(self, strs):
#         output = ""
#         for word in strs:
#             sub_output = ""
#             for c in word:
#                 sub_output += f"{ord(c)}-"
#             output += f"{sub_output}/"
#         return output

#     def decode(self, s):
#         words = s.split("/")[:-1]
#         result = []
#         for w in words:
#             characters = w.split("-")[:-1]
#             word = ""
#             for c in characters:
#                 word += chr(int(c))
#             result.append(word)
#         return result
#
# O(nm) where m is the length of word


class Solution:
    def encode(self, strs):
        output = ""
        for s in strs:
            output += f"{len(s)}#{s}"
        return output

    def decode(self, s):
        result = []
        i = 0
        j = 1
        while i < len(s):
            # since the first characters are the lenght of the string
            # lets find the end of length by hitting the first '#'
            while s[j] != "#":
                j += 1
            # get length
            length = s[i:j]
            # set i to the start of the word
            i = j + 1
            # set j to the end of the word
            j = i + int(length)
            word = s[i:j]
            result.append(word)
            # set i and j to the beginning of the next word's length
            i = j
        return result


# O(n)
