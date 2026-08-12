class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            rem = prefix % k

            if rem in count:
                res += count[rem]

            count[rem] = count.get(rem, 0) + 1

        return res
        