class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return divmod(s.count(letter)*100, len(s))[0]