"""
I. Question

https://leetcode.com/problems/find-median-from-data-stream/

II. Solution

Intuition

The above two approaches gave us some valuable insights on how to tackle this problem. Concretely, one can infer two things:
1. If we could maintain direct access to median elements at all times, then finding the median would take a constant amount of time.
2. If we could find a reasonably fast way of adding numbers to our containers, additional penalties incurred could be lessened.

But perhaps the most important insight, which is not readily observable, is the fact that we only need a consistent way to access the median elements. Keeping the entire input sorted is not a requirement.

    Well, if only there were a data structure which could handle our needs.

As it turns out there are two data structures for the job:

- Heaps (or Priority Queues 1)
- Self-balancing Binary Search Trees (we'll talk more about them in Approach 4)

Heaps are a natural ingredient for this dish! Adding elements to them take logarithmic order of time. They also give direct access to the maximal/minimal elements in a group.

If we could maintain two heaps in the following way:

- A max-heap to store the smaller half of the input numbers
- A min-heap to store the larger half of the input numbers

This gives access to median values in the input: they comprise the top of the heaps!

Wait, what? How?

If the following conditions are met:
1. Both the heaps are balanced (or nearly balanced)
2. The max-heap contains all the smaller numbers while the min-heap contains all the larger numbers

then we can say that:

1. All the numbers in the max-heap are smaller or equal to the top element of the max-heap (let's call it x)
2. All the numbers in the min-heap are larger or equal to the top element of the min-heap (let's call it y)

Then x and/or y are smaller than (or equal to) almost half of the elements and larger than (or equal to) the other half. That is the definition of median elements.

This leads us to a huge point of pain in this approach: balancing the two heaps!

Algorithm

- Two priority queues:
1. A max-heap lo to store the smaller half of the numbers
2. A min-heap hi to store the larger half of the numbers

- he max-heap lo is allowed to store, at worst, one more element more than the min-heap hi. Hence if we have processed k elements:
* If k=2∗n+1(∀n∈Z), then lo is allowed to hold n+1 elements, while hi can hold n elements.
* If k=2∗n(∀n∈Z), then both heaps are balanced and hold n elements each.

This gives us the nice property that when the heaps are perfectly balanced, the median can be derived from the tops of both heaps. Otherwise, the top of the max-heap lo holds the legitimate median.

- Adding a number num:
* Add num to max-heap lo. Since lo received a new element, we must do a balancing step for hi. So remove the largest element from lo and offer it to hi.
* The min-heap hi might end holding more elements than the max-heap lo, after the previous operation. We fix that by removing the smallest element from hi and offering it to lo.

The above step ensures that we do not disturb the nice little size property we just mentioned.



Note :
- Need to modify __lt__ because by the default heapq is min heap
- Remember whenereve we take the element out or add new element, we interact with PQEntry object, not the value of the object, so access the value by PQEntry.value instead 

"""


import heapq

class PQEntry_min:
    """
    By the default heapq is min heap
    """
    def __init__(self, value):
        self.value =  value
    def __lt__(self, other):
        return self.value < other.value

class PQEntry_max:
    """
    Need to modify __lt__ because by the default heapq is min heap
    """
    def __init__(self,value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value


class MedianFinder:
    def __init__(self):
        self.min_heap = [] # Store all elements bigger than the median
        self.max_heap = [] # Store all elements smaller than the median
        self.nums = []
        

    def addNum(self, num: int) -> None:
        # we add new element to max_heap then we take the top element from the max heap to add to the min heap. In this way, we make sure that all elements in the min_heap is higher than all the elements in the max_heap
        self.nums.append(num)
        heapq.heappush(self.max_heap, PQEntry_max(num))
        top_max_heap = heapq.heappop(self.max_heap).value
        heapq.heappush(self.min_heap, PQEntry_min(top_max_heap))
        
        
        # We need to make sure one heap is equal to another or have more elements than another heap at maximum one. Since in above we take element from max_heap to min_heap, so to be able to keep 2 heap balance or near balance, we need to take element from min_heap to max_heap
        # whenever min_heap is longer than max_heap
        if len(self.max_heap) < len(self.min_heap):
            top_min_heap = heapq.heappop(self.min_heap).value
            heapq.heappush(self.max_heap, PQEntry_max(top_min_heap))
        


    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0].value
        elif len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0].value + self.min_heap[0].value) * 0.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()