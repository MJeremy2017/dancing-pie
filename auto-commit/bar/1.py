"""
A,B,C,D,E,F are houses. for a test case [{"A", "B"}, {"B", "C"}, {"D"}]
House B has neighbours HouseA , House C. House A has only House B as neighbour, house D has no neighbours.
So find the houses which are not neighbours. Answer should be as a list of list , keep the number of
inner-list to a minimum eg [['A', 'C', 'D'], ['B', 'D']] is accepted.

"""

from collections import defaultdict


def non_neighbors(graph):
    ms = defaultdict(set)
    hs = set()
    for it in graph:
        if len(it) == 2:
            a, b = it
            ms[a].add(b)
            ms[b].add(a)
            hs.add(a)
            hs.add(b)
        else:
            for i in it:
                hs.add(i)
    non_neighbors = defaultdict(set)
    for ng in hs:
        non_neighbors[ng] = hs - ms[ng] - {ng}
    ans = []

    print(non_neighbors)

    def _dfs(p, nn):
        if len(nn) == 0:
            p.sort()
            if p not in ans:
                ans.append(p)
            return
        for ng in nn:
            nn2 = nn.intersection(non_neighbors[ng])
            _dfs(p + [ng], nn2)

    for ng in hs:
        _dfs([ng], non_neighbors[ng])
    return ans


if __name__ == '__main__':

    test_cases = [
        [{"A", "B"}, {"B", "C"}, {"D"}],
        [{"A"}, {"B", "C"}, {"D"}],
        [{"A", "B"}, {"B", "C"}, {"D"}],
        [{"A"}, {"B", "C"}, {"D", "E"}],
        [{"A"}, {"B", "C"}, {"D", "E"}, {"F"}, {"G"}],
        [{"A", "B"}, {"B", "C"}, {"D"}, {"A", "E"}, {"B", "E"}, {"C", "E"}]
    ]

    for tc in test_cases:
        res = non_neighbors(tc)
        print('ans', res)
