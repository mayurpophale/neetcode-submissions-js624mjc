class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for word in arr:
            freq[word] = freq.get(word, 0) + 1
        for num in arr:
            if freq[num] == 1:
                k -=1
                if k==0:
                    return num
                
        return ""