def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    # since we only want alphanumerics we want each character to be in the range of the following unicodes
    def isAlphanumeric(c):
        return (
            (ord("A") <= ord(c) <= ord("Z"))
            or (ord("a") <= ord(c) <= ord("z"))
            or (ord("0") <= ord(c) <= ord("9"))
        )

    # start pointers from start and end of string
    i = 0
    j = len(s) - 1
    while i < j:
        # if its not alphanumeric ignore it
        while not isAlphanumeric(s[i]) and i < j:
            i += 1
        while not isAlphanumeric(s[j]) and i < j:
            j -= 1
        # if its equal proceed till the loop is over
        if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        # if the characters aren't equal, return False
        else:
            return False
    # if loop completes, it is valid
    return True
