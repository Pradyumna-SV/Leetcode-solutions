class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = [word for word in s.split(" ") if word]
        return len(word[-1])
        