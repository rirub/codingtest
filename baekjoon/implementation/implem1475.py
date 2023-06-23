a = {'0':0, '1':0,'2':0, '3':0,'4':0, '5':0, '6':0, '7':0, '8':0}
n = list(input())
for i in range(len(n)):
    if n[i]=='9':
       n[i]='6'
    a[n[i]]+=1
a['6'] = (a['6']+1) // 2
print(max(a.values()))
