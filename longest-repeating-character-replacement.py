def characterReplacement(s, k):
    """
    s: str
    k: Lint
    :rVal: int
    """

    # MOVING WINDOW
    
    # 'freq' holds the frequencies of each character in 's'.
    freq = {}
    # 'result' is the answer.
    # 'maxFreq' is the frequency of the character with the maximum
    # frequency in the current window.
    result = maxFreq = 0
    
    # 'end' is the last index in the current window.
    # 'char' is the character in 's' at index 'end'.
    for end, char in enumerate(s):
        # Set frequency of the character to 1 if it is not in freq
        # or add 1 to the current frequency if it exists.
        freq[char] = freq.get(char, 0) + 1
        
        # Set the maxFreq to the frequency of the current character
        # if it is greater than maxFreq currently. We want to keep
        # maxFreq to be the frequency of the character that occurs
        # most times in the window, so we update it if another
        # character's frequency exceeds the current.
        maxFreq = max(maxFreq, freq[char])
        
        # 'result - maxFreq' represents how many characters in the window
        # need to be changed to make all the letters the same. This check
        # ensures that we cannot make more than 'k' changes to the string.
        if result - maxFreq < k:
            # Increase the number of same characters, result, by one if
            # we can still make changes (result - maxFreq < k).
            result += 1
        # In this condition, we are shifting the window since we have exceeded
        # 'k' in the current window.
        else:
            # Subtract 1 from the frequency of the character at the start
            # index of the window, since it will no longer be included in
            # the shifted window.
            freq[s[end - result]] -= 1
            
    return result