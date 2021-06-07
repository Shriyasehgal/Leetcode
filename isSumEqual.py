def isSumEqual( firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        f=0
        s=0
        t=0
        
        first=list(firstWord)
        for i in range(len(first)):
            f=f+ord(first[i])-97        
        
        second=list(secondWord)
        for i in range(len(second)):
            s=s+ord(second[i])-97
    
        
        
        target=list(targetWord)
        for i in range(len(target)):
            t=t+ord(target[i])-97
        
        if f+s == t:
            return True
        return False
        
isSumEqual('j','j','bi')
