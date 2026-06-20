class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            ch = [0] * 26
            for c in s:
                ch[ord(c) - ord("a")] += 1
            key = tuple(ch)
            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(s)

        return list(anagrams.values())
