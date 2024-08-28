class SegmentTree:
    tree = None
    size = None

    def __init__(self, nums: list):
        self.size = len(nums)
        n = self.size * 4
        self.tree = [0] * n
        self.construct(nums, 0, self.size - 1, 0)

    def construct(self, nums: list, start: int, end: int, index: int) -> int:
        if start == end:
            self.tree[index] = nums[start]
            return self.tree[index]
        mid = (start + end) // 2
        # current tree for range sum query, so we are storing sum of both segments left + right
        # if tree is for range min query we will store min from both sides min(left, right),
        # and for max, max(left, right)
        self.tree[index] = self.construct(nums, start, mid, index * 2 + 1) \
                           + self.construct(nums, mid + 1, end, index * 2 + 2)
        return self.tree[index]

    def update(self, index: int, value: int):
        return self.__update(0, self.size - 1, index, value, 0)

    def __update(self, start: int, end: int, index_to_update: int, current_index: int, value: int) -> int:
        # out of bound
        if index_to_update < start or index_to_update > end:
            return self.tree[current_index]
        if index_to_update == start and index_to_update == end:
            self.tree[current_index] = value
            return self.tree[current_index]
        mid = (start + end) // 2
        self.tree[current_index] = self.__update(start, mid, index_to_update, current_index * 2 + 1, value) \
                                   + self.__update(mid + 1, end, index_to_update, current_index * 2 + 2, value)
        return self.tree[current_index]

    def get_range_sum(self, left: int, right: int) -> int:
        return self.__get_range_sum(left, right, 0, self.size - 1, 0)

    def __get_range_sum(self, query_start: int, query_end: int, start: int, end: int, index: int) -> int:
        # out of range
        if query_end < start or query_start > end:
            return 0
        # overlap
        if query_start <= start and query_end >= end:
            return self.tree[index]
        mid = (start + end) // 2
        return self.__get_range_sum(query_start, query_end, start, mid, index * 2 + 1) \
            + self.__get_range_sum(query_start, query_end, mid + 1, end, index * 2 + 2)
        # above is for range sum query so left + right
        # for range min query we will take min from both, min(left,right)
        # and for max, max(left,right)


if __name__ == '__main__':
    segment_tree = SegmentTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(segment_tree.tree)

    result = segment_tree.get_range_sum(0, 9)
    print(f'result : {result}')
