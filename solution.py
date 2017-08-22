def solution(args):
    l = args
    ans = []
    ns = ''
    sing = [str(i) for i in args]
    ans2 = ''
    for i in range(0, len(l)-2):
        if l[i]+2 == l[i+2]:
            for o in range(len(l)-1,0,-1):
                try:
                    if ans and l[i] < ans[-1]:
                        break
                    if i+o <= len(l)-1 and l[i]+o == l[i+o]:
                        ans.append(l[i])
                        ans.append('-')
                        ans.append(l[i+o])
                        ns = ns + str(l[i]) +'-'+ str(l[i+o])+','
                        break
                except:
                    pass
        else:
            if l[i] == l[0] or l[i] > ans[-1]:
                ans.append(l[i])
            ns = ns + str(l[i])+','
    
    for u in range(len(ans),0,-1):
        try:
            if l[(u*-1)] > int(ans[-1]):
                ans.append(l[u*-1])
        except:
            pass
    for w in range(0,len(ans)):
        if ans[w] == '-':
            ans2 = ans2[:-1:] +'-'
        else:
            ans2 = ans2 + str(ans[w])  + ','
    return ans2[:-1:]
