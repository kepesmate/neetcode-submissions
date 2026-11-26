class Solution:
    def isValid(self, s: str) -> bool:
        start = ["(", "{", "["]
        end   = [")", "}", "]"]
        pr_map = {")": "(", "}": "{", "]": "["}

        stack = []

        for ch in s:
            if ch in start:
                stack.append(ch)
            elif ch in end:
                if len(stack) == 0 or stack[-1] != pr_map[ch]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) != 0:
            return False
        return True