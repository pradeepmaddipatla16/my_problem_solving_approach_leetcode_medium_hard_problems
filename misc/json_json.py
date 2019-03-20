r = [(1,0.345336,'asfdfsdgsgs'),(2,0.3464564,'adfdgsdggs'),(3,0.56456474,'asfwsdsfsd')]
inter_list = []
print(r[0])
for each in r:
    print(each)
    jd = dict(zip(['dp_id','score','hash_email'],each))
    inter_list.append(jd)
print(inter_list)