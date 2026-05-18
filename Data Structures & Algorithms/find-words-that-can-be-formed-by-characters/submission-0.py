from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        ans = 0

        for word in words:
            word_count = Counter(word)
            can_form = True

            for ch in word_count:
                if word_count[ch] > char_count[ch]:
                    can_form = False
                    break

            if can_form:
                ans += len(word)

        return ans