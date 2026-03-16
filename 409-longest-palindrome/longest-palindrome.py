class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        map = defaultdict(int)
        odd_found = False

        for i in s:
            map[i] += 1

        for i in map.keys():
            if map[i]%2 == 0:
                ans += map[i]
            else:
                ans += map[i] - 1
                odd_found = True
        
        if odd_found:
            ans += 1

        return ans


