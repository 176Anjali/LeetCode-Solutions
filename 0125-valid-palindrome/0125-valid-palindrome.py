class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rev=[]
        s=s.lower()
        for i in s:
            if i.isalnum():
                rev.append(i)
        st=" ".join(rev)
        if st==st[::-1]:
            return True
        else:
            return False
