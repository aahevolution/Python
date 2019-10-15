l=[]
cnt=0
size=int(input("Enter size"))
for i in range(0,size):
    num=int(input("Enter element"))
    l.append(num)
print("List:",l)
ch=int(input("Enter number to be count:"))
for i in range(0,size):
    if ch==l[i]:
        cnt+=1
print("Count of %d:"%ch,cnt)
