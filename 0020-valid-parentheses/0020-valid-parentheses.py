class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack or stack.pop()!=pairs[i]:
                    return False
        return len(stack)==0
