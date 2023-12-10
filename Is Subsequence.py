class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_split = list(s)
        t_split = list(t)
        i = 0
        j = 0
        count = 0
        while i < len(s_split) and j < len(t_split):
            if s_split[i] == t_split[j]:
                count += 1
                i +=1
            j += 1
        return count == len(s_split) 
