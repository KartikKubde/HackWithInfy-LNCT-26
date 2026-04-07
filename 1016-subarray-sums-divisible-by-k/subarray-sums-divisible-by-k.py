class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        sum = 0
        f = defaultdict(int)
        f[0] = 1

        for i in range(n):
            sum += nums[i]
            rem = sum % k 
            if(rem<0):
                rem = rem + k
            ans += f[rem]
            f[rem] += 1

        return ans