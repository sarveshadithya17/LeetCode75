class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        # Create a dictionary to store the count of each element
        count_dict = {}
        
        # Count occurrences of each element
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        # Check if the counts are unique
        unique_counts = set(count_dict.values())
        
        return len(unique_counts) == len(count_dict)
