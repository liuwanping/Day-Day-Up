def guessNumber(n):
    l=1
    r=n
    while l<=r:
        m=(l+r)//2
        if guess(m)==-1:
            r=m-1
        elif guess(m)==1:
            l=m+1
        elif guess(m)==0:
            return m 