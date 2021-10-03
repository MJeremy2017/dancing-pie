from collections import defaultdict

def word_distance(word1, word2, A):
    # word1 != word2
    first = -1
    n = len(A)
    ans = n
    for i in range(n):
        if A[i] == word1:
            if second != -1:
                ans = min(ans, i - second)
            first = i
        if A[i] == word2:
            if first != -1:
                ans = min(ans, i - first)
            second = i
    return ans


def word_distance2(word1, word2, A):
    # collect word
    word_collection = defaultdict(list)
    n = len(A)
    for i in range(n):
        if A[i] == word1:
            word_collection[word1].append(i)
        if A[i] == word2:
            word_collection[word2].append(i)

    i, j = 0, 0
    c1 = word_collection[word1]
    c2 = word_collection[word2]
    ans = n
    while i < len(c1) and j < len(c2):
        if j != i:
            ans = min(ans, j-i)
        if c1[i] < c2[j]:
            i += 1
        else:
            j += 1
    return ans
