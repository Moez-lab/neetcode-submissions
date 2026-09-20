class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while (left<right):
                s = nums[i]+nums[left]+nums[right]
                if s == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif s<0:
                    left+=1
                else:
                    right-=1
        output =list(map(list, set(map(tuple, result))))
        return output
