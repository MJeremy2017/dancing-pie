# s = 'AA', 'XY', ...
def sheetNumber(s):
    ans = 0
    for i in s:
        ans = ans * 26 + (ord(i) - ord('A') + 1)
    return ans

def reverse(n):
    ans = ""
    while n > 0:
        n -= 1
        m = n % 26
        ans = chr(m+ord('A')) + ans
        n = n // 26
        
    return ans

if __name__ == '__main__':
    values = ['A', 'AB', 'CE', 'XYZ']
    for v in values:
        t = sheetNumber(v)
        print(t)
        org = reverse(t)
        print(org)
