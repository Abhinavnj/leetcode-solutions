class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        :s: str
        :rVal: bool
        """

        s = ''.join(i for i in s if i.isalnum()).lower()
        return s == s[::-1]

        # INITIAL:
        # s = ''.join(i for i in s if i.isalnum()).lower()
        # print(s)
        # i, j = 0, len(s) - 1
        # while i <= j:
        #     if s[i] != s[j]:
        #         return False
        #     i += 1
        #     j -= 1
            
        # return True