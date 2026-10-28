import heapq
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.arr = []
        n = len(nums)
        for i in range(min(k,n)):
            heapq.heappush(self.arr, nums[i])
        for i in range(k,n):
            if nums[i]>self.arr[0]:
                heapq.heappop(self.arr)
                heapq.heappush(self.arr, nums[i])
    

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