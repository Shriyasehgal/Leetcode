class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        cur = chars[0]
        i = 0
        j = 1
        while i < len(chars):
            if j < len(chars) and cur == chars[j]:
                chars.pop(j)
                count+=1
            else:
                idx = j
                if count > 1:
                    while count != 0:
                        temp = count % 10
                        count //=10
                        chars.insert(idx,str(temp))
                        j+=1
                i = j
                if j < len(chars):
                    cur = chars[j]
                    j+=1
                    count = 1
        return len(chars)
        
        
                    
                    
                
        