def check(li,n,p):
    li.sort()
    cnt=li[:p].count(li[p-1])
    ix=p-1
    for i in range(p,n):
        if li[:i+1].count(li[i])>cnt:
            cnt=li[:i+1].count(li[i])
            ix=i
    charge=0
    for i in range(ix-1,ix-p):
        charge+=li[ix]-li[i]
    return charge
if __name__=='__main__':
    t=int(input())
    ips=[]
    ranges=[]
    for i in range(t):
        k=tuple(map(int,input().split()))
        ranges.append(k)
        ips.append(list(map(int,input().split())))
    for i in range(t):
        print('Case #{}: {}'.format(i+1,check(ips[i],ranges[i][0],ranges[i][1])))
    