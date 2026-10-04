class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += chr(len(word)) + word
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            n = ord(s[i])
            res.append(s[i+1:i+n+1])
            i += n + 1
        
        return res