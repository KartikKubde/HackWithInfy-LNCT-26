class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # using hashmap
        n = len(nums)
        hashmap = defaultdict(int)

        for i in range(n):
            remain = target - nums[i]

            if remain in hashmap:
                return[hashmap[remain],i]
            hashmap[nums[i]] = i



        
        
        
        
        
        
        # using 2 pointer + sorting
        # nums = sort(nums)                         #[2,7,11,15]
        # i = 0				    
        # j = len(nums) - 1


        # while(i<j):
        #     sum = nums[i] + nums[j]
        #     # ans = []	    

        #     if(sum==target):
        #         # ans.append(i)
        #         # ans.append(j)
        #         return [i,j]

        #     elif(sum > target):
        #         j -= 1

        #     else:
        #         i += 1

        # return -1
