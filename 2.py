rost = input().split
list = int(input())
a = 0

for b in rang(len(rost)):
    if int(rost[b])>=list:
        a+=1
print(a+1)
