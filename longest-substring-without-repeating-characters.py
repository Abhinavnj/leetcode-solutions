def lengthOfLongestSubstring(s):
    """
    :s: str
    :rVal: int
    """
    used = {}
    maxLen = start = 0
    for i, c in enumerate(s):
        # Second condition ensures that you don't go into if and reset
        # just because you have seen it before. You don't want to reset
        # if the start is after where you last saw the "repeated" character.
        if c in used and start <= used[c]:
            # Does not actually restart loop from used[c] + 1, but keeps track
            # of location where the current unrepeating substring starts
            start = used[c] + 1
        else:
            maxLen = max(maxLen, i - start + 1)
        
        used[c] = i
    
    return maxLen