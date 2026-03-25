def recursive_min(n):
    if len(n)==1:
        return n[0]
    else:
        m=recursive_min(n[1:])
        return n[0] if n[0]<m else m
print(recursive_min([4,2,9,1,5]))