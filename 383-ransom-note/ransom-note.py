class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        have = defaultdict(int)
        m = len(magazine)

        for c in magazine:
            have[c] += 1

        for c in ransomNote:
            if c not in have:
                return False
            elif have[c] == 1:
                del have[c]
            else:
                have[c] -= 1
        
        return True
