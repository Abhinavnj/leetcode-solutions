from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    """
    :s: str
    :t: str 
    :rVal: bool
    """

    return Counter(s) == Counter(t)