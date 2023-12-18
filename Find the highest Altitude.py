class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt=[]
        i = 0
        j = 1
        sum = 0
        alt.append(sum)
        sum = gain[i]
        alt.append(gain[i])
        while i<len(gain) and j<len(gain):
            sum = sum + gain[j]
            alt.append(sum)
            j+=1
        return max(alt)
