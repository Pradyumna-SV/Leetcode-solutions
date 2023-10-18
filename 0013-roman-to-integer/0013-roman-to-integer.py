class Solution:
    def romanToInt(self, s: str) -> int:
        hasht = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        a = []
        for c in s:
            a.append(hasht[c])
        for i in range(len(a)-1):
            if a[i]<a[i+1]:
                a[i] = -a[i]
        return sum(a)