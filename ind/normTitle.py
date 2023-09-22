from typing import List
from collections import defaultdict


class NormTitle:
    def __init__(self, title_list: List[str]):
        self.word2index = self.get_word_index(title_list)
        self.title_list = title_list

    def highest_score_title(self, title: str):
        words = title.strip().split(" ")
        idx_score = defaultdict(int)
        ans = 0
        for word in words:
            indices = self.word2index.get(word)
            if indices:
                for ind in indices:
                    idx_score[ind] += 1
                    if idx_score[ind] > ans:
                        ans = ind
        return ans

    def get_word_index(self, title_list):
        mp = defaultdict(list)
        for idx, title in enumerate(title_list):
            words = title.strip().split(" ")
            for word in words:
                mp[word].append(idx)
        return mp
        