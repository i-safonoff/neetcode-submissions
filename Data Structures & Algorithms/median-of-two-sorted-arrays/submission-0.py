class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        c = (m + n + 1) // 2
        l, r = 0, m - 1
        
        while True:
            i = (l + r) // 2
            j = c - i - 2

            n1l = nums1[i] if i >= 0 else float("-infinity")
            n1r = nums1[i+1] if i + 1 < m else float("infinity")
            n2l = nums2[j] if j >= 0 else float("-infinity")
            n2r = nums2[j+1] if j + 1 < n else float("infinity")

            if n1l <= n2r and n2l <= n1r:
                if (m + n) % 2:
                    return max(n1l, n2l)
                return (max(n1l, n2l) + min(n1r, n2r)) / 2
            elif n1l > n2r:
                r = i - 1
            else:
                l = i + 1
        