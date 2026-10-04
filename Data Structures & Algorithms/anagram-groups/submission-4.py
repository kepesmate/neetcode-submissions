class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        groups = {}

        for word in strs:
            key = str(sorted(word))
            if key in groups.keys():
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())