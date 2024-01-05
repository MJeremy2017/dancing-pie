def solution(s: str) -> str:
    def _split(st):
        if st == "":
            return "", 1
        i = 0
        r = ""
        while i < len(st):
            if st[i].isdigit():
                break
            r += st[i]
            i += 1
        if i < len(st):
            return r, int(st[i:])
        return r, 1

    ans = ""
    ms = []
    for ch in s:
        if ch == "[":
            ms.append(ans)
            ans = ""
        elif ch == "]":
            ms.append(ans)
            ans = ""
            fst = ms.pop()
            if ms:
                snd = ms.pop()
            else:
                snd = ""
            st, num = _split(snd)
            ans = st + num * fst
        else:
            ans += ch
    return ans


if __name__ == '__main__':
    testcases = [("3[a2[c]]", "accaccacc"), ("3[a2[c]]dc[2[a]]", "accaccaccdcaa")]
    for inp, want in testcases:
        got = solution(inp)
        print('got', got)
        assert got == want
        print("=============")
