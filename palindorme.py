import re
def alphnum(s):
    processed = s.lower()
    res = re.sub(r'[^a-z0-9]', '', processed)
    return res


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    for i in range(len(s)):

        if alphnum(s[i]) == '':
            continue

        for j in range(len(s) - 1, -1, -1):
            print(i,j)
            if alphnum(s[j]) == '':
                continue

            elif alphnum(s[i]) != alphnum(s[j]):
                return False
            else:
                continue
    return True

print(isPalindrome('I ama;s;'))