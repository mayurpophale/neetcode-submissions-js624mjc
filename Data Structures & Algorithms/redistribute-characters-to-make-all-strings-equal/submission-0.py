class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        freq = {}

        for word in words:
            for ch in word:
                freq[ch] = freq.get(ch,0) + 1

        for count in freq.values():
            if count % n !=0:
                return False
        return True