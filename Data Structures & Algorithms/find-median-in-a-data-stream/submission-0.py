

class MedianFinder:
    '''
    Maintain two heaps that each contain half the numbers, a minheap with the biggest numbers, and maxheap w/ the smallest
    We choose to add to the minheap first, and only to the maxheap when it's a smaller size
    If it's to be added to the minheap, check if it's bigger than the biggest number in the maxheap.
    If so, it to the minheap, else pop the maxheap's largest number and add that to the minheap, and add this number to the maxheap in replacement
    If it's to be added to the maxheap, check if it's smaller than the minheap's smallest number.
    If so, add it to the maxheap, else pop the minheap's smallest number, add that to the maxheap, and add this number to the minheap in replacement

    Median is just the smallest number of the minheap if minheap is larger in size (it'll only be 1 element finder, and that element is the median)
    Or it's the mean of the largest maxheap number and smallest minheap number (avg of the smallest num of the large half and the largest num of the small half)

    Time: O(logn) for a minheap/maxheap addition, O(1) for retrieving the median
    Space: O(n) for n numbers
    '''

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if not self.minheap:
            heapq.heappush(self.minheap, num)
            return

        if len(self.maxheap) < len(self.minheap):
            smallest_big = self.minheap[0]


            if num >= smallest_big:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, num)
                heapq.heappush_max(self.maxheap, smallest_big)
            else:
                heapq.heappush_max(self.maxheap, num)


        else:
            biggest_small = self.maxheap[0]

            if num <= biggest_small:
                heapq.heappop_max(self.maxheap)
                heapq.heappush_max(self.maxheap, num)
                heapq.heappush(self.minheap, biggest_small)
            else:
                heapq.heappush(self.minheap, num)

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (self.maxheap[0] + self.minheap[0]) / 2
        else:
            return self.minheap[0]
        