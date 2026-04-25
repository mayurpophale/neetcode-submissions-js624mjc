class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j]:
                        l.append(words[i])
                        pass
        return list(set(l))