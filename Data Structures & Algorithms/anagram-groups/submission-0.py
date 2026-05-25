from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for word in strs:
            # sort characters
            key = "".join(sorted(word))

            # add original word
            groups[key].append(word)

        return list(groups.values())