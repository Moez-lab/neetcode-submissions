class Solution:
    def encode(self, strs: list[str]) -> str:
        # e.g., ["Hello", "World"] -> "5#Hello5#World"
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            hash_idx = s.find("#", i)
            length = int(s[i:hash_idx])
            
            # Read exactly 'length' characters ahead
            res.append(s[hash_idx + 1 : hash_idx + 1 + length])
            
            # Jump past this word
            i = hash_idx + 1 + length
            
        return res