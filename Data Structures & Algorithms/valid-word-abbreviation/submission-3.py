class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m = len(word), len(abbr)
        i = j = 0

        while i < n and j < m:
            if abbr[j] == "0":
                return False
            
            if word[i] == abbr[j]:
                i, j = i + 1, j + 1
            elif abbr[j].isalpha():
                return False
            else:
                num = 0
                while j < m and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            
        return i == n and j == m
