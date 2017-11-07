def s(l):return l if 2>len(l)else l[1::-1]+s(l[2:])
def m(n):
 l=range(1,n+1)
 print l
 l=s(l[::-1])
 print l
 while l!=sorted(l):l=s(l[::-1]);print l
