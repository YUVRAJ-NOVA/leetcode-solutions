import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.arr = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.arr)<self.k:
            heapq.heappush(self.arr, val)
        elif val>self.arr[0]:
            heapq.heappop(self.arr)
            heapq.heappush(self.arr, val)
        return self.arr[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)