ct = [54,396,131,198,225,258,87,258,128,211,57,235,114,258,144,220,39,175,330,338,297,288]
pt = []
for num in ct:
    #print(num)
    flag = num % 37
    pt.append(flag)
print(pt)