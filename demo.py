name='Prashil'
count=0
chara=input("Enter the substring")
for i in range(0,len(name)):
    x=i
    for j in range(0,len(chara)):
        if chara[j] == name[x]:
            count=count+1
        else:
            continue
if count==len(chara):
    print("Yes a substring")
else:
    print("No")

