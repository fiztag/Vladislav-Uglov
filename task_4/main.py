f1=open('файл.txt')
x1=[]
while True:
    str=f1.readline().split()
    if not str:
        break
    x=str[0]
    x1.append(float(x))
f1.close()
x=(max(x1)+min(x1))/2
count=0
ymin=abs(x-x1[1])
x2=float(0)
for i in range(0,len(x1)):
    y1=abs(x-x1[i])
    if y1<ymin:
        ymin=y1
        x2=x1[i]
for i in range(0,len(x1)):
    while x1[i]>x2 or x1[i]<x2:
        if x1[i]>x2:
            x1[i]-=1
        else:
            x1[i]+=1
        count=count+1
print(count)