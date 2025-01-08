def is_palind(s):
    if s == s[::-1]:
        res = True
    else:
        res = False
    return res

word = "redder"
print(is_palind(word))

def is_symm(s):
    length = len(s)
    mid = length//2
    if length%2 ==0:
        return s[:mid] == s[mid:]
    else:
        return s[:mid] == s[mid+1]

word1 = "asdasd"    
print(is_symm(word1))
    