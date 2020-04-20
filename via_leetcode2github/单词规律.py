class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        return list(map(pattern.index, pattern)) == list(map(words.index, words))
