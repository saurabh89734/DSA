class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        left = 0
        res = 0

        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res