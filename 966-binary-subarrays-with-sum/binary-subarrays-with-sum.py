class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum = 0
        dict = defaultdict(int)
        dict[0] = 1
        res = 0

        for i in range(len(nums)):
            sum += nums[i]
            q = sum - goal
            f = dict[q]
            res += f
            dict[sum] += 1

        return res