---
title: "Median of Two Sorted Arrays in Python (LeetCode Hard)"
date: 2023-01-19T03:00:00+08:00
lastmod: 2023-01-19T03:00:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "Given an integer array nums and an integer k, return the number of good subarrays of nums."
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: ["Python", "Sliding Windows", "Sliding Window Algorithm", "Leetcode", "Leetcode Medium"]
toc:
  enable: true
---
## Solution
Most Python solution you can find usding either this or kth solution they sliced the `nums1` and `nums2` for loop and it makes the time complexity from $O(Logn)$ $O(nLogn)$.

**Slicing Examples:**
1. `return self.kth(a, b[ib + 1:], k - ib - 1)` by [clue](https://leetcode.com/clue/)
2. `return self.findKth(A[:i],B[j:],i)` by [yawnzheng](https://leetcode.com/yawnzheng/)

### Optimized
Here I share a solution using pointer to avoid such the problem.

{{< youtube LPFhl65R7ww >}}

If you don't understand the concept please have a look at the above video first by [@tusharroy2525](https://www.youtube.com/@tusharroy2525/about). 

![featured-image.jpg](featured-image.jpg)

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        _len = len(nums1) + len(nums2)
        if len(nums1) > len(nums2): # let nums1 be the short one
            nums1, nums2 = nums2, nums1

        mid1 = len(nums1) // 2
        while True:
            mid2 = (_len+1) // 2 - mid1 -1
            if (
                1 <= mid1 <= len(nums1) and
                0 <= mid2+1 < len(nums2) and
                nums1[mid1-1] > nums2[mid2+1]
            ):
                mid1 -= 1
            elif (
                0 <= mid1 < len(nums1) and 
                0 <= mid2 < len(nums2) and
                nums2[mid2] > nums1[mid1]
            ):
                mid1 += 1
            
            # found the partition
            else:
                lu = nums1[mid1-1] if 1 <= mid1 <= len(nums1) else -(10**6)
                ld = nums2[mid2] if 0 <= mid2 < len(nums2) else -(10**6)
                ru = nums1[mid1] if 0 <= mid1 < len(nums1) else 10**6
                rd = nums2[mid2+1] if 0 <= mid2+1 < len(nums2) else 10**6
                if _len % 2 == 1:
                    return max(lu, ld)
                return ( max(lu, ld) + min(ru, rd) ) /2
```