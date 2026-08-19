class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre,max_pre = 0,0
        curr = 0
        res = 0
        for  n in nums:
            curr+=n
            res =  max(res,abs(curr - min_pre), abs(curr - max_pre))
            min_pre =min(min_pre,curr)
            max_pre =max(max_pre,curr)


        return res




        