class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        n = len(s)

        while i < n:
            delimiter_idx = s.find("#", i)
            length = int(s[i:delimiter_idx])

            start = delimiter_idx + 1
            end = start + length
            res.append(s[start:end])

            i = end

        return res