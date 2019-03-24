# get both arrays as input
input()
astring = input().strip().split()
adict = dict()
for x in astring:
    x = int(x)
    if x in adict.keys():
        adict[x] += 1
    else:
        adict[x] = 1

input()
bstring = input().strip().split()
bdict = dict()
for x in bstring:
    x = int(x)
    if x in bdict.keys():
        bdict[x] += 1
    else:
        bdict[x] = 1

aset = set(adict.keys())
bset = set(bdict.keys())
# print(aset)
# print(bset)
union = aset | bset
intersection = aset & bset
missing_nums = set()

for key in union:
    if key not in intersection:
        missing_nums.add(key)
    elif adict[key] != bdict[key]:
        missing_nums.add(key)
        
print( " ".join( list( map(str, sorted(list(missing_nums) ) ) )))
