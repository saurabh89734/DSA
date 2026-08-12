class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remi = {0:-1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r  not in remi:
                remi[r] = i
            elif i - remi[r] > 1:
                return True
        return False


                
           
        

        
        