#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)


    def selectionSort(self, nums):
        """
        Repeatly choose the smallest elements
        """
        for i in range(len(nums)):
            i_n = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i_n]:
                    i_n = j
            nums[i], nums[i_n] = nums[i_n], nums[i]


    def bubbleSort(self, nums):
        """
        Constantly sort next to next elements
        """
        # Note here that is nums, not nums - 1 in case of there are 2 elements
        for i in range(0, len(nums)):
            for j in range(len(nums)- 1, i-1, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]

        return nums


    def recursiveBubbleSort(self, nums, start):
        """
        Constantly sort next to next elements
        """
        # Note here that is nums, not nums - 1 in case of there are 2 elements
        if len(nums) - start == 1:
            return

        self.recursiveBubbleSort(self, nums, start + 1)

        for i in range(start, len(nums)):
            if nums[i] < nums[i+1]:
                nums[i], num[i+1] = nums[i+1], nums[i]


    def insertionSort(self, nums):
        """
        Maintaining the shortest list to the left and insert elements to that portion
        """
        for i in range(1, len(nums)):
            # Here we can use some binary search (but still we have to swap???)
            for j in range(i, 0, -1):
                if nums[j] > nums[j-1]:
                    break
                nums[j], nums[j-1] = nums[j-1], nums[j]


    def mergeSort(self, nums, start, end):
        """
        Divide and conquer, into half and sort each
        """
        if end - start <= 1:
            return

        mid = start + (end - start) // 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid, end)

        self.merge(nums, start, mid, end)


    def merge(self, nums, start, mid , end):
        copy = nums[start:end]
        first = start
        second = mid
        for i in range(start, end):
            if first < mid and (second == end or copy[first - start] < copy[second - start]):
                nums[i] = copy[first - start]
                first += 1
            else:
                nums[i] = copy[second - start]
                second += 1

    def quickSort(self, nums):
        """
        Choose a pivot. Making sure that the pivot is at the right place
        """
        if len(nums) <= 1:
            return nums


        p = nums[len(nums) // 2]
        E = []
        L = []
        R = []

        for i in nums:
            if i < p:
                L.append(i)
            elif i == p:
                E.append(i)
            else:
                R.append(i)

        return self.quickSort(L) + E + self.quickSort(R)


    def quickSortInplace(self, nums, low, high):
        # Handling equal to pivot is hard
        def partition(nums, low, high, p):
            ml = low
            mr = low
            print(p)
            for i in range(low, high):
                if nums[i] < p:
                    # Right and left and the number: it's 3 way swapping
                    nums[i], nums[ml], nums[mr] = nums[mr], nums[i], nums[ml]
                    ml += 1
                    mr += 1
                elif nums[i] == p:
                    nums[i], nums[mr] = nums[mr], nums[i]
                    mr += 1

            return (ml, mr)

        if (high - low) <= 1:
            return nums

        pivot = nums[low]
        ml, mr = partition(nums, low, high, pivot)
        self.quickSortInplace(nums, low, ml)
        self.quickSortInplace(nums, mr, high)
        return nums

    def heapSort(self, nums):
        def maintainHeap(heap, end, start): # 1
            cur = start
            while 2 * cur + 1 < end:
                l = 2 * cur + 1 # 1
                r = 2 * cur + 2 # 2
                big = l if (r >= end or heap[l] > heap[r]) else r
                if heap[cur] >= heap[big]: # 7 3
                    break
                heap[cur], heap[big] = heap[big], heap[cur]
                cur = big

        # Build heap bottom up
        # if a node has index: i -> 2i+ 1
        # Node that we has to use maintain heap since node on top would go all the way to the bottom
        for i in range(len(nums) - 1, -1, -1):
            maintainHeap(nums, len(nums), i)


        for i in range(len(nums)): # 0
            heapSize = len(nums) - i # 2
            nums[0], nums[heapSize - 1] = nums[heapSize -1], nums[0] # swap 5 and 3
            maintainHeap(nums, heapSize -1, 0)

        return nums
# @lc code=end
