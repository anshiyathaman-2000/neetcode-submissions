class Solution:
    def isValid(self, s: str) -> bool:
        Stack=[]
        closeToOpen={"]":"[",")":"(","}":"{"}
        for c in s:
            if c in closeToOpen:
                if Stack and Stack[-1]==closeToOpen[c]:
                    Stack.pop()
                else:
                        return False
            else:
                Stack.append(c)
        return True if not Stack else  False