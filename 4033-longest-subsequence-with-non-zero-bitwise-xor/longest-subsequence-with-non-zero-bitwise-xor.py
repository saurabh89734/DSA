class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)

        total_xor = 0
        zero_count = 0

        for num in nums:
            total_xor ^= num

            if num == 0:
                zero_count += 1

        # Case 1
        if total_xor != 0:
            return n

        # Case 2
        # XOR = 0, but at least one non-zero exists
        if zero_count != n:
            return n - 1

        # Case 3
        # All elements are zero
        return 0