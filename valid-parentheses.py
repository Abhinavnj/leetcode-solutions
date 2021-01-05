def isValid(s):
    """
    :s: str
    :rVal: bool
    """

    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            stack.append(char)
            
    return not stack
    
    # INITIAL ATTEMPT:
    # stack = []
    # opening = ['(', '[', '{']
    # closing = [')', ']', '}']
    
    # for char in s:
    #     if char in opening:
    #         stack.append(char)
    #     elif stack and char == closing[opening.index(stack[-1])]:
    #         stack.pop()
    #     else:
    #         return False

    # return not stack