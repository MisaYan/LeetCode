class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        word_set = set(words)
        for word in sorted(words, key=lambda x: (-len(x), x)):
            for i in range(1, len(word)+1):
                if word[:i] not in word_set:
                    break
            else:
                return word
        return ""
