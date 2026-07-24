class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
          
        ans = left = right = 0
        count_zero = 0

        while right < len(nums):
            if nums[right] == 0:
                count_zero +=1
            while count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
          
            ans= max (ans,right-left+1)
            right +=1

        return ans
        
         
      

        





        
        