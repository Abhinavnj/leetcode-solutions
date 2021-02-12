def lengthOfLongestSubstring(s):
    """
    s: str
    rVal: int
    """

    used = {} # dict to track the location where each distinct character in s was last seen
    maxLen = start = 0
    for i, c in enumerate(s):
        # Second condition ensures that you don't go into if and reset
        # just because you have seen it before. You don't want to reset
        # if the start is after where you last saw the "repeated" character.

        # Restart the substring location if c is found again to where you
        # last found it + 1, since c is the first character that has repeating
        # since then
        if c in used and start <= used[c]:
            # Does not actually restart loop from used[c] + 1, but keeps track
            # of location where the current unrepeating substring starts
            start = used[c] + 1
        else:
            # Set to the max of previous max length or the current length
            # being tracked
            maxLen = max(maxLen, i - start + 1)
        
        # Set new location for where c was last found, or the first location
        # if this is the first time seeing the character
        used[c] = i
    
    return maxLen
