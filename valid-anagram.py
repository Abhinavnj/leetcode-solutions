from collections import Counter

def isAnagram(s, t):
    """
    s: str
    t: str 
    rVal: bool
    """

    return Counter(s) == Counter(t)