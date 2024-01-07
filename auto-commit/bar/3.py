"""
Median of stream
"""

import heapq as hq


def median_of_stream(stream):
    hp_max = []
    hp_min = []
    sz = 0
    for value in stream:
        hq.heappush(hp_max, -value)
        while len(hp_max) > len(hp_min):
            v = -hq.heappop(hp_max)
            hq.heappush(hp_min, v)
        sz += 1
        if sz & 1:
            print(hp_min[0])
        else:
            print((-hp_max[0] + hp_min[0]) / 2.0)


if __name__ == '__main__':
    s = [3, 12, 6, 1, 4, 7]
    median_of_stream(s)
