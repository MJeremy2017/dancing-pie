"""
A,B,C,D,E,F are houses. for a test case [{"A", "B"}, {"B", "C"}, {"D"}]
House B has neighbours House A , House C. House A has only House B as neighbour, house D has no neighbours.
So find the houses which are not neighbours. Answer should be as a list of list , keep the number of
inner-list to a minimum eg [['A', 'C', 'D'], ['B', 'D']] is accepted.

"""

from collections import defaultdict


def find_non_neighbours(A):
    house_all = set()
    adj = defaultdict(set)
    for it in A:
        if len(it) == 1:
            for e in it:
                adj[e] = set()
                house_all.add(e)
        else:
            a, b = it
            adj[a].add(b)
            adj[b].add(a)
            house_all.add(a)
            house_all.add(b)

    x_adj = defaultdict(set)
    for k, neigh in adj.items():
        x_adj[k] = house_all - neigh - {k}
    print(x_adj)

    ans = []

    def _dfs(path, non: set):
        if len(non) == 0:
            if sorted(path) not in ans:
                ans.append(sorted(path))
            return
        for node in non:
            _dfs(path + [node], non.intersection(x_adj[node]))

    for node in house_all:
        _dfs([node], x_adj[node])
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
        res = find_non_neighbours(tc)
        print('ans', res)
