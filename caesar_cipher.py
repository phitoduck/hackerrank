import string

n = int(input())
s = input()
k = int(input()) % 26

result = ""

def rotate_upper(char, k):
    val = ord(char) + k
    val -= 65
    val %= 26
    val += 65
    return chr(val)

def rotate_lower(char, k):
    val = ord(char) + k
    val -= 97
    val %= 26
    val += 97
    return chr(val)
    

for char in s:
    if char in string.ascii_lowercase:
        result += rotate_lower(char, k)
    elif char in string.ascii_uppercase:
        result += rotate_upper(char, k)
    else:
        result += char
    
print(result)   
