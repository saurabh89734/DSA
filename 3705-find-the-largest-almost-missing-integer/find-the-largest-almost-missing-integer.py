class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)

        count = Counter(nums)

        # Case 1
        if k == 1:
            ans = -1

            for num in nums:
                if count[num] == 1:
                    ans = max(ans, num)

            return ans

        # Case 2
        if k == n:
            return max(nums)

        # Case 3
        ans = -1

        if count[nums[0]] == 1:
            ans = max(ans, nums[0])

        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans