class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            reminder = prefix % k
            if reminder in count:
                ans +=count[reminder]
            count[reminder] = count.get(reminder,0)+1
            
        return ans



    