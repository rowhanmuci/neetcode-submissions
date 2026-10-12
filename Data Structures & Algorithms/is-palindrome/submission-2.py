class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for c in s :
            if c.isalnum():
                result.append(c.lower())
        s = "".join(result)
        return s == s[::-1]