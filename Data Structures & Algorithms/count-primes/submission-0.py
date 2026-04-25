class Solution:
    def countPrimes(self, n: int) -> int:
        table = [True]*n
        if n<2:
            return 0
        table[0],table[1] = False,False
        i=2
        while (i<n):
            if table[i] == True:
                for j in range(i*2,n,i):
                    table[j] = False
            i +=1

        return table.count(True)