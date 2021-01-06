def longestPalindrome(self, s: str) -> str:
    """
    s: str
    rVal: str
    T: O(n)
    """

    # If empty or len = 1 or s is a palindrome
    if len(s) <= 1 or s == s[::-1]:
        return s
    
    # 'r' holds the number of characters in the current longest palindrome
    r, start = 1, 0
    for i in range(1, len(s)):
        oddStart = i-r-1
        evenStart = i-r
        
        odd = s[oddStart:i+1]
        even = s[evenStart:i+1]
        
        # If the start index of 'odd' is >= 0 and
        # odd is a palindrome
        if oddStart >= 0 and odd == odd[::-1]:
            start = oddStart
            r += 2
        # Else if even is a palindrome
        elif even == even[::-1]:
            start = evenStart
            r += 1
    
    return s[start: start+r]