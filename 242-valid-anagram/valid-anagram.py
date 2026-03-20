class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for i in s:
            s_map[i] += 1

        for i in t:
            t_map[i] += 1

        if(s_map == t_map):
            return True
        else:
            return False

        