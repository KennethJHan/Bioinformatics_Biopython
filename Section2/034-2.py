#034-2.py

seq = "AGTTTATAG"
count_dic = {}

for s in seq:
    if s in count_dic:
        count_dic[s] += 1
    else:
        count_dic[s] = 1
        
for k, v in count_dic.items():
    print("%s: %s" % (k, v))
