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

nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    
if len(nums) == 3:
    if sum(nums) == 0:
        print([nums])
else:    
    dictpairs = dict()
    dicttriples = dict()
    result = []
    templist = [x for x in nums]
    contador = 0
    for index, num in enumerate(nums):
        del templist[0]
        contador += 1
        for index2,num2 in enumerate(templist):
            combination = "".join(sorted(str(index) + str(index2+contador)))
            if combination not in dictpairs.keys():
                dictpairs[combination] = sorted([num,num2])
    for index,num in enumerate(nums):
        for key,lista in dictpairs.items():
            if str(index) not in key:
                dicttriples["".join(sorted(str(index)+str(key)))] = sorted(lista+[num])
    for lista in dicttriples.values():
        if sum(lista) == 0:
            if lista not in result:
                result.append(lista)

print(result)