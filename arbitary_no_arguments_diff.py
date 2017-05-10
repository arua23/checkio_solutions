def checkio(*args):
    n=list(args)
    if len(n)>=1:
        high=float(max(n))
        low=float(min(n))
        return float(high-low)
    return 0    
    
##print(checkio(-1,2,3.20012))
print(checkio())
