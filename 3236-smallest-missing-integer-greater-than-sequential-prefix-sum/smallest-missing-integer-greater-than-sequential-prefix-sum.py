class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        # Step 1: Find the sequential prefix sum
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break

        # Step 2: Find the smallest missing integer >= prefix_sum
        num_set = set(nums)
        x = prefix_sum
        while x in num_set:
            x += 1

        return x