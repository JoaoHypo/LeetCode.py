'''
3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

#In this code, was the first time i had contact with pointers in python, since 
# it's not a native function of the language, we need to create a pointer alternative
# that in the end works as the same.

def threeSum(self, nums: list[int]) -> list[list[int]]:
    # If the length of the input array is less than 3, return an empty list
    if len(nums) <3:
        return []

    # Sort the input array
    nums.sort()
    # Initialize an empty list to store the triplets
    result = []

    # Iterate through the elements of the input array (skipping the first and the last element)
    for i in range(len(nums) - 2):
        # Skip the current iteration if the current element is the same as the previous one
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Set the "left" pointer to be the element next to the current one
        left = i + 1
        # Set the "right" pointer to be the last element of the input array
        right = len(nums) - 1

        # Move the two pointers towards each other until they meet
        while left < right:
            # Calculate the sum of the elements pointed by the three pointers
            total = nums[left] + nums[right] + nums[i]
            # If the sum of the elements is 0, add the three elements to the result list
            if total == 0:
                result.append([nums[i],nums[left],nums[right]])
                # Move both the "left" and "right" pointers
                left += 1
                right -= 1
                # Skip duplicates by checking if the elements pointed by the pointers are the same as the previous ones
                # If the element pointed by the "left" pointer is the same as the previous one, move the "left" pointer
                while nums[left] == nums[left -1] and left < right:
                    left += 1
                # If the element pointed by the "right" pointer is the same as the previous one, move the "right" pointer
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1 

            # If the sum of the elements is less than 0, move the "left" pointer right
            elif total < 0:
                left += 1
            # If the sum of the elements is greater than 0, move the "right" pointer left
            else:
                right -= 1

    # Return the "result" list containing all the triplets that sum to 0
    return result
