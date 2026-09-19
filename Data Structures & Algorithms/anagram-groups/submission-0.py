class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for word in strs:
            char=[0]*26
            for cha in word:
                char[ord(cha)-ord("a")]+=1
            key = tuple(char)
            if key not in anagrams:
                anagrams[key]=[]
            anagrams[key].append(word)
        return list(anagrams.values())
