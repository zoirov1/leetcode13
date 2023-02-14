class Solution:
    def romanToInt(self, s: str) -> int:
        dct={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ls=[]
        ls.extend(s)
        s_m=0
        if len(ls)==1:
            return dct[ls[0]]
        i=0
        while i<len(ls):
            if i+1<len(ls):
                if dct[ls[i]]<dct[ls[i+1]]:
                    s_m+=dct[ls[i+1]]-dct[ls[i]]
                    i+=1
                else:
                    s_m+=dct[ls[i]]
            else:
                s_m+=dct[ls[i]]
            i+=1
        return s_m

        