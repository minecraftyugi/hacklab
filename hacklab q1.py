def t(l):return len(l)/2and l[-2:]+t(l[:-2])or l
def m(n):
 l=t(range(1,n+1));print l
 while~-l[0]:l=t(l);print l
