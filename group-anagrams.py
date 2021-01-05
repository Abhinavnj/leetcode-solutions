def groupAnagrams(strs):
    """
    strs: List[str]
    rVal: List[List[str]]
    T: O(n)
    """

    # Values of 'groups' are the lists of words that are anagrams
    # corresponding to the alphabetically sorted version of each word.
    groups = {}
    
    for w in strs:
        # Set 'key' equal to the sorted version of the string
        key = ''.join(sorted(w))
        # **Could also use tuple as key since 'list' is not hashable
        # key = tuple(sorted(w))
        
        # Set the value at this key as the words that match it when
        # they are sorted. The words are stored in a list, which is
        # the value.
        groups[key] = groups.get(key, []) + [w]
    
    # The values of the dictionary are stored in a list, which is a
    # list of lists containing the anagram groups in this case.
    return groups.values()