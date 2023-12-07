class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    # Initialize two variables to positive infinity.
    first = math.inf
    second = math.inf

    # Iterate through the array 'nums'.
    for num in nums:
      # If the current number is less than or equal to 'first',
      # update 'first' to the current number.
      if num <= first:
        first = num
      # If the current number is less than or equal to 'second',
      # update 'second' to the current number.
      elif num <= second:  # first < num <= second
        second = num
      else:
        # If none of the above conditions is met, it means we found
        # a number greater than 'second', and we have an increasing
        # triplet subsequence. Return True.
        return True  # first < second < num (third)

    # If the loop completes without finding an increasing triplet
    # subsequence, return False.
    return False
