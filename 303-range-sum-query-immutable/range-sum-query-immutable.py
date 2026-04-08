class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        pre_sum = 0
        for i in nums:
            pre_sum += i
            self.prefix.append(pre_sum)

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix[right]

        if(left>0):
            l = self.prefix[left-1]
        else:
            l = 0

        return r-l
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)