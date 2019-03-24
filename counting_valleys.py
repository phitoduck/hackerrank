# To count the valleys, we increment the num_valleys every time we 
# step up to zero from below

input()
path = input()

pos = 0
num_valleys = 0
for step in path:
    if step == "U":
        
        if pos == -1:
            num_valleys += 1
        
        pos += 1
    else:
        pos -= 1
        
print(num_valleys)
