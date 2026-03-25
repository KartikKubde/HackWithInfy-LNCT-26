class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = defaultdict(int)
        st = []
        n = len(nums2)
        # g = len(nums1)
        ans = []

        for j in range(n-1,-1,-1):
            while(st and st[-1] < nums2[j]):
                st.pop()
            
            if(len(st) == 0):
                m[nums2[j]] = -1
            else:
                m[nums2[j]] = st[-1]

            st.append(nums2[j])

        for i in range(len(nums1)):
            ans.append(m[nums1[i]])

        return ans