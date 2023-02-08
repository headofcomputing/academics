
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    numbers=[]
    count = 1
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] != s[j]:
                count += 1
            else:
                numbers.append(count)
                count = 1
    return max(numbers)
print(lengthOfLongestSubstring("abcabcbb"))
