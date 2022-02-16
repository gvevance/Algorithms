''' 
https://leetcode.com/problems/3sum-closest/

3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 10^4 

Solution : 2 pointer method. O(n^2).
 
'''

def threeSumClosest(nums , target) :
    
    if len(nums) == 3 :
        return nums[0]+nums[1]+nums[2]
    
    nums.sort()
    closest = 1e9
    for i in range(len(nums)-2) :
        l,r = i+1,len(nums)-1
        while(r>l) :
            if nums[i]+nums[l]+nums[r] == target :
                return target
            
            elif nums[i]+nums[l]+nums[r] < target :
                if abs(target - (nums[i]+nums[l]+nums[r])) < abs(closest - target) :
                    closest = nums[i]+nums[l]+nums[r]
                l += 1
                
            else :
                if abs(nums[i]+nums[l]+nums[r] - target) < abs(closest - target) :
                    closest = nums[i]+nums[l]+nums[r]
                r -= 1
    
    return closest

if __name__ == "__main__" :

    A = [1,2,3,4,5,6]
    target = 30
    print(threeSumClosest(A,target))