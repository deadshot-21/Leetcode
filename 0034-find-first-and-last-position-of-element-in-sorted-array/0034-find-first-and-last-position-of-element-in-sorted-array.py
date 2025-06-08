class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary(isLeft):    
            l, r = 0 , len(nums) - 1
            i = -1
            while l<=r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    i = mid
                    if isLeft:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid]> target:
                    r = mid - 1
                else:
                    l = mid + 1  
            return i         
        return [binary(True),binary(False)]