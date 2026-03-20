class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map = Counter(chars)
        total_length = 0
        
        for word in words:

            word_count = Counter(word)
            valid = True

            for ch in word_count:
                if word_count[ch] > char_map[ch]:
                    valid = False
                    break

            if valid:
                total_length += len(word)

        return total_length

