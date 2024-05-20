
#Given a roman numeral, convert it to an integer
class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"O":0}
        sm=0
        i=0
        while i<=len(s)-1:
            cur=s[i]
            try:
                nxt=s[i+1]
            except:
                nxt="O"
            if d[cur]>=d[nxt]:
                total=d[cur]
                sm=sm+total
                i=i+1
            elif d[cur]<d[nxt]:
                total=d[nxt]-d[cur]
                sm=sm+total
                i=i+2
        return sm