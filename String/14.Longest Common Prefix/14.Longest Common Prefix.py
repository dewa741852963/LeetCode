class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        add=''
        j=0
        res = min(strs, key=len, default='')
        for i in range(len(res)):
            if j==1:
                break
            for k in range(len(strs)-1):
                if strs[k][i] == strs[k+1][i]:
                    if k+2==len(strs):
                        add+=str(strs[k][i])
                else:
                    j=1
                    break
        if len(strs)==1:
            add=strs[0]
            
        return(add)
