class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1

        while i<j:
            sum1 = nums[i] + nums[j]

            if sum1 == target:
                 return [i+1,j+1]
            elif sum1>target:
                j-=1
                    
            else:
                 i+=1


                
        






            
              
        