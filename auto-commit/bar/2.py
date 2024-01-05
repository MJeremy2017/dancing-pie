def solution(s):
    def _is_str(ch):
        return ord("a") <= ord(ch) <= ord("z")

    def _is_num(ch):
        return ch in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

    ans = ""
    ms = []
    tmp2 = ""
    i = 0
    while i < len(s):
        print(i)
        if s[i] == "]":
            while i < len(s) and s[i] == "]" and len(ms):
                chs = ms.pop()
                k = 1
                if len(ms) and _is_num(ms[-1]):
                    k = int(ms.pop())
                tmp2 = (chs+tmp2) * k
                print("pop", chs, i, tmp2, ms)
                i += 1
            ans += tmp2
            tmp2 = ""
            continue
        while i < len(s) and s[i] != "[":
            tmp = ""
            while i < len(s) and _is_str(s[i]):
                tmp += s[i]
                print("here")
                i += 1
            if len(tmp):
                ms.append(tmp)
            if _is_num(s[i]):
                ms.append(s[i])
                i += 1
            break
        if s[i] == "[":
            i += 1
        print(ms)
    return ans


if __name__ == '__main__':
    testcases = [("3[a2[c]]", "accaccacc"), ("3[a2[c]]dc[2[a]]", "accaccaccdcaa")]
    for inp, want in testcases:
        got = solution(inp)
        print('got', got)
        assert got == want
        print("=============")
