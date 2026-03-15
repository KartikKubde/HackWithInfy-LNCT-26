class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = "balloon"

        for ch in text:
            if ch in balloon:
                counter[ch] += 1

        for ch in balloon:
            if ch not in counter:
                return 0

        count_b = counter["b"]
        count_a = counter["a"]
        count_l = counter["l"] // 2
        count_o = counter["o"] // 2
        count_n = counter["n"]

        result = min(count_b, count_a, count_l, count_o, count_n)

        return result