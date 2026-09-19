class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char1=list(s)
        char2=list(t)
        char1.sort()
        char2.sort()
        if char1 == char2:
            return True 
        else:
            return False